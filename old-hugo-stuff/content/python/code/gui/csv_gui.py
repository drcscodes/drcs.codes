#!/usr/bin/env python3

import csv
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    qApp,
    QAction,
    QWidget,
    QAbstractItemView,
    QFileDialog,
    QTableView
)
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem
)
from PyQt5.QtCore import (
    Qt,
    QAbstractTableModel,
    QVariant
)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("CSV GUI")
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        self.create_file_menu(menu_bar)
        self.create_show_menu(menu_bar)

    def create_file_menu(self, menu_bar):
        exit = QAction("Exit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip("Exit CSV GUI")
        exit.triggered.connect(qApp.quit)

        open = QAction("&Open", self)
        open.setShortcut("Ctrl+O")
        open.setStatusTip("Open a CSV file")
        open.triggered.connect(self.open_file)

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(open)
        file_menu.addAction(exit)

    def create_show_menu(self, menu_bar):
        # Make this an instance variable so we can access it from other methods
        self.show_picture_action = QAction("&Pic", self)
        self.show_picture_action.setShortcut("Ctrl+P")
        self.show_picture_action.setStatusTip("Show picture")
        self.show_picture_action.triggered.connect(self.show_picture)

        show_menu = menu_bar.addMenu("&File")
        show_menu.addAction(self.show_picture_action)

    def open_file(self):
        file_name, filter = \
            QFileDialog.getOpenFileName(self, "Open file", ".",
                                        "All files (*);;CSV Files (*.csv)")

        with open(file_name) as fin:
            csv_data = [row for row in csv.reader(fin)]
        table_model = SimpleTableModel(csv_data[0], csv_data[1:])
        table_view = QTableView()
        table_view.setModel(table_model)
        self.list_view.setSelectionMode(QAbstractItemView.SelectRows)

class SimpleTableModel(QAbstractTableModel):

    def __init__(self, headers, rows):
        QAbstractTableModel.__init__(self, None)
        self.headers = headers
        self.rows = rows

    def rowCount(self, parent):
        return len(self.rows)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if (not index.isValid()) or (role != Qt.DisplayRole):
            return QVariant()
        else:
            return QVariant(self.rows[index.row()][index.column()])

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return QVariant()
        elif orientation == Qt.Vertical:
            return section + 1
        else:
            return self.headers[section]


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
