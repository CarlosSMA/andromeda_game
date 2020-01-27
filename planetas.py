"""
ARMAS
0 - SEM ARMA
1 - ARCO E FLECHA
2 - ESPADA
3 - PISTOLA
"""

import combate
import imagens
import crafting
import textos
from random import randint
import sys
from time import sleep

# PLANETA_1


def mostrar_arma(arma):
  if arma == 0:
    return "Arma: Nenhuma"
  elif arma == 1:
    return "Arma: Arco e flecha"
  elif arma == 2:
    return "Arma: Espada"
  elif arma == 3:
    return "Arma: Pistola"

def imagem_astronauta(arma):
  if arma == 0:
    imagens.astronauta_0()
  elif arma == 1:
    imagens.astronauta_1()
  elif arma == 2:
    imagens.astronauta_2()
  elif arma == 3:
    imagens.astronauta_3()

def imagem_monstro():
  random = randint(1,5)

  if random == 1:
    imagens.monstro_random_1()
  elif random == 2:
    imagens.monstro_random_2()
  elif random == 3:
    imagens.monstro_random_3()
  elif random == 4:
    imagens.monstro_random_4()
  elif random == 5:
    imagens.monstro_random_5()

def inimigos_random_azathoth(var,inimigo,vida,monstrosRestantes):
  
  if var == 1 and inimigo == 1:
    imagem_astronauta(arma)
    imagens.monstro_random_chuva()
    vida = combate.combate(arma,vida,"monstro",2)
    if vida > 0 and vida < 100:
      vida*=2
      monstrosRestantes-=1
      print("Monstro:",10 - monstrosRestantes + 1)
    elif vida > 0:
      monstrosRestantes-=1
      print("Monstro:",10 - monstrosRestantes + 1)
  
  if var == 1 and inimigo == 2:
    imagem_astronauta(arma)
    imagens.monstro_random_gas()
    vida = combate.combate(arma,vida,"monstro",2)
    if vida > 0 and vida < 100:
      vida*=2
      monstrosRestantes-=1
      print("Monstro:",10 - monstrosRestantes + 1)
    elif vida > 0:
      monstrosRestantes-=1
      print("Monstro:",10 - monstrosRestantes + 1)

  return [vida,monstrosRestantes]

# RANDOMS
def chuva_acida():
    resposta = input("A chuva ácida chegou! Você quer voltar para o último checkpoint ("+str(checkpoint)+"m.) [S/N]? ")
    return resposta

 # CHANCE DE ENCONTRAR UMA CAVERNA
def checkpoint_caverna(distancia,vida):

    print("Você encontrou uma caverna a",distancia,"METROS de distância do objetivo!")
    print("Ela será o seu checkpoint agora.")
    checkpoint = distancia

    return checkpoint

 # CHANCE DE ENCONTRAR UM MONSTRO
def encontrar_monstros(i):
    valor1 = randint(1,5)

    indice = 20 - i

    valor2 = randint(1, indice)
    soma = int(valor2*2) + valor1
    media = int((soma/3))
    
    if media <= 4:
        return True
    else:
        return False

