#!/usr/bin/env python3

import sqlite3
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    qApp,
    QAction,
    QTabWidget,
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
from PyQt5.QtSql import (
    QSqlDatabase,
    QSqlQuery,
    QSqlQueryModel
)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("SQLite Browser")
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        self.create_file_menu(menu_bar)

    def create_file_menu(self, menu_bar):
        exit = QAction("Exit", self)
        exit.setShortcut("Ctrl+Q")
        exit.setStatusTip("Exit SQLite Browser")
        exit.triggered.connect(qApp.quit)

        open = QAction("&Open", self)
        open.setShortcut("Ctrl+O")
        open.setStatusTip("Open a SQLite database")
        open.triggered.connect(self.open_db)

        file_menu = menu_bar.addMenu("&File")
        file_menu.addAction(open)
        file_menu.addAction(exit)

    def open_db(self):
        db_file, filter = \
            QFileDialog.getOpenFileName(self, "Open Database", ".",
                                        "All files (*);;SQLite databases (*.db)")

        conn = sqlite3.connect(db_file)
        curs = conn.cursor()
        curs.execute("select name from sqlite_master where type='table'")
        tabs = QTabWidget()
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(db_file)
        db.open()
        for table_data in curs:
            table_name = table_data[0]
            table_model = QSqlQueryModel()
            # for i, column_data in enumerate(curs.description):
            #     table_model.setHeaderData(i, Qt.Horizontal, column_data[0])
            table_model.setQuery(f"select * from {table_name}")
            table_view = QTableView()
            table_view.setModel(table_model)
            tabs.addTab(table_view, table_name)
        self.setCentralWidget(tabs)


if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
