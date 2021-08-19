import csv,sys

from typing import *

from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant
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
    QLineEdit,
    QTableView, QDialog, qApp, QGroupBox, QFormLayout, QDialogButtonBox)
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QPixmap)

class SimpleTableModel(QAbstractTableModel):

    def __init__(self, data: List[Dict[str, str]]):
        QAbstractTableModel.__init__(self, None)
        self.data = data
        self.headers = [k for k, v in data[0].items()]
        self.rows = [[v for k, v in record.items()] for record in data]

    def rowCount(self, parent):
        return len(self.rows)

    def columnCount(self, parent):
        return len(self.headers)

    def data(self, index, role):
        if (not index.isValid()) or (role != Qt.DisplayRole):
            return QVariant()
        else:
            return QVariant(self.rows[index.row()][index.column()])

    def row(self, index):
        return self.data[index]

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return QVariant()
        elif orientation == Qt.Vertical:
            return section + 1
        else:
            return self.headers[section]

class MainWindow(QWidget):

    def __init__(self, data):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Scripters GUI")

        self.table_model = SimpleTableModel(data)
        self.table_view = QTableView()
        self.table_view.setModel(self.table_model)
        self.table_view.setSelectionMode(QAbstractItemView.SelectRows | QAbstractItemView.SingleSelection)

        self.show_item_button = QPushButton("Scripter Details ...")
        self.show_item_button.clicked.connect(self.show_item)
        self.show_item_button.setEnabled(False)
        self.table_view.clicked.connect(self.enable_show_item_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.table_view)
        vbox.addWidget(self.show_item_button)
        self.setLayout(vbox)

    def show_item(self):
        current_index = self.table_view.currentIndex().row()
        selected_item = self.table_model.row(current_index)
        ScripterDetailsDialog(selected_item).exec()

    def enable_show_item_button(self):
        if self.table_view.currentIndex() == -1:
            self.show_item_button.setEnabled(False)
        else:
            self.show_item_button.setEnabled(True)

class ScripterDetailsDialog(QDialog):

    def __init__(self, row):
        super(ScripterDetailsDialog, self).__init__()
        self.setWindowTitle("Scripter Details")
        form_group_box = QGroupBox()
        layout = QFormLayout()
        for k, v in row.items():
            layout.addRow(QLabel(k), QLabel(v))
        form_group_box.setLayout(layout)

        pic_label = QLabel()
        try :
            pixmap = QPixmap(row["Picture URL"])
            pic_label.setPixmap(pixmap)
        except:
            print("Couldn't open pic file: ", row["Picture URL"])
            pic_label.setText("No picture.")

        buttons = QDialogButtonBox(QDialogButtonBox.Ok)
        buttons.accepted.connect(self.accept)

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(form_group_box)
        vbox_layout.addWidget(pic_label)
        vbox_layout.addWidget(buttons)
        self.setLayout(vbox_layout)

if __name__=='__main__':
    app = QApplication(sys.argv)

    data = [row for row in csv.DictReader(open("scripters.csv"))]
    main = MainWindow(data)
    main.show()
    sys.exit(app.exec_())
