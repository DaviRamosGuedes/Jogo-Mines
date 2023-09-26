import random


def main():
    # Input de nome e dificuldade
    nick = input("Escolha o Nome: ")
    vida = 3
    nivel = 0
    posicao = 0
    dinheiro = 10

    print(f'-\n\
Seu saldo é de R${dinheiro},00\n\
Você tem {vida} vidas\n\
Utilize com sabedoria\n\
Iniciando o jogo na casa: {posicao}\n\
\n\
Escolha um nivel válido!')

# Verificar o nível e definir as variaveis de cada nível
    while nivel not in ('1', '2', '3'):
        nivel = (input("Defina o nivel: (1)Easy (2)Medium (3)Hard: "))

    if nivel == '1':
        tabuleiro = 30
        num_vidas = random.sample(range(1, tabuleiro), 4)
        num_bombas = random.sample(range(1, tabuleiro), 8)
        print('Iniciando jogo no nivel Easy')

    elif nivel == '2':
        tabuleiro = 25
        num_vidas = random.sample(range(1, tabuleiro), 3)
        num_bombas = random.sample(range(1, tabuleiro), 10)
        print('Iniciando jogo no nivel Medium')

    elif nivel == '3':
        tabuleiro = 20
        num_vidas = random.sample(range(1, tabuleiro), 2)
        # mudei bombas pra testar, voltar pra 15 dps
        num_bombas = random.sample(range(1, tabuleiro), 19)
        print('Iniciando jogo no nivel Hard.')

# Rolar o dado
    while posicao < tabuleiro:
        input("Precione a tecla ENTER para rolar o dado.")
        rolar_dado = random.randint(1, 6)
        posicao = posicao + rolar_dado
        print(f"Você está na casa:{posicao}\n")

    # verificar primeiro se está em bomba e BUFF-vida ao mesmo tempo
        if posicao in (num_bombas) and posicao in (num_vidas):
            posicao -= 2
            print(
                f"QUE AZAR VC CAIU NA CASA DO CAOS! \nVOLTE DUAS! \nAgora você está na casa {posicao}\n")

    # Verificar se caiu na bomba
        elif posicao in (num_bombas):
            if dinheiro >= 5:
                pergunta1 = input(
                    "Você caiu em uma BOMBA \nPular uma casa por R$ 5,00? (1)sim (2)nao: ")

    # Verificar se tem dinheiro e se vai querer gastar
                if pergunta1.lower() in ('1', 's', 'sim'):
                    dinheiro -= 5
                    posicao += 1
                    print(f"O seu saldo é: R${dinheiro},00 \n")

                elif pergunta1.lower() not in ('1', 's', 'sim') and vida > 0:  # se pergunta != ' s '
                    vida -= 1
                    print(f"Seu número de vidas agora é: {vida}\n")

                else:
                    print("Game OVERRRR!!")
                    pergunta = input("deseja recomeçar? (1)sim (2)nao: ")

                    if pergunta in ('1', 's', 'sim'):
                        posicao = 0
                        vida = num_vidas
                        dinheiro = 10
                        return main()

                    elif pergunta == '2':
                        print("ENCERRADO")
                        break

            elif vida > 0:
                print(
                    "Caiu novamente em uma bomba!\nVocê está sem dinheiro e perdeu uma vida.")
                vida -= 1
                print(f"Seu número de vidas agora é:{vida}\n")

            elif vida == 0 and dinheiro < 5:
                print(f"Que azar, você caiu em mais uma bomba\nGame OVERRRR!!")
                pergunta = input("deseja recomeçar? (1)sim (2)nao: ")

                if pergunta in ('1', 's', 'sim'):
                    posicao = 0
                    vida = num_vidas
                    dinheito = 10
                    return main()

                else:
                    print('Chegamos ao final do jogo!\nObrigado por participar.')
                    break

    # Verificar se caiu no Buff de vida
        elif posicao in (num_vidas):
            vida += 1
            print("Você caiu na casa da vida\nSeu número de vidas agora é:", vida)

    if vida >= 0 and posicao >= tabuleiro:
        print('BOA', nick, 'VC GANHOU!!')


main()
