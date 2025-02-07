import sys
import os
import time
import requests
import pythoncom
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QIcon
from pywinauto import Desktop

class NoWatermark(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Medal Watermark Bypass')
        self.setWindowIcon(QIcon("nw.ico"))
        self.setGeometry(100, 100, 500, 400)
        self.layout = QtWidgets.QVBoxLayout()
        self.log_area = QtWidgets.QTextEdit(self)
        self.log_area.setReadOnly(True)
        self.layout.addWidget(self.log_area)
        self.download_button = QtWidgets.QPushButton('Start Download', self)
        self.download_button.clicked.connect(self.start_download)
        self.layout.addWidget(self.download_button)
        self.setLayout(self.layout)
        self.setStyleSheet("""
            QWidget {
                background-color: #2E2E2E;
                color: #FFFFFF;
            }
            QPushButton {
                background-color:rgb(117, 84, 159);
                color: white;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: rgb(117, 84, 159);
            }
            QTextEdit {
                background-color: #1E1E1E;
                color: #FFFFFF;
                border: 1px solid rgb(117, 84, 159);
            }
        """)
    def log(self, message):
        self.log_area.append(message)

    def start_download(self):
        self.download_button.setEnabled(False)
        self.thread = DownloadThread()
        self.thread.log_signal.connect(self.log)
        self.thread.finished.connect(lambda: self.download_button.setEnabled(True))
        self.thread.start()

class DownloadThread(QtCore.QThread):
    log_signal = QtCore.pyqtSignal(str)

    def run(self):
        pythoncom.CoInitialize() 
        self.log_signal.emit("🔍 Scanning for the Medal Window...")
        video_url = self.no_watermark()
        self.log_signal.emit(f"🎯 Extracted download URL")  # : {video_url}
        filename = video_url.split("/")[-1].split("?")[0]
        download_path = os.path.join(os.getcwd(), filename)
        self.log_signal.emit(f"⬇️ Downloading video to: {download_path}")
        response = requests.get(video_url, stream=True)
        if response.status_code == 200:
            with open(download_path, "wb") as f:
                for chunk in response.iter_content(1024): 
                    f.write(chunk)
            self.log_signal.emit("✅ Download complete!")
        else:
            self.log_signal.emit(f"❌ Failed to download: {response.status_code}")
        pythoncom.CoUninitialize()

    def no_watermark(self):
        while True:
            try:
                for window in Desktop(backend="win32").windows():
                    title = window.window_text()
                    if title.startswith("https://cdn.medal.tv/ugcc/content-concat/"):
                        self.log_signal.emit(f"✅ Found Window")  # : {title}
                        window.close()
                        return title
            except Exception as e:
                self.log_signal.emit(f"❌ Error: {e}")
            time.sleep(1)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    downloader = NoWatermark()
    downloader.show()
    sys.exit(app.exec_())
