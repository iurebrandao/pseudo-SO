import sys

class FileInfo:
    def __init__(self, info_line):
        line = info_line.split(',')
        self.nome_arquivo = line[0]
        self.primeiro_bloco = int(line[1])
        self.n_blocos = int(line[2])


class FileOp:
    def __init__(self, info_line):
        line = info_line.split(',')
        self.ID_Processo = int(line[0])
        self.Codigo_Operacao = int(line[1])
        self.Nome_arquivo = line[2]
        self.se_operacaoCriar_numero_blocos = int(line[3]) if len(line) == 4 else None


class FileManager:
    def __init__(self):
        with open(sys.argv[2], 'r') as f:
            lines = f.read().splitlines()
            self.n_blocos = int(lines[0])
            self.n_segmentos = int(lines[1])
            self.files = [FileInfo(line) for line in lines[2 : self.n_segmentos + 2]]
            self.operations = [FileOp(line) for line in lines[self.n_segmentos + 2:]]

        # Write initial files to disk
        self.disk = [None] * self.n_blocos
        for file in self.files:
            self.disk[file.primeiro_bloco: file.primeiro_bloco + file.n_blocos] = [file.nome_arquivo] * file.n_blocos

    def print(self):
        for block in self.disk:
            nome = block if block is not None else '0'
            print(nome + ' | ', end='')

    def run_op(self, process):
        operation = None

        for op in self.operations:
            if op.ID_Processo == process.PID:
                operation = op
                break

        if operation is not None:
            if operation.Codigo_Operacao == 0:
                self.create_file(process, operation)
            else:
                self.delete_file(process, operation)
        else:
            print("Error")
            # TODO error message

        process.tempo_de_processador -= 1

    def create_file(self, process, operation):
        first_bock_fit = None

        for i in range(len(self.disk) - operation.se_operacaoCriar_numero_blocos):
            if all(b is None for b in self.disk[i: i + operation.se_operacaoCriar_numero_blocos]):
                first_bock_fit = i

        if first_bock_fit is not None:
            self.disk[first_bock_fit: first_bock_fit + operation.se_operacaoCriar_numero_blocos] = [operation.Nome_arquivo] * operation.se_operacaoCriar_numero_blocos
            process.created_files.append(operation.Nome_arquivo)
        else:
            print("Não cabe no disco")
            # TODO error message

    def delete_file(self, process, operation):
        if process.prioridade != 0 and operation.Nome_arquivo not in process.created_files:
            print("O processo não pode deletar o arquivo")
            # TODO error message

        self.disk = map(lambda block: None if block == operation.Nome_arquivo else block, self.disk)
