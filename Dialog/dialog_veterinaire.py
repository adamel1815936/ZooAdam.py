####################################################################################
###  420-2G4 - Programmation orientée objet
###  Travail: Exercice Gestion du zoo
###  Nom: Adam Elmouftaquir
###  No étudiant: 1815936
###  No Groupe:
###  Description du fichier: Boîte de dialogue vétérinaire
####################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot, QDate
# Importer la boite de dialogue
import UI_PY.Dialog_veterinaire
from PyQt5 import QtWidgets
# Importation des classes
from Classes.Classe_Veterinaire import *
from Classes.Classe_Animal import *
from Classes.Classe_Enclos import Enclos
from Classes.Classe_Mammifere import Mammifere
from Classes.Classe_Oiseau import Oiseau
from Classes.Classe_Reptile import Reptile
from PyQt5 import QtWidgets
# Pour les gestionnaires d'événements
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# Liste des items de la listview cours choisis
list_enclos_listview = []


def Verifier_numero_employe_existe(p_numero_emp):
    """
    Vérifier si le numéro d'employé est déjà présent
    """
    for elt in Veterinaire.ls_veterinaire:
        if elt.Numero_emp == p_numero_emp:
            return True
        else:
            return False


def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_erreur_numero_employe__existe.setVisible(False)
    objet.label_erreur_numero_employe_existe_pas.setVisible(False)
    objet.label_erreur_numero_employe_invalide.setVisible(False)
    objet.label_erreur_nom_employe.setVisible(False)
    objet.label_erreur_date_naiss.setVisible(False)
    objet.label_erreur_prenom_employe.setVisible(False)
    objet.label_erreur_fichier.setText("")


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreveterinaire(QtWidgets.QDialog, UI_PY.Dialog_veterinaire.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreveterinaire, self).__init__(parent)
        self.model = None
        self.label_erreur_fichier = None
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Vétérinaire")

    @pyqtSlot()
    # Bouton Serialiser
    def on_pushButton_serialiser_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Instancier un objet
        MonVeterinaire = Veterinaire()
        # Données pour les attributs de l'objet Vétérinaire
        MonVeterinaire.Numero_emp = self.lineEdit_numero_employe.text()
        MonVeterinaire.Nom = self.lineEdit_nom_employe.text()
        MonVeterinaire.Date_naiss = self.dateEdit_datenaiss_employe.date()
        MonVeterinaire.Prenom = self.lineEdit_prenom_employe.text()
        MonVeterinaire.list_enclos = self.comboBox_enclos_animal.currentText()
        # Si le numéro, le nom, la date de naissance et le prénom sont valides :
        if MonVeterinaire.Numero_emp != "" and MonVeterinaire.Nom != "" and MonVeterinaire.Date_naiss != "" and MonVeterinaire.Prenom != "":
            # Sérialiser l'objet en question
            result = MonVeterinaire.serialiser(
                "." + "/" + "code_veterinaire" + "/" + MonVeterinaire.Numero_emp + "_" + MonVeterinaire.Nom + "_" + MonVeterinaire.Date_naiss + "_" + MonVeterinaire.Prenom + ".json")
            # Si la sérialisation fonctionne
            if result == 0:
                # Réinitialiser les lineEdit et le dateEdit
                self.lineEdit_numero_employe.clear()
                self.lineEdit_nom_employe.clear()
                self.dateEdit_datenaiss_employe.setDate(QDate(2000, 1, 1))
                self.lineEdit_prenom_employe.clear()
                self.label_erreur_fichier.setText("")
            # Si ça ne fonctionne pas, afficher les messages d'erreur
            elif result == 1:
                # Afficher le message d'erreur d'écriture dans le fichier
                self.label_erreur_fichier.setText("<font color=\"#ff0000\">Erreur d'écriture dans le fichier</font>")
            else:
                # Afficher le message d'erreur d'ouverture du fichier
                self.label_erreur_fichier.setText("<font color=\"#ff0000\">Erreur d'ouverture du fichier</font>")
        # Si le numéro est invalide, afficher un message d'erreur
        if MonVeterinaire.Numero_emp == "":
            self.lineEdit_numero_employe.clear()
            self.label_erreur_numero_employe_invalide.setVisible(True)
        # Si le nom d'employé est invalide, effacer le lineEdit du nom d'employé et afficher un message d'erreur
        if MonVeterinaire.Nom == "":
            self.lineEdit_nom_employe.clear()
            self.label_erreur_nom_employe.setVisible(True)
        # Si la date de naissance d'employé est invalide, afficher un message d'erreur
        if MonVeterinaire.Date_naiss == "":
            self.label_erreur_date_naiss.setVisible(True)
        # Si le prénom est invalide, afficher un message d'erreur
        if MonVeterinaire.Prenom == "":
            self.lineEdit_nom_employe.clear()
            self.lineEdit_prenom_employe.setVisible(True)

    @pyqtSlot()
    def on_pushButton_ajouter_enclos_listview_clicked(self):
        # Verifier que l'item n'a pas été déjà ajouté à la listview
        trouv = False
        for elt in list_enclos_listview:
            if elt == self.comboBox_enclos_animal.currentText():
                trouv = True
        if not trouv:
            # Ajouter l'enclos (l'item en question) à la listView
            item = QStandardItem(self.comboBox_enclos_animal.currentText())
            self.model.appendRow(item)
            list_enclos_listview.append(self.comboBox_enclos_animal.currentText())
