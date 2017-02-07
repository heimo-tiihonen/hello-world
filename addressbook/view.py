'''
Created on 6.2.2017

@author: heimo
'''
from addressbook.model import Contact

from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout)


class UI():  
    #Main menu actions
    CONST_ACTION_FIND = '1'
    CONST_ACTION_ADD = '2'
    CONST_ACTION_LIST = '3'
    CONST_ACTION_EXIT = '4'
    
    #Contact-menu actions
    CONST_ACTION_MODIFY = '1'
    CONST_ACTION_REMOVE = '2'
    CONST_ACTION_RETURN = '3'

    def __init__(self, presenter):
        self.presenter = presenter
        
    
class CUI(UI):
               
    def init(self):
        super().__init__()
    
    
    def main(self):
        menu = '''Valitse toiminto:
        {}) Etsi yhteystietoa nimellä
        {}) Lisää yhteystieto
        {}) Lista kaikista yhteystiedoista
        {}) Poistu ohjelmasta'''.format(UI.CONST_ACTION_FIND, UI.CONST_ACTION_ADD, UI.CONST_ACTION_LIST, UI.CONST_ACTION_EXIT )

        main_menu_actions = (UI.CONST_ACTION_FIND, UI.CONST_ACTION_ADD, UI.CONST_ACTION_LIST, UI.CONST_ACTION_EXIT)
        
        while True:
            print(menu)
            action = input('Valintasi -> ')
            if action in main_menu_actions:
                self.presenter.main(action)
            else:
                self.showmessage('Väärä valinta!')
            
 
    def contactmenu(self):
        contact_menu = '''
        {}) Muokkaa yhteystietoa
        {}) Poista yhteystieto
        {}) Palaa takaisin'''.format(UI.CONST_ACTION_MODIFY, UI.CONST_ACTION_REMOVE, UI.CONST_ACTION_RETURN)
        
        print(contact_menu)
        return input('Valintasi -> ')
             
    
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
    
    def __init__(self):
        super().__init__()
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

        
    