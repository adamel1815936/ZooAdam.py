####################################################################################
###  420-2G4 - Programmation orientée objet
###  Travail: Exercice Gestion du zoo
###  Nom: Adam Elmouftaquir
###  No étudiant: 1815936
###  No Groupe:
###  Description du fichier: Boîte de dialogue recherche
####################################################################################

#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################


# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
# Importer la boite de dialogue
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import UI_PY.DialogRecherche
from PyQt5 import QtWidgets
# Importation des classes
from Classes.Classe_Veterinaire import *
from Classes.Classe_Animal import Animal
from Classes.Classe_Enclos import Enclos

# Liste des animaux de la listview
ls_animaux_listview = []


######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetrerecherche(QtWidgets.QDialog, UI_PY.DialogRecherche.Ui_Dialog):
    def __init__(self, parent=None):
        """
        Constructeur de la fenêtre qui affiche la liste des étudiants
        """
        super(Fenetrerecherche, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Boîte de dialogue Recherche")

    @pyqtSlot()
    def on_pushButton_afficher_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Afficher
        """
        # Instancier un objet et remplir la comboBox avec les numéros d'enclos tirés de la liste des enclos
        MaRecherche = Recherche()
        MaRecherche.list_enclos = self.comboBox_enclos_animal.currentText()
        # Instancier une boite de dialogue FenetreRecherche
        dialog = FenetreRecherche()
        # Préparer la listview
        model = QStandardItemModel()
        dialog.ls_animaux_listview.setModel(model)
        for elt in Animal.ls_animaux:
            item = QStandardItem(elt.Numero_animal + " : Enclos " + elt.Enclos)
            model.appendRow(item)
        # Afficher la boite de dialogue
        dialog.show()
        dialog.exec_()
