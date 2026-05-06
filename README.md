# Benchmark

Nesse repositório estou colocando um dos meus trabalho de Sistemas Operacionais, a temática principal seria o funcionamento de threads e processos. Dessa maneira foi feito um benchmark para analisar desempenho de threads e processos em alguns tipos de tarefas como I/O-Bound e CPU-Bound.

* I/O-Bound: São tarefas que dependem de
periféricos ou redes (fazer download de um arquivo, ler o disco rígido, consultar um banco
de dados). Nessas tarefas, a CPU passa a maior parte do tempo ociosa (idle), apenas
esperando os dados chegarem.

* CPU-Bound: São tarefas pesadas que ocupam uma porcentagem altíssima da CPU a todo momento, como algoritmos de criptografia e processamento de imagens.

## Tecnologias utilizadas

- **Linguagem:** Python  
- **Bibliotecas:** `threading`, `multiprocessing`, `time`

## Especificação

Foram adotados 3 tipos de abordagens para executar as tarefas, sendo elas:

* Execução Sequencial
* Multithreading
* Multiprocessing

Para cada abordagem foi feito dado uma tarefa do tipo I/O-Bound e uma do tipo CPU-Bound. Na primeira fiz uma funçâo que iniciava e ja usava um `time.sleep(0.1)` para simular uma espera da placa de rede ou disco.

Já na segunda fiz uma função que usaria um processamento alto da CPU, calcular quantos numeros primos existiam em um intervalo de 2 a 30.000. A primeira função no teste seria executada 50 vezes e a segunda função 10 vezes.

## Resultados

| Tipo de Tarefa | Sequencial (s) | Multithread (s) | Multiprocesso (s) |
|:--------------|--------------:|---------------:|------------------:|
| I/O-Bound     | 9.03          | 🟢 **0.16**    | 0.44              |
| CPU-Bound     | 19.66         | 18.67          | 🟢 **4.43**       |

## Análise

🔵 I/O-Bound
* O multithreading apresentou o melhor desempenho.

* Isso ocorre porque, durante a espera (sleep), o Python libera o GIL, permitindo que outras threads sejam executadas.

* Multiprocessing também melhora o desempenho, mas possui maior overhead.

Conclusão: Threads são mais eficientes para tarefas I/O-Bound

🔴 CPU-Bound
* O multithreading não trouxe ganho significativo.

* Isso acontece devido ao GIL (Global Interpreter Lock), que impede execução paralela de threads em tarefas de CPU.

* O multiprocessing teve melhor desempenho por utilizar múltiplos núcleos da CPU.

Conclusão: Multiprocessing é mais eficiente para tarefas CPU-Bound


## Sobre o GIL

O GIL (Global Interpreter Lock) é um mecanismo do Python que permite que apenas uma thread execute código Python por vez. Isso impacta diretamente tarefas CPU-Bound, limitando o uso de múltiplas threads para processamento paralelo.


O desempenho limitado do multithreading em tarefas CPU-bound está diretamente relacionado ao GIL do Python, que impede execução paralela de threads. Em linguagens como C, onde não há esse mecanismo, threads podem executar em paralelo real, resultando em ganhos significativos de desempenho para tarefas computacionalmente intensas.