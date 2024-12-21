import random

numero_secreto = random.randint(1, 100) # Definindo o numero aleatorio


def acertou(numEscolhido): 
    if numero_secreto == numEscolhido:
        return 'Você acertou! Parabéns!!'
    elif numero_secreto < numEscolhido:
        return 'Você errou! Tente um número menor...'
    else:
        return 'Você errou! Tente um número maior...'


def escolha():
    print('Bem-vindo ao Modo Difícil do Jogo de Adivinhação!')
    print('Você tem 10 tentativas para adivinhar o número secreto entre 1 e 100.')

    tentativas = 0 

    while tentativas < 10: # Maximo de tentativa
        try:
            numEscolhido = int(input('Digite sua tentativa: '))
            tentativas += 1

            resultado = acertou(numEscolhido)
            print(resultado)

            if numero_secreto == numEscolhido:
                print(f'Você precisou de {tentativas} tentativa(s).')
                break
        except ValueError:
            print('Por favor, insira um número válido!') 


    if tentativas == 10 and numero_secreto != numEscolhido:
        print(f'Você perdeu! O número secreto era {numero_secreto}. Tente novamente!') # Se o usuário ultrapassou o limite 

escolha()
