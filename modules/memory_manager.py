
SIZE_REAL_TIME_MEMORY = 64
SIZE_USER_MEMORY = 960

class MemoryManager:
    def __init__(self):
        self.memory = [0] * (SIZE_REAL_TIME_MEMORY + SIZE_USER_MEMORY)

    def alloc_memory(self, process):
        memory_start = 0
        if process.prioridade != 0:
            memory_start = SIZE_REAL_TIME_MEMORY

        for i in range(memory_start, len(self.memory) - process.blocos_em_memoria):
            if sum(self.memory[i: process.blocos_em_memoria]) == 0:
                self.memory[i: process.blocos_em_memoria] = [1] * process.blocos_em_memoria
                process.offset = i
                return True

        return False

    def free_memory(self, process):
        self.memory[process.offset: process.offset + process.blocos_em_memoria] = [0] * process.blocos_em_memoria
