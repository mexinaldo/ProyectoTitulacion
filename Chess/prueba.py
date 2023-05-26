import subprocess

class Prueba:
    def __init__(self, filename):
        self.filename = filename
        subprocess.Popen(['C:\Program Files (x86)\Windows Media Player\wmplayer.exe', self.filename])
