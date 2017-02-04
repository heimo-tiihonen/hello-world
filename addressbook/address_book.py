'''
Address Book

Practicing Python
'''

import pickle
import os.path
import copy

class Contact:
       
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    
    def __str__(self):
        return '''        Nimi: {}
        Puhelinnumero: {}
        Sähköposti: {}
        -----------------------------------'''.format(self.name, self.phone_number, self.email)
                

class AddressBook:
    def __init__(self):
        self.contacts = {}
        # The name of the file where we will store the dictionary
        self.contacts_file = 'contacts.data'
        
        # Read contacts from file if it exists 
        if os.path.isfile(self.contacts_file): 
            try:
                f = open(self.contacts_file, 'rb')
                
                # Load contacts-dictionary from the file
                self.contacts = pickle.load(f)
                f.close()
            except IOError:
                print('I/O error ({}): {}'.format(IOError.errno, IOError.strerror))
            except pickle.PickleError as p:
                print('Pickle error: {}', p)
        
        
    def _savecontacts(self):
        try:
            f = open(self.contacts_file, 'wb')
            pickle.dump(self.contacts, f)
            f.close()
        except IOError: 
            print('I/O error ({}): {}'.format(IOError.errno, IOError.strerror))
        except pickle.PickleError as p:
            print('Pickle error: {}', p)
            

    def _mainmenu(self):
        menu = '''Valitse toiminto:
        1) Etsi yhteystietoa nimellä
        2) Lisää yhteystieto
        3) Lista kaikista yhteystiedoista
        4) Poistu ohjelmasta'''
        
        while True:
            print(menu)
            menu_command = input('Valintasi -> ')
        
            #Process input
            if menu_command == '1':
                #Search for contact
                self._searchcontact()
            elif menu_command == '2':
                #Add contact
                self._addcontact()
            elif menu_command == '3':
                #List all Contacts
                self._listcontacts()
            elif menu_command == '4':
                #exit program
                print('Poistutaan ohjelmasta...')
                break
            else:
                #Print error message
                print('Väärä valinta!')
                
        
    def _contactmenu(self, contactkey):
        contact_menu = '''
        1) Muokkaa yhteystietoa
        2) Poista yhteystieto
        3) Palaa takaisin'''
        
        while True:
            print(contact_menu)
            menu_command = input('Valintasi -> ');
            if menu_command == '1':
                self._modifycontact(self.contacts[contactkey])
                break
            elif menu_command == '2':
                print('Poistettu yhteystieto {}'.format(self.contacts[contactkey]))
                del self.contacts[contactkey]
                self._savecontacts()
                break
            elif menu_command == '3':
                break
            else:
                print('Väärä valinta!')
                
        
    def _addcontact(self):
        name = input('Nimi: ')
        phone_number = input('Puhelinnumero: ')
        email = input('Sähköposti: ')
        self.contacts[name] = Contact(name, phone_number, email)
        self._savecontacts()
    
        
    def _listcontacts(self):
        if self.contacts:  
            for key, contact in self.contacts.items():
                print(contact)
        else:
            print('Yhteystietoja ei löytynyt!')
            
               
    
    def _searchcontact(self):
        searchstring = input('Hae nimellä -> ')
        if searchstring in self.contacts:
            print(self.contacts[searchstring])
            self._contactmenu(searchstring)
        else:
            print('Yhteystietoa ei löytynyt.')
        
    
    def _modifycontact(self, contact):
        contact_old = copy.copy(contact)
        name = input('Nimi: ({}) -> '.format(contact.name))
        phone_number = input('Puhelinnumero: ({}) -> '.format(contact.phone_number))
        email = input('Sähköposti: ({}) -> '.format(contact.email))
        namechanged = False
        if name:
            contact.name = name
            namechanged = True
        if phone_number:
            contact.phone_number = phone_number
        if email:
            contact.email = phone_number
        #If contact has been modified, save all contacts
        if name or phone_number or phone_number:
            if namechanged:
                del self.contacts[contact_old.name]
                self.contacts[name] = contact 
            self._savecontacts()
            print('Tallennettu!')
        else:
            print('Ei muutoksia!')
            
        
    def run(self):     
        self._mainmenu()
        
    
if __name__ == '__main__':
    ab = AddressBook()
    ab.run()
    
    
