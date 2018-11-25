import sys

class FileInfo:
    def __init__(self, info_line):
        line = info_line.split(',')
        self.nome_arquivo = line[0].strip()
        self.primeiro_bloco = int(line[1])
        self.n_blocos = int(line[2])


class FileOp:
    def __init__(self, info_line):
        line = info_line.split(',')
        self.ID_Processo = int(line[0])
        self.Codigo_Operacao = int(line[1])
        self.Nome_arquivo = line[2].strip()
        self.se_operacaoCriar_numero_blocos = int(line[3]) if len(line) == 4 else None


class FileManager:
    def __init__(self):
        with open(sys.argv[2], 'r') as f:
            lines = f.read().splitlines()
            self.n_blocos = int(lines[0])
            self.n_segmentos = int(lines[1])
            self.files = [FileInfo(line) for line in lines[2: self.n_segmentos + 2]]
            self.operations = [FileOp(line) for line in lines[self.n_segmentos + 2:]]

        # Write initial files to disk
        self.disk = [None] * self.n_blocos
        for file in self.files:
            self.disk[file.primeiro_bloco: file.primeiro_bloco + file.n_blocos] = [file.nome_arquivo] * file.n_blocos
        self.print_disk()

    def print_disk(self):
        print("\tMapa do disco => | ", end='')
        for block in self.disk:
            nome = block if block is not None else '0'
            print(nome + ' | ', end='')

    def run_op(self, process):
        operation = None

        print("\nSistema de arquivos => ")

        # Find the next operation for the current running process
        for op in self.operations:
            if op.ID_Processo == process.PID:
                operation = op
                self.operations.remove(op)
                break

        if operation is not None:
            if operation.Codigo_Operacao == 0:
                self.create_file(process, operation)
            elif operation.Codigo_Operacao == 1:
                self.delete_file(process, operation)
            else:
                print("\tFalha: Operação desconhecida")
        else:
            print("\tNão foi encontrada nenhuma operação para o processo " + str(process.PID))

        self.print_disk()

    def create_file(self, process, operation):
        first_bock_fit = None

        # Check if file already exists
        if operation.Nome_arquivo not in self.disk:
            # Search the first continuous segment that can store the file
            for i in range(len(self.disk) - operation.se_operacaoCriar_numero_blocos):
                if all(b is None for b in self.disk[i: i + operation.se_operacaoCriar_numero_blocos]):
                    first_bock_fit = i

            if first_bock_fit is not None:
                # Write the file to the disk
                self.disk[first_bock_fit: first_bock_fit + operation.se_operacaoCriar_numero_blocos] =\
                    [operation.Nome_arquivo] * operation.se_operacaoCriar_numero_blocos

                # Stores the information that the file belongs to the current process
                process.created_files.append(operation.Nome_arquivo)

                # Print the details of the new file
                blocks_str = ', '.join(str(x) for x in list(range(first_bock_fit, first_bock_fit + operation.se_operacaoCriar_numero_blocos)))
                print("\tSucesso: O processo " + str(process.PID) + " criou o arquivo " + operation.Nome_arquivo +
                      " (blocos " + blocks_str + ")")
            else:
                print("\tFalha: O processo " + str(process.PID) + " não pode criar o arquivo " + operation.Nome_arquivo +
                      " (falta de espaço)")
        else:
            print("\tFalha: O processo " + str(process.PID) + " não pode criar o arquivo " + operation.Nome_arquivo +
                  " (arquivo já existe no disco)")

    def delete_file(self, process, operation):
        # Check if file exists
        if operation.Nome_arquivo in self.disk:
            # Check if the process has permission to delete tha file
            if process.prioridade == 0 or operation.Nome_arquivo in process.created_files:
                self.disk = list(map(lambda block: None if block == operation.Nome_arquivo else block, self.disk))
                print("\tSucesso: O processo " + str(process.PID) + " deletou o arquivo " + operation.Nome_arquivo)
            else:
                print("\tFalha: O processo " + str(process.PID) + " não pode deletar o arquivo " + operation.Nome_arquivo)
        else:
            print("\tFalha: O processo " + str(process.PID) + " não pode deletar o arquivo " + operation.Nome_arquivo +
                  " (arquivo não existe)")
