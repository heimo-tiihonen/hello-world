'''
Created on 6.2.2017

@author: heimo
'''


class Presenter:
    '''
    classdocs
    '''

    def __init__(self, model):
        self.addressbook = model
        
        
    def set_ui(self, ui):
        self.ui = ui
    
    
    def search_contact(self):
        searchstring = self.ui.get_search_string()
        contact = self.addressbook.get_contact(searchstring)
        if contact:
            self.ui.show_contact(contact)
            self.ui.show_contact_dialog(contact)
        else:
            self.ui.showmessage('Yhteystietoa ei löytynyt nimellä: ' + searchstring)
                

    def add_contact(self):
        contact = self.ui.add_contact()
        success = self.addressbook.add_contact(contact)
        if success:
            self.ui.showmessage('Yhteystieto lisätty!')
        else:
            self.ui.showmessage('Yhteystietoa ei voitu lisätä!')
    
    
    def list_contacts(self):
        contacts = self.addressbook.get_contacts()
        if contacts:  
            self.ui.list_contacts(contacts)
        else:
            self.ui.showmessage('Yhteystietoja ei löytynyt!')


    def remove_contact(self, contact_name):
        self.addressbook.remove_contact(contact_name)
        self.ui.showmessage('Yhteystieto poistettu!')
        
        
    def modify_contact(self, contact_name):
        contact = self.addressbook.get_contact(contact_name)
        old_contact_name = contact.name
        changed_contact = self.ui.modify_contact(contact)

        self.addressbook.remove_contact(old_contact_name)
        self.addressbook.add_contact(changed_contact) 
        self.ui.showmessage('Muutokset tallennettu!')
   
        
class PresenterGUI(Presenter):

    def add_contact(self):
        
        contact = self.ui.add_contact()      
        success = self.addressbook.add_contact(contact)
        if success:
            self.ui.add_list_item(contact.name)
            self.ui.deactivate_selection_actions()
            self.ui.showmessage('Yhteystieto lisätty!')
        else:
            self.ui.showmessage('Yhteystietoa ei voitu lisätä!')
    
    
    def modify_contact(self):
        contact_name = self.ui.get_selected_contact()
        super().modify_contact(contact_name)
    
    
    def remove_contact(self):
        contact_name = self.ui.get_selected_contact()
        self.ui.remove_selected_item()
        self.ui.deactivate_selection_actions()
        super().remove_contact(contact_name)
        
        
    def selection_changed(self):
        self.ui.activate_selection_actions()
