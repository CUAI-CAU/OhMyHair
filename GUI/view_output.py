import sys
import urllib.request
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic, QtGui 
import torch # For model's output

### Connect to ui file ###
form_class = uic.loadUiType("output.ui")[0]

### Prediction of model ###
prediction_vec = torch.Tensor([0.1864, 0.4095, 0.4885, 0.0716, 0.5891, 0.2249]) # it's a temp prediction... (needed to be amended)
prediction_list = ['미세각질', '피지과다', '모낭사이홍반', '모낭홍반농포', '비듬', '탈모']
prediction = prediction_list[torch.argmax(prediction_vec)]

### Disease description ###
description = []    
with open("disease_explained.txt", 'r') as f:
    for line in f:
        description.append(line)


### GUI Output ###
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # Set the window title
        self.setWindowTitle("Oh My Head - CUAI winter project - Healthcare team")

        # Set size of window
        # self.setFixedSize(1280, 600)
        self.setFixedSize(1400, 700)

        # Title image
        self.qPixmapFileVar_title = QPixmap()
        self.qPixmapFileVar_title.load("logo_output.png")
        self.qPixmapFileVar_title = self.qPixmapFileVar_title.scaledToWidth(200)
        self.title_box.setPixmap(self.qPixmapFileVar_title)

        # Scalp text
        self.scalp_txt.setText("당신의 두피는 *{}*인 것으로 보입니다.".format(prediction))
        self.scalp_txt.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Bold))

        # Scalp image
        self.qPixmapFileVar_scalp = QPixmap()
        self.qPixmapFileVar_scalp.load("my_scalp.jpg")
        self.qPixmapFileVar_scalp = self.qPixmapFileVar_scalp.scaledToWidth(300)
        self.my_scalp.setPixmap(self.qPixmapFileVar_scalp)

        # Model prediction
        self.result_txt.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.model_prediction.setText("미세각질이 %.4f만큼, 피지과다가 %.4f만큼, 모낭사이홍반이 %.4f만큼, 모낭홍반농포가 %.4f만큼, 비듬이 %.4f만큼, 탈모가 %.4f만큼 있습니다."\
                                       % tuple(prediction_vec.tolist()))
        self.model_prediction.setFont(QtGui.QFont("Arial", 15))

        # Disease description
        self.result_txt2.setText(prediction + " 관련 정보")
        self.result_txt2.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.disease.setText(description[prediction_list.index(prediction)].split(':')[1].strip())
        self.disease.setFont(QtGui.QFont("Arial", 15))

        # Survey title
        self.analysis_title.setFont(QtGui.QFont("Arial", 15, QtGui.QFont.Bold))

        ## Survey figures
        # shampoo
        self.qPixmapFileVar_title2 = QPixmap()
        self.qPixmapFileVar_title2.load(f"figure/{prediction}_샴푸사용빈도.png")
        self.qPixmapFileVar_title2 = self.qPixmapFileVar_title2.scaledToWidth(720)
        self.shampoo_figure.setPixmap(self.qPixmapFileVar_title2)
        # perm
        self.qPixmapFileVar_title3 = QPixmap()
        self.qPixmapFileVar_title3.load(f"figure/{prediction}_펌주기.png")
        self.qPixmapFileVar_title3 = self.qPixmapFileVar_title3.scaledToWidth(720)
        self.perm_figure.setPixmap(self.qPixmapFileVar_title3)
        # dye
        self.qPixmapFileVar_title4 = QPixmap()
        self.qPixmapFileVar_title4.load(f"figure/{prediction}_염색주기.png")
        self.qPixmapFileVar_title4 = self.qPixmapFileVar_title4.scaledToWidth(720)
        self.dye_figure.setPixmap(self.qPixmapFileVar_title4)

        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 

    myWindow = WindowClass() 

    myWindow.show()

    app.exec_()