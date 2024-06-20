from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon
import random

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(415, 5, 271, 561))
        self.label.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(0, 0, 91, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("3х5")
        self.move_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_up_button.setGeometry(QtCore.QRect(530, 80, 40, 90))
        self.move_up_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_up_button.setText("")
        self.move_up_button.setIcon(QIcon('Вверх.png'))
        self.move_up_button.setIconSize(QtCore.QSize(80, 100))
        self.move_up_button.setObjectName("move_up_button")
        self.move_left_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_left_button.setGeometry(QtCore.QRect(420, 220, 90, 40))
        self.move_left_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_left_button.setText("")
        self.move_left_button.setIcon(QIcon('Влево'))
        self.move_left_button.setIconSize(QtCore.QSize(100, 80))
        self.move_left_button.setObjectName("move_left_button")
        self.move_right_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_right_button.setGeometry(QtCore.QRect(590, 220, 90, 40))
        self.move_right_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_right_button.setText("")
        self.move_right_button.setIcon(QIcon('Вправо.png'))
        self.move_right_button.setIconSize(QtCore.QSize(100, 80))
        self.move_right_button.setObjectName("move_right_button")
        self.move_down_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_down_button.setGeometry(QtCore.QRect(530, 300, 40, 90))
        self.move_down_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_down_button.setText("")
        self.move_down_button.setIcon(QIcon('Вниз.png'))
        self.move_down_button.setIconSize(QtCore.QSize(80, 100))
        self.move_down_button.setObjectName("move_down_button")
        self.label_Csore = QtWidgets.QLabel(self.centralwidget)
        self.label_Csore.setGeometry(QtCore.QRect(10, 30, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Csore.setFont(font)
        self.label_Csore.setObjectName("label_Csore")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(10, 510, 93, 28))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 399, 407))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridgame = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridgame.setContentsMargins(0, 0, 0, 0)
        self.gridgame.setObjectName("gridgame")
        self.grid_labels = []
        for i in range(4):
            row = []
            for j in range(4):
                label = QtWidgets.QLabel(self.gridLayoutWidget)
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setStyleSheet("border: 1px solid black;")
                row.append(label)
                self.gridgame.addWidget(label, i, j)
            self.grid_labels.append(row)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Инициализация игры
        self.init_game()
        self.add_Functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2048 Game"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Help"))
        self.comboBox.setItemText(1, _translate("MainWindow", "6x6"))
        self.comboBox.setItemText(2, _translate("MainWindow", "4x4"))
        self.comboBox.setItemText(3, _translate("MainWindow", "restart")) 
        self.comboBox.setItemText(4, _translate("MainWindow", "5x3"))
        self.label_Csore.setText(_translate("MainWindow", "Очки :  0"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Exit"))

    def add_Functions(self):
        self.pushButton_Exit.clicked.connect(self.close)
        self.comboBox.activated[str].connect(self.handle_combobox)
        self.move_up_button.clicked.connect(lambda: self.handle_move("up"))
        self.move_left_button.clicked.connect(lambda: self.handle_move("left"))
        self.move_right_button.clicked.connect(lambda: self.handle_move("right"))
        self.move_down_button.clicked.connect(lambda: self.handle_move("down"))

    def handle_combobox(self, text):
        if text == "Help":
            self.show_help()
        elif text == "6x6":
            self.open_6x6_window()
        elif text == "4x4":
            self.init_game()
        elif text == "restart":
            self.init_game(self.board_size)
        elif text == "5x3":  
            self.open_5x3_window()
            
    def open_5x3_window(self):
        self.new_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow5x3()
        self.ui.setupUi(self.new_window)
        self.new_window.show()

    def show_help(self):
        help_message = "Информация о игре 2048: используйте стрелки для перемещения плиток. Слияние одинаковых плиток удваивает их значение."
        QMessageBox.information(None, "Help", help_message)

    def close(self):
        QtWidgets.qApp.quit()

    def open_6x6_window(self):
        self.new_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow6x6()
        self.ui.setupUi(self.new_window)
        self.new_window.show()

    def init_game(self, board_size=(4, 4)):
        if isinstance(board_size, int):
            board_size = (board_size, board_size)
        self.board_size = board_size
        self.score = 0
        self.board = [[0]*self.board_size[1] for _ in range(self.board_size[0])]
        self.add_random_tile()
        self.add_random_tile()
        self.update_ui()

    def add_random_tile(self):
        empty_tiles = [(i, j) for i in range(self.board_size[0]) for j in range(self.board_size[1]) if self.board[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.board[i][j] = random.choice([2, 4])

    def update_ui(self):
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                value = self.board[i][j]
                label = self.grid_labels[i][j]
                if value == 0:
                    label.setText("")
                    label.setStyleSheet("background-color: lightgrey; border: 1px solid black;")
                else:
                    label.setText(str(value))
                    label.setStyleSheet("background-color: rgb(255, 127, 191); border: 1px solid black;")
        self.label_Csore.setText(f"Очки : {self.score}")
        self.check_win_condition()
		
    def check_win_condition(self):
        for row in self.board:
            if 32 in row:
                self.show_win_message()
                break

    def show_win_message(self):
        QMessageBox.information(None, "Режим 4х4", "Поздравляю с победой! Для начала игры заново, закройте окно игры и нажмите на соответствующую кнопку в выпадающем списке.")

    def handle_move(self, direction):
        moved = False
        if direction == "left":
            moved = self.move_left_handler()
        elif direction == "right":
            moved = self.move_right_handler()
        elif direction == "up":
            moved = self.move_up_handler()
        elif direction == "down":
            moved = self.move_down_handler()
        if moved:
            self.add_random_tile()
            self.update_ui()

    def move_left_handler(self):
        moved = False
        for i in range(self.board_size[0]):
            new_row, was_changed = self.merge(self.board[i])
            if was_changed:
                self.board[i] = new_row
                moved = True
        return moved

    def move_right_handler(self):
        moved = False
        for i in range(self.board_size[0]):
            new_row, was_changed = self.merge(list(reversed(self.board[i])))
            if was_changed:
                self.board[i] = list(reversed(new_row))
                moved = True
        return moved

    def move_up_handler(self):
        moved = False
        for j in range(self.board_size[1]):
            column = [self.board[i][j] for i in range(self.board_size[0])]
            new_column, was_changed = self.merge(column)
            if was_changed:
                for i in range(self.board_size[0]):
                    self.board[i][j] = new_column[i]
                moved = True
        return moved

    def move_down_handler(self):
        moved = False
        for j in range(self.board_size[1]):
            column = [self.board[i][j] for i in range(self.board_size[0])]
            new_column, was_changed = self.merge(list(reversed(column)))
            if was_changed:
                for i in range(self.board_size[0]):
                    self.board[i][j] = list(reversed(new_column))[i]
                moved = True
        return moved

    def merge(self, row):
        non_zero = [num for num in row if num != 0]
        merged = []
        skip = False
        was_changed = False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i < len(non_zero) - 1 and non_zero[i] == non_zero[i + 1]:
                merged.append(2 * non_zero[i])
                self.score += 2 * non_zero[i]
                skip = True
                was_changed = True
            else:
                merged.append(non_zero[i])
        merged += [0] * (self.board_size[1] - len(merged))
        if len(merged) != len(row) or any(merged[i] != row[i] for i in range(len(row))):
            was_changed = True
        return merged, was_changed               
class Ui_MainWindow6x6(object):
	
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 710)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(700, 0, 271, 561))
        self.label.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.move_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_up_button.setGeometry(QtCore.QRect(815, 80, 40, 90))
        self.move_up_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_up_button.setText("")
        self.move_up_button.setIcon(QIcon('Вверх.png'))
        self.move_up_button.setIconSize(QtCore.QSize(80, 100))
        self.move_up_button.setObjectName("move_up_button")
        self.move_left_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_left_button.setGeometry(QtCore.QRect(710, 220, 90, 40))
        self.move_left_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_left_button.setText("")
        self.move_left_button.setIcon(QIcon('Влево'))
        self.move_left_button.setIconSize(QtCore.QSize(100, 80))
        self.move_left_button.setObjectName("move_left_button")
        self.move_right_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_right_button.setGeometry(QtCore.QRect(870, 220, 90, 40))
        self.move_right_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_right_button.setText("")
        self.move_right_button.setIcon(QIcon('Вправо.png'))
        self.move_right_button.setIconSize(QtCore.QSize(100, 80))
        self.move_right_button.setObjectName("move_right_button")
        self.move_down_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_down_button.setGeometry(QtCore.QRect(815, 300, 40, 90))
        self.move_down_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_down_button.setText("")
        self.move_down_button.setIcon(QIcon('Вниз.png'))
        self.move_down_button.setIconSize(QtCore.QSize(80, 100))
        self.move_down_button.setObjectName("move_down_button")
        self.label_Csore = QtWidgets.QLabel(self.centralwidget)
        self.label_Csore.setGeometry(QtCore.QRect(10, 30, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Csore.setFont(font)
        self.label_Csore.setObjectName("label_Csore")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(10, 510, 93, 28))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 599, 599))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridgame = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridgame.setContentsMargins(0, 0, 0, 0)
        self.gridgame.setObjectName("gridgame")
        self.grid_labels = []
        for i in range(6):
            row = []
            for j in range(6):
                label = QtWidgets.QLabel(self.gridLayoutWidget)
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setStyleSheet("border: 1px solid black;")
                row.append(label)
                self.gridgame.addWidget(label, i, j)
            self.grid_labels.append(row)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Инициализация игры
        self.init_game()
        self.add_Functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2048 Game"))
        self.label_Csore.setText(_translate("MainWindow", "Очки :  0"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Exit"))

    def add_Functions(self):
        self.pushButton_Exit.clicked.connect(self.close)
        self.move_up_button.clicked.connect(lambda: self.handle_move("up"))
        self.move_left_button.clicked.connect(lambda: self.handle_move("left"))
        self.move_right_button.clicked.connect(lambda: self.handle_move("right"))
        self.move_down_button.clicked.connect(lambda: self.handle_move("down"))

    def close(self):
        QtWidgets.qApp.quit()

    def init_game(self, board_size=(6, 6)):
        if isinstance(board_size, int):
            board_size = (board_size, board_size)
        self.board_size = board_size
        self.score = 0
        self.board = [[0]*self.board_size[1] for _ in range(self.board_size[0])]
        self.add_random_tile()
        self.add_random_tile()
        self.update_ui()

    def add_random_tile(self):
        empty_tiles = [(i, j) for i in range(self.board_size[0]) for j in range(self.board_size[1]) if self.board[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.board[i][j] = random.choice([2, 4])

    def update_ui(self):
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                value = self.board[i][j]
                label = self.grid_labels[i][j]
                if value == 0:
                    label.setText("")
                    label.setStyleSheet("background-color: lightgrey; border: 1px solid black;")
                else:
                    label.setText(str(value))
                    label.setStyleSheet("background-color: rgb(255, 127, 191); border: 1px solid black;")
        self.label_Csore.setText(f"Очки : {self.score}")
        self.check_win_condition()

    def check_win_condition(self):
        for row in self.board:
            if 32 in row:
                self.show_win_message()
                break

    def show_win_message(self):
        QMessageBox.information(None, "Режим 6х6", "Поздравляю с победой! Для начала игры заново, закройте окно игры и нажмите на соответствующую кнопку в выпадающем списке.")

    def handle_move(self, direction):
        moved = False
        if direction == "left":
            moved = self.move_left_handler()
        elif direction == "right":
            moved = self.move_right_handler()
        elif direction == "up":
            moved = self.move_up_handler()
        elif direction == "down":
            moved = self.move_down_handler()
        if moved:
            self.add_random_tile()
            self.update_ui()

    def move_left_handler(self):
        moved = False
        for i in range(self.board_size[0]):
            new_row, was_changed = self.merge(self.board[i])
            if was_changed:
                self.board[i] = new_row
                moved = True
        return moved

    def move_right_handler(self):
        moved = False
        for i in range(self.board_size[0]):
            new_row, was_changed = self.merge(list(reversed(self.board[i])))
            if was_changed:
                self.board[i] = list(reversed(new_row))
                moved = True
        return moved

    def move_up_handler(self):
        moved = False
        for j in range(self.board_size[1]):
            column = [self.board[i][j] for i in range(self.board_size[0])]
            new_column, was_changed = self.merge(column)
            if was_changed:
                for i in range(self.board_size[0]):
                    self.board[i][j] = new_column[i]
                moved = True
        return moved

    def move_down_handler(self):
        moved = False
        for j in range(self.board_size[1]):
            column = [self.board[i][j] for i in range(self.board_size[0])]
            new_column, was_changed = self.merge(list(reversed(column)))
            if was_changed:
                for i in range(self.board_size[0]):
                    self.board[i][j] = list(reversed(new_column))[i]
                moved = True
        return moved

    def merge(self, row):
        non_zero = [num for num in row if num != 0]
        merged = []
        skip = False
        was_changed = False
        for i in range(len(non_zero)):
            if skip:
                skip = False
                continue
            if i < len(non_zero) - 1 and non_zero[i] == non_zero[i + 1]:
                merged.append(2 * non_zero[i])
                self.score += 2 * non_zero[i]
                skip = True
                was_changed = True
            else:
                merged.append(non_zero[i])
        merged += [0] * (self.board_size[1] - len(merged))
        if len(merged) != len(row) or any(merged[i] != row[i] for i in range(len(row))):
            was_changed = True
        return merged, was_changed
class Ui_MainWindow5x3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(415, 5, 271, 561))
        self.label.setStyleSheet("background-color: rgb(232, 232, 232);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.move_up_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_up_button.setGeometry(QtCore.QRect(530, 80, 40, 90))
        self.move_up_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_up_button.setText("")
        self.move_up_button.setIcon(QIcon('Вверх.png'))
        self.move_up_button.setIconSize(QtCore.QSize(80, 100))
        self.move_up_button.setObjectName("move_up_button")
        self.move_left_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_left_button.setGeometry(QtCore.QRect(420, 220, 90, 40))
        self.move_left_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_left_button.setText("")
        self.move_left_button.setIcon(QIcon('Влево'))
        self.move_left_button.setIconSize(QtCore.QSize(100, 80))
        self.move_left_button.setObjectName("move_left_button")
        self.move_right_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_right_button.setGeometry(QtCore.QRect(590, 220, 90, 40))
        self.move_right_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_right_button.setText("")
        self.move_right_button.setIcon(QIcon('Вправо.png'))
        self.move_right_button.setIconSize(QtCore.QSize(100, 80))
        self.move_right_button.setObjectName("move_right_button")
        self.move_down_button = QtWidgets.QPushButton(self.centralwidget)
        self.move_down_button.setGeometry(QtCore.QRect(530, 300, 40, 90))
        self.move_down_button.setStyleSheet("background-color: rgb(255, 127, 191);")
        self.move_down_button.setText("")
        self.move_down_button.setIcon(QIcon('Вниз.png'))
        self.move_down_button.setIconSize(QtCore.QSize(80, 100))
        self.move_down_button.setObjectName("move_down_button")
        self.label_Csore = QtWidgets.QLabel(self.centralwidget)
        self.label_Csore.setGeometry(QtCore.QRect(10, 30, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Csore.setFont(font)
        self.label_Csore.setObjectName("label_Csore")
        self.pushButton_Exit = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Exit.setGeometry(QtCore.QRect(10, 510, 93, 28))
        self.pushButton_Exit.setObjectName("pushButton_Exit")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 80, 399, 407))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridgame = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridgame.setContentsMargins(0, 0, 0, 0)
        self.gridgame.setObjectName("gridgame")
        self.grid_labels = []
        for i in range(5):
            row = []
            for j in range(3):
                label = QtWidgets.QLabel(self.gridLayoutWidget)
                label.setAlignment(QtCore.Qt.AlignCenter)
                label.setStyleSheet("border: 1px solid black;")
                row.append(label)
                self.gridgame.addWidget(label, i, j)
            self.grid_labels.append(row)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Инициализация игры
        self.init_game()
        self.add_Functions()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "2048 Game"))
        self.label_Csore.setText(_translate("MainWindow", "Очки :  0"))
        self.pushButton_Exit.setText(_translate("MainWindow", "Exit"))

    def add_Functions(self):
        self.pushButton_Exit.clicked.connect(self.close)
        self.move_up_button.clicked.connect(lambda: self.handle_move("up"))
        self.move_left_button.clicked.connect(lambda: self.handle_move("left"))
        self.move_right_button.clicked.connect(lambda: self.handle_move("right"))
        self.move_down_button.clicked.connect(lambda: self.handle_move("down"))

    def close(self):
        QtWidgets.qApp.quit()

    def init_game(self, board_size=(5, 3)):
        if isinstance(board_size, int):
            board_size = (board_size, board_size)
        self.board_size = board_size
        self.score = 0
        self.board = [[0]*self.board_size[1] for _ in range(self.board_size[0])]
        self.add_random_tile()
        self.add_random_tile()
        self.update_ui()

    def add_random_tile(self):
        empty_tiles = [(i, j) for i in range(self.board_size[0]) for j in range(self.board_size[1]) if self.board[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.board[i][j] = random.choice([2, 4])

    def update_ui(self):
        for i in range(self.board_size[0]):
            for j in range(self.board_size[1]):
                value = self.board[i][j]
                label = self.grid_labels[i][j]
                if value == 0:
                    label.setText("")
                    label.setStyleSheet("background-color: lightgrey; border: 1px solid black;")
                else:
                    label.setText(str(value))
                    label.setStyleSheet("background-color: rgb(255, 127, 191); border: 1px solid black;")
        self.label_Csore.setText(f"Очки : {self.score}")
        self.check_win_condition()

    def check_win_condition(self):
        for row in self.board:
            if 32 in row:
                self.show_win_message()
                break

    def show_win_message(self):
        QMessageBox.information(None, "Режим 5х3", "Поздравляю с победой! Для начала игры заново, закройте окно игры и нажмите на соответствующую кнопку в выпадающем списке.")

    def handle_move(self, direction):
        moved = False
        if direction == "left":
            moved = self.move_left_handler()
        elif direction == "right":
            moved = self.move_right_handler()
        elif direction == "up":
            moved = self.move_up_handler()
        elif direction == "down":
            moved = self.move_down_handler()
        if moved:
            self.add_random_tile()
            self.update_ui()

    def move_left_handler(self):
        moved = False
        for i in range(self.board_size[0]):
            new_row, was_changed = self.merge(self.board[i])
            if was_changed:
                self.board[i] = new_row
                moved = True
        return moved

    def move_right_handler(self):
        moved = False
        for i in range(self.board_size[0]):
            new_row, was_changed = self.merge(list(reversed(self.board[i])))
            if was_changed:
                self.board[i] = list(reversed(new_row))
                moved = True
        return moved

    def move_up_handler(self):
        moved = False
        for j in range(self.board_size[1]):
            column = [self.board[i][j] for i in range(self.board_size[0])]
            new_column, was_changed = self.merge(column)
            if was_changed:
                for i in range(self.board_size[0]):
                    self.board[i][j] = new_column[i]
                moved = True
        return moved

    def move_down_handler(self):
        moved = False
        for j in range(self.board_size[1]):
            column = [self.board[i][j] for i in range(self.board_size[0])]
            new_column, was_changed = self.merge(list(reversed(column)))
            if was_changed:
                for i in range(self.board_size[0]):
                    self.board[i][j] = list(reversed(new_column))[i]
                moved = True
        return moved

    def merge(self, line):
        new_line = [i for i in line if i != 0]
        was_changed = False
        for i in range(len(new_line) - 1):
            if new_line[i] == new_line[i + 1]:
                new_line[i] *= 2
                new_line[i + 1] = 0
                self.score += new_line[i]
                was_changed = True
        new_line = [i for i in new_line if i != 0]
        new_line.extend([0] * (len(line) - len(new_line)))
        if new_line != line:
            was_changed = True
        return new_line, was_changed
class MainWindow5x3(QtWidgets.QMainWindow, Ui_MainWindow5x3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
