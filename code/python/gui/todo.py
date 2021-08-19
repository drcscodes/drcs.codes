#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QListView,
    QAbstractItemView,
    QMessageBox,
    QLineEdit
)
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem
)

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Todo List")

        self.list_view = QListView()
        self.list_model = QStandardItemModel(self.list_view)
        self.list_view.setModel(self.list_model)

        self.list_view.setSelectionMode(QAbstractItemView.SingleSelection)

        self.line_edit = QLineEdit()

        self.add_button = QPushButton("Add")
        self.add_button.setEnabled(False)

        self.add_button.clicked.connect(self.add_todo_item)
        self.line_edit.textChanged.connect(self.enable_add_button)

        self.show_item_button = QPushButton("Show item ...")
        self.show_item_button.clicked.connect(self.show_item)
        self.show_item_button.setEnabled(False)
        self.list_view.clicked.connect(self.enable_show_item_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.list_view)
        vbox.addWidget(self.line_edit)
        vbox.addWidget(self.add_button)
        vbox.addWidget(self.show_item_button)
        self.setLayout(vbox)

    def add_todo_item(self):
        list_item = QStandardItem(self.line_edit.text())
        self.list_model.appendRow(list_item)
        self.line_edit.setText('')
        self.line_edit.setFocus()

    # Handles the Show Item ... button click. Gets selected item
    # from list, displays in a message box.
    def show_item(self):
        current_index = self.list_view.currentIndex().row()
        selected_item = self.list_model.item(current_index).text()
        reply = QMessageBox.information(self,
                                        "Selected Todo Item",
                                        selected_item,
                                        QMessageBox.Ok)


    def enable_add_button(self):
        if len(self.line_edit.text()) == 0:
            self.add_button.setEnabled(False)
        else:
            self.add_button.setEnabled(True)

    def enable_show_item_button(self):
        if self.list_view.currentIndex() == -1:
            self.show_item_button.setEnabled(False)
        else:
            self.show_item_button.setEnabled(True)


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    exit_code = app.exec_()
    sys.exit(exit_code)
