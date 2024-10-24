# Projeto : Adivinhe a bandeira (Guess the flag)
# código feito por Brendow Cavalcante


import random
import os


# bandeira e as opções de resposta
bandeira = ["Brasil","Argentina","México","Venezuela","Inglaterra","Coreia do Sul",
            "Japão","Estados Unidos","China","Chile"]

respostas_opcoes = [["brasil","estados unidos","frança"],
                    ["coreia do sul","japão","argentina"],
                    ["italia","reino unido","méxico"],
                    ["venezuela","croacia","japão"],
                    ["brasil","inglaterra","reino unido"],
                    ["japão","coreia do norte","coreia do sul"],
                    ["japão","coreia do sul","méxico"],
                    ["frança","rússia","estados unidos"],
                    ["portugal","china","coreia do norte"],
                    ["china","chile","bélgica"]]

# respostas corretas seguindo a ordem da lista de opcoes
respostas_corretas = ["brasil","argentina","méxico","venezuela","inglaterra",
                      "coreia do sul","japão","estados unidos","china","chile"]


# escolhendo de forma aleatoria a sequência dos questionários através de uma lista que 
# gera números aleátorios, sem repetir
list_i = random.sample(range(10), 10)

# limpar console
clear = lambda: os.system('cls')

def main():
    inicio()



def inicio():
    clear()
    print("       JOGO - ADIVINHE A BANDEIRA \n\n")
    print("  1. Começar    2. Fechar Jogo \n\n")

    decisao_usuario = int(input(":"))

    if decisao_usuario == 1:
        nome = input("Digite seu nome: ")
        jogo_em_andamento(nome)
    else :
        print("Jogo fechou.")


def jogo_em_andamento(usuario_nome):
    # pontos do usuário
    pontos = 0 

    for l in list_i:
        clear()
        print(f" Jogador : {usuario_nome}   Pontos : {pontos}\n\n")
        print(f"     BANDEIRA > {bandeira[l]}\n\n")
        print(f" {respostas_opcoes[l][0]}    {respostas_opcoes[l][1]}     {respostas_opcoes[l][2]}\n\n")

        usuario_resposta = input(":")
        if usuario_resposta == respostas_corretas[l]:
            pontos = pontos + 1
    
    resultado_jogo(pontos)


def resultado_jogo(pontos_usuario):
    clear()
    print("    RESULTADO \n\n")
    print(f"      {pontos_usuario}/10 \n\n")

    if pontos_usuario >= 0 and pontos_usuario <= 5:
        print("Você foi péssimo, estude mais.")
    elif pontos_usuario >= 6 and pontos_usuario <= 8:
        print("foi bom, mas pode melhorar.")
    elif pontos_usuario >= 9 and pontos_usuario <= 10:
        print("excelente, parabéns!")

    press_qualquer_tecla = input("Pressione qualquer tecla para continuar : ")

    inicio()



main()