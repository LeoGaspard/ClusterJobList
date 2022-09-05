import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6 import QtCore
from PySide6 import QtWidgets

import configparser

from Job import Job
from ClusterConnection import ClusterConnection

from MainWindow import MainWindow
from MainWindow import Tab
from AccountSettingDialog import AccountSettingsDialog
from programSettingsDialog import ProgramSettingsDialog

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.setFont( QFont("Monospace") )
        self.directory = os.path.dirname( argv[0] )
        self.thread_manager = QThreadPool()
        # Reads the parameters, if doesn't exist creates a parameter file with defaults
        self.config = configparser.ConfigParser()
        self.config.read(self.directory+'/config')

        self.change_theme( self.config['UI']['theme'] )
        self.set_colors(self.config['COLORS'])

        # Reads the accounts if exists
        profiles = configparser.ConfigParser()
        profiles.read(self.directory+'/profiles')

        # Creates the Mainwindow object
        self.main_window = MainWindow()

        # Reads the finished jobs
        try:
            parser = configparser.ConfigParser()
            parser.read(self.directory+"/../logs/jobs_finished")

            for job in parser.sections():
                cluster      = parser[job]['cluster']
                job_id       = int(job)
                name         = parser[job]['name']
                status       = parser[job]['status']
                submit_time  = parser[job]['submit_time']
                start_time  = parser[job]['start_time']
                time_left  = parser[job]['time_left']
                run_time     = parser[job]['run_time']
                nodes        = int( parser[job]['nodes'] )
                cpus         = int( parser[job]['cpus'] )
                memory       = parser[job]['status']
                comment      = parser[job]['comment']

                self.main_window.tabs["Finished jobs"].addJob(Job(cluster, job_id, name, status, submit_time, start_time,
                                                  run_time, time_left, nodes, cpus, memory, comment=comment ), self.colors )
        except FileNotFoundError:
            pass

        self.main_window.show()

        self.__setup_profiles(profiles)

        # Connects the menubar actions
        self.main_window.new_account.triggered.connect( self.new_account )
        def makeConnect(x):
            return lambda: self.manage_account(x)
        for pro in self.profiles:
            self.main_window.account_actions[ pro.name ].triggered.connect( makeConnect(pro) )

        self.main_window.settings.triggered.connect( self.app_settings )
        self.main_window.update_action.triggered.connect( self.update_safe )

        self.update_safe()

        self.Timer = QTimer(self)
        self.Timer.setInterval( float( self.config['APPLICATION']['refresh_rate'] ) * 60000 )
        self.Timer.timeout.connect( self.update_safe)
        self.Timer.start()
    def set_colors(self, colors):
        self.colors = {}
        for c in colors.keys():
            col = [ int(i) for i in colors[c].split(',') ]
            self.colors[c] = col
    @Slot(str)
    def change_theme(self, theme):
        File = QtCore.QFile(self.directory+'/../themes/'+theme+".qss")
        File.open( QtCore.QFile.ReadOnly | QtCore.QFile.Text)
        qss = QtCore.QTextStream(File)
        #setup stylesheet
        self.setStyleSheet(qss.readAll())
    @Slot(None)
    def update_safe(self):
        self.thread_manager.start( self.update )
    @Slot(None)
    def update(self):
       for pro in self.profiles:
           pro.update_jobs( self.config['APPLICATION']['notification_mode'])
       self.main_window.update_gui.emit( self.colors )
       self.thread.stop()
    def app_settings(self):
        colors = self.colors.copy()
        msgBox = ProgramSettingsDialog()
        msgBox.doubleSpinBox.setValue( float( self.config['APPLICATION']['refresh_rate'] ) )
        if self.config['APPLICATION']['notification_mode'] == "Job start + job end":
            msgBox.comboBox.setCurrentIndex(0)
        elif self.config['APPLICATION']['notification_mode'] == "Job end":
            msgBox.comboBox.setCurrentIndex(1)
        elif self.config['APPLICATION']['notification_mode'] == "Job start":
            msgBox.comboBox.setCurrentIndex(2)
        elif self.config['APPLICATION']['notification_mode'] == "None":
            msgBox.comboBox.setCurrentIndex(3)

        for root, dirs, files in os.walk(self.directory+'/../themes/'):
            files = [f for f in files if f[0] != '.']
            for f in files:
                msgBox.comboBox_2.addItem(f.replace('.qss', ''))

        for i in range(msgBox.comboBox_2.count()):
            if msgBox.comboBox_2.itemText(i) == self.config['UI']['theme']:
                msgBox.comboBox_2.setCurrentIndex(i)

        def pushButtonColor() :
            try:
                color = colors[ msgBox.comboBox_3.currentText().lower() ]
            except KeyError:
                color = colors['default']
            msgBox.pushButton.setStyleSheet("border: 3px solid #808080;background-color:rgb({:3.0f},{:3.0f},{:3.0f})".format(*color))

        def color_selection():
            color_dialog = QColorDialog()
            if color_dialog.exec():
                colors[ msgBox.comboBox_3.currentText().lower() ] = list( color_dialog.currentColor().getRgb() )[:-1]
                pushButtonColor()


        pushButtonColor()

        msgBox.pushButton.clicked.connect( color_selection )
        msgBox.comboBox_2.currentIndexChanged.connect(lambda x: self.change_theme( msgBox.comboBox_2.itemText(x) ))
        msgBox.comboBox_3.currentIndexChanged.connect(pushButtonColor)

        if msgBox.exec():
            self.colors = colors
            self.config['APPLICATION']['refresh_rate'] = "{:4.1f}".format( msgBox.doubleSpinBox.value() )
            self.config['APPLICATION']['notification_mode'] = msgBox.comboBox.currentText()
            self.config['UI']['theme'] = msgBox.comboBox_2.currentText()

            for c in colors.keys():
                col = "{:3.0f},{:3.0f},{:3.0f}".format(colors[c][0], colors[c][1], colors[c][2])
                self.config['COLORS'][c] = col

            with open("config", 'w') as f:
                self.config.write( f )
    def new_account(self):
        msgBox = AccountSettingsDialog()
        msgBox.label_6.setText("New profile")
        if msgBox.exec():
            name = msgBox.name.text()
            host = msgBox.host.text()
            user = msgBox.username.text()
            key_file = msgBox.sshkeyfile.text()
            gateway = None
            if msgBox.gateway.text() != "":
                gateway = ( msgBox.gatewayuser.text(), msgBox.gateway.text() )

            profile = ClusterConnection( name, host, user, key_file, gateway)

            # Writes the changes in the profiles file
            saved_profiles = configparser.ConfigParser()
            saved_profiles.read(self.directory+"/profiles")

            saved_profiles[ name ] = {}
            saved_profiles[ name ]['host'] = profile.host
            saved_profiles[ name ]['key_file'] = profile.key_file
            saved_profiles[ name ]['username'] = profile.user
            saved_profiles[ name ]['gateway'] = profile.gateway[1]
            saved_profiles[ name ]['gateway_username'] = profile.gateway[0]

            self.profiles.append( profile )
            self.main_window.add_tab( profile )

            def makeConnect(x):
                return lambda: self.manage_account(x)
            self.main_window.account_actions[ name ].triggered.connect( makeConnect(profile) )

            with open(self.directory+"/profiles", "w") as pro_file:
                saved_profiles.write( pro_file )
    def manage_account(self, profile):
        msgBox = AccountSettingsDialog()
        msgBox.label_6.setText("Profile {}".format(profile.name) )
        msgBox.name.setText(profile.name)
        msgBox.host.setText(profile.host)
        msgBox.username.setText(profile.user)
        msgBox.sshkeyfile.setText(profile.key_file)
        if profile.gateway is not None:
            msgBox.gatewayuser.setText(profile.gateway[0])
            msgBox.gateway.setText(profile.gateway[1])

        if msgBox.exec_():
            old_name = profile.name
            profile.name = msgBox.name.text()
            profile.host = msgBox.host.text()
            profile.user = msgBox.username.text()
            profile.key_file = msgBox.sshkeyfile.text()
            if msgBox.gateway.text() != "":
                gateway = ( msgBox.gatewayuser.text(), msgBox.gateway.text() )

            for job in profile.job_list:
                job.cluster = profile.name

            # Writes the changes in the profiles file
            saved_profiles = configparser.ConfigParser()
            saved_profiles.read(self.directory+"/profiles")

            saved_profiles[ old_name ]['host'] = profile.host
            saved_profiles[ old_name ]['key_file'] = profile.key_file
            saved_profiles[ old_name ]['username'] = profile.user
            saved_profiles[ old_name ]['gateway'] = profile.gateway

            if profile.name != old_name:
                saved_profiles._sections[ profile.name ] = saved_profiles._sections[ old_name ]
                saved_profiles._sections.pop( old_name )
                self.main_window.tabWidget.setTabText( self.main_window.tabs[ old_name ].index  , profile.name)
                self.main_window.tabs[ profile.name ] = self.main_window.tabs[ old_name ]
                self.main_window.tabs.pop( old_name )

            with open(self.directory+"/profiles", "w") as pro_file:
                saved_profiles.write( pro_file )
    def __setup_profiles(self, profiles):
        self.profiles = []
        for name in profiles.sections():
            self.profiles.append( ClusterConnection( name , profiles[name]['host'] , profiles[name]['username'] ,
                                  profiles[name]['key_file'], (profiles[name]['gateway_username'], profiles[name]['gateway']) ) )
            self.main_window.add_tab( self.profiles[-1] )

            try:
                parser = configparser.ConfigParser()
                parser.read(self.directory+"/../logs/jobs_{}".format(name))

                for job in parser.sections():
                    cluster      = parser[job]['cluster']
                    job_id       = int(job)
                    name         = parser[job]['name']
                    status       = parser[job]['status']
                    submit_time  = parser[job]['submit_time']
                    start_time  = parser[job]['start_time']
                    time_left  = parser[job]['time_left']
                    run_time     = parser[job]['run_time']
                    nodes        = int( parser[job]['nodes'] )
                    cpus         = int( parser[job]['cpus'] )
                    memory       = parser[job]['status']
                    comment      = parser[job]['comment']

                    self.profiles[-1].job_list.append( Job(cluster, job_id, name, status, submit_time, start_time,
                                                      run_time, time_left, nodes, cpus, memory, comment=comment ) )
            except FileNotFoundError:
                pass
    def close(self):
        for pro in self.profiles:
            parser = configparser.ConfigParser()
            for j in pro.job_list:
                parser[ str(j.job_id) ] = {}
                parser[ str(j.job_id) ]['cluster']       = j.cluster
                parser[ str(j.job_id) ]['name']          = j.name
                parser[ str(j.job_id) ]['status']        = j.status
                parser[ str(j.job_id) ]['submit_time']   = j.submit_time
                parser[ str(j.job_id) ]['start_time']    = j.start_time
                parser[ str(j.job_id) ]['run_time']      = j.run_time
                parser[ str(j.job_id) ]['time_left']     = j.time_left
                parser[ str(j.job_id) ]['nodes']         = str(j.nodes)
                parser[ str(j.job_id) ]['cpus']          = str(j.cpus)
                parser[ str(j.job_id) ]['memory']        = j.memory
                parser[ str(j.job_id) ]['is_finished']   = str(j.cluster)
                parser[ str(j.job_id) ]['comment']       = j.comment

            with open(self.directory+"/../logs/jobs_{}".format(pro.name), 'w') as f:
                parser.write( f )

        parser = configparser.ConfigParser()
        for j in self.main_window.tabs["Finished jobs"].jobs:
            parser[ str(j.job_id) ] = {}
            parser[ str(j.job_id) ]['cluster']       = j.cluster
            parser[ str(j.job_id) ]['name']          = j.name
            parser[ str(j.job_id) ]['status']        = j.status
            parser[ str(j.job_id) ]['submit_time']   = j.submit_time
            parser[ str(j.job_id) ]['start_time']    = j.start_time
            parser[ str(j.job_id) ]['run_time']      = j.run_time
            parser[ str(j.job_id) ]['time_left']     = j.time_left
            parser[ str(j.job_id) ]['nodes']         = str(j.nodes)
            parser[ str(j.job_id) ]['cpus']          = str(j.cpus)
            parser[ str(j.job_id) ]['memory']        = j.memory
            parser[ str(j.job_id) ]['is_finished']   = str(j.cluster)
            parser[ str(j.job_id) ]['comment']       = j.comment

        with open(self.directory+"/../logs/jobs_finished", 'w') as f:
            parser.write( f )
