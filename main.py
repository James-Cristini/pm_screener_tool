import os
import sys
import sip
import string
import webbrowser
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtCore import QThread, SIGNAL, pyqtSlot, QString
from PyQt4.QtGui import QApplication, QMainWindow, QWidget, QDialog, QMessageBox, QTableWidgetItem, QMovie
from time import sleep
from screener_ui import Ui_pm_screener
from stem_filter import get_stem_conflicts, strip_names
from micro import get_micro_data, micro_excel_doc

#TODO UPDATE ALL MICRO functions and tables to accept new data structure


reload(sys)
sys.setdefaultencoding('utf-8')

class MainWindow(QMainWindow):

    micro_data = {}

    def __init__(self):
        super(MainWindow, self).__init__()
        #self.ui = uic.loadUi('pm_screener.ui')
        self.ui = Ui_pm_screener()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('tool.ico'))

        self.ui.filter_build_doc_btn.clicked.connect(self.build_filter_doc)
        self.ui.filter_inn_radio.setChecked(True)

        self.ui.google_search_btn.clicked.connect(self.search_google)
        self.ui.google_just_names_radio.setChecked(True)

        self.ui.micro_username_input.setText("addisontemp")
        self.ui.micro_password_input.setText("addisontemp")
        self.ui.micro_password_input.setEchoMode(QtGui.QLineEdit.Password)
        self.ui.micro_search_btn.clicked.connect(self.search_micromedex)
        self.ui.micro_table.cellClicked.connect(self.micro_cell_clicked)
        self.ui.micro_table.setSortingEnabled(True)

        self.ui.micro_to_excel_btn.clicked.connect(self.micro_to_excel)

        self.ui.micro_progress_bar.setRange(0,1)

        self.ui.filter_pharma_radio.setChecked(True)

        self.ui.exit_btn.clicked.connect(self.close_app)

        #self.ui.show()

    def build_filter_doc(self):
        if self.ui.filter_pharma_radio.isChecked():
            check_type = "PHARMA"
        else:
            check_type = "INN"

        ignore = str(self.ui.filter_ignore_line.text())
        names_list = self.get_names_list(self.ui.filter_names_input.toPlainText())
        self.filter_file_name = "stem_conflicts" + ".xls"

        if names_list:
            try:
                get_stem_conflicts(names_list, ignore, self.filter_file_name, check_type)
                self.filter_doc_done()
            except IOError:
                #print "File already open"
                QMessageBox.warning(Screener, "File already open", "The stem_conflicts file is currently open; close this file first and try again") % (file_name)

    def filter_doc_done(self):
        choice = QtGui.QMessageBox.question(self, "Open", "Stem Filter doc is finished, would you like to open now?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice ==  QtGui.QMessageBox.Yes:
            try:
                os.system("start " + str(self.filter_file_name))
            except IOError:
                #print "File already open"
                QMessageBox.warning(self, "File already open", "The stem_conflicts file is currently open; close this file first and try again") % ( str(self.filter_file_name))
        else:
            QMessageBox.warning(self, "Saved", "The file has been saved as stem_conflicts")
        self.ui.filter_build_doc_btn.setEnabled(True)

    def search_google(self):
        if self.ui.google_just_names_radio.isChecked():
            #print "Searching the names via Google"
            keyword = ""
        elif self.ui.google_with_key_radio.isChecked():
            #print "Searching the names and keyword via Google"
            keyword = str(self.ui.google_key_input.text()).strip(string.whitespace).replace(" ", "+")
        stripped_names = self.get_stripped_names_list(self.get_names_list(self.ui.google_names_input.toPlainText()))

        if stripped_names:
            choice = QtGui.QMessageBox.question(self, "Open pages", "This will open {} browser tabs, are you sure you want to do that?".format(len(stripped_names)), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

            if choice == QtGui.QMessageBox.Yes :
                self.ui.google_search_btn.setEnabled(False)
                self.google_thread = GoogleThread(stripped_names, keyword)
                self.connect(self.google_thread, SIGNAL("finished()"), self.google_search_done)
                self.google_thread.start()
        # else :
        #     QMessageBox.warning(self, "No Names", "No names entered!")

    def get_names_list(self, text_input):
        # Replace special characters in input text, easier to handle
        names_text = (str(text_input).replace(u"\u2018", '"').replace(u"\u2019", '"').\
            replace(u"\u201c",'"').replace(u"\u201d", '"').replace(u"\u2013", "-"))
        new_text = ""

        for x in range(len(names_text)-1) :
            if names_text[x] == "*" and names_text[x+1] not in string.letters :
                pass
            else :
                new_text += names_text[x]
        try:
            new_text += names_text[-1]
            names_list = new_text.split("\n")
            return names_list
        except IndexError:
            QMessageBox.warning(self, "No Names", "No names entered")

    def get_stripped_names_list(self, names_list):
        stripped_names = []
        if names_list:
            for x in names_list:
                stripped_names += strip_names(x)
            return stripped_names

    def google_search_done(self):
        self.ui.google_search_btn.setEnabled(True)

    def search_micromedex(self):
        # Searches Micromedex, finds hits, and builds a table within the app displaying hits
        username = str(self.ui.micro_username_input.text())
        password = str(self.ui.micro_password_input.text())
        if username and password:

            self.names_to_micro = self.get_names_list(self.ui.micro_names_input.toPlainText())
            if self.names_to_micro:
                # self.movie = QtGui.QMovie("loading.gif")
                # self.ui.micro_status.setMovie(self.movie)
                # self.movie.start()
                self.ui.micro_progress_bar.setRange(0,0)
                self.ui.micro_search_btn.setEnabled(False)
                self.micro_thread = MicromedexThread(self.names_to_micro, username, password)
                self.connect(self.micro_thread, SIGNAL("finished()"), self.micro_search_done)
                self.micro_thread.start()
        else:
            QMessageBox.warning(self, "Missing Info", "Missing Username and/or Password")

    def micro_search_done(self):
        # self.movie.stop()
        # self.ui.micro_status.clear()
        self.ui.micro_progress_bar.setRange(0,1)
        self.build_micro_table()

        QtGui.QMessageBox.information(self, "Done!", "Micro search finished!")
        self.ui.micro_search_btn.setEnabled(True)

    def build_micro_table(self):
        self.ui.micro_table.setRowCount(0)
        self.ui.micro_table.setColumnCount(0)
        self.ui.micro_table.setColumnCount(4)
        self.ui.micro_table.setHorizontalHeaderLabels(["Name(s)", "# Hits", "Conflicts", "Link"])
        self.ui.micro_table.horizontalHeader().setStretchLastSection(True)


        for name_rationale in self.names_to_micro:
            for name_on_line in self.micro_data[name_rationale]:
                name_link = "http://www.micromedexsolutions.com/micromedex2/librarian/CS/D1A629/ND_PR/evidencexpert/ND_P/evidencexpert/DUPLICATIONSHIELDSYNC/6270A7/ND_PG/evidencexpert/ND_B/evidencexpert/ND_AppProduct/evidencexpert/ND_T/evidencexpert/PFActionId/evidencexpert.ShowProductSearchResults?SearchTerm=" + name_on_line + "&searchType=Tox-Tool-Product-Substance&searchContent=MARTINDALE"
                name_cell = name_on_line
                num_hits_cell = 0
                conflict_cell = ""
                for conflict_name in self.micro_data[name_rationale][name_on_line]:
                    countries = ", ".join(self.micro_data[name_rationale][name_on_line][conflict_name])
                    conflict_cell += "".join([conflict_name, " (", countries, "); "])
                    num_hits_cell += len(self.micro_data[name_rationale][name_on_line][conflict_name])
                num_hits_cell *= len(self.micro_data[name_rationale])
                conflict_cell = conflict_cell.strip(";")

                rowPosition = self.ui.micro_table.rowCount()
                self.ui.micro_table.insertRow(rowPosition)
                self.ui.micro_table.setItem(rowPosition, 0, QTableWidgetItem(name_cell))
                self.ui.micro_table.setItem(rowPosition, 1, QTableWidgetItem(str(num_hits_cell)))
                self.ui.micro_table.setItem(rowPosition, 2, QTableWidgetItem(conflict_cell))
                self.ui.micro_table.setItem(rowPosition, 3, QTableWidgetItem(name_link))

        header = self.ui.micro_table.horizontalHeader()
        header.setResizeMode(0, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        header.setResizeMode(2, QtGui.QHeaderView.Stretch)
        self.highlight_conflict_cells()

    def highlight_conflict_cells(self):
        rowPosition = self.ui.micro_table.rowCount()
        for row in range(rowPosition):
            num_of_hits = self.ui.micro_table.item(row, 1).text()

            if int(self.ui.micro_table.item(row, 1).text()):
                self.ui.micro_table.item(row, 1).setBackground(QtGui.QColor(255,239,213))

            name = str(self.ui.micro_table.item(row, 0).text())

            if self.micro_data["DYMs"][name] == True:
                self.ui.micro_table.item(row, 3).setBackground(QtGui.QColor(240,128,128))


    @pyqtSlot(int,int)
    def micro_cell_clicked(self, item, item2):
        name = str(self.ui.micro_table.item(item, 0).text())

        if item2 == 2:
            #print "getting number of hits"
            hits_text = str(self.ui.micro_table.item(item, item2).text())
            if hits_text:
                QMessageBox.information(self,
            				"Hits for " + name + ":",
            				"{}".format(hits_text))

        elif item2 == 3:
            name_url = "http://www.micromedexsolutions.com/micromedex2/librarian/CS/D1A629/ND_PR/evidencexpert/ND_P/evidencexpert/DUPLICATIONSHIELDSYNC/6270A7/ND_PG/evidencexpert/ND_B/evidencexpert/ND_AppProduct/evidencexpert/ND_T/evidencexpert/PFActionId/evidencexpert.ShowProductSearchResults?SearchTerm=" + name + "&searchType=Tox-Tool-Product-Substance&searchContent=MARTINDALE"
            webbrowser.open(name_url)

    def micro_to_excel(self):
        if self.micro_data:
            self.ui.micro_search_btn.setEnabled(False)
            #micro_excel_doc(self.names_list, Screener.micro_data)
            self.build_micro_doc_thread = MicromedexDocThread()
            self.connect(self.build_micro_doc_thread, SIGNAL("finished()"), self.micro_excel_done)
            self.build_micro_doc_thread.start()
        else:
            QMessageBox.warning(Screener, "No data", "You haven't searched anything in Micromedex yet!")

    def micro_excel_done(self):
        #TODO ask to open file now
        choice = QtGui.QMessageBox.question(self, "Open", "Micromedex excel doc is finished, would you like to open now?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice ==  QtGui.QMessageBox.Yes:
            try:
                os.system("start " + "micro_data.xls")
            except IOError:
                #print "File already open"
                QMessageBox.warning(self, "File already open", "The micro_data file is currently open; close this file first and try again") % ( str(self.filter_file_name))
        else:
            QMessageBox.warning(self, "Saved", "The file has been saved as micro_data")
        self.ui.micro_to_excel_btn.setEnabled(True)

    def close_app(self):
        choice = QtGui.QMessageBox.question(self, "Quit", "Leave?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

        if choice == QtGui.QMessageBox.Yes :
            sys.exit()
        else :
            #print "No: Not exiting..."
            pass


class GoogleThread(QThread):
    def __init__(self, stripped_names, keyword):
        QThread.__init__(self)
        self.stripped_names = stripped_names
        self.keyword = keyword

    def __del__(self):
        self.wait()

    def run(self):
        if Screener.ui.google_just_names_radio.isChecked():
            #print "Just Names Checked"
            for name in self.stripped_names:
                url = "".join(["https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=", name])
                webbrowser.open(url)
                sleep(0.2)

        if Screener.ui.google_with_key_radio.isChecked():
            #print "Names and Keyword Checked"
            for name in self.stripped_names:
                url = "".join(["https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=", name, "+", self.keyword ])
                webbrowser.open(url)
                sleep(0.2)


class MicromedexThread(QThread):
    def __init__(self, stripped_names, username, password):
        QThread.__init__(self)
        self.stripped_names = stripped_names
        self.names_list = stripped_names
        self.username = username
        self.password = password

    def __del__(self):
        self.wait()

    def run(self):
        Screener.micro_data = get_micro_data(self.names_list, self.username, self.password)

class MicromedexDocThread(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        micro_excel_doc(Screener.names_to_micro, Screener.micro_data)



if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")

    Screener = MainWindow()
    Screener.show()

    sip.setdestroyonexit(False)
    sys.exit(app.exec_())
