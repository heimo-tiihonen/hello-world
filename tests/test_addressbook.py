'''
Created on 4.2.2017

@author: heimo
'''
import unittest
from addressbook.model import Model, Contact

class TestModel(unittest.TestCase):    

    def test_add_contact(self):
        TestModel.ab.add_contact(TestModel.contact)
        self.assertEqual(TestModel.ab._contacts['Testi'].name, TestModel.contact.name)
        
    def test_get_contact(self):
        contact = TestModel.ab.get_contact(TestModel.contact.name)
        self.assertEqual(contact.name, TestModel.contact.name)
        
    def test_get_contacts(self):
        contacts = TestModel.ab.get_contacts()
        self.assertEqual(contacts[TestModel.contact.name].name, TestModel.contact.name)
        
    def test_remove_contact(self):
        TestModel.ab.remove_contact(TestModel.contact)
        self.assertTrue(len(self.ab._contacts) == 0)
        
    def test__save_contacts(self):
        self.assertTrue(TestModel.ab._savecontacts())
    
    @classmethod
    def setUpClass(cls):
        super(TestModel, cls).setUpClass()
        cls.ab = Model()
        cls.contact = Contact('Testi', '0445014190', 'testi@testi.fi')
        

if __name__ == "__main__":
    unittest.main()
    