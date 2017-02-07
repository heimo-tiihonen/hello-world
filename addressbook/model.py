'''
Address Book

Practicing Python
'''

import pickle
import os.path

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
        self._contacts = {}

        # The name of the file where we will store the dictionary
        self._contacts_file = 'contacts.data'
        
        # Read _contacts from file if it exists 
        if os.path.isfile(self._contacts_file): 
            try:
                f = open(self._contacts_file, 'rb')
                
                # Load _contacts-dictionary from the file
                self._contacts = pickle.load(f)
                f.close()
            except IOError:
                print('I/O error ({}): {}'.format(IOError.errno, IOError.strerror))
            except pickle.PickleError as p:
                print('Pickle error: {}', p)
        
        
    def _savecontacts(self):
        try:
            f = open(self._contacts_file, 'wb')
            pickle.dump(self._contacts, f)
            f.close()
            return True
        except IOError: 
            print('I/O error ({}): {}'.format(IOError.errno, IOError.strerror))
            return False
        except pickle.PickleError as p:
            print('Pickle error: {}', p)
            return False
                
    
    def add_contact(self, contact):
        self._contacts[contact.name] = contact
        self._savecontacts()

            
    def remove_contact(self, contact):
        del self._contacts[contact.name]
        self._savecontacts()


    def get_contact(self, searchstring):
        if searchstring in self._contacts:
            return self._contacts[searchstring]
            
            
    def get_contacts(self):
        return self._contacts
        
    