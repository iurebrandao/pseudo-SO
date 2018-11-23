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


class ProcessManager:
    def __init__(self):
        with open(sys.argv[1], 'r') as f:
            self.processes_to_start = [ProcessInfo(line) for line in f]