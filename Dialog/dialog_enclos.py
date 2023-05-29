####################################################################################
###  420-2G4 - Programmation orientée objet
###  Travail: Exercice Gestion du zoo
###  Nom: Adam Elmouftaquir
###  No étudiant: 1815936
###  No Groupe:
###  Description du fichier: Boîte de dialogue enclos
####################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_enclos
# Importation des classes
from Classes.Classe_Enclos import *
from PyQt5 import QtWidgets
# Pour les gestionnaires d'événements
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem


def Verifier_numero_enclos_existe(p_numero_enclos):
    """
    Vérifier si l'enclos est déjà présent
    """
    for elt in Enclos.ls_enclos:
        if elt.Numero_enclos == p_numero_enclos:
            return True
        else:
            return False


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreenclos(QtWidgets.QDialog, UI_PY.Dialog_enclos.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreenclos, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Enclos")

    def Reinitialiser_label_erreur(self):
        """
        Réinitialiser les labels d'erreur
        """
        self.label_erreur_numero_enclos_existe.setVisible(False)
        self.label_erreur_numero_enclos_existe_pas.setVisible(False)
        self.label_erreur_validation_numero_enclos.setVisible(False)
        self.label_erreur_nom_enclos.setVisible(False)

    def Reinitialiser_controles(self):
        """
        Réinitialiser les lineEdits
        """
        self.lineEdit_numero_enclos.clear()
        self.lineEdit_nom_enclos.clear()

    @pyqtSlot()
    # Bouton Ajouter enclos
    def on_pushButton_Ajouter_enclos_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Cacher les labels qui affichent les erreurs
        self.Reinitialiser_label_erreur()
        # Instancier un objet
        MonEnclos = Enclos()
        # Entrée de donnée pour les attributs de l'objet et validations
        MonEnclos.Numero_enclos = self.lineEdit_numero_enclos.text()
        if MonEnclos.Numero_enclos == "":
            self.label_erreur_validation_numero_enclos.setVisible(True)
        else:
            Verifier_numero_enclos = Verifier_numero_enclos_existe(MonEnclos.Numero_enclos)
            if Verifier_numero_enclos:
                self.label_erreur_numero_enclos_existe.setVisible(True)
        MonEnclos.Nom_enclos = self.lineEdit_nom_enclos.text()
        if MonEnclos.Nom_enclos == "":
            self.label_erreur_nom_enclos.setVisible(True)
        MonEnclos.Type = self.comboBox_type_enclos.currentText()
        MonEnclos.Taille = self.comboBox_taille_enclos.currentText()
        MonEnclos.Localisation = self.comboBox_localisation.currentText()
        # Si toutes les validations sont bonnes, ajouter l'objet instancié dans la liste
        if MonEnclos.Numero_enclos != "" and MonEnclos.Nom_enclos != "" and not Verifier_numero_enclos_existe:
            # Ajouter l'objet instancié à la liste
            Enclos.ls_enclos.append(MonEnclos)
            # Réinitialiser les contrôles
            self.Reinitialiser_controles()

    @pyqtSlot()
    # Bouton Supprimer enclos
    def pushButton_supprimer_enclos_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Cacher les labels qui affichent les erreurs
        self.Reinitialiser_label_erreur()
        # Instancier un objet
        MonEnclos = Enclos()
        # Entrée de donnée pour les attributs de l'objet et validations
        MonEnclos.Numero_enclos = self.lineEdit_numero_enclos.text()
        if MonEnclos.Numero_enclos == "":
            self.label_erreur_validation_numero_enclos.setVisible(True)
        else:
            Verifier_numero_enclos = Verifier_numero_enclos_existe(MonEnclos.Numero_enclos)
            if Verifier_numero_enclos:
                self.label_erreur_numero_enclos_existe.setVisible(True)
        MonEnclos.Nom_enclos = self.lineEdit_nom_enclos.text()
        if MonEnclos.Nom_enclos == "":
            self.label_erreur_nom_enclos.setVisible(True)
        MonEnclos.Type = self.comboBox_type_enclos.currentText()
        MonEnclos.Taille = self.comboBox_taille_enclos.currentText()
        MonEnclos.Localisation = self.comboBox_localisation.currentText()
        # Si le numéro, le nom et que le numéro n'existe pas dans la liste:
        if MonEnclos.Numero_enclos != "" and MonEnclos.Nom_enclos != "" and not Verifier_numero_enclos_existe:
            # Supprimer l'objet instancié à la liste
            Enclos.ls_enclos.remove(MonEnclos)
            # Réinitialiser les contrôles
            self.Reinitialiser_controles()
