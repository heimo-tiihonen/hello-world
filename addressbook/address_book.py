'''
Created on 7.2.2017

@author: heimo
'''
from PyQt5.QtWidgets import QApplication
from addressbook.presenter import Presenter, PresenterGUI
from addressbook.view import GUI, CUI
import sys


if __name__ == '__main__': 
    
    #TODO: Check sys.argv for which UI to use
    
    #Console User Interface
    #presenter = Presenter()
    #ui = CUI(presenter)
    #presenter.set_ui(ui)
    #sys.exit(ui.main())
    
    #Graphical User Interface
    app = QApplication(sys.argv)
    presenter = PresenterGUI()
    ui = GUI(presenter)
    sys.exit(app.exec_())
    