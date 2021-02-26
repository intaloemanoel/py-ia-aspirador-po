import random

class Agente(object):
    def __init__(self, quartos, posAtual, pontos):
        self.quartos = quartos
        self.posAtual = posAtual
        self.pontos = pontos

    # MOVER PARA A DIREITA = ADICIONAR 1 NA POS
    def direita(self):
        print("Movendo para a direita!")
        self.posAtual += 1

    # MOVER PARA A ESQUERDA = DIMINUIR 1 NA POS
    def esquerda(self):
        print("Movendo para a esquerda!")
        self.posAtual -= 1

    # AO LIMPAR, MUDA O QUARTO[I] PARA LIMPO
    def limpar(self):
        print("Limpando o quarto")
        self.quartos[self.posAtual] = 0
        self.pontos += 1

    def noOp(self):
        print("Nao tenho nada para fazer no Quarto!")
        return 0

def acao(agente, quartos):
    if quartos[agente.posAtual] == 1:
        agente.limpar()
    elif quartos[agente.posAtual] == 0:
        agente.noOp()
        if agente.posAtual == 0:
            agente.direita()
        elif agente.posAtual == 1:
            agente.esquerda()

def randEstado(quarto, i):
    estadoRandom = random.randint(0, 1)
    if estadoRandom == 1:
        quarto[i] += 1

def main():
    print("Exercicio Pratico I")

    quartos = [0,1]

    # COMECA QUARTO A E COM 0 PONTOS
    aspirador = Agente(quartos, 0, 0)

    i = 0
    while i < 1000:
        print(i)
        i += 1
        acao(aspirador, quartos)
        if aspirador.posAtual == 0:
            randEstado(quartos, aspirador.posAtual + 1)
        elif aspirador.posAtual == 1:
            randEstado(quartos, aspirador.posAtual - 1)

    print("A pontuacao foi:", aspirador.pontos)


if __name__ == "__main__":
    main()
