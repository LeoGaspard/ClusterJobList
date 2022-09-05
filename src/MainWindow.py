# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from Job import Job

StatusRole = Qt.UserRole + 1000
Short_strRole = Qt.UserRole + 1001
ColorRole = Qt.UserRole + 1002

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("Mr. Cluster Mc Clusterface")

        self.centralwidget = QWidget(MainWindow)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.tabWidget.setCurrentIndex(0)

    # setupUi

class MainWindow(QMainWindow, Ui_MainWindow):

    update_gui = Signal( dict )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.update_action = QAction("Update")
        self.update_action.setShortcut('Ctrl+R')

        self.new_account = QAction("New account", self)
        self.new_account.setShortcut('Ctrl+N')
        self.new_account.setStatusTip("Creates a new account")

        self.settings = QAction("Application settings", self)
        self.settings.setShortcut('Ctrl+S')
        self.settings.setStatusTip("Opens the application settings")

        self.menubar = self.menuBar()
        self.SettingsMenu = self.menubar.addMenu("&Settings")
        self.ManageAccounts = self.SettingsMenu.addMenu("&Accounts settings")
        self.ManageAccounts.addAction(self.new_account)
        self.ManageAccounts.addSeparator()

        self.menubar.addAction(self.update_action)
        self.SettingsMenu.addAction(self.settings)

        self.tabs = {}
        self.account_actions = {}

        class Dummy():
            def __init__(self, name):
                self.name = name
                self.job_list = []

        self.add_tab( Dummy("Running jobs") , account=False)
        self.add_tab( Dummy("Finished jobs") , account=False)

        self.update_gui.connect( self.update_jobs )

    def add_tab(self, profile, account=True):
        widget       = QWidget()
        tab = Tab(self, profile)
        self.tabs[ profile.name ] = tab
        self.tabWidget.addTab(tab, profile.name )

        if account:
            action = QAction( profile.name , self)
            action.setStatusTip("Opens the account settings")
            self.account_actions[profile.name] = action
            self.ManageAccounts.addAction(action)

        old_widget = self.tabWidget.currentWidget()

        self.tabWidget.setCurrentWidget( self.tabs[ profile.name] )
        self.tabs[ profile.name ].index = self.tabWidget.currentIndex()
        self.tabWidget.setCurrentWidget( old_widget )

    def update_jobs(self, color):
        running_tab = self.tabs['Running jobs']
        finished_tab = self.tabs['Finished jobs']
        for tab_name in self.tabs.keys():
            tab = self.tabs[ tab_name ]
            tab.scroll_right.update()
            for it in range( tab.listWidget.count() ):
                tab.listWidget.item(it).update( color )
            if tab_name == "Running jobs" or tab_name == "Finished jobs":
                continue
            for job in tab.jobs:
                if job not in tab.displayed_jobs:
                    item = CustomListItem( job  , color)
                    tab.listWidget.addItem( item )
                    tab.displayed_jobs.append(job.job_id)
                if job.is_finished and job not in finished_tab.jobs:
                    for it in range( tab.listWidget.count() ):
                        if job.job_id == tab.listWidget.item(it).ID:
                            tab.listWidget.takeItem(it)
                            ind = tab.displayed_jobs.index( job.job_id )
                            tab.displayed_jobs.pop(ind)
                            break
                    item = CustomListItem( job , color )
                    finished_tab.listWidget.addItem( item )
                    finished_tab.jobs.append( job )
                    try:
                        ind = running_tab.jobs.index( job.job_id )
                        for it in range( running_tab.listWidget.count() ):
                            if job.job_id == running_tab.listWidget.item(it).ID:
                                running_tab.listWidget.takeItem(it)
                                break
                        running_tab.jobs.pop(ind)
                    except ValueError:
                        pass
                    tab.jobs.pop( tab.jobs.index( job.job_id) )
                elif job not in running_tab.jobs:
                    item = CustomListItem( job , color)
                    running_tab.listWidget.addItem( item )
                    running_tab.jobs.append( job )
            tab.listWidget.repaint()

