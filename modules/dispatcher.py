from modules import file_manager as fm
from modules import process_manager as pm
from modules import memory_manager as mm
from modules import queue_manager as qm
from modules import io_manager as im


class Dispatcher:
    def __init__(self):
        print('Iniciando o SO...')
        self.processManager = pm.ProcessManager()
        self.fileManager = fm.FileManager()
        self.memoryManager = mm.MemoryManager()
        self.queueManager = qm.QueueManager()
        self.ioManager = im.IoManager()

        self.runningProcess = None

    def run(self):
        # Ordena os processos por odem de chegada
        self.processManager.processes_to_start.sort(key=lambda x: x.tempo_de_inicializacao)

        # Inicializando o PID para os processos e o tempo do sistema
        PID = 0
        time = 0

        while len(self.processManager.processes_to_start) != 0 or not self.queueManager.empty():
            print("\n\n\n\n--- Tempo " + str(time) + " ---")

            # Verifica se chegaram novos processos
            for process in self.processManager.processes_to_start.copy():
                if process.tempo_de_inicializacao > time or self.queueManager.process_limit_reached():
                    break

                # Tenta alocar os recursos de IO requisitados pelo processo
                io_get_result = self.ioManager.getIOdevice(process, PID)
                if not io_get_result:
                    continue

                # Tenta alocar a memória requisitada pelo processo
                memory_alloc_result = self.memoryManager.alloc_memory(process)
                if memory_alloc_result:
                    self.processManager.processes_to_start.remove(process)

                    # Inicia o processo
                    process.PID = PID
                    PID += 1

                    # Aciona o processo na fila de processos prontos de acordo com sua prioridade
                    self.queueManager.add_new_process(process)

                    # Imprime as informaçoes do novo processo
                    process.print()
                else:
                    self.ioManager.releaseIOdevice(process)

            # Encontra qual o próximo processo que irá executar de acordo com as regras de prioridade e de preempção
            self.runningProcess = self.queueManager.get_next_running_process(self.runningProcess)

            if self.runningProcess is not None:
                if not self.runningProcess.cpu_time_ended():
                    self.runningProcess.program_count += 1
                    self.runningProcess.current_quantum_used += 1

                    self.runningProcess.print_instruction()

                    # Executa a operação no sistema de arquivos
                    self.fileManager.run_op(self.runningProcess)

                # Encerra o processo quando seu tempo total de CPU foi utilizado
                if self.runningProcess.cpu_time_ended():
                    self.memoryManager.free_memory(self.runningProcess)
                    self.queueManager.remove_process(self.runningProcess)
                    self.ioManager.releaseIOdevice(self.runningProcess)
                    self.runningProcess = None

            time += 1
