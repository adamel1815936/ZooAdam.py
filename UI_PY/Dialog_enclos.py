# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Brouillon2\Dialog_enclos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(755, 641)
        self.label_numero_enclos = QtWidgets.QLabel(Dialog)
        self.label_numero_enclos.setGeometry(QtCore.QRect(80, 70, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_numero_enclos.setFont(font)
        self.label_numero_enclos.setObjectName("label_numero_enclos")
        self.lineEdit_numero_enclos = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_numero_enclos.setGeometry(QtCore.QRect(80, 100, 181, 41))
        self.lineEdit_numero_enclos.setObjectName("lineEdit_numero_enclos")
        self.lineEdit_nom_enclos = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_nom_enclos.setGeometry(QtCore.QRect(80, 220, 181, 41))
        self.lineEdit_nom_enclos.setObjectName("lineEdit_nom_enclos")
        self.label_nom_enclos = QtWidgets.QLabel(Dialog)
        self.label_nom_enclos.setGeometry(QtCore.QRect(80, 190, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_nom_enclos.setFont(font)
        self.label_nom_enclos.setObjectName("label_nom_enclos")
        self.label_taille_enclos = QtWidgets.QLabel(Dialog)
        self.label_taille_enclos.setGeometry(QtCore.QRect(80, 310, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_taille_enclos.setFont(font)
        self.label_taille_enclos.setObjectName("label_taille_enclos")
        self.comboBox_taille_enclos = QtWidgets.QComboBox(Dialog)
        self.comboBox_taille_enclos.setGeometry(QtCore.QRect(80, 340, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_taille_enclos.setFont(font)
        self.comboBox_taille_enclos.setObjectName("comboBox_taille_enclos")
        self.comboBox_taille_enclos.addItem("")
        self.comboBox_taille_enclos.addItem("")
        self.comboBox_taille_enclos.addItem("")
        self.label_type_enclos = QtWidgets.QLabel(Dialog)
        self.label_type_enclos.setGeometry(QtCore.QRect(480, 190, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_type_enclos.setFont(font)
        self.label_type_enclos.setObjectName("label_type_enclos")
        self.comboBox_type_enclos = QtWidgets.QComboBox(Dialog)
        self.comboBox_type_enclos.setGeometry(QtCore.QRect(480, 220, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_type_enclos.setFont(font)
        self.comboBox_type_enclos.setObjectName("comboBox_type_enclos")
        self.comboBox_type_enclos.addItem("")
        self.comboBox_type_enclos.addItem("")
        self.comboBox_type_enclos.addItem("")
        self.comboBox_type_enclos.setItemText(2, "")
        self.comboBox_localisation = QtWidgets.QComboBox(Dialog)
        self.comboBox_localisation.setGeometry(QtCore.QRect(480, 350, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_localisation.setFont(font)
        self.comboBox_localisation.setObjectName("comboBox_localisation")
        self.comboBox_localisation.addItem("")
        self.comboBox_localisation.addItem("")
        self.comboBox_localisation.addItem("")
        self.label_localisation = QtWidgets.QLabel(Dialog)
        self.label_localisation.setGeometry(QtCore.QRect(480, 320, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_localisation.setFont(font)
        self.label_localisation.setObjectName("label_localisation")
        self.pushButton_Ajouter_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_Ajouter_enclos.setGeometry(QtCore.QRect(80, 460, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_Ajouter_enclos.setFont(font)
        self.pushButton_Ajouter_enclos.setObjectName("pushButton_Ajouter_enclos")
        self.pushButton_supprimer_enclos = QtWidgets.QPushButton(Dialog)
        self.pushButton_supprimer_enclos.setGeometry(QtCore.QRect(480, 460, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_supprimer_enclos.setFont(font)
        self.pushButton_supprimer_enclos.setObjectName("pushButton_supprimer_enclos")
        self.label_erreur_numero_enclos_existe = QtWidgets.QLabel(Dialog)
        self.label_erreur_numero_enclos_existe.setGeometry(QtCore.QRect(80, 150, 211, 16))
        self.label_erreur_numero_enclos_existe.setObjectName("label_erreur_numero_enclos_existe")
        self.label_erreur_numero_enclos_existe_pas = QtWidgets.QLabel(Dialog)
        self.label_erreur_numero_enclos_existe_pas.setGeometry(QtCore.QRect(80, 160, 211, 16))
        self.label_erreur_numero_enclos_existe_pas.setObjectName("label_erreur_numero_enclos_existe_pas")
        self.label_erreur_validation_numero_enclos = QtWidgets.QLabel(Dialog)
        self.label_erreur_validation_numero_enclos.setGeometry(QtCore.QRect(80, 170, 421, 31))
        self.label_erreur_validation_numero_enclos.setObjectName("label_erreur_validation_numero_enclos")
        self.label_erreur_nom_enclos = QtWidgets.QLabel(Dialog)
        self.label_erreur_nom_enclos.setGeometry(QtCore.QRect(80, 270, 421, 31))
        self.label_erreur_nom_enclos.setObjectName("label_erreur_nom_enclos")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_numero_enclos.setText(_translate("Dialog", "Numéro enclos"))
        self.label_nom_enclos.setText(_translate("Dialog", "Nom enclos"))
        self.label_taille_enclos.setText(_translate("Dialog", "Taille enclos"))
        self.comboBox_taille_enclos.setItemText(0, _translate("Dialog", "Petit"))
        self.comboBox_taille_enclos.setItemText(1, _translate("Dialog", "Moyen"))
        self.comboBox_taille_enclos.setItemText(2, _translate("Dialog", "Grand"))
        self.label_type_enclos.setText(_translate("Dialog", "Type enclos"))
        self.comboBox_type_enclos.setItemText(0, _translate("Dialog", "Intérieur"))
        self.comboBox_type_enclos.setItemText(1, _translate("Dialog", "Extérieur"))
        self.comboBox_localisation.setItemText(0, _translate("Dialog", "Section A"))
        self.comboBox_localisation.setItemText(1, _translate("Dialog", "Section B"))
        self.comboBox_localisation.setItemText(2, _translate("Dialog", "Section C"))
        self.label_localisation.setText(_translate("Dialog", "Localisation"))
        self.pushButton_Ajouter_enclos.setText(_translate("Dialog", "Ajouter enclos"))
        self.pushButton_supprimer_enclos.setText(_translate("Dialog", "Supprimer enclos"))
        self.label_erreur_numero_enclos_existe.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff0000;\">Ce numéro d\'enclos existe déjà</span></p></body></html>"))
        self.label_erreur_numero_enclos_existe_pas.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff0000;\">Ce numéro d\'enclos n\'existe pas</span></p></body></html>"))
        self.label_erreur_validation_numero_enclos.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; color:#ff0000;\">Entrer un </span><span style=\" font-family:\'Arial,sans-serif\'; font-size:9pt; color:#ff0000;\">nombre entier sur 5 caractères suivi de trois lettres</span></p></body></html>"))
        self.label_erreur_nom_enclos.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-family:\'Arial,sans-serif\'; font-size:9pt; color:#ff0000;\">Alphabétique de longueur maximale égale à  25 lettres.</span><span style=\" font-family:\'Arial,sans-serif\'; font-size:9pt; font-weight:600; color:#ff0000;\"/></p></body></html>"))
