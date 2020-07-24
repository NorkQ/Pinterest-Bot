# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ana.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from Functions import Functions
from threading import Thread

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 640)
        MainWindow.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1005, 625))
        self.tabWidget.setObjectName("tabWidget")
        self.uyeler = QtWidgets.QWidget()
        self.uyeler.setObjectName("uyeler")
        self.ara_edit = QtWidgets.QLineEdit(self.uyeler)
        self.ara_edit.setGeometry(QtCore.QRect(10, 10, 811, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ara_edit.setFont(font)
        self.ara_edit.setObjectName("ara_edit")
        self.ara_buton = QtWidgets.QPushButton(self.uyeler)
        self.ara_buton.setGeometry(QtCore.QRect(830, 10, 161, 31))
        self.ara_buton.setObjectName("ara_buton")
        self.tablo = QtWidgets.QTreeWidget(self.uyeler)
        self.tablo.setGeometry(QtCore.QRect(10, 50, 980, 510))
        self.tablo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tablo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tablo.setTabKeyNavigation(False)
        self.tablo.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tablo.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablo.setIndentation(20)
        self.tablo.setItemsExpandable(True)
        self.tablo.setAnimated(False)
        self.tablo.setAllColumnsShowFocus(False)
        self.tablo.setWordWrap(False)
        self.tablo.setHeaderHidden(False)
        self.tablo.setObjectName("tablo")
        self.tablo.header().setCascadingSectionResizes(False)
        self.tablo.header().setDefaultSectionSize(140)
        self.tablo.header().setHighlightSections(False)
        self.tablo.header().setSortIndicatorShown(False)

        self.isim_soyisim_edit = QtWidgets.QLineEdit(self.uyeler)
        self.isim_soyisim_edit.setGeometry(QtCore.QRect(10, 570, 160, 25))

        self.mail_edit = QtWidgets.QLineEdit(self.uyeler)
        self.mail_edit.setGeometry(QtCore.QRect(180, 570, 160, 25))

        self.tel_no_edit = QtWidgets.QLineEdit(self.uyeler)
        self.tel_no_edit.setGeometry(QtCore.QRect(350, 570, 160, 25))

        self.anahtar_edit = QtWidgets.QLineEdit(self.uyeler)
        self.anahtar_edit.setGeometry(QtCore.QRect(520, 570, 160, 25))

        self.sure_edit = QtWidgets.QLineEdit(self.uyeler)
        self.sure_edit.setGeometry(QtCore.QRect(690, 570, 160, 25))

        self.ekle_buton = QtWidgets.QPushButton(self.uyeler)
        self.ekle_buton.setGeometry(QtCore.QRect(860, 569, 130, 27))

        self.tabWidget.addTab(self.uyeler, "")
        self.uyarilar = QtWidgets.QWidget()
        self.uyarilar.setObjectName("uyarilar")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.uyarilar)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 981, 541))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.uyarilar)
        self.pushButton.setGeometry(QtCore.QRect(10, 562, 981, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.uyarilar, "")

        self.elementler = QtWidgets.QWidget()
        self.tabWidget.addTab(self.elementler, "")

        self.ara_edit_elem = QtWidgets.QLineEdit(self.elementler)
        self.ara_edit_elem.setGeometry(QtCore.QRect(10, 10, 811, 31))
        font_elem = QtGui.QFont()
        font_elem.setPointSize(12)
        self.ara_edit_elem.setFont(font)
        self.ara_edit_elem.setObjectName("ara_edit")
        self.ara_buton_elem = QtWidgets.QPushButton(self.elementler)
        self.ara_buton_elem.setGeometry(QtCore.QRect(830, 10, 161, 31))
        self.ara_buton_elem.setObjectName("ara_buton")
        self.tablo_elem = QtWidgets.QTreeWidget(self.elementler)
        self.tablo_elem.setGeometry(QtCore.QRect(10, 50, 980, 510))
        self.tablo_elem.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tablo_elem.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tablo_elem.setTabKeyNavigation(False)
        self.tablo_elem.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.tablo_elem.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablo_elem.setIndentation(20)
        self.tablo_elem.setItemsExpandable(True)
        self.tablo_elem.setAnimated(False)
        self.tablo_elem.setAllColumnsShowFocus(False)
        self.tablo_elem.setWordWrap(False)
        self.tablo_elem.setHeaderHidden(False)
        self.tablo_elem.setObjectName("tablo")
        self.tablo_elem.header().setCascadingSectionResizes(False)
        self.tablo_elem.header().setDefaultSectionSize(140)
        self.tablo_elem.header().setHighlightSections(False)
        self.tablo_elem.header().setSortIndicatorShown(False)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NorkQ Pinner Admin"))
        self.ara_edit.setPlaceholderText(_translate("MainWindow", "Ara..."))
        self.ara_buton.setText(_translate("MainWindow", "Ara"))

        self.ara_edit_elem.setPlaceholderText(_translate("MainWindow", "Ara..."))
        self.ara_buton_elem.setText(_translate("MainWindow", "Ara"))

        self.isim_soyisim_edit.setPlaceholderText(_translate("MainWindow", "İsim-Soyisim"))
        self.mail_edit.setPlaceholderText(_translate("MainWindow", "Mail"))
        self.tel_no_edit.setPlaceholderText(_translate("MainWindow", "Tel No"))
        self.anahtar_edit.setPlaceholderText(_translate("MainWindow", "Anahtar"))
        self.sure_edit.setPlaceholderText(_translate("MainWindow", "Süre"))

        self.ekle_buton.setText(_translate("MainWindow", "Ekle"))

        self.tablo.setSortingEnabled(False)
        self.tablo.headerItem().setText(0, _translate("MainWindow", "id"))
        self.tablo.headerItem().setText(1, _translate("MainWindow", "isim-soyisim"))
        self.tablo.headerItem().setText(2, _translate("MainWindow", "mail"))
        self.tablo.headerItem().setText(3, _translate("MainWindow", "tel-no"))
        self.tablo.headerItem().setText(4, _translate("MainWindow", "anahtar"))
        self.tablo.headerItem().setText(5, _translate("MainWindow", "tarih"))
        self.tablo.headerItem().setText(6, _translate("MainWindow", "süre"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uyeler), _translate("MainWindow", "Üyeler"))
        self.pushButton.setText(_translate("MainWindow", "Uyarıyı Gönder"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.uyarilar), _translate("MainWindow", "Uyarılar"))

        self.tablo_elem.setSortingEnabled(False)
        self.tablo_elem.headerItem().setText(0, _translate("MainWindow", "Element Değişken İsmi"))
        self.tablo_elem.headerItem().setText(1, _translate("MainWindow", "Element Değişken Değeri"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.elementler), _translate("MainWindow", "Elementler"))

        self.functions = Functions(self)
        self.ara_buton.clicked.connect(self.functions.findText)
        self.tablo.itemChanged.connect(self.functions.editItem)
        self.tablo_elem.itemChanged.connect(self.functions.editItem_elem)
        self.ekle_buton.clicked.connect(self.functions.uye_ekle)
        self.pushButton.clicked.connect(self.uyari_gonder)

    def uyari_gonder(self):
        thread = Thread(target=self.functions.uyari_gonder, daemon=True)
        thread.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
