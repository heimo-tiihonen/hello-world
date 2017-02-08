'''
Created on 6.2.2017

@author: heimo
'''
from addressbook.model import Contact

from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QLineEdit, QInputDialog, QMessageBox)


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
        presenter.set_ui(self)
    
    
class CUI(UI):
               
    
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
                if selection == UI.CONST_ACTION_FIND:
                    self.presenter.search_contact()
                elif selection == UI.CONST_ACTION_ADD:
                    self.presenter.add_contact()
                elif selection == UI.CONST_ACTION_LIST:
                    self.presenter.list_contacts()    
                elif selection == UI.CONST_ACTION_EXIT:
                    self.showmessage('Poistutaan ohjelmasta...')
                    break
            else:
                self.showmessage('Väärä valinta!')
            
    
    def show_contact_dialog(self, contact):
        contact_menu = '''
        1) Muokkaa yhteystietoa
        2) Poista yhteystieto
        3) Palaa takaisin'''
        
        contact_actions = (UI.CONST_ACTION_MODIFY, UI.CONST_ACTION_REMOVE)
        
        while True:
            print(contact_menu)
            selection = int(input('Valintasi -> '))
            selection += 4 #Modify selection to action id
            if selection in contact_actions:
                if selection == UI.CONST_ACTION_MODIFY:
                    self.presenter.modify_contact(contact)
                    break
                elif selection == UI.CONST_ACTION_REMOVE:
                    self.presenter.remove_contact(contact)
                    break    
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
    
        
    def get_search_string(self):
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
        
        self.okButton = QPushButton("Search")
        self.edit = QLineEdit('', self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.okButton)
        hbox.addWidget(self.edit)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()
        
        #Set event handlers
        #self.okButton.clicked.connect(self.presenter.search_contact())
           
        
    def show_contact_dialog(self):
        
        text, ok = QInputDialog.getText(self, 'Input Dialog', 
            'Enter your name:')
        
        if ok:
            self.edit.text()
                    
                    
    def get_search_string(self):
        return self.edit.text()
    
    def showmessage(self, message):
        # ok = QMessageBox.setText(self, message)
        pass
        
    