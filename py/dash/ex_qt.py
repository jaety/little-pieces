import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import (
    QApplication, 
    QDockWidget, 
    QHBoxLayout, 
    QListWidget,
    QMainWindow,
    QTextEdit,
    QTreeView
)

"""
1. The model is a collection of functions

TODO
1. How to allow adding functions from the UI
2. Writing the model to source 
"""

class Function:
    def __init__(self, arg_names, name, inputs=None, impl=None):
        self.arg_names = arg_names
        self.name = name
        self.inputs = inputs if inputs else {}
        self.impl = impl

    def signature(self):
        return "{}({})".format(self.name, ", ".join(self.arg_names))

def simple_expr():
    a = Function([],'a')
    b = Function([],'b')
    c = Function(['x','y'],'plus',{'x': a, 'y': b})
    d = Function(['x','y'],'minus',{'x':b, 'y':c})
    return d

class FunctionModel(QStandardItemModel):
    def __init__(self, expr):
        super(FunctionModel, self).__init__()
        self._add_func(expr,self.invisibleRootItem()) 
        self.setHeaderData(0, Qt.Horizontal, "Expr Tree")

    def _add_func(self,func,parent,prefix=""):
        item = QStandardItem(prefix + func.signature())
        parent.appendRow(item)
        for arg_name in func.arg_names:
            self._add_func(func.inputs[arg_name],item,arg_name + " = ")

class TreeModel(QStandardItemModel):
    def __init__(self):
        super(TreeModel, self).__init__()
        parentItem = self.invisibleRootItem()
        for i in range(4):
            item = QStandardItem("item %d" % i)
            parentItem.appendRow(item)
            parentItem = item 
        self.setHeaderData(0, Qt.Horizontal, "Item")


class ExprApp(QMainWindow):
    def __init__(self,parent=None):
        super(ExprApp, self).__init__(parent)
        self._init_main_window()
        self._init_tree_dock()
        self.setWindowTitle("Expression Browser")

    def _init_tree_dock(self):
        self.tree_dock = QDockWidget("Expression Tree", self)
        self.tree_view = QTreeView(self.tree_dock)
        self.set_expr(simple_expr())

        self.tree_dock.setWidget(self.tree_view)
        self.tree_dock.setFloating(False)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.tree_dock)

    def set_expr(self, expr):
        self.tree_model = FunctionModel(expr)
        self.tree_view.setModel(self.tree_model)

    def _init_main_window(self):
        self.setCentralWidget(QTextEdit())




class MyApp(QMainWindow):
    def __init__(self, parent=None):
        super(MyApp, self).__init__(parent)
        self.treeModel = FunctionModel(simple_expr())
        self.treeView = QTreeView(self)
        self.treeView.setModel(self.treeModel)

        self.setCentralWidget(self.treeView)
        self.setWindowTitle('My App')

class DockDemo(QMainWindow):
    def __init__(self,parent=None):
        super(DockDemo, self).__init__(parent)
        layout=QHBoxLayout()

        self.items=QDockWidget('Expression Tree',self)

        self.treeModel = FunctionModel(simple_expr())
        self.treeView = QTreeView(self)
        self.treeView.setModel(self.treeModel)

        self.items.setWidget(self.treeView)
        self.items.setFloating(False)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.LeftDockWidgetArea,self.items)

        self.setLayout(layout)
        self.setWindowTitle('Dock')

if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=ExprApp()
    demo.show()
    sys.exit(app.exec_())





"""
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
app = QApplication([])

window = QWidget()
layout = QHBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec()
"""