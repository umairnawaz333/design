from PyQt5 import QtCore,QtGui,QtWidgets
import sys
import db_operations as db

def add_data2(self):
    _translate = QtCore.QCoreApplication.translate
    query_C = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'multan'"
    query_R = "SELECT * from PSL.dbo.multan"
    data_C = db.get(query_C)
    data_R = db.get(query_R)
    i = 0
    for col in data_C:
        for c in col:
            self.purchase_treeWidget.headerItem().setText(i, _translate("Dialog", c))
            i += 1
    j = 0
    k = 0
    for row in data_R:
        item_0 = QtWidgets.QTreeWidgetItem(self.purchase_treeWidget)
        k = 0
        for r in row:
            self.purchase_treeWidget.topLevelItem(j).setText(k, _translate("Dialog", str(r)))
            k += 1
        j += 1