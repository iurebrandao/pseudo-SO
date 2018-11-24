from modules import file_manager as fm
from modules import process_manager as pm
from modules import memory_manager as mm
from modules import queue_manager as qm


class Dispatcher:
    def __init__(self):
        self.processManager = pm.ProcessManager()
        self.fileManager = fm.FileManager()
        self.memoryManager = mm.MemoryManager()
        self.queueManager = qm.QueueManager()

        self.runningProcess = None

    def run(self):
        print('Iniciando o SO...')
        # Ordenando os processos por odem de chegada
        self.processManager.processes_to_start.sort(key=lambda x: x.tempo_de_inicializacao, reverse=True)

        # Inicializando o PID para os processos
        PID = 0
        time = 0

        while len(self.processManager.processes_to_start) != 0 or not self.queueManager.empty():
            for process in self.processManager.processes_to_start:
                if process.tempo_de_inicializacao > time:
                    break

                if self.memoryManager.alloc_memory(process):
                    self.processManager.processes_to_start.remove(process)
                    process.PID = PID
                    PID += 1
                    self.queueManager.add_new_process(process)
                    process.print()

            self.runningProcess = self.queueManager.get_next_running_process(self.runningProcess)

            if self.runningProcess is not None:
                self.fileManager.run_op(self.runningProcess)

                if self.runningProcess.tempo_de_processador == 0:
                    self.memoryManager.free_memory(self.runningProcess)
                    self.queueManager.remove_process(self.runningProcess)
                    self.runningProcess = None

            time += 1

        self.fileManager.print()

    def print_file_system(self, operation, process):
        print('Sistema de arquivos =>')
        print('operacao ' + str(operation) + '=> ' + 'Falha')
        print('O processo ' + str(process.PID) + ' executou com sucesso')
        print('\n')
