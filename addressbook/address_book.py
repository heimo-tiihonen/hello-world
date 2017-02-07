'''
Created on 7.2.2017

@author: heimo
'''
from PyQt5.QtWidgets import QApplication
from addressbook.presenter import Presenter
from addressbook.view import GUI, CUI
import sys


if __name__ == '__main__': 
    
    #TODO: Check sys.argv for which UI to use
    presenter = Presenter()
    
    #Console User Interface
    ui = CUI(presenter)
    presenter.set_ui(ui)
    ui.main()
    
    #Graphical User Interface
    #app = QApplication(sys.argv)
    #ui = GUI(presenter)
    #presenter.set_ui(ui)
    #sys.exit(app.exec_())
    