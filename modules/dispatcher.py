from modules import file_manager as fm
from modules import process_manager as pm

class Dispatcher():
    def __init__(self):
        processManager = pm.ProcessManager()
        fileManager = fm.FileManager()