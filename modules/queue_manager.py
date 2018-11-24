
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
        if runningProcess is None:
            if len(self.queueRealTime):
                return self.queueRealTime[0]
            if len(self.queueUserPriority1):
                return self.queueUserPriority1[0]
            if len(self.queueUserPriority2):
                return self.queueUserPriority2[0]
            if len(self.queueUserPriority3):
                return self.queueUserPriority3[0]
        else:
            if runningProcess.prioridade == 0:
                return runningProcess

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
