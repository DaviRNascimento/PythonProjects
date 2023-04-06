# Código que cria uma interface gráfica, usando PyQt6, e calcula a quntidade de comida necessária para uma festa.

# # ainda não está da maneira que eu gostaria, mas para não estourar o prazo de entrega, mando-o como uma prévia do que pretendo fazer.

# meu objetivo é colocar mais de uma janela para recebimento e saída de dados, sendo a primeira uma capa, a segunda para escolha dos itens, e a terceira como saida do que
# será necessário para a realização da reunião, sugerindo ainda outros itens adicionais.


from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMainWindow
from PyQt6 import QtGui
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt
import sys


# classe da tela principal:
class Party_Organizer(QMainWindow):
    def __init__(self):
        super().__init__()

        # definimos a paleta de cores da janela:
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(126, 194, 239))
        self.setPalette(palette)

        # definimos um título:
        self.setWindowTitle("Party Organizer")

        # label para pessoas:
        people_label = self.people_label = QLabel(
            "Quantidade de pessoas: ", self)
        self.people_label.move(45, 30)
        people_label.setWordWrap(True)

        # label para doces:
        candies_label = self.candies_label = QLabel(
            "Quantidade de doces:", self)
        self.candies_label.move(45, 100)
        candies_label.setWordWrap(True)

        # label para salgados:
        snacks_label = self.snacks_label = QLabel(
            "Quantidade de Salgados:", self)
        self.snacks_label.move(45, 150)
        snacks_label.setWordWrap(True)

        # label para bebidas:
        drinks_label = self.drinks_label = QLabel(
            "Quantidade de Bebidas ( Litro )", self)
        self.drinks_label.move(45, 200)
        drinks_label.setWordWrap(True)

        # label para bolo;
        cake_label = self.cake_label = QLabel("Fatias de bolo:", self)
        self.cake_label.move(45, 250)

        # definimos a fonte da label
        font_general = QtGui.QFont()
        font_general.setPointSize(10)
        font_general.setBold(True)
        font_general.setFamily('Arial')
        people_label.setFont(font_general)
        candies_label.setFont(font_general)
        snacks_label.setFont(font_general)
        drinks_label.setFont(font_general)
        cake_label.setFont(font_general)

        # campo em branco para entrada de dados em pessoas:
        people_entry = self.people_entry = QLineEdit(self)
        self.people_entry.move(200, 30)

        # campo em branco para entrada de dados em doces:
        candies_entry = self.candies_entry = QLineEdit(self)
        self.candies_entry.move(200, 100)

        # campo em branco para entrada de dados em salgados:
        snacks_entry = self.snacks_entry = QLineEdit(self)
        self.snacks_entry.move(200, 150)

        # campo em branco para entrada de dados em bebidas:
        drinks_entry = self.drinks_entry = QLineEdit(self)
        self.drinks_entry.move(200, 200)

        # campo em branco para entrada de dados em bolo:
        cake_entry = self.cake_entry = QLineEdit(self)
        self.cake_entry.move(200, 250)

        # alinhamento dos dados na blank:
        self.people_entry.setAlignment(Qt.AlignmentFlag(-3))
        self.cake_entry.setAlignment(Qt.AlignmentFlag(-3))
        self.drinks_entry.setAlignment(Qt.AlignmentFlag(-3))
        self.snacks_entry.setAlignment(Qt.AlignmentFlag(-3))
        self.candies_entry.setAlignment(Qt.AlignmentFlag(-3))

        # decoramos o campo de entrada de dados:
        people_entry.setStyleSheet(
            "background-color: rgb(91, 211, 239); border: 2px solid; border-radius: 3px; font-style: italic")
        people_entry.setPlaceholderText("pessoas")

        candies_entry.setStyleSheet(
            "background-color:  rgb(91, 129, 239); border: 2px solid; border-radius: 3px; font-style: italic")
        candies_entry.setPlaceholderText("doces")

        snacks_entry.setStyleSheet(
            "background-color:  rgb(91, 129, 239); border: 2px solid; border-radius: 3px; font-style: italic")
        snacks_entry.setPlaceholderText("salgados")

        drinks_entry.setStyleSheet(
            "background-color:  rgb(91, 129, 239); border: 2px solid; border-radius: 3px; font-style: italic")
        drinks_entry.setPlaceholderText("bebidas")

        cake_entry.setStyleSheet(
            "background-color:  rgb(91, 129, 239); border: 2px solid; border-radius: 3px; font-style: italic")
        cake_entry.setPlaceholderText("bolo")

        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.move(200, 300)
        self.calculate_button.clicked.connect(self.calculate_food)

    # funçao que calcula a quantidade necessária de comida:
    def calculate_food(self):
        num_people = int(self.people_entry.text())

        num_candies = num_people * 2
        num_snacks = num_people * 2
        num_drink = int(num_people * 0.5)
        num_cake = num_people * 2

        self.candies_entry.setText(str(num_candies))
        self.snacks_entry.setText(str(num_snacks))
        self.drinks_entry.setText(str(num_drink))
        self.cake_entry.setText(str(num_cake))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Party_Organizer()

    # define a geometria da janela principal do GUI:
    window.setGeometry(100, 100, 400, 400)

    window.show()

    # garante que a aplicação eja finalizada de forma adequada quando o usuário fechar a janela principal da GUI:
    sys.exit(app.exec())
