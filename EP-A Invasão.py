"""Após uma seleção muito rigorosa, você foi escolhido como o mais capacitado para a realização de uma tarefa de essencial importância para a continuidade da espécie humana.
CONFIDENCIAL: A Terra será invadida por extraterrestres com a intenção de total extermínio de seus habitantes para futura ocupação do planeta. Descobrir a data dessa invasão é de vital importância para impedir tamanha destruição. Informantes alienígenas aliados conseguiram obter o códifo de ataque e as regras para sua decodificação. Sua tarefa será desenvolver um programa que leia o código secreto e o decodifique, determinanndo a data da invasão.

### Mensagem dos Informantes
O código é composto por três partes: a primeira parte são dois números naturais m e n, a segunda parte é formada por m números naturais e a terceira por n números naturais.
Para determinar a data do evento, é necessário escolher o método correto: Método A ou Método B. Para saber o método adequado, existe o seguinte procedimento: (I) soma-se todos os m números, obtendo sm; (II) soma-se todos os dígitos de sm, obtendo sd; (III) se sd é par, aplica-se o Método A, caso contrário, aplica-se o Método B.

### Método A
Instruções: (I) ordena-se crescentemente os n números; (II) multiplica-se cada um dos n números por sua posição na sequência, considerando que o 1o item tem posição 1; (III) somam-se os n números já multiplicados, obtendo sn.

### Método B
Instruções: (I) soma-se a cada um dos n números o respectivo valor da sequência (1, 2, 4, 7, 11, 16, ...); (II) para cada n número já acrescido, tomam-se os dois dígitos mais à direita para serem acumulados; (III) o acúmulo total gera sn.

### Descobrindo a data
Descoberto o valor de sn, para determinar a data da invasão calcula-se o resto da divisão inteira de sn por 31, que representa o dia da invasão, adote zero como dia 31. De modo análogo, o resto da divisão inteira de sn por 12 indica o mês da invasão, o resto zero indicando dezembro. O ano, infelizmente, não pode ser descoberto.

### Observações
1) Faça a validação da entrada: (I) 0 < m < 6; (II) 0 < n < 11; (III) para todo x pertencente aos m números, 0 < x < 500.
2) Não use funções/métodos pré-definidos da linguagem para ordenar ou somar os itens das listas.
3) Considere que fevereiro possui 28 dias, pois os extraterrestres não atacam em anos bissextos.
4) Caso o procedimento resulte em um dia que excede o máximo para o mês descoberto, deve-se supor que o código foi corrompido. Uma mensagem deve indicar essa situação!
"""
def metodo_a(lista):
    # Ordenando a lista crescentemente
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] < lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    
    # Multiplicando o número por sua posição
    for i in range(len(lista)):
        lista[i] = lista[i] * (i + 1)
    
    # Soma total
    sn = 0
    for i in range(len(lista)):
        sn = sn + lista[i]
    
    # Retorno da função
    return sn

def metodo_b(lista):
    # Somando os elementos da lista às suas posições
    for i in range(len(lista)):
        lista[i] = lista[i] + (i + 1)
    
    # Tomando os dois digitos mais a direita
    for i in range(len(lista)):
        lista[i] = lista[i] % 100
    
    # Soma total
    sn = 0
    for i in range(len(lista)):
        sn = sn + lista[i]
    
    # Retorno da função
    return sn

def entrada_m():
    m = input(int("m: "))

    while m > 6 and m < 0:
        m = input(int("m deve estar no intervalo 0 < m < 6.\nm: "))
    
    return m

def entrada_n():
    n = input(int("n: "))

    while n < 0 and n > 11:
        n = input(int("n deve estar no intervalo 0 < n < 11.\nn: "))

    return n

def entrada_x(tam:int, lista:list, nome_lista:str):
    for i in range(len(tam)):
        lista.append = input(int(f"{nome_lista}[{i}]: "))
        while lista[i] < 0 and lista[i] > 500:
            lista[i] = input(int(f"O número deve pertencer ao intervalo 0 < x < 500\n{nome_lista}[{i}]: "))

def main():
    m = entrada_m()
    n = entrada_n()
    entrada_x(m, lista_m, 'm')
    entrada_x(n, lista_n, 'n')