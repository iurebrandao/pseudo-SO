from modules import file_manager as fm
from modules import process_manager as pm


class Dispatcher:
    def __init__(self):
        self.processManager = pm.ProcessManager()
        self.fileManager = fm.FileManager()

    def run(self):
        print('Iniciando o SO...')
        # Ordenando os processos por odem de chegada
        self.processManager.processes_to_start.sort(key=lambda x: x.tempo_de_inicializacao, reverse=True)

        # Inicializando o PID para os processos
        PID = 0
        for process in self.processManager.processes_to_start:
            process.PID = PID
            PID += 1
            self.print_dispatcher(process)
            operation = 0
            self.print_file_system(operation, process)


    def print_dispatcher(self, process):
        print('dispatcher =>')
        print('PID: ' + str(process.PID))
        print('offset: ')
        print('blocks: ' + str(process.blocos_em_memoria))
        print('priority: ' + str(process.prioridade))
        print('time: ' + str(process.tempo_de_processador))
        print('printer: ' + str(process.numero_codigo_da_impresora_requisitada))
        print('scanner: ' + str(process.requisicao_do_scanner))
        print('modem: ' + str(process.requisicao_do_modem))
        print('\n')

    def print_file_system(self, operation, process):
        print('Sistema de arquivos =>')
        print('operacao ' + str(operation) + '=> ' + 'Falha')
        print('O processo ' + str(process.PID) + ' executou com sucesso')
        print('\n')
