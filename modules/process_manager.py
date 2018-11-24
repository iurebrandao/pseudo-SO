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
        self.program_count = 0

    def print(self):
        print('dispatcher =>')
        print('\tPID: ' + str(self.PID))
        print('\toffset: ' + str(self.offset))
        print('\tblocks: ' + str(self.blocos_em_memoria))
        print('\tpriority: ' + str(self.prioridade))
        print('\ttime: ' + str(self.tempo_de_processador))
        print('\tprinter: ' + str(self.numero_codigo_da_impresora_requisitada))
        print('\tscanner: ' + str(self.requisicao_do_scanner))
        print('\tmodem: ' + str(self.requisicao_do_modem))
        print()

    def print_instruction(self):
        print("Process " + str(self.PID) + " =>")
        if self.program_count == 1:
            print("\tSTARTED")
        print("\tExecuted instruction " + str(self.program_count))
        if self.cpu_time_ended():
            print("\treturn SIGINT")

    def cpu_time_ended(self):
        return self.program_count == self.tempo_de_processador


class ProcessManager:
    def __init__(self):
        with open(sys.argv[1], 'r') as f:
            self.processes_to_start = [ProcessInfo(line) for line in f]
