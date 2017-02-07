'''
Created on 6.2.2017

@author: heimo
'''

from addressbook.model import AddressBook
from addressbook.view import UI
import copy
import sys


class Presenter:
    '''
    classdocs
    '''

    def __init__(self):
        self.addressbook = AddressBook()
    
    def set_ui(self, ui):
        self.ui = ui
    
    def _searchcontact(self, searchstring):
        contacts = self.addressbook.get_contact(searchstring)
        return contacts
                
    def _add_contact(self):
        contact = self.ui.add_contact()
        self.addressbook.add_contact(contact)
        self.ui.showmessage('Yhteystieto lisätty!')
    
    
    def _listcontacts(self):
        contacts = self.addressbook.get_contacts()
        if contacts:  
            for key, contact in contacts.items():
                self.ui.showcontact(contact)
        else:
            self.ui.showmessage('Yhteystietoja ei löytynyt!')

    
    def _modifycontact(self, contact):
        old_contact = copy.copy(contact)
        changed_contact = self.ui.modifycontact(contact)

        if changed_contact.name:
            contact.name = changed_contact.name
        if changed_contact.phone_number:
            contact.phone_number = changed_contact.phone_number
        if changed_contact.email:
            contact.email = changed_contact.phone_number
        #If contact has been modified, replace old contact with new
        if changed_contact.name or changed_contact.phone_number or changed_contact.email:
            self.addressbook.remove_contact(old_contact)
            self.addressbook.add_contact(contact) 
            self.ui.showmessage('Muutokset tallennettu!')
        else:
            self.ui.showmessage('Ei muutoksia!')
            
            
    def main(self, action):
        #Process input
        if action == UI.CONST_ACTION_FIND:
            searchstring = self.ui.searchcontact()
            contact = self._searchcontact(searchstring)
            if contact:
                self.ui.contactmenu(contact)
            else:
                self.ui.showmessage('Ei löytynyt yhteystietoja nimellä: ' + searchstring)
        elif action == UI.CONST_ACTION_ADD:
            #Add contact
            self._add_contact()
        elif action == UI.CONST_ACTION_LIST:
            #List all Contacts
            self._listcontacts()    
        elif action == UI.CONST_ACTION_EXIT:
            self.ui.showmessage('Poistutaan ohjelmasta...')
            sys.exit()
        
        
    def contactmenu(self, action, contact):
        if action == UI.CONST_ACTION_MODIFY:
            self._modifycontact(contact)
        elif action == UI.CONST_ACTION_REMOVE:
            self.ui.showmessage('Poistettu yhteystieto!')
            self.addressbook.remove_contact(contact)            
    
