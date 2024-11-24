import sys

from PyQt6.QtWidgets import QApplication, QStackedWidget, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt6.uic import loadUi
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.db = sqlite3.connect('D:\\Project\\base.sqlite')
        self.c = self.db.cursor()
        self.setFixedSize(800, 600)
        # loadUi('D:\Project\data\\all_books.ui', self)
        

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

        # self.book_inf_screen.book_quotes.clicked.connect(self.switch_to_notebook)
        # self.book_inf_screen.book_retelling.clicked.connect(self.switch_to_notebook)
        # self.book_inf_screen.book_review.clicked.connect(self.switch_to_notebook)

        self.book_notebook_screen.back_btn.clicked.connect(self.switch_to_inf_screen)

        self.book_inf_screen.back_button.clicked.connect(self.switch_to_book_add_screen)

        self.book_add_screen.book_add_btn.clicked.connect(self.add_book)

        self.book_add_screen.back_btn.clicked.connect(self.switch_to_all_books)

        self.all_books.add_new_book.clicked.connect(self.switch_to_book_add_screen_from_all)

        self.book_inf_screen.back_button.clicked.connect(self.switch_to_all_books)

        self.book_add_screen.book_add_btn.clicked.connect(self.switch_to_all_books)

        self.switch_to_all_books()


    def switch_to_quotes(self, id):
        self.stacked_widget.setCurrentWidget(self.book_notebook_screen)
        text = self.c.execute(f"""SELECT * FROM mylibrary WHERE ID = {id}""")
        for i in text:
            self.book_notebook_screen.notebook.setPlainText(i[6])

        self.book_notebook_screen.back_btn.blockSignals(True)
        try:
            self.book_notebook_screen.back_btn.clicked.disconnect()
        except TypeError:
            pass
        self.book_notebook_screen.back_btn.clicked.connect(lambda: self.go_back_quotes(id))
        self.book_notebook_screen.back_btn.blockSignals(False)

        # self.book_notebook_screen.back_btn.clicked.connect(lambda: self.go_back_quotes(id))

    
    def go_back_quotes(self, id):
        self.c.execute(f"""UPDATE mylibrary SET quotes = '{self.book_notebook_screen.notebook.toPlainText()}' WHERE ID = {id}""")
        self.db.commit()

    def switch_to_retelling(self, id):
        self.stacked_widget.setCurrentWidget(self.book_notebook_screen)
        text = self.c.execute(f"""SELECT * FROM mylibrary WHERE ID = {id}""")
        for i in text:
            self.book_notebook_screen.notebook.setPlainText(i[5])
        self.book_notebook_screen.back_btn.blockSignals(True)
        try:
            self.book_notebook_screen.back_btn.clicked.disconnect()
        except TypeError:
            pass
        self.book_notebook_screen.back_btn.clicked.connect(lambda: self.go_back_retelling(id))
        self.book_notebook_screen.back_btn.blockSignals(False)

        # self.book_notebook_screen.back_btn.clicked.connect(lambda: self.go_back_quotes(id))

    def go_back_retelling(self, id):
        print(type(self.book_notebook_screen.notebook.toPlainText()))
        self.c.execute(f"""UPDATE mylibrary SET brief_retelling = '{self.book_notebook_screen.notebook.toPlainText()}' WHERE ID = {id}""")
        self.db.commit()
    
    def switch_to_review(self, id):
        self.stacked_widget.setCurrentWidget(self.book_notebook_screen)
        text = self.c.execute(f"""SELECT * FROM mylibrary WHERE ID = {id}""")
        for i in text:
            self.book_notebook_screen.notebook.setPlainText(i[7])
        self.book_notebook_screen.back_btn.blockSignals(True)
        try:
            self.book_notebook_screen.back_btn.clicked.disconnect()
        except TypeError:
            pass
        self.book_notebook_screen.back_btn.clicked.connect(lambda: self.go_back_review(id))
        self.book_notebook_screen.back_btn.blockSignals(False)

        # self.book_notebook_screen.back_btn.clicked.connect(lambda: self.go_back_quotes(id))
        
    def go_back_review(self, id):
        print(type(self.book_notebook_screen.notebook.toPlainText()))
        self.c.execute(f"""UPDATE mylibrary SET review = '{self.book_notebook_screen.notebook.toPlainText()}' WHERE ID = {id}""")
        self.db.commit()


    def switch_to_inf_screen(self):
        self.stacked_widget.setCurrentWidget(self.book_inf_screen)

    def switch_to_book_add_screen(self):
        self.book_add_screen.title.clear()
        self.book_add_screen.author.clear()
        self.book_add_screen.genre.clear()
        self.book_add_screen.release_year.clear()
        self.stacked_widget.setCurrentWidget(self.book_add_screen)

    def switch_to_all_books(self):
        self.stacked_widget.setCurrentWidget(self.all_books)
        self.buttons = []
        books = self.c.execute("""SELECT ID, title, release_year, author,
                           genre FROM mylibrary""")
        self.books_id = []
        button_widget = QWidget(self)
        button_layout = QVBoxLayout(button_widget)
        scroll_area = self.all_books.scrollArea
        
        button_layout.setSpacing(10) 

        for i in books:
            button = QPushButton(self)
            button.setText(i[1])
            self.buttons.append(button)
            button.setFixedSize(400, 50)
            self.books_id.append(i[0])
            button.clicked.connect(self.get_book_info)
            button_layout.addWidget(button)

        button_widget.setLayout(button_layout)
        scroll_area.setWidget(button_widget)

        self.all_books.layout().addWidget(scroll_area)

    # def switch_to_book_add_screen_from_all(self):
    #     self.stacked_widget.setCurrentWidget(self.book_add_screen)
        
    def switch_to_book_add_screen_from_all(self):
        self.book_add_screen.title.clear()
        self.book_add_screen.author.clear()
        self.book_add_screen.genre.clear()
        self.book_add_screen.release_year.clear()
        self.stacked_widget.setCurrentWidget(self.book_add_screen)

    def get_book_info(self, id):
        books = self.c.execute("""SELECT ID, title, release_year, author,
                               genre FROM mylibrary""")
        id = self.buttons.index(self.sender())
        book_info = list(books)[id]

        if book_info:
            id, title, release_year, author, genre = book_info
            self.book_inf_screen.book_name.setText(title)
            self.book_inf_screen.book_year.setText(str(release_year))
            self.book_inf_screen.book_author.setText(author)
            self.book_inf_screen.book_genre.setText(genre)
            self.stacked_widget.setCurrentWidget(self.book_inf_screen)

        self.book_inf_screen.del_book_btn.blockSignals(True)
        try:
            self.book_inf_screen.del_book_btn.clicked.disconnect()
        except TypeError:
            pass
        self.book_inf_screen.del_book_btn.clicked.connect(lambda: self.del_book(id))
        self.book_inf_screen.del_book_btn.blockSignals(False)

        self.book_inf_screen.book_quotes.blockSignals(True)
        self.book_inf_screen.book_retelling.blockSignals(True)
        self.book_inf_screen.book_review.blockSignals(True)
        try:
            self.book_inf_screen.book_quotes.clicked.disconnect()
            self.book_inf_screen.book_retelling.clicked.disconnect()
            self.book_inf_screen.book_review.clicked.disconnect()
        except TypeError:
            pass

        self.book_inf_screen.book_quotes.clicked.connect(lambda: self.switch_to_quotes(id))
        self.book_inf_screen.book_retelling.clicked.connect(lambda: self.switch_to_retelling(id))
        self.book_inf_screen.book_review.clicked.connect(lambda: self.switch_to_review(id))
        self.book_inf_screen.book_quotes.blockSignals(False)
        self.book_inf_screen.book_retelling.blockSignals(False)
        self.book_inf_screen.book_review.blockSignals(False)

    def add_book(self):
        self.book_add_screen.res_label.clear()
        if self.book_add_screen.title.toPlainText() != '':
            self.c.execute(f"""INSERT INTO mylibrary (title, release_year, author,
                           genre) VALUES ('{self.book_add_screen.title.toPlainText()}',
            '{self.book_add_screen.release_year.toPlainText()}', '{self.book_add_screen.author.toPlainText()}',
            '{self.book_add_screen.genre.toPlainText()}')""")
            self.db.commit()
            print('book was added')
            self.stacked_widget.setCurrentWidget(self.book_add_screen)
        else:
            self.book_add_screen.res_label.setText('Введите название книги')
    
    def del_book(self, id):
        self.c.execute(f"""DELETE FROM mylibrary WHERE ID = {id}""")
        self.db.commit()
        self.switch_to_all_books()
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())