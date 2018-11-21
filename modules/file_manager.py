import sys

class FileInfo:
    nome_arquivo = ''
    primeiro_bloco = 0
    n_blocos = 0

    def __init__(self, info_line):
        line = info_line.split(',')
        self.nome_arquivo = line[0]
        self.primeiro_bloco = int(line[1])
        self.n_blocos = int(line[2])

class FileOp:
    ID_Processo = 0
    Codigo_Operação = 0
    Nome_arquivo = ''
    se_operacaoCriar_numero_blocos = 0

    def __init__(self, info_line):
        line = info_line.split(',')
        self.ID_Processo = int(line[0])
        self.Codigo_Operação = int(line[1])
        self.Nome_arquivo = line[2]
        self.se_operacaoCriar_numero_blocos = int(line[3]) if len(line) == 4 else None

class FileManager():
    n_blocos = 0
    n_segmentos = 0
    files = []
    operations = []

    def __init__(self):
        with open(sys.argv[2], 'r') as f:
            lines = f.read().splitlines()
            self.n_blocos = int(lines[0])
            self.n_segmentos = int(lines[1])
            self.files = [FileInfo(line) for line in lines[2 : self.n_segmentos + 2]]
            self.operations = [FileOp(line) for line in lines[self.n_segmentos + 2 :]]