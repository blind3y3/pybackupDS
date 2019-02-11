from PyQt5.QtWidgets import *
from os import listdir, getenv
from datetime import datetime
from ctypes import *
import zipfile

resolution = [windll.user32.GetSystemMetrics(0), windll.user32.GetSystemMetrics(1)]
backups_dir = listdir(path=getenv('appdata') + "\\Backups\\")
zip_name = datetime.strftime(datetime.now(), "%d.%m.%Y_%H-%M-%S")


class GUI(QWidget):
	def __init__(self):
		super().__init__()
		self.initGUI()

	def initGUI(self):

		self.update()
		width = 640
		height = 480
		left = resolution[0]/2 - (width / 2)
		top = resolution[1]/2 - (height / 2)
		self.setGeometry(left, top, width, height)
		self.setWindowTitle('Backuper')

		textbox = QPlainTextEdit(str(backups_dir), self)
		textbox.move(10, 10)
		textbox.setFixedSize(width/2 - 20, height-20)

		ds2_button = QPushButton('DS2', self)
		ds2_button.move(width/2, 10)
		ds2_button.setFixedSize(width/2 - 20, 50)

		ds3_button = QPushButton('DS3', self)
		ds3_button.move(width / 2, 70)
		ds3_button.setFixedSize(width / 2 - 20, 50)

		label = QLabel('Wait for backup.', self)
		label.move(width/2, height - 60)
		label.setFixedSize(width / 2 - 20, 50)

		def ds2_backup():
			source = getenv('appdata') + '\\DarkSoulsII\\0110000108168c6b\\DS2SOFS0000.sl2'
			destination = getenv('appdata') + '\\Backups\\DS2_' + zip_name + '.zip'
			backup_it = zipfile.ZipFile(destination, 'w')
			backup_it.write(source, compress_type=zipfile.ZIP_DEFLATED)
			label.setText('DS2 was backuped!')
			textbox.appendPlainText('-' * 50)
			textbox.appendPlainText('Бэкапы находятся по адресу %appdata%\\Backups\\')

		def ds3_backup():
			source = getenv('appdata') + '\\DarkSoulsIII\\0110000108168c6b\\DS30000.sl2'
			destination = getenv('appdata') + '\\Backups\\DS3_' + zip_name + '.zip'
			backup_it = zipfile.ZipFile(destination, 'w')
			backup_it.write(source, compress_type=zipfile.ZIP_DEFLATED)
			label.setText('DS3 was backuped!')
			textbox.appendPlainText('-' * 50)
			textbox.appendPlainText('backups will place in %appdata%\\Backups\\')

		ds2_button.clicked.connect(ds2_backup)
		ds3_button.clicked.connect(ds3_backup)

		self.show()


app = QApplication([])
gui = GUI()
app.setStyle('Fusion')
app.exec()
