'''
Created on 6.2.2017

@author: heimo
'''
from addressbook.model import Contact

from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout)


class UI():  
    #actions
    CONST_ACTION_FIND = 1
    CONST_ACTION_ADD = 2
    CONST_ACTION_LIST = 3
    CONST_ACTION_EXIT = 4
    CONST_ACTION_MODIFY = 5
    CONST_ACTION_REMOVE = 6

    def __init__(self, presenter):
        self.presenter = presenter
        
    
class CUI(UI):
               
    def __init__(self, presenter):
        super().__init__(presenter)
    
    
    def main(self):
        menu = '''Valitse toiminto:
        1) Etsi yhteystietoa nimellä
        2) Lisää yhteystieto
        3) Lista kaikista yhteystiedoista
        4) Poistu ohjelmasta'''
        
        main_actions = (UI.CONST_ACTION_FIND, UI.CONST_ACTION_ADD, UI.CONST_ACTION_LIST, UI.CONST_ACTION_EXIT)
        while True:
            print(menu)
            selection = int(input('Valintasi -> '))
            if selection in main_actions:
                self.presenter.process_action(selection)
            else:
                self.showmessage('Väärä valinta!')
            
 
    def contact_menu(self, contact):
        contact_menu = '''
        1) Muokkaa yhteystietoa
        2) Poista yhteystieto
        3) Palaa takaisin'''
        
        self.showcontact(contact)
        contact_actions = (UI.CONST_ACTION_MODIFY, UI.CONST_ACTION_REMOVE)
        
        while True:
            print(contact_menu)
            selection = int(input('Valintasi -> '))
            selection += 4 #Modify selection to action id
            if selection in contact_actions:
                self.presenter.process_contact_action(selection, contact)
            elif selection == 7:
                break
            else:
                self.showmessage('Väärä valinta!')

    
    def modifycontact(self, contact):
        new_name = input('Nimi: ({}) -> '.format(contact.name))
        new_phone_number = input('Puhelinnumero: ({}) -> '.format(contact.phone_number))
        new_email = input('Sähköposti: ({}) -> '.format(contact.email))
        return Contact(new_name, new_phone_number, new_email)


    def add_contact(self):
        name = input('Nimi: ')
        phone_number = input('Puhelinnumero: ')
        email = input('Sähköposti: ')
        return Contact(name, phone_number, email)
    
        
    def searchcontact(self):
        return input('Hae nimellä -> ')    
        
    def showcontact(self, contact):
        print(contact)
        
    def showmessage(self, message):
        print(message)
        

class GUI(UI, QWidget):
    
    def __init__(self, presenter):
        UI.__init__(self, presenter)
        QWidget.__init__(self)
        self._initUI()
        
        
    def _initUI(self):
        
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        
        #Set event handlers
        #okButton.clicked.connect(self.showdialog)
        
        self.show()

        
    