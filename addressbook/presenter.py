'''
Created on 6.2.2017

@author: heimo
'''

from addressbook.model import AddressBook
import copy


class Presenter:
    '''
    classdocs
    '''

    def __init__(self):
        self.addressbook = AddressBook()
    
    def set_ui(self, ui):
        self.ui = ui
    
    def search_contact(self):
        searchstring = self.ui.get_search_string()
        contact = self.addressbook.get_contact(searchstring)
        if contact:
            self.ui.showcontact(contact)
            self.ui.show_contact_dialog(contact)
        else:
            self.ui.showmessage('Yhteystietoa ei löytynyt nimellä: ' + searchstring)
                

    def add_contact(self):
        contact = self.ui.add_contact()
        self.addressbook.add_contact(contact)
        self.ui.showmessage('Yhteystieto lisätty!')
    
    
    def list_contacts(self):
        contacts = self.addressbook.get_contacts()
        if contacts:  
            for key, contact in contacts.items():
                self.ui.showcontact(contact)
        else:
            self.ui.showmessage('Yhteystietoja ei löytynyt!')

    def remove_contact(self, contact):
        self.addressbook.remove_contact(contact)
        self.ui.showmessage('Yhteystieto poistettu!')
        
        
    def modify_contact(self, contact):
        old_contact = copy.copy(contact)
        changed_contact = self.ui.modifycontact(contact)

        if changed_contact.name:
            contact.name = changed_contact.name
        if changed_contact.phone_number:
            contact.phone_number = changed_contact.phone_number
        if changed_contact.email:
            contact.email = changed_contact.email
        #If contact has been modified, replace old contact with new
        if changed_contact.name or changed_contact.phone_number or changed_contact.email:
            self.addressbook.remove_contact(old_contact)
            self.addressbook.add_contact(contact) 
            self.ui.showmessage('Muutokset tallennettu!')
        else:
            self.ui.showmessage('Ei muutoksia!')
    
