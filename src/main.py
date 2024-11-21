import sys

from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow
from PyQt6.uic import loadUi
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect('D:\\Project\\libr.db')
        self.c = self.db.cursor()
        self.setFixedSize(800, 600)
        loadUi('D:\Project\data\\all_books.ui', self)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.all_books = loadUi('D:\Project\data\\all_books.ui')
        self.book_list_screen = loadUi('D:\Project\data\\book_list_screen.ui')
        self.book_inf_screen = loadUi('D:\Project\data\\book_inf_screen.ui')
        self.book_notebook_screen = loadUi('D:\Project\data\\book_notebook_screen.ui')
        self.book_add_screen = loadUi('D:\Project\data\\book_add_screen.ui')

        self.stacked_widget.addWidget(self.all_books)
        self.stacked_widget.addWidget(self.book_inf_screen)
        self.stacked_widget.addWidget(self.book_notebook_screen)
        self.stacked_widget.addWidget(self.book_list_screen)
        self.stacked_widget.addWidget(self.book_add_screen)

        self.book_inf_screen.book_quotes.clicked.connect(self.switch_to_notebook)
        self.book_inf_screen.book_retelling.clicked.connect(self.switch_to_notebook)
        self.book_inf_screen.book_review.clicked.connect(self.switch_to_notebook)

        self.book_notebook_screen.back_btn.clicked.connect(self.switch_to_inf_screen)

        self.book_inf_screen.back_button.clicked.connect(self.switch_to_book_add_screen)

        self.book_add_screen.book_add_btn.clicked.connect(self.add_book)

        self.book_add_screen.back_btn.clicked.connect(self.switch_to_all_books)

        self.all_books.add_new_book.clicked.connect(self.switch_to_book_add_screen_from_all)

    def switch_to_notebook(self):
        self.stacked_widget.setCurrentWidget(self.book_notebook_screen)

    def switch_to_inf_screen(self):
        self.stacked_widget.setCurrentWidget(self.book_inf_screen)

    def switch_to_book_add_screen(self):
        self.stacked_widget.setCurrentWidget(self.book_add_screen)

    def switch_to_all_books(self):
        self.stacked_widget.setCurrentWidget(self.all_books)

    def switch_to_book_add_screen_from_all(self):
        self.stacked_widget.setCurrentWidget(self.book_add_screen)

    def add_book(self):
        self.book_add_screen.res_label.clear()
        if self.book_add_screen.title.toPlainText() != '':
            self.c.execute(f"""INSERT INTO library VALUES ('1', '{self.book_add_screen.title.toPlainText()}',
            '{self.book_add_screen.title.toPlainText()}', '{self.book_add_screen.title.toPlainText()}',
            '{self.book_add_screen.title.toPlainText()}', '', '', '')""")
            self.db.commit()
            print('book was added')
            self.stacked_widget.setCurrentWidget(self.book_add_screen)
        else:
            self.book_add_screen.res_label.setText('Введите навзание книги')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())