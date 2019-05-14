from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import purchase as home
import add_item_app
import db_operations as db
class my_home_app(home.Ui_Dialog,QtWidgets.QDialog):
    def __init__(self,lis=None):
        super(my_home_app,self).__init__()
        self.setupUi(self)
        self.submit_pushButton.clicked.connect(self.close)
        self.add_pushButton.clicked.connect(self.add_data)
        # self.lis=lis
        # print(self.lis)
        self.lis = lis
        self.show_data(lis)


    def add_data(self):
        if self.lis==None:
            self.ui = add_item_app.my_home_app(self.lis)
        else:
            if len(self.lis)==1:
                self.ui = add_item_app.my_home_app(list(self.lis[0]))
            else:
                self.ui = add_item_app.my_home_app(self.lis)
        self.ui.show()
        self.hide()

    def show_data(self,array):
        _translate = QtCore.QCoreApplication.translate
        l=['id','Name','Fanme','Phn #','scor','50s']
        i=0
        for col in l:
            self.purchase_treeWidget.headerItem().setText(i, _translate("Dialog", col))
            i += 1
        j = 0
        k = 0

        print(array)
        if array!=None:

            j=0
            k=0
            # if len(array) >1:
            for t in array:
                item_0 = QtWidgets.QTreeWidgetItem(self.purchase_treeWidget)
                k=0
                for row in t:
                    print(row)
                    self.purchase_treeWidget.topLevelItem(j).setText(k, _translate("Dialog", str(row)))
                    k += 1
                j+=1
            # else:
            #     for row in array:
            #         self.purchase_treeWidget.topLevelItem(0).setText(k, _translate("Dialog", str(row)))
            #         k += 1
            # print('a')
            # l=[]
            # for ab in array:
            #     print(ab)
            #     l.append(QtWidgets.QTreeWidgetItem(ab))
            # self.purchase_treeWidget.addTopLevelItems(array)
        # print(list)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_app = my_home_app()
    my_app.show()
    app.exec()
