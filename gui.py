#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import summ



class Interface(QWidget):

	def __init__(self):
		super().__init__()
		self.initUI()


	def initUI(self):


		#configurações de janela
		self.resize(600,700)
		self.setWindowTitle('Tokenizer - Tópicos CC 2016.2 UFPI')
		self.setStyleSheet("background-color: gray")


		#declaração de inputs e outputs
		self.textChoose = QLineEdit(self)
		self.textChoose.setStyleSheet("background-color: white")

		self.textShow = QLabel(self)
		self.textShow.setStyleSheet("background-color: white")
		self.textShow.setWordWrap(True)

		self.scroll = QScrollArea(self)
		self.scroll.setWidget(self.textShow)
		self.scroll.setWidgetResizable(True)

		#customização da fonte do output
		font = QFont("Arial", 12, QFont.Bold)
		self.textShow.setAlignment(Qt.AlignTop)
		self.textShow.setFont(font)

		#caixa "sobre"
		self.message = QMessageBox(self)
		self.message.setWindowTitle("Sobre")
		self.message.setText("	DIE - UFPI - Ciência da Computação\n\n"
			"Programa desenvolvido como trabalho da disciplina de Tópicos em Computação\n\n"
			"Professor: Raimundo Moura\n\n"
			"Alunos: Pablo, Arthur e Renato\n\n"
			"Período: 2016.2")
		font = QFont("Arial", 12, QFont.DemiBold)
		self.message.setFont(font)
		self.message.setStyleSheet("background-color: white")

		#declaração de botões e descrições
		self.chooseFile = QPushButton('Escolher Arquivo', self)
		self.chooseFile.setToolTip('Escolher um arquivo texto de entrada.')
		self.chooseFile.setStyleSheet("QPushButton { background-color: white }"
				"QPushButton:pressed { background-color: grey }" )

		self.about = QPushButton('Sobre', self)
		self.about.setToolTip('Informações sobre o aplicativo')
		self.about.setStyleSheet("QPushButton { background-color: white }"
				"QPushButton:pressed { background-color: grey }" )

		#declaração e definição de layout
		lay1 = QVBoxLayout(self)
		lay2 = QHBoxLayout()
		lay2.addWidget(self.textChoose)
		lay2.addWidget(self.chooseFile)
		lay1.addLayout(lay2)
		lay1.addWidget(self.scroll)
		lay1.addWidget(self.about)

		self.setLayout(lay1)


		#declaração de conexões entre botões e ações
		self.chooseFile.clicked.connect(self.escolherArquivo)

		self.about.clicked.connect(self.itsAbout)

		#mostrando a tela
		self.show()

	#funções utilizadas

	def escolherArquivo(self):
		filename = QFileDialog().getOpenFileName(self, 'Selecionar arquivo de entrada','/home', ".txt(*.txt)")
		if filename == ('',''):
			self.textShow.setText("Arquivo Inválido.")
			return
		self.textChoose.setText(str(filename[0]))
		text = summ.tokenizer(filename[0])
		self.textShow.setText(text)


	def itsAbout(self):
		self.message.exec_()


#loop de execução
if __name__ == '__main__':

	app = QApplication(sys.argv)
	app.setStyle("fusion")
	apt = Interface()
	sys.exit(app.exec_())