class CustomListItem(QListWidgetItem):
    def __init__(self, job, color):
        super(CustomListItem, self).__init__()
        self.job    = job
        self.status = job.status
        self.ID     = job.job_id
        self.short_str = "{:06.0f}  {:10s}  {:10s}  {:10s}".format(job.job_id, job.name[:10], job.status[:10], job.run_time[:10])
        try:
            self.color = color[ job.status.lower() ]
        except KeyError:
            self.color = color[ 'default' ]

    def update(self, color):
        try:
            self.color = color[ self.job.status.lower() ]
        except KeyError:
            self.color = color[ 'default' ]
        self.short_str = "{:06.0f}  {:10s}  {:10s}  {:10s}".format(self.job.job_id, self.job.name[:10], self.job.status[:10], self.job.run_time[:10])

    @property
    def status(self):
        return self.data(StatusRole)

    @status.setter
    def status(self, status):
        self.setData(StatusRole, status)

    @property
    def short_str(self):
        return self.data(Short_strRole)

    @short_str.setter
    def short_str(self, short_str):
        self.setData(Short_strRole, short_str)

    @property
    def color(self):
        return self.data(ColorRole)

    @color.setter
    def color(self, color):
        self.setData(ColorRole, color)


class CustomStyledItemDelegate(QStyledItemDelegate):
    def paint(self, painter, option, index):
        super(CustomStyledItemDelegate, self).paint(painter, option, index)

        status = index.data(StatusRole)
        short_str = index.data(Short_strRole)

        font = QFont(option.font)
        fm   = QFontMetrics(font)

        statusRect = QRect(option.rect)
        statusRect.setSize( QSize( 3*fm.height(), fm.height() ) )

        color = QColor( *index.data(ColorRole) )
        painter.save()
        painter.setFont(font)
        pen = painter.pen()
        pen.setColor( color)
        painter.setPen(pen)
        painter.drawText(statusRect, "{:^5s}".format("\u2b24"), Qt.AlignHCenter | Qt.AlignVCenter)
        painter.restore()

        strRect = QRect(option.rect)
        strRect.setHeight(fm.height())
        strRect.setLeft( statusRect.right() )

        color = ( option.palette.color( QPalette.BrightText )
                if option.state & QStyle.State_Selected
                else option.palette.color( QPalette.WindowText )
                )

        painter.save()
        painter.setFont(font)
        pen = painter.pen()
        pen.setColor(color)
        painter.setPen(pen)
        painter.drawText(strRect, short_str, Qt.AlignLeft | Qt.AlignVCenter)
        painter.restore()

class CustomListWidget(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)

class Tab(QWidget):
    def __init__(self, ParentWindow, profile):
        self.name = profile.name
        self.jobs = profile.job_list
        self.displayed_jobs = []
        super().__init__()

        self.layout = QHBoxLayout(self)

        self.frame = QFrame(self)
        self.frame.setFrameShape( QFrame.StyledPanel )
        self.frame.setFrameShadow( QFrame.Raised )

        self.frameVerticalLayout = QVBoxLayout( self.frame )

        # Set the left part #

        # Label on top of left part
        self.leftLabel = QLabel(self.frame)
        self.leftLabel.setText(" {:^5s}{:^8s}{:^10s} {:^10s}   {:^10s}".format("Tag", "JobID", "Job Name", "Status", "Runtime") )
        self.frameVerticalLayout.addWidget( self.leftLabel )

        # Left list
        self.listWidget  = CustomListWidget(self)
        self.listWidget.itemSelectionChanged.connect( self.displayJob )
        self.frameVerticalLayout.addWidget(self.listWidget)
        self.listWidget.setItemDelegate( CustomStyledItemDelegate(self) )

        # Line between scroll areas
        self.line         = QFrame(self)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.scroll_right = JobInfo(self)
        self.scroll_right.textEdit.textChanged.connect(self.updateJobComment)

        self.layout.addWidget(self.frame)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.scroll_right)
        self.layout.setStretch(0, 4)
        self.layout.setStretch(1, 4)
        self.layout.setStretch(2, 5)

        self.frame.setMaximumWidth(500)
        self.frame.setMinimumWidth(500)
        self.scroll_right.setMinimumWidth(400)

       #ParentWindow.tabWidget.addTab(self, name)

    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if self.name == 'Finished jobs':
                key = event.key()
                text = event.text()

                if key == Qt.Key_Delete and len( self.listWidget.selectedItems() ) > 0 :
                    id = self.listWidget.selectedItems()[0].ID
                    msgBox = QMessageBox( QMessageBox.Question,
                                "Delete job",
                                "Do you want to delete job {} ?".format(id),
                                QMessageBox.Cancel | QMessageBox.Ok,
                                defaultButton = QMessageBox.Ok
                                )
                    ret = msgBox.exec()
                    if ret == QMessageBox.Ok:
                        self.removeJob( id )

    def addJob(self, job, color):
        item = CustomListItem( job , color )
        self.listWidget.addItem( item )
        self.jobs.append( job )

    def displayJob(self):
        if len( self.listWidget.selectedItems() ) > 0:
            index = self.jobs.index( self.listWidget.selectedItems()[0].ID )
            self.scroll_right.showJobInfo( self.jobs[ index ] )

    def removeJob(self, id):
        ind = self.jobs.index( id )
        for it in range( self.listWidget.count() ):
            if id == self.listWidget.item(it).ID:
                self.listWidget.takeItem(it)
                break
        self.jobs.pop(ind)

    def updateJobComment(self):
        if len( self.listWidget.selectedItems() ) > 0:
            ind = self.jobs.index( self.listWidget.selectedItems()[0].ID )
            self.jobs[ind].comment = self.scroll_right.textEdit.toPlainText()

