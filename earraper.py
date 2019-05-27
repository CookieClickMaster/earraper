from pydub import AudioSegment
from PyQt5.QtGui import QFont, QIcon, QPixmap 
from PyQt5.QtWidgets import QWidget, QLabel, QSlider, QLineEdit, QApplication, QPushButton, QFileDialog, QRadioButton
from PyQt5.QtCore import Qt, QByteArray
from time import sleep
from threading import Thread
import sys
import win32gui, win32con

Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)


def iconFromBase64(base64):
    pixmap = QPixmap()
    pixmap.loadFromData(QByteArray.fromBase64(base64))
    icon = QIcon(pixmap)
    return icon 

image_base64 = b"R0lGODlhGQAZAHAAACH5BAEAAPwALAAAAAAZABkAhwAAAAAAMwAAZgAAmQAAzAAA/wArAAArMwArZgArmQArzAAr/wBVAABVMwBVZgBVmQBVzABV/wCAAACAMwCAZgCAmQCAzACA/wCqAACqMwCqZgCqmQCqzACq/wDVAADVMwDVZgDVmQDVzADV/wD/AAD/MwD/ZgD/mQD/zAD//zMAADMAMzMAZjMAmTMAzDMA/zMrADMrMzMrZjMrmTMrzDMr/zNVADNVMzNVZjNVmTNVzDNV/zOAADOAMzOAZjOAmTOAzDOA/zOqADOqMzOqZjOqmTOqzDOq/zPVADPVMzPVZjPVmTPVzDPV/zP/ADP/MzP/ZjP/mTP/zDP//2YAAGYAM2YAZmYAmWYAzGYA/2YrAGYrM2YrZmYrmWYrzGYr/2ZVAGZVM2ZVZmZVmWZVzGZV/2aAAGaAM2aAZmaAmWaAzGaA/2aqAGaqM2aqZmaqmWaqzGaq/2bVAGbVM2bVZmbVmWbVzGbV/2b/AGb/M2b/Zmb/mWb/zGb//5kAAJkAM5kAZpkAmZkAzJkA/5krAJkrM5krZpkrmZkrzJkr/5lVAJlVM5lVZplVmZlVzJlV/5mAAJmAM5mAZpmAmZmAzJmA/5mqAJmqM5mqZpmqmZmqzJmq/5nVAJnVM5nVZpnVmZnVzJnV/5n/AJn/M5n/Zpn/mZn/zJn//8wAAMwAM8wAZswAmcwAzMwA/8wrAMwrM8wrZswrmcwrzMwr/8xVAMxVM8xVZsxVmcxVzMxV/8yAAMyAM8yAZsyAmcyAzMyA/8yqAMyqM8yqZsyqmcyqzMyq/8zVAMzVM8zVZszVmczVzMzV/8z/AMz/M8z/Zsz/mcz/zMz///8AAP8AM/8AZv8Amf8AzP8A//8rAP8rM/8rZv8rmf8rzP8r//9VAP9VM/9VZv9Vmf9VzP9V//+AAP+AM/+AZv+Amf+AzP+A//+qAP+qM/+qZv+qmf+qzP+q///VAP/VM//VZv/Vmf/VzP/V////AP//M///Zv//mf//zP///wAAAAAAAAAAAAAAAAjAAPcJHEiwoMGDB8UAQMiwYCYAADI1bPgQIjGCkwDcmLhPGUSIygh6hDjxo0WDChciNAlRYkeX+1IKVDYpU02WIAVCFDMwRsR9OHFe7LhzIMmgLIfqVLnP50ikED8RfLhxX8aKUAEoXToTAJqsJwmSJJoya0ixMQQ+zAgWZkwAkwR+xQpVaUWjC8ECOJvy7MO0Bct+HJqT68EbLN3i5YlwhcmzA4lBrMrQ5NavABiXLCyQWAzIHFtybKhM8+jTCAMCADs="

app = QApplication(sys.argv)

window = QWidget()

icon = iconFromBase64(image_base64)
window.setWindowIcon(icon)

window.setGeometry(0, 0, 410, 370)
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
    if b1.isChecked() == True:
    	sndboosted = sndloud.low_pass_filter(lowpassfreq)
    	sndboosted.export("Earraped.mp3", format='mp3')
    elif b2.isChecked() == True:
    	sndboosted = sndloud.low_pass_filter(lowpassfreq)
    	sndboosted2 = sndboosted.low_pass_filter(lowpassfreq)
    	sndboosted2.export("Earraped.mp3", format='mp3')
    elif b3.isChecked() == True:
    	sndboosted = sndloud.low_pass_filter(lowpassfreq)
    	sndboosted2 = sndboosted.low_pass_filter(lowpassfreq)
    	sndboosted3 = sndboosted2.low_pass_filter(lowpassfreq)
    	sndboosted3.export("Earraped.mp3", format='mp3')
    else:
        pass
    	
   	
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
btn.move(9,70)
btn.resize(385,30)
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

nb3 = QLabel("500", window)
nb3.move(166,118)
nb3.setFont(QFont("Arial thin", 8, QFont.Black))
nb3.setStyleSheet('color: gray')
nb3.show()

nb3 = QLabel("2250", window)
nb3.move(270,118)
nb3.setFont(QFont("Arial thin", 8, QFont.Black))
nb3.setStyleSheet('color: gray')
nb3.show()

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

b1 = QRadioButton("x1", window)
b1.setChecked(True)
b1.move(140, 187)
b1.show()

b2 = QRadioButton("x2", window)
b2.setChecked(False)
b2.move(180, 187)
b2.show()

b3 = QRadioButton("x3", window)
b3.setChecked(False)
b3.move(220, 187)
b3.show()

con = QLabel("Convert", window)
con.move(10,210)
con.setFont(QFont("Arial", 12, QFont.Black))
con.show()

ln3 = QLabel("____________________", window)
ln3.move(92,197)
ln3.setFont(QFont("Arial bold", 17, QFont.Black))
ln3.show()

btn2 = QPushButton("Convert", window)
btn2.clicked.connect(runcon)
btn2.setFont(QFont("Arial light", 10, QFont.Black))
btn2.resize(385,70)
btn2.move(10,235)
btn2.show()

nb3 = QLabel("*Note: Output file will be exported to the same directory as Earraper", window)
nb3.move(10,310)
nb3.setFont(QFont("Arial thin", 8, QFont.Black))
nb3.setStyleSheet('color: gray')
nb3.show()

st = QLabel("Status:", window)
st.move(10,330)
st.setFont(QFont("Arial", 12, QFont.Black))
st.show()

stat = QLabel("Idle                                                  ", window)
stat.move(80,330)
stat.setFont(QFont("Arial", 12, QFont.Black))
stat.setStyleSheet('color: green')
stat.show()

d = QLabel("Filter Multiplier:", window)
d.move(10,185)
d.setFont(QFont("Arial light", 11, QFont.Black))
d.show()

window.show()

sys.exit(app.exec_())
