import sys
from PyQt5.QtWidgets import *


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.textEdit1 = QTextEdit()
        self.textEdit2 = QTextEdit()

        lbl0 = QLabel("origin")
        lbl1 = QLabel("after")
        vbox = QVBoxLayout()
        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        lbl_cb = QLabel("Choose:")
        self.cb = QComboBox()
        self.cb.addItems(["Remove Duplicate"])
        self.cb.addItem("Original")
        # self.cb.currentIndexChanged.connect(self.cb_changed)
        hbox1.addWidget(lbl_cb)
        hbox1.addWidget(self.cb)

        btn1 = QPushButton("Convert")
        btn2 = QPushButton("Import")
        btn3 = QPushButton("Export")
        btn1.clicked.connect(self.button_clicked)
        btn2.clicked.connect(self.button_import)
        btn3.clicked.connect(self.button_export)
        hbox2.addWidget(btn1)
        hbox2.addStretch(0)
        hbox2.addWidget(btn2)
        hbox2.addWidget(btn3)

        vbox.addLayout(hbox1)
        vbox.addWidget(lbl0)
        vbox.addWidget(self.textEdit1)
        vbox.addLayout(hbox2)
        vbox.addWidget(lbl1)
        vbox.addWidget(self.textEdit2)

        self.setLayout(vbox)
        self.resize(250, 150)
        self.center()

        self.setWindowTitle('Text Edit')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def button_clicked(self):
        if self.cb.currentText() == "Remove Duplicate":
            lst2 = []
            lst = self.textEdit1.toPlainText().split()
            for i in lst:
                if i in lst2:
                    continue
                lst2.append(i)
            self.textEdit2.clear()
            for j in lst2:
                self.textEdit2.append(j)
        else:
            self.textEdit2.setPlainText(self.textEdit1.toPlainText())

    def button_import(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Open', 'E:\\TestDatas', 'Text(*.txt)')
        if fname != '':
            f = open(fname, 'r', encoding='UTF-8')
            line = f.read()
            self.textEdit1.setText(line)
            f.close()

    def button_export(self):
        fname, _ = QFileDialog.getSaveFileName(self, 'Save', 'E:\\TestDatas', 'Text(*.txt)')
        if fname != '':
            f = open(fname, 'w', encoding='UTF-8')
            f.write(self.textEdit2.toPlainText())
            f.close()

    def cb_changed(self):
        print(self.cb.currentText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
