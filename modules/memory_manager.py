
SIZE_REAL_TIME_MEMORY = 64
SIZE_USER_MEMORY = 960


class MemoryManager:
    def __init__(self):
        self.memory = [0] * (SIZE_REAL_TIME_MEMORY + SIZE_USER_MEMORY)

    def alloc_memory(self, process):
        memory_start = 0

        # If the process isn't real-time it cannot use the first SIZE_REAL_TIME_MEMORY blocks of the memory
        if process.prioridade != 0:
            memory_start = SIZE_REAL_TIME_MEMORY

        for i in range(memory_start, len(self.memory) - process.blocos_em_memoria + 1):
            if sum(self.memory[i: i + process.blocos_em_memoria]) == 0:
                self.memory[i: i + process.blocos_em_memoria] = [1] * process.blocos_em_memoria
                process.offset = i
                return True

        print("Memory => Não foi possível alocar " + str(process.blocos_em_memoria) + " blocos na memória")

        return False

    def free_memory(self, process):
        self.memory[process.offset: process.offset + process.blocos_em_memoria] = [0] * process.blocos_em_memoria