class JobInfo(QScrollArea):
    def __init__(self, ParentWindow):
        super().__init__(ParentWindow)
        self.setWidgetResizable(True)
        self.setEnabled(True)
        self.job = None

        self.widget = QWidget()

        self.layout = QVBoxLayout(self.widget)
        self.layout.setAlignment(Qt.AlignLeft|Qt.AlignTop)
        self.setWidget(self.widget)

        #Organising the layouts
        self.JobIDLayout = QHBoxLayout()
        self.JobIDLeftLayout = QVBoxLayout()
        self.JobIDRightLayout = QVBoxLayout()

        self.JobIDLayout.addLayout(self.JobIDLeftLayout)
        self.JobIDLayout.addLayout(self.JobIDRightLayout)

        self.line1 = QFrame(self.widget)
        self.line1.setFrameShape(QFrame.HLine)
        self.line1.setFrameShadow(QFrame.Sunken)

        self.JobSpecLayout = QVBoxLayout()
        self.JobSpecDataLayout = QHBoxLayout()
        self.JobSpecLeftLayout = QVBoxLayout()
        self.JobSpecRightLayout = QVBoxLayout()

        self.JobSpecLayout.addLayout(self.JobSpecDataLayout)
        self.JobSpecDataLayout.addLayout(self.JobSpecLeftLayout)
        self.JobSpecDataLayout.addLayout(self.JobSpecRightLayout)
        self.JobSpecLayout.setStretch(1,8)

        self.line2 = QFrame(self.widget)
        self.line2.setFrameShape(QFrame.HLine)
        self.line2.setFrameShadow(QFrame.Sunken)

        self.JobTimesLayout = QVBoxLayout()
        self.JobTimesDataLayout = QHBoxLayout()
        self.JobTimesLeftLayout = QVBoxLayout()
        self.JobTimesRightLayout = QVBoxLayout()

        self.JobTimesLayout.addLayout(self.JobTimesDataLayout)
        self.JobTimesDataLayout.addLayout(self.JobTimesLeftLayout)
        self.JobTimesDataLayout.addLayout(self.JobTimesRightLayout)
        self.JobTimesLayout.setStretch(1, 8)

        self.line3 = QFrame(self.widget)
        self.line3.setFrameShape(QFrame.HLine)
        self.line3.setFrameShadow(QFrame.Sunken)

        self.textEdit = QTextEdit(self.widget)

        self.layout.addLayout(self.JobIDLayout)
        self.layout.addWidget(self.line1)
        self.layout.addLayout(self.JobSpecLayout)
        self.layout.addWidget(self.line2)
        self.layout.addLayout(self.JobTimesLayout)
        self.layout.addWidget(self.line3)
        self.layout.addWidget(self.textEdit)


        # Creating the labels
        self.jobClusterLabel = QLabel(self.widget)
        self.jobClusterLabel.setText("Cluster")

        self.JobIDLabel = QLabel(self.widget)
        self.JobIDLabel.setText("Job ID")

        self.JobNameLabel = QLabel(self.widget)
        self.JobNameLabel.setText("Job Name")

        self.jobClusterData = QLabel(self.widget)
        self.JobIDData = QLabel(self.widget)
        self.JobNameData = QLabel(self.widget)

        self.JobIDLeftLayout.addWidget(self.jobClusterLabel)
        self.JobIDLeftLayout.addWidget(self.JobIDLabel)
        self.JobIDLeftLayout.addWidget(self.JobNameLabel)

        self.JobIDRightLayout.addWidget(self.jobClusterData)
        self.JobIDRightLayout.addWidget(self.JobIDData)
        self.JobIDRightLayout.addWidget(self.JobNameData)


        self.NodesLabel = QLabel(self.widget)
        self.NodesLabel.setText("Number of nodes")

        self.CPULabel = QLabel(self.widget)
        self.CPULabel.setText("Number of CPUs")

        self.MemoryLabel = QLabel(self.widget)
        self.MemoryLabel.setText("Memory")

        self.StatusLabel = QLabel(self.widget)
        self.StatusLabel.setText("Status")

        self.NodesData = QLabel(self.widget)
        self.CPUData = QLabel(self.widget)
        self.MemoryData = QLabel(self.widget)
        self.StatusData = QLabel(self.widget)

        self.JobSpecLeftLayout.addWidget(self.NodesLabel)
        self.JobSpecLeftLayout.addWidget(self.CPULabel)
        self.JobSpecLeftLayout.addWidget(self.MemoryLabel)
        self.JobSpecLeftLayout.addWidget(self.StatusLabel)
        self.JobSpecRightLayout.addWidget(self.NodesData)
        self.JobSpecRightLayout.addWidget(self.CPUData)
        self.JobSpecRightLayout.addWidget(self.MemoryData)
        self.JobSpecRightLayout.addWidget(self.StatusData)

        self.JobStartLabel = QLabel(self.widget)
        self.JobStartLabel.setText("Start time")

        self.JobRunningLabel = QLabel(self.widget)
        self.JobRunningLabel.setText("Runtime")

        self.JobLeftLabel = QLabel(self.widget)
        self.JobLeftLabel.setText("Time left")

        self.JobSubmitLabel = QLabel(self.widget)
        self.JobSubmitLabel.setText("Submit time")

        self.JobStartData = QLabel(self.widget)
        self.JobRunningData = QLabel(self.widget)
        self.JobLeftData = QLabel(self.widget)
        self.JobSubmitData = QLabel(self.widget)

        self.JobTimesLeftLayout.addWidget(self.JobSubmitLabel)
        self.JobTimesLeftLayout.addWidget(self.JobStartLabel)
        self.JobTimesLeftLayout.addWidget(self.JobRunningLabel)
        self.JobTimesLeftLayout.addWidget(self.JobLeftLabel)
        self.JobTimesRightLayout.addWidget(self.JobSubmitData)
        self.JobTimesRightLayout.addWidget(self.JobStartData)
        self.JobTimesRightLayout.addWidget(self.JobRunningData)
        self.JobTimesRightLayout.addWidget(self.JobLeftData)

        self.layout.setStretch(0, 1)
        self.layout.setStretch(1, 1)
        self.layout.setStretch(2, 1)
        self.layout.setStretch(3, 2)
        self.layout.setStretch(4, 1)
        self.layout.setStretch(5, 2)
        self.layout.setStretch(6, 80)

    def showJobInfo(self, job):
        self.job = job
        self.jobClusterData.setText( job.cluster )
        self.JobIDData.setText( str(job.job_id) )
        self.JobNameData.setText(job.name)
        self.NodesData.setText( str(job.nodes) )
        self.CPUData.setText( str(job.cpus) )
        self.MemoryData.setText( job.memory )
        self.StatusData.setText( job.status )
        self.JobStartData.setText( job.start_time )
        self.JobRunningData.setText( job.run_time )
        self.JobLeftData.setText( job.time_left)
        self.JobSubmitData.setText( job.submit_time )
        self.textEdit.setText( job.comment )
    def update(self):
        if self.job is not None:
             self.jobClusterData.setText( self.job.cluster )
             self.JobIDData.setText( str(self.job.job_id) )
             self.JobNameData.setText(self.job.name)
             self.NodesData.setText( str(self.job.nodes) )
             self.CPUData.setText( str(self.job.cpus) )
             self.MemoryData.setText( self.job.memory )
             self.StatusData.setText( self.job.status )
             self.JobStartData.setText( self.job.start_time )
             self.JobRunningData.setText( self.job.run_time )
             self.JobLeftData.setText( self.job.time_left)
             self.JobSubmitData.setText( self.job.submit_time )
             self.textEdit.setText( self.job.comment )
