'''
Address Book

Practicing Python
'''

import pickle
import os.path
from sqlalchemy import Column, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


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
                

class Model:
    def __init__(self):
        self._contacts = {}


    def add_contact(self, contact):
        if not contact.name in self._contacts:
            self._contacts[contact.name] = contact
            self._savecontacts()
            return True
        else:
            return False

            
    def remove_contact(self, contact_name):
        del self._contacts[contact_name]
        self._savecontacts()


    def get_contact(self, searchstring):
        if searchstring in self._contacts:
            return self._contacts[searchstring]
            
            
    def get_contacts(self):
        return self._contacts
    
    
class ModelPickle(Model):
    def __init__(self):
        super().__init__()

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
        

class ModelDB(Model):
    engine = create_engine('sqlite://///Users//heimo//Source//harjoitus//addressbook//contacts.db', echo=True)   
    Base = declarative_base(bind=engine)
    Session = sessionmaker(bind=engine)
        
    def __init__(self):
        super().__init__()
        self.session = ModelDB.Session()
        #ModelDB.Base.metadata.create_all()
        for contact in self.session.query(ContactMapping):
            self._contacts[contact.name] = contact        
        
        
    def _savecontacts(self):
        ModelDB.Base.metadata.drop_all()
        ModelDB.Base.metadata.create_all()
        
        for key, contact in self._contacts.items():
            self.session.add(contact)
        self.session.commit()

    def add_contact(self, contact):
        if not contact.name in self._contacts:
            self._contacts[contact.name] = ContactMapping(contact)
            self._savecontacts()
            return True
        else:
            return False
        
        
class ContactMapping(Contact, ModelDB.Base):
    __tablename__ = 'contacts'
    name = Column(String(20), primary_key=True)
    phone_number = Column(String(20))
    email = Column(String(20))

    def __init__(self, contact):
        super().__init__(contact.name, contact.phone_number, contact.email)
