# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accountSettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(419, 530)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 50))
        self.label_6.setMaximumSize(QSize(16777215, 50))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))
        self.label_3.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.label_4)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 25))
        self.label_5.setMaximumSize(QSize(16777215, 25))

        self.verticalLayout_2.addWidget(self.label_5)

        self.label_7 = QLabel(Dialog)
        self.label_7.setMinimumSize( QSize(0, 25) )
        self.label_7.setMaximumSize( QSize(16777215, 25) )

        self.verticalLayout_2.addWidget(self.label_7)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.name = QLineEdit(Dialog)
        self.name.setObjectName(u"name")

        self.verticalLayout_3.addWidget(self.name)

        self.host = QLineEdit(Dialog)
        self.host.setObjectName(u"host")

        self.verticalLayout_3.addWidget(self.host)

        self.username = QLineEdit(Dialog)
        self.username.setObjectName(u"username")

        self.verticalLayout_3.addWidget(self.username)

        self.sshkeyfile = QLineEdit(Dialog)
        self.sshkeyfile.setObjectName(u"sshkeyfile")

        self.verticalLayout_3.addWidget(self.sshkeyfile)

        self.gateway = QLineEdit(Dialog)
        self.gateway.setObjectName(u"gateway")

        self.verticalLayout_3.addWidget(self.gateway)

        self.gatewayuser = QLineEdit(Dialog)

        self.verticalLayout_3.addWidget(self.gatewayuser)

        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Account settings", u"Account settings", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Account ", None))
        self.label_7.setText("Gateway username")
        self.label.setText(QCoreApplication.translate("Dialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Host", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"User name", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"SSH key file", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Gateway", None))
    # retranslateUi

class AccountSettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
