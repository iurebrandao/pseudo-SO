import sys


class MemoryManager:
    def __init__(self):
        self.blocos_tempo_real = 64
        self.blocos_usuario = 960
        self.offset = []

    def alloc_memory(self, process):

        if process.prioridade == 0:
            if self.blocos_tempo_real >= process.blocos_em_memoria:
                self.blocos_tempo_real = self.blocos_tempo_real - process.blocos_em_memoria
                return True

        if self.blocos_usuario >= process.blocos_em_memoria:
            self.blocos_usuario = self.blocos_usuario - process.blocos_em_memoria
            self.alocado_em_espaco_usuario = True
            return True

        return False

    def free_memory(self, process):

        if process.alocado_em_espaco_usuario:
            self.blocos_usuario += process.blocos_em_memoria
        else:
            self.blocos_tempo_real += process.blocos_em_memoria
