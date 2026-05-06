import time
import threading
import multiprocessing


# ==========================================
# 1. FUNÇÕES ALVO DO TESTE
# ==========================================

def simular_io(tarefa_id):
    """
    Tarefa A: I/O Bound
    Objetivo: Simular uma espera por rede ou disco rígido.
    Instruções: Utilize a função time.sleep() para pausar a execução por 0.1 segundos.
    """
    print(f"Tarefa {tarefa_id}: Iniciando I/O...")
    time.sleep(0.1)
    

def fatoracao_pesada(tarefa_id):
    """
    Tarefa B: CPU Bound
    Objetivo: Forçar o processador a realizar cálculos matemáticos intensos.
    Instruções: Escreva um algoritmo que encontre todos os números primos 
    entre 2 e 30.000. Retorne a quantidade de números primos encontrados.
    """
    n = 30000
    cont = 0
    
    for num in range(2, n + 1):
        eh_primo = True

        for i in range(2, num):
            if num % i == 0:
                eh_primo = False
                break

        if eh_primo:
            cont += 1

    return cont
            

# ==========================================
# 2. FUNÇÃO DE BENCHMARKING (MOTOR DE TESTES)
# ==========================================

def executar_benchmarking(nome_tarefa, funcao_alvo, quantidade_execucoes):
    print(f"\n--- Iniciando Benchmarking: {nome_tarefa} ({quantidade_execucoes} iterações) ---")

    # ---------------------------------------------------------
    # A. TESTE SEQUENCIAL
    # ---------------------------------------------------------
    inicio = time.perf_counter()
    
    for i in range(quantidade_execucoes):
        funcao_alvo(i)
        
    tempo_seq = time.perf_counter() - inicio
    print(f"[Sequencial] Tempo: {tempo_seq:.4f} segundos")
    
    

    # ---------------------------------------------------------
    # B. TESTE COM MULTITHREADING
    # ---------------------------------------------------------
    inicio = time.perf_counter()
    
    threads_list = [] # lista para armazenar as threads.
    
    # Cria e inicia as threads
    for i in range(quantidade_execucoes):
        t = threading.Thread(target=funcao_alvo,args=(i,))
        threads_list.append(t)
        t.start()
    
    for t in threads_list:
        t.join() # processo principal aguarda as threads terminarem
    
    tempo_thread = time.perf_counter() - inicio
    print(f"[Multithread] Tempo: {tempo_thread:.4f} segundos")

    
    
    # ---------------------------------------------------------
    # C. TESTE COM MULTIPROCESSING
    # ---------------------------------------------------------
    inicio = time.perf_counter()
    
    process_list = [] # lista para armazenar processos
    
    for i in range(quantidade_execucoes):
        p = multiprocessing.Process(target=funcao_alvo,args=(i,))
        process_list.append(p)
        p.start()
        
    for p in process_list:
        p.join()
    
    tempo_proc = time.perf_counter() - inicio
    print(f"[Multiprocesso] Tempo: {tempo_proc:.4f} segundos")



# ==========================================
# 3. BLOCO PRINCIPAL DE EXECUÇÃO
# ==========================================

if __name__ == '__main__':
    # Esta linha é OBRIGATÓRIA no Windows para evitar que a biblioteca 
    # multiprocessing entre em loop infinito ao criar processos filhos.
    multiprocessing.freeze_support() 
    
    print("Iniciando bateria de testes. Por favor, aguarde (pode demorar alguns segundos)...")
    
    # Roda bateria de testes I/O (Simula 50 downloads/leituras simultâneas)
    executar_benchmarking("Tarefa I/O-Bound (Espera de Rede/Disco)", simular_io, 50)
    
    # Roda bateria de testes CPU (Calcula primos pesados 10 vezes)
    executar_benchmarking("Tarefa CPU-Bound (Matemática Pesada)", fatoracao_pesada, 10)
    
    print("\nTestes concluídos! Use estes tempos para montar a tabela do seu relatório.")