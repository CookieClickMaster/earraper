from pydub import AudioSegment
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from time import sleep
from threading import Thread

app = QtWidgets.QApplication([])
window = QtWidgets.QWidget()

window.setWindowIcon(QtGui.QIcon("i.ico"))

window.setGeometry(0, 0, 410, 330)
window.setWindowTitle("Earraper")
window.show()

def openfile():
    global fl
    options = QtWidgets.QFileDialog.Options()
    options |= QtWidgets.QFileDialog.DontUseNativeDialog
    fileName, _ = QtWidgets.QFileDialog.getOpenFileName(window,"Choose File", "","Sound Files (*.mp3)", options=options)
    if fileName:
    	print(fileName)
    	fl = fileName
    	btn.setText(fl)
    	

def status():
    stat.setStyleSheet('color: green')
    stat.setText("Converting...")
    sleep(2)
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
    print(lowpassfreq)
    sound = AudioSegment.from_mp3(fl)
    sndloud = sound + db
    status()
    sndboosted = sndloud.low_pass_filter(lowpassfreq)
    sndboosted.export("Earraped.mp3", format='mp3')
    



erpr = QtWidgets.QLabel("Earraper V1.0", window)
erpr.move(250,5)
erpr.setFont(QtGui.QFont("Arial", 17, QtGui.QFont.Black))
erpr.show()

dev = QtWidgets.QLabel("Developed by cududont", window)
dev.move(10,18)
dev.setFont(QtGui.QFont("Arial thin", 8, QtGui.QFont.Black))
dev.show()

ln1 = QtWidgets.QLabel("__________________________", window)
ln1.move(8,10)
ln1.setFont(QtGui.QFont("Arial bold", 17, QtGui.QFont.Black))
ln1.show()

inp = QtWidgets.QLabel("Input File (MP3 Only)", window)
inp.move(10,45)
inp.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Black))
inp.show()

ln2 = QtWidgets.QLabel("_____________", window)
ln2.move(196,33)
ln2.setFont(QtGui.QFont("Arial bold", 17, QtGui.QFont.Black))
ln2.show()

btn = QtWidgets.QPushButton("Choose File", window)
btn.clicked.connect(openfile)
btn.setFont(QtGui.QFont("Arial light", 10, QtGui.QFont.Black))
btn.resize(385,30)
btn.move(9,70)
btn.show()

sett = QtWidgets.QLabel("Settings", window)
sett.move(10,100)
sett.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Black))
sett.show()

ln3 = QtWidgets.QLabel("____________________", window)
ln3.move(92,88)
ln3.setFont(QtGui.QFont("Arial bold", 17, QtGui.QFont.Black))
ln3.show()

lp = QtWidgets.QLabel("Lowpass Cutoff (Hz):", window)
lp.move(10,130)
lp.setFont(QtGui.QFont("Arial light", 11, QtGui.QFont.Black))
lp.show()

slider = QtWidgets.QSlider(Qt.Horizontal, window)
slider.setFocusPolicy(Qt.StrongFocus)
slider.setTickInterval(2500)
slider.move(175,130)
slider.setMaximum(6000)
slider.setMinimum(1000)
slider.setValue(3500)
slider.setTickPosition(2)
slider.show()
slider.resize(218,23)

nb1 = QtWidgets.QLabel("1000", window)
nb1.move(166,118)
nb1.setFont(QtGui.QFont("Arial thin", 8, QtGui.QFont.Black))
nb1.setStyleSheet('color: gray')
nb1.show()

nb2 = QtWidgets.QLabel("3500", window)
nb2.move(270,118)
nb2.setFont(QtGui.QFont("Arial thin", 8, QtGui.QFont.Black))
nb2.setStyleSheet('color: gray')
nb2.show()

nb3 = QtWidgets.QLabel("6000", window)
nb3.move(374,118)
nb3.setFont(QtGui.QFont("Arial thin", 8, QtGui.QFont.Black))
nb3.setStyleSheet('color: gray')
nb3.show()

lpsd = QtWidgets.QLabel("dB Increase: ", window)
lpsd.move(10,157)
lpsd.setFont(QtGui.QFont("Arial light", 11, QtGui.QFont.Black))
lpsd.show()

plus = QtWidgets.QLabel("+", window)
plus.move(107,161)
plus.setFont(QtGui.QFont("Arial light", 9, QtGui.QFont.Black))
plus.show()

txt = QtWidgets.QLineEdit(window)
txt.setText("50")
txt.resize(80,20)
txt.move(120,158)
txt.show()

con = QtWidgets.QLabel("Convert", window)
con.move(10,180)
con.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Black))
con.show()

ln3 = QtWidgets.QLabel("____________________", window)
ln3.move(92,167)
ln3.setFont(QtGui.QFont("Arial bold", 17, QtGui.QFont.Black))
ln3.show()

btn2 = QtWidgets.QPushButton("Convert", window)
btn2.clicked.connect(runcon)
btn2.setFont(QtGui.QFont("Arial light", 10, QtGui.QFont.Black))
btn2.resize(385,70)
btn2.move(10,205)
btn2.show()

nb3 = QtWidgets.QLabel("*Note: Output file will be exported to the same directory as Earraper", window)
nb3.move(10,280)
nb3.setFont(QtGui.QFont("Arial thin", 8, QtGui.QFont.Black))
nb3.setStyleSheet('color: gray')
nb3.show()

st = QtWidgets.QLabel("Status:", window)
st.move(10,300)
st.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Black))
st.show()

stat = QtWidgets.QLabel("Idle                              ", window)
stat.move(80,300)
stat.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Black))
stat.setStyleSheet('color: green')
stat.show()


(app.exec_())
