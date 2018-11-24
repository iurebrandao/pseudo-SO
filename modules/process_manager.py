import sys

class ProcessInfo:
    """ Represents the instance of one process """
    def __init__(self, info_line):
        info = info_line.split(',')
        self.tempo_de_inicializacao = int(info[0])
        self.prioridade = int(info[1])
        self.tempo_de_processador = int(info[2])
        self.blocos_em_memoria = int(info[3])
        self.numero_codigo_da_impresora_requisitada = int(info[4])
        self.requisicao_do_scanner = int(info[5])
        self.requisicao_do_modem = int(info[6])
        self.numero_codigo_do_disco = int(info[7])

        self.offset = -1
        self.PID = -1
        self.created_files = []

    def print(self):
        print('dispatcher =>')
        print('PID: ' + str(self.PID))
        print('offset: ' + str(self.offset))
        print('blocks: ' + str(self.blocos_em_memoria))
        print('priority: ' + str(self.prioridade))
        print('time: ' + str(self.tempo_de_processador))
        print('printer: ' + str(self.numero_codigo_da_impresora_requisitada))
        print('scanner: ' + str(self.requisicao_do_scanner))
        print('modem: ' + str(self.requisicao_do_modem))
        print('\n')


class ProcessManager:
    def __init__(self):
        with open(sys.argv[1], 'r') as f:
            self.processes_to_start = [ProcessInfo(line) for line in f]