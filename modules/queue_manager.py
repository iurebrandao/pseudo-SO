
QUANTUM = 1  # Instruction
MAX_PROCESSES = 1000

class QueueManager:
    def __init__(self):
        self.queueRealTime = []
        self.queueUserPriority1 = []
        self.queueUserPriority2 = []
        self.queueUserPriority3 = []

    def add_new_process(self, process):
        if process.prioridade == 0:
            self.queueRealTime.append(process)
        elif process.prioridade == 1:
            self.queueUserPriority1.append(process)
        elif process.prioridade == 2:
            self.queueUserPriority2.append(process)
        elif process.prioridade == 3:
            self.queueUserPriority3.append(process)

    def get_next_running_process(self, runningProcess):
        # If the process has used all it's quantum the process is interrupted and its priority decreases
        if runningProcess and runningProcess.current_quantum_used == QUANTUM and runningProcess.prioridade != 0:
            self.decrease_priority(runningProcess)
            runningProcess = None

        nextProcess = runningProcess

        if nextProcess is None:
            if len(self.queueRealTime):
                nextProcess = self.queueRealTime[0]
                nextProcess.current_quantum_used = 0
            elif len(self.queueUserPriority1):
                nextProcess = self.queueUserPriority1[0]
                nextProcess.current_quantum_used = 0
            elif len(self.queueUserPriority2):
                nextProcess = self.queueUserPriority2[0]
                nextProcess.current_quantum_used = 0
            elif len(self.queueUserPriority3):
                nextProcess = self.queueUserPriority3[0]
                nextProcess.current_quantum_used = 0

        return nextProcess

    def decrease_priority(self, process):
        if process.prioridade == 1:
            self.queueUserPriority1.remove(process)
            process.prioridade = 2
            self.queueUserPriority2.append(process)

        elif process.prioridade == 2:
            self.queueUserPriority2.remove(process)
            process.prioridade = 3
            self.queueUserPriority3.append(process)

        elif process.prioridade == 3:
            # The process already has the lowest priority, so just move the process to the end of the queue
            self.queueUserPriority3.remove(process)
            self.queueUserPriority3.append(process)

    def remove_process(self, process):
        if process.prioridade == 0:
            self.queueRealTime.remove(process)
        elif process.prioridade == 1:
            self.queueUserPriority1.remove(process)
        elif process.prioridade == 2:
            self.queueUserPriority2.remove(process)
        elif process.prioridade == 3:
            self.queueUserPriority3.remove(process)

    def empty(self):
        return len(self.queueRealTime) == 0 and\
               len(self.queueUserPriority1) == 0 and\
               len(self.queueUserPriority2) == 0 and\
               len(self.queueUserPriority3) == 0

    def process_limit_reached(self):
        return MAX_PROCESSES <= (len(self.queueRealTime) +
                                 len(self.queueUserPriority1) +
                                 len(self.queueUserPriority2) +
                                 len(self.queueUserPriority3))
