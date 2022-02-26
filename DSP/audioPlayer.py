from PyQt5 import QtMultimedia
from PyQt5.QtCore import QUrl

file = QUrl.fromLocalFile(wav_file) # 音频文件路径
content = QtMultimedia.QMediaContent(file)
player.setMedia(content)
player.setVolume(50.0)
player.play()