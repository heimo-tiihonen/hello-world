'''
Created on 7.2.2017

@author: heimo
'''
from PyQt5.QtWidgets import QApplication
from addressbook.model import ModelPickle, ModelDB
from addressbook.presenter import Presenter, PresenterGUI
from addressbook.view import GUI, CUI
import sys


if __name__ == '__main__': 
    
    #TODO: Check sys.argv for which UI to use
    
    #Console User Interface
    model = ModelDB()
    presenter = Presenter(model)
    ui = CUI(presenter)
    presenter.set_ui(ui)
    sys.exit(ui.main())
    
    #Graphical User Interface
    #app = QApplication(sys.argv)
    #model = ModelDB()
    #presenter = PresenterGUI(model)
    #ui = GUI(presenter)
    #sys.exit(app.exec_())
    