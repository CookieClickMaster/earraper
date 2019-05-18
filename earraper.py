from pydub import AudioSegment
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QLineEdit, QApplication, QPushButton, QFileDialog
from PyQt5.QtCore import Qt
from time import sleep
from threading import Thread
import sys

app = QApplication(sys.argv)
window = QWidget()

window.setGeometry(0, 0, 410, 330)
window.setWindowTitle("Earraper")


def openfile():
    global fl
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(window,"Choose File", "","Sound Files (*.mp3)", options=options)
    if fileName:
    	fl = fileName
    	btn.setText(fl)

    	

def status():
    stat.setStyleSheet('color: green')
    stat.setText("Done!")
    sleep(1)
    stat.setText("Idle")
    
    
def runcon():
    Thread(target=convert).start()

def convert():
    dbs = txt.text()
    db = int(dbs)
    lowpassfreq = slider.value()
    (lowpassfreq)
    sound = AudioSegment.from_mp3(fl)
    sndloud = sound + db
    stat.setStyleSheet('color: green')
    stat.setText("Converting...")
    sndboosted = sndloud.low_pass_filter(lowpassfreq)
    sndboosted.export("Earraped.mp3", format='mp3')
    status()
   
    



erpr = QLabel("Earraper V1.0", window)
erpr.move(250,5)
erpr.setFont(QFont("Arial", 17, QFont.Black))
erpr.show()
dev = QLabel("Developed by cududont", window)
dev.move(10,18)
dev.setFont(QFont("Arial thin", 8, QFont.Black))
dev.show()

ln1 = QLabel("__________________________", window)
ln1.move(8,10)
ln1.setFont(QFont("Arial bold", 17, QFont.Black))
ln1.show()

inp = QLabel("Input File (MP3 Only)", window)
inp.move(10,45)
inp.setFont(QFont("Arial", 12, QFont.Black))
inp.show()

ln2 = QLabel("_____________", window)
ln2.move(196,33)
ln2.setFont(QFont("Arial bold", 17, QFont.Black))
ln2.show()

btn = QPushButton("Choose File", window)
btn.clicked.connect(openfile)
btn.setFont(QFont("Arial light", 10, QFont.Black))
btn.resize(385,30)
btn.move(9,70)
btn.show()

sett = QLabel("Settings", window)
sett.move(10,100)
sett.setFont(QFont("Arial", 12, QFont.Black))
sett.show()

ln3 = QLabel("____________________", window)
ln3.move(92,88)
ln3.setFont(QFont("Arial bold", 17, QFont.Black))
ln3.show()

lp = QLabel("Lowpass Cutoff (Hz):", window)
lp.move(10,130)
lp.setFont(QFont("Arial light", 11, QFont.Black))
lp.show()

slider = QSlider(Qt.Horizontal, window)
slider.setFocusPolicy(Qt.StrongFocus)
slider.setTickInterval(2250)
slider.move(175,130)
slider.setMaximum(5000)
slider.setMinimum(500)
slider.setValue(2755)
slider.setTickPosition(2)
slider.show()
slider.resize(218,23)

nb1 = QLabel("500", window)
nb1.move(166,118)
nb1.setFont(QFont("Arial thin", 8, QFont.Black))
nb1.setStyleSheet('color: gray')
nb1.show()

nb2 = QLabel("2250", window)
nb2.move(270,118)
nb2.setFont(QFont("Arial thin", 8, QFont.Black))
nb2.setStyleSheet('color: gray')
nb2.show()

nb3 = QLabel("5000", window)
nb3.move(374,118)
nb3.setFont(QFont("Arial thin", 8, QFont.Black))
nb3.setStyleSheet('color: gray')
nb3.show()

lpsd = QLabel("dB Increase: ", window)
lpsd.move(10,157)
lpsd.setFont(QFont("Arial light", 11, QFont.Black))
lpsd.show()

plus = QLabel("+", window)
plus.move(107,161)
plus.setFont(QFont("Arial light", 9, QFont.Black))
plus.show()

txt = QLineEdit(window)
txt.setText("50")
txt.resize(80,20)
txt.move(120,158)
txt.show()

con = QLabel("Convert", window)
con.move(10,180)
con.setFont(QFont("Arial", 12, QFont.Black))
con.show()

ln3 = QLabel("____________________", window)
ln3.move(92,167)
ln3.setFont(QFont("Arial bold", 17, QFont.Black))
ln3.show()

btn2 = QPushButton("Convert", window)
btn2.clicked.connect(runcon)
btn2.setFont(QFont("Arial light", 10, QFont.Black))
btn2.resize(385,70)
btn2.move(10,205)
btn2.show()

nb3 = QLabel("*Note: Output file will be exported to the same directory as Earraper", window)
nb3.move(10,280)
nb3.setFont(QFont("Arial thin", 8, QFont.Black))
nb3.setStyleSheet('color: gray')
nb3.show()

st = QLabel("Status:", window)
st.move(10,300)
st.setFont(QFont("Arial", 12, QFont.Black))
st.show()

stat = QLabel("Idle                              ", window)
stat.move(80,300)
stat.setFont(QFont("Arial", 12, QFont.Black))
stat.setStyleSheet('color: green')
stat.show()

window.show()

sys.exit(app.exec_())
