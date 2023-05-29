####################################################################################
###  420-2G4 - Programmation orientée objet
###  Travail: Exercice Gestion du zoo
###  Nom: Adam Elmouftaquir
###  No étudiant: 1815936
###  No Groupe:
###  Description du fichier: Boîte de dialogue animal
####################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################

# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
import UI_PY.Dialog_animal
from PyQt5 import QtWidgets
# Importation des classes
from Classes.Classe_Animal import *
from Classes.Classe_Enclos import Enclos
from Classes.Classe_Mammifere import Mammifere
from Classes.Classe_Oiseau import Oiseau
from Classes.Classe_Reptile import Reptile
from PyQt5 import QtWidgets
# Pour les gestionnaires d'événements
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem


def Verifier_numero_animal_existe(p_numero_animal):
    """
    Vérifier si le numéro d'animal est déjà présent
    """
    for elt in Animal.ls_animaux:
        if elt.Numero_Animal == p_numero_animal:
            return True
        else:
            return False


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetreanimal(QtWidgets.QDialog, UI_PY.Dialog_animal.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetreanimal, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue animal")

    def Reinitialiser_label_erreur(self):
        """
        Réinitialiser les labels d'erreur
        """
        self.label_erreur_numero_animal_existe.setVisible(False)
        self.label_erreur_numero_animal_existe_pas.setVisible(False)
        self.label_erreur_numero_animal_invalide.setVisible(False)
        self.label_erreur_poids_animal.setVisible(False)
        self.label_erreur_longueur_bec.setVisible(False)

    def Reinitialiser_controles(self):
        """
        Réinitialiser les lineEdits
        """
        self.lineEdit_numero_animal.clear()
        self.lineEdit_surnom_animal.clear()
        self.lineEdit_poids_animal.clear()
        self.lineEdit_longueur_bec.clear()

    @pyqtSlot()
    # Bouton Ajouter animal
    def on_pushButton_Ajouter_animal_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Cacher les labels qui affichent les erreurs
        self.Reinitialiser_label_erreur()
        # Instancier un objet
        MonAnimal = Animal()
        # Entrée de donnée pour les attributs de l'objet et validations
        MonAnimal.Numero_animal = self.lineEdit_numero_animal.text()
        if MonAnimal.Numero_animal == "":
            self.label_erreur_numero_animal_invalide.setVisible(True)
        else:
            Verifier_numero_animal = Verifier_numero_animal_existe(MonAnimal.Numero_animal)
            if Verifier_numero_animal:
                self.label_erreur_numero_animal_existe.setVisible(True)
        MonAnimal.Surnom = self.lineEdit_surnom_animal.text()
        MonAnimal.Poids = self.lineEdit_poids_animal.text()
        if MonAnimal.Poids == "":
            self.label_erreur_poids_animal.setVisible(True)
        MonAnimal.Famille = self.comboBox_famille_animal.currentText()
        MonAnimal.Enclos = self.comboBox_enclos_animal.currentText()
        MonAnimal.Couleur_poil = self.comboBox_couleur_poil.currentText()
        MonAnimal.Longueur_bec = self.lineEdit_longueur_bec.text()
        if MonAnimal.Longueur_bec == "":
            self.label_erreur_longueur_bec.setVisible(True)
        MonAnimal.Venimeux = self.comboBox_venimeux.currentText()
        # Si toutes les validations sont bonnes, ajouter l'objet instancié dans la liste:
        if MonAnimal.Numero_animal != "" and MonAnimal.Poids != "" and MonAnimal.Longueur_bec != "" and not Verifier_numero_animal_existe:
            # Ajouter l'objet instancié à la liste
            Animal.ls_animaux.append(MonAnimal)
            # Réinitialiser les contrôles
            self.Reinitialiser_controles()

    @pyqtSlot()
    # Bouton Rechercher animal
    def on_pushButton_Rechercher_animal_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Rechercher
        """
        # Cacher les labels qui affichent les erreurs
        self.Reinitialiser_label_erreur()
        # Instancier un objet
        MonAnimal = Animal()
        # Saisie de donnée de recherche pour les attributs de l'objet et validations
        MonAnimal.Numero_animal = self.lineEdit_numero_animal.setText("")
        if MonAnimal.Numero_animal == "":
            self.label_erreur_numero_animal_invalide.setVisible(True)
        else:
            Verifier_numero_animal = Verifier_numero_animal_existe(MonAnimal.Numero_animal)
            if Verifier_numero_animal:
                self.label_erreur_numero_animal_existe.setVisible(True)
        MonAnimal.Surnom = self.lineEdit_surnom_animal.setText("")
        MonAnimal.Poids = self.lineEdit_poids_animal.setText("")
        if MonAnimal.Poids == "":
            self.label_erreur_poids_animal.setVisible(True)
        MonAnimal.Famille = self.comboBox_famille_animal.setItemText(0, "")
        MonAnimal.Enclos = self.comboBox_enclos_animal.setItemText(0, "")
        MonAnimal.Couleur_poil = self.comboBox_couleur_poil.setItemText(0, "")
        MonAnimal.Longueur_bec = self.lineEdit_longueur_bec.setText("")
        if MonAnimal.Longueur_bec == "":
            self.label_erreur_longueur_bec.setVisible(True)
        MonAnimal.Venimeux = self.comboBox_venimeux.setItemText(0, "")
        # Si toutes les validations sont bonnes, vérifier si l'objet recherché est dans la liste:
        if MonAnimal.Numero_animal != "" and MonAnimal.Poids != "" and MonAnimal.Longueur_bec != "" and not Verifier_numero_animal_existe:
            for elt in Animal.ls_animaux:
                # Chercher dans la liste des animaux un animal qui correspond au numéro entré
                if elt.Numero_Animal == self.lineEdit_numero_animal.text():
                    elt.Surnom = self.lineEdit_surnom_animal.text()
                    elt.Poids = self.lineEdit_poids_animal.text()
                    elt.Famille = self.comboBox_famille_animal.currentText()
                    elt.Enclos = self.comboBox_enclos_animal.currentText()
                    elt.Couleur_poil = self.comboBox_couleur_poil.currentText()
                    elt.Longueur_bec = self.lineEdit_longueur_bec.text()
                    elt.Venimeux = self.comboBox_venimeux.currentText()
            Animal.ls_animaux.index(MonAnimal)
            # Réinitialiser les contrôles
            self.Reinitialiser_controles()
