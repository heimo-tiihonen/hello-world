'''
Created on 6.2.2017

@author: heimo
'''
from addressbook.model import Contact

from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QLineEdit, QInputDialog, QMessageBox, QListWidget, QListWidgetItem)


class UI():  
        
    #actions - TODO: These can be removed
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
                    self.presenter.modify_contact(contact.name)
                    break
                elif selection == UI.CONST_ACTION_REMOVE:
                    self.presenter.remove_contact(contact.name)
                    break    
            elif selection == 7: 
                break
            else:
                self.showmessage('Väärä valinta!')

    
    def modify_contact(self, contact):
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
    
    
    def show_contact(self, contact):
        '''Show contact
        
        bool = True if called from search action'''
        
        print(contact)
    
        
    def showmessage(self, message):
        print(message)
    
    def list_contacts(self, contacts):
        for key, contact in contacts.items():
            self.show_contact(contact)
        

class GUI(UI, QWidget):
    
    def __init__(self, presenter):
        UI.__init__(self, presenter)
        QWidget.__init__(self)
        self.list_items = []
        self._initUI()
        
        
    def _initUI(self):
        
        self.search_button = QPushButton("Search")
        self.add_button = QPushButton("Add")
        self.edit_button = QPushButton("Edit")
        self.delete_button = QPushButton("Delete")
        self.edit = QLineEdit('', self)
        self.list = QListWidget(self)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.search_button)
        hbox.addWidget(self.edit)
        self.presenter.list_contacts()

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.add_button)
        hbox2.addWidget(self.edit_button)
        hbox2.addWidget(self.delete_button)
        self.deactivate_selection_actions()
        
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.list)
        vbox.addLayout(hbox2)
        
        self.setLayout(vbox)    
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Address Book')
        self.show()
        
        #Set event handlers
        self.search_button.clicked.connect(self.presenter.search_contact)
        self.add_button.clicked.connect(self.presenter.add_contact)
        self.edit_button.clicked.connect(self.presenter.modify_contact)
        self.delete_button.clicked.connect(self.presenter.remove_contact)
        self.list.itemSelectionChanged.connect(self.presenter.selection_changed)
        
        
    def show_contact_dialog(self, contact):
        #TODO: activate edit and modify buttons
        pass
                    
    def get_search_string(self):
        return self.edit.text()
    
    
    def showmessage(self, message):
        mb = QMessageBox()
        mb.setText(message)
        mb.exec()
        
        
    def show_contact(self, contact):
        if contact.name in self.list_items:
            self.list.setCurrentRow(self.list_items.index(contact.name))
        else:
            return Exception('TODO') #TODO: Return exception
    
    
    def modify_contact(self, contact):
        #Show contact edit form
        return Contact(contact.name, contact.phone_number, contact.email)
      

    def list_contacts(self, contacts):
        for key, contact in contacts.items():
            self.list_items.append(contact.name) 
            self.list.addItem(contact.name)
    
    
    def add_contact(self):
        contact = Contact('nimi', '123456', 'email@domain.com')
        return contact
    
    
    def add_list_item(self, name):
        self.list_items.append(name)
        self.list.addItem(name)
    
    
    def remove_selected_item(self):
        selected = self.list.currentRow()
        self.list.takeItem(selected)
        
        
    def get_selected_contact(self):
        selected = self.list.currentRow()
        return self.list_items[selected]
    
    
    def activate_selection_actions(self):
        self.edit_button.setEnabled(True)
        self.delete_button.setEnabled(True)
        
        
    def deactivate_selection_actions(self):
        self.edit_button.setDisabled(True)
        self.delete_button.setDisabled(True)
        
    