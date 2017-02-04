'''
Created on 4.2.2017

@author: heimo
'''
import unittest
from addressbook.address_book import AddressBook, Contact

class Test(unittest.TestCase):

    def test_savecontacts(self):
        ab = AddressBook()
        ab.contacts['Testi'] = Contact('Testi', '0445014190', 'testi@testi.fi')
        ab._savecontacts()
        
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()