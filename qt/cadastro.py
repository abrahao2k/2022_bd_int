''' código SQL do banco utilizado neste exemplo

create database grafico;

use grafico;

create table pessoa(
id int primary key auto_increment,
nome varchar(100) not null,
email varchar(100));

'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import mariadb
conexao = mariadb.connect(host="localhost", user="root",
    password="", database="grafico")
cursor = conexao.cursor()

class Ui_Janela(object):
    def setupUi(self, Janela):
        Janela.setObjectName("Janela")
        Janela.resize(292, 112)
        self.centralwidget = QtWidgets.QWidget(Janela)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_nome = QtWidgets.QLabel(self.centralwidget)
        self.label_nome.setObjectName("label_nome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_nome)
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setObjectName("label_email")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_email)
        self.lineEdit_nome = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nome.setObjectName("lineEdit_nome")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_nome)
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_email)
        self.pushButton_inserir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_inserir.setObjectName("pushButton_inserir")
        self.pushButton_inserir.clicked.connect(self.inserir)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pushButton_inserir)
        Janela.setCentralWidget(self.centralwidget)

        self.retranslateUi(Janela)
        QtCore.QMetaObject.connectSlotsByName(Janela)

    def retranslateUi(self, Janela):
        _translate = QtCore.QCoreApplication.translate
        Janela.setWindowTitle(_translate("Janela", "Cadastro de Pessoas"))
        self.label_nome.setText(_translate("Janela", "Nome:"))
        self.label_email.setText(_translate("Janela", "Email:"))
        self.pushButton_inserir.setText(_translate("Janela", "Inserir"))

    def inserir(self):
        nome  = self.lineEdit_nome.text()
        email = self.lineEdit_email.text()
        cmd = "INSERT INTO pessoa VALUES (null, %s, %s)"
        cursor.execute(cmd, (nome, email) )
        conexao.commit()
        
        msg = QMessageBox()
        msg.setText("Inserido com sucesso.")
        msg.setWindowTitle("Aviso")
        msg.exec_()
        
        self.lineEdit_nome.setText("")
        self.lineEdit_email.setText("")
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Janela = QtWidgets.QMainWindow()
    ui = Ui_Janela()
    ui.setupUi(Janela)
    Janela.show()
    sys.exit(app.exec_())
