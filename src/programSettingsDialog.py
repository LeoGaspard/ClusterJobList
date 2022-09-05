# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'programSettingsDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QFrame, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

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


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.doubleSpinBox = QDoubleSpinBox(Dialog)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.verticalLayout_3.addWidget(self.doubleSpinBox)

        self.comboBox = QComboBox(Dialog)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_3.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout_3.addWidget(self.comboBox_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 25))
        self.frame.setMaximumSize(QSize(16777215, 25))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.comboBox_3 = QComboBox(self.frame)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")

        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.horizontalLayout_2.setSpacing(10)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(25, 25))
        self.pushButton.setMaximumSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalLayout_2.setStretch(0, 15)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addWidget(self.frame)


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
        Dialog.setWindowTitle(QCoreApplication.translate("Program settings", u"Program settings", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Program settings", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Refresh Rate (min)", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Notifications", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Theme", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Status color", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Job start + job end", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Job end", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Job start", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"None", None))
        self.comboBox.setItemText(4, "")

        self.comboBox_3.setItemText(0, QCoreApplication.translate("Dialog", u"BOOT_FAIL", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("Dialog", u"CANCELLED", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("Dialog", u"COMPLETED", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("Dialog", u"CONFIGURING", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("Dialog", u"COMPLETING", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("Dialog", u"DEADLINE", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("Dialog", u"FAILED", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("Dialog", u"NODE_FAIL", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("Dialog", u"OUT_OF_MEMORY", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("Dialog", u"PENDING", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("Dialog", u"PREEMPTED", None))
        self.comboBox_3.setItemText(11, QCoreApplication.translate("Dialog", u"RUNNING", None))
        self.comboBox_3.setItemText(12, QCoreApplication.translate("Dialog", u"RESV_DEL_HOLD", None))
        self.comboBox_3.setItemText(13, QCoreApplication.translate("Dialog", u"REQUEUE_FED", None))
        self.comboBox_3.setItemText(14, QCoreApplication.translate("Dialog", u"REQUEUE_HOLD", None))
        self.comboBox_3.setItemText(15, QCoreApplication.translate("Dialog", u"REQUEUD", None))
        self.comboBox_3.setItemText(16, QCoreApplication.translate("Dialog", u"RESIZING", None))
        self.comboBox_3.setItemText(17, QCoreApplication.translate("Dialog", u"REVOKED", None))
        self.comboBox_3.setItemText(18, QCoreApplication.translate("Dialog", u"SIGNALING", None))
        self.comboBox_3.setItemText(19, QCoreApplication.translate("Dialog", u"SPECIAL_EXIT", None))
        self.comboBox_3.setItemText(20, QCoreApplication.translate("Dialog", u"STAGE_OUT", None))
        self.comboBox_3.setItemText(21, QCoreApplication.translate("Dialog", u"STOPPED", None))
        self.comboBox_3.setItemText(22, QCoreApplication.translate("Dialog", u"SUSPENDED", None))
        self.comboBox_3.setItemText(23, QCoreApplication.translate("Dialog", u"TIMEOUT", None))
    # retranslateUi

class ProgramSettingsDialog(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args ,**kwargs)
        self.setupUi(self)

