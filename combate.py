from random import randint
import imagens
import planetas

def combate(arma,vida,tipo,planeta):
  if arma == 0:   # SEM ARMA
    dano = randint(10,15)
  elif arma == 1: # ARCO E FLECHA
    dano = randint(20,25)
  elif arma == 2: # ESPADA
   dano = randint(30,45)
  elif arma == 3: # PISTOLA
    dano = randint(50,65)
  # "Monstro:[VIDA,DANO]"
  monstros = {
    "monstros":[randint(30,50),randint(10,15)],
    "kraken":[75,30],
    "imp":[100,20],
    "azathoth":[120,40]
  }

  if tipo == "monstro":
    dano_monstro = randint(10,15)
    vida_monstro = randint(30,50)
  elif tipo == "imp":
    dano_monstro = randint(20,40)
    vida_monstro = 100
  elif tipo == "ogro":
    dano_monstro = randint(40,45)
    vida_monstro = 120

  print(planetas.mostrar_arma(arma))
  while (vida_monstro <= 0 or vida >= 0): #se fc menor que 0 o monstro num iria viver pra sempre ?
    resposta = input("\n1 - Ataque\n2 - Defesa (Recuperar Vida)\nAção: ")
    while (resposta != "1"and resposta != "2"):
      resposta = input("Resposta inválida.\n1 - Ataque\n2 - Defesa (Recuperar Vida)\nAção: ")


    if resposta == "1":
      random = randint(0,3)
      if random == 0 or random == 1 or random == 2:
        print("\n--------------\nGOLPE BEM-SUCEDIDO\n--------------\n")
        vida -= dano_monstro
        vida_monstro -= dano
      elif random == 3:
        print("\n--------------\nGOLPE FALHO\n--------------\n")
        vida -= 2 * dano_monstro

    elif resposta == "2":
      vida += 10
      vida -= (dano_monstro/2)
      print("\n")

    if planeta == 1 and vida >= 100:
      vida = 100
      print("JOGADOR\nVida:",vida,"(MAX)\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\nMONSTRO\nVida:",vida_monstro)
    elif planeta == 2 and vida >= 200:
      vida = 200
      print("JOGADOR\nVida:",vida,"(MAX)\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\nMONSTRO\nVida:",vida_monstro)
    elif planeta == 1:
      print("JOGADOR\nVida:",vida,"\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\nMONSTRO\nVida:",vida_monstro)
    elif planeta == 2:
      print("JOGADOR\nVida:",vida,"\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n\nMONSTRO\nVida:",vida_monstro)

    if vida <= 0:
      print("Game over!\n")
      return False
    elif vida_monstro <= 0:
      print("Você derrotou o monstro!\n")
      return vida
