from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import purchase as home
import add_item
import home_app
class my_home_app(add_item.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self,prev_lis=None):
        super(my_home_app,self).__init__()
        self.setupUi(self)
        self.cancel_Button.clicked.connect(self.exit)
        self.add_Button.clicked.connect(self.add_item)
        self.item_list=prev_lis
    def exit(self):
        self.hide()
        self.go = home_app.my_home_app()
        self.go.show()

    def add_item(self):
        if self.item_list !=None:
            it = [self.code_lineEdit.text(), self.name_lineEdit.text(), self.catagory_lineEdit.text(),
                  self.subc_lineEdit.text(), self.price_lineEdit.text(), self.item_lineEdit.text()]
            l3 = tuple(self.item_list)
            l4=[]
            l4.append(l3)
            if len(l4) ==1:
                self.item_list = [self.item_list]+[it]
            else:
                self.item_list = self.item_list + [it]

        else:
            it = [(self.code_lineEdit.text(), self.name_lineEdit.text(), self.catagory_lineEdit.text(),
                  self.subc_lineEdit.text(), self.price_lineEdit.text(), self.item_lineEdit.text())]
            self.item_list = it
        self.close()
        self.go = home_app.my_home_app(self.item_list)
        # home_app.my_home_app.show_data(item_list)
        self.go.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_app = my_home_app()
    my_app.show()
    app.exec()
