with open('processos.txt', 'r') as f:
    processos = f.read().splitlines()

array_aux = []
for proc in processos:
    array_aux.append(proc.split(','))

array_processos = []
for proc in array_aux:
    array_processos.append({
        "t_inicializacao": proc[0],
        "prioridade": proc[1],
        "t_processador": proc[2],
        "blocos_mem": proc[3],
        "cod_impressora": proc[4],
        "req_scanner": proc[5],
        "req_modem": proc[6],
        "cod_disco": proc[7],
    })

print(array_processos)

# with open('descricao.txt', 'r') as f:


