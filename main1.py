import sys

from PyQt6.QtWidgets import QApplication, QWidget, QStackedWidget, QMainWindow
from PyQt6.uic import loadUi


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('data\\book_inf_screen.ui')

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.book_list_screen = loadUi('data\\book_list_screen.ui')
        self.book_inf_screen = loadUi('data\\book_inf_screen.ui')
        self.book_notebook_screen = loadUi('data\\book_notebook_screen.ui')

        self.stacked_widget.addWidget(self.book_notebook_screen)
        self.stacked_widget.addWidget(self.book_inf_screen)
        self.stacked_widget.addWidget(self.book_list_screen)

        self.book_inf_screen.book_quotes.clicked.connect(self.switch_to_notebook)
        self.book_inf_screen.book_retelling.clicked.connect(self.switch_to_notebook)
        self.book_inf_screen.book_review.clicked.connect(self.switch_to_notebook)

        self.book_notebook_screen.back_btn.clicked.connect(self.switch_to_inf_screen)

    def switch_to_notebook(self):
        self.stacked_widget.setCurrentWidget(self.book_notebook_screen)

    def switch_to_inf_screen(self):
        self.stacked_widget.setCurrentWidget(self.book_inf_screen)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