#EVENTO CENTRAL
def jogo_1():

  # VARIÁVEIS DE CONTROLE
    global resposta
    global arma
    explicacao_combate=0
    vida = 100
    arma = 0
    material = 0
    distancia = 500
    global checkpoint
    checkpoint = distancia
    resposta_chuva=""
    global temperatura
    temperatura = 0
    hipertermia = 0
    global qttMaterial
    qttMaterial = 0
    indice = 1

   # LOOP DO JOGO
    while (distancia > 0):
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        resposta_chuva=""

        # PERGUNTAR SE O USUÁRIO QUER AVANÇAR OU NÃO
        resposta = input("Você quer avançar[S/N]? ")
        while (resposta != "S" and resposta != "N"):
            resposta = input("Insira uma resposta válida. Você quer voltar para o último checkpoint[S/N]? ")

        # SE O JOGADOR ANDAR, A DISTÂNCIA DIMINUI, MAS MAIS MONSTROS APARECEM
        if resposta == "S":
            distancia-=randint(50,75)
            indice+=1

            # OCORRÊNCIA DE COMBATE E ATUALIZAÇÃO DE VIDAS
            if encontrar_monstros(indice) == True:
                textos.limpar_tela()

                # PARA O PRIMEIRO COMBATE, O JOGADOR IRÁ RECEBER UMA EXPLICAÇÃO DA MECÂNICA
                if explicacao_combate == 0:
                  textos.tutorial_combate()
                explicacao_combate+=1
                sleep(0.025)

                # MOSTRAR A IMAGEM DO ASTRONAUTA COM A ARMA
                imagem_astronauta(arma)
                imagem_monstro()
                sleep(0.5)
                vida = combate.combate(arma,vida,"monstro",1)
                if vida == False:
                  break
                  
        # SE ELE NÃO ANDAR, MENOS MONSTROS APARECEM (FALTA PROGRAMAR O CALOR)
        elif resposta == "N":
            indice-=2
            encontrar_monstros(indice)
            if indice <= 0:
                indice = 0
                encontrar_monstros(indice)

        # CHANCE DE MINERAR MATERIAL E CRAFTAR
        material = randint(1,4)
        qttMaterial_aux = randint(5,10)

        if material == 1:
          print("Você quer minerar",qttMaterial_aux,"materiais, mas ganhar 10% de calor[S/N]? ",end="")
          resposta_minerar = input()

          # ATUALIZAR VALOR DA ARMA E DOS MATERIAIS
          if resposta_minerar == "S":
            qttMaterial = crafting.craftar(qttMaterial_aux,arma)
            arma = qttMaterial[1]
            qttMaterial = qttMaterial[0]
            temperatura += 10

        # CHECKPOINT E RECUPERAR VIDA
        caverna = randint(1,6)
        if caverna == 1:
            checkpoint = checkpoint_caverna(distancia,vida)
            distancia = checkpoint
            if vida <= 70: 
              vida += 30

        # SISTEMA DE CALOR
        hipertermia = randint(1,2)
        if hipertermia == 1:
            temperatura+=10
            if temperatura >= 100:
                print("Você queimou até a morte. Game over!")
                break

        # CHUVA ACIDA E GAME OVER
        chuva = randint(1,4)
        if chuva == 1:
          resposta_chuva = chuva_acida()
          if resposta_chuva == "S":
              distancia = checkpoint
              imagens.chuva()

              if temperatura <= 0:
                temperatura  = 0
              elif temperatura >= 40:
                temperatura-=40
          elif resposta_chuva == "N":
              print("Você corroeu até a morte. Game over!")
              break

        # IMPRIMIR VALORES

        for i in range(5):
          print("\t",end="")
        print("Vida:",vida)
        for i in range(5):
          print("\t",end="")
        print("Distância:",distancia)
        for i in range(5):
          print("\t",end="")
        print("Temperatura: "+str(temperatura)+"%")
        for i in range(5):
          print("\t",end="")
        print("Material:",qttMaterial)
        for i in range(5):
          print("\t",end="")
        print("Checkpoint:",checkpoint)
        for i in range(5):
          print("\t",end="")
        print(mostrar_arma(arma),"("+str(arma)+")")

    # QUANDO O JOGADOR FINALIZA O JOGO
    if distancia <= 0:
      imagens.imp()
      if combate.combate(arma,vida,"imp",1) > 0:
        sleep(3)
        imagens.medalha()
        sleep(3)
        textos.limpar_tela()
        textos.selecao_planetas()
      else:
        print(end="")


# PLANETA 2
def jogo_2():
  global resposta
  global arma
  explicacao_combate=0
  vida = 200
  arma = 2
  material = 0
  distancia = 500
  global checkpoint
  checkpoint = distancia
  resposta_chuva=""
  global temperatura
  temperatura = 0
  hipertermia = 0
  global qttMaterial
  qttMaterial = 0
  indice = 1
  monstrosRestantes = 10

  while (monstrosRestantes > 0 and vida > 0):
    arma = 2
    """
    INIMIGOS RANDOM
    1 - GÁS
    2 - CHUVA
    3 - CHUVA
    """
    random=randint(1,4)
    tipo_inimigo=randint(1,2)

    # INIMIGOS RANDOM EM SITUAÇÕES ESPECÍFICAS
    monstrosRestantes = inimigos_random_azathoth(random,tipo_inimigo,vida,monstrosRestantes)
    vida = monstrosRestantes[0]
    monstrosRestantes = monstrosRestantes[1]
    
    # INIMIGOS COMUNS
    imagem_astronauta(arma)
    imagem_monstro()
    vida = combate.combate(arma,vida,"monstro",2)
    if vida > 0 and vida < 100:
      vida*=2
      monstrosRestantes-=1
      print("Monstro:",10 - monstrosRestantes)
    elif vida > 0:
      monstrosRestantes-=1
      print("Monstro:",10 - monstrosRestantes)


  # LUTA CONTRA O OGRO
  imagem_astronauta(arma)
  imagens.ogro()
  vida = combate.combate(arma,vida,"ogro",2)
  if vida > 0:
    vida*=2
    monstrosRestantes-=1
    print("Você conseguiu!")
    sleep(3)
    imagens.medalha()
    sleep(4)
    textos.limpar_tela()
    textos.selecao_planetas()
