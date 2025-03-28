import numpy as np

def process_log(file_path):
    tempos = []
    
    with open(file_path, 'r') as file:
        for line in file:
            try:
                tempos.append(float(line.strip()))
            except ValueError:
                pass  
                
    if tempos:
        media = np.mean(tempos)
        desvio = np.std(tempos)
        print(f'Média do tempo de execução: {media:.2f} segundos')
        print(f'Desvio padrão: {desvio:.2f} segundos')
    else:
        print("Nenhum dado válido encontrado.")


process_log('log.txt')
