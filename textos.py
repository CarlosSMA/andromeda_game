from time import sleep
import sys
import imagens
import planetas

def limpar_tela():
    for i in range(50):
        sys.stdout.flush()
        sleep(0.025)
        print()

def texto_1():
    print("Olá, desbravador interestelar")
    sleep(3)

    print("Como você sabe, nosso planeta está sofrendo com uma praga")
    print("que está afetando nossas plantações e deixando escassa a nossa alimentação.\n")
    sleep(8)

    print("Sua Missão é encontrar uma nova casa para a espécie humana e, ocasionalmente,")
    print("parar em outros planetas para coletar dados úteis para a humanidade no futuro.\n")
    sleep(8)

    print("Boa viagem e que a sorte esteja sempre a seu favor.")
    sleep(4)

def planeta_1():
    print("Você chegou no planeta Ahiriu, é um planeta com temperaturas extremamente elevadas e com muitos vulcões.")
    sleep(6)

    print("Ao chegar no planeta, as grades de extração e aceleração do propulsor da sua nave se danificaram.")
    sleep(5)

    print("Para consertá-las, você precisa de um minério que só existe no topo de vulcões.")
    sleep(5)

    print("Contudo, você também precisa construir um traje para se proteger dos gases vulcânicos.")
    sleep(5)

    print("TOME CUIDADO COM AS CHUVAS VULCÂNICAS. ABRIGUE-SE NA CAVERNA MAIS PRÓXIMA QUANDO ELAS APARECEREM!")
    sleep(5)

    print("Minere o máximo de materiais possíveis, para construir armas cada vez mais poderosas.")
    sleep(5)



    print("Boa sorte!")
    sleep(2)

def planeta_2():
  print("Você chegou no planeta Azathoth, e ao alcançar sua exosfera, recebeu uma mensagem de um de seus nativos. Ela fala:")
  sleep(4)

  print("Olá, desbravador estelar. Pedimos urgentemente a sua ajuda! Dentro das amplas florestas do nosso planeta, existe um terrível ogro, que assombra o nosso povo há décadas! Mate-o, que te darei várias recompensas!")
  sleep(7)

  print("No entanto, tenha cuidado! O nosso planeta está praticamente habitado por mais destas horrendas criaturas! Deixamos uma espada guardada em sua nave, use-a para matar 10 inimigos e, finalmente, chegar ao ogro.")
  sleep(10)

  print("Boa sorte!")
  sleep (2)

def planeta_3():
  print("Você chegou no planeta Proteu, um planeta repleto de água e gelo em toda a sua superfície.")
  sleep(5)

  print("Seu objetivo é coletar o máximo de água potável possível e transportá-la para a Terra.")
  sleep(5)

  print("A distância para o reservatório está marcada em seu HUD.")
  sleep(5)

  print("Boa sorte!")
  sleep(2)

def selecao_planetas():
    
    dicionario = {
    "nome_planetas":["Ahiriu", "Azathoth", " ??????"],
    "id_planetas":[117,142,"??????"],
    "tipo_planetas":["Vulcânico","Monstruoso","??????"]
    }
    
    nome = list(dicionario.values())
    id = list(dicionario.values())
    tipo = list(dicionario.values())
    for i in range(3):
        imagens.planetas()
        print("Planeta",nome[0][i])
        print('ID:',id[1][i])
        print("Tipo:",tipo[2][i])
        sleep(3)
        
    resposta=int(input("Insira o ID do planeta escolhido: "))
    while (resposta != 117 and resposta != 142):
            print("ERROR")
            resposta=int(input("Insira o ID do planeta escolhido: "))
    if resposta == 117:
      imagens.intro_p1()
      sleep(4)
      limpar_tela()
      planeta_1()
      limpar_tela()
      planetas.jogo_1()
    elif resposta == 142:
      imagens.intro_p2()
      sleep(4)
      limpar_tela()
      planeta_2()
      limpar_tela()
      planetas.jogo_2()



def tutorial_combate():
  print ("Tutorial de combate :")
  sleep(2)

  print ("ATAQUE - 75% DE CHANCE DE VOCÊ ACERTAR O ATAQUE E NÃO PERDER VIDA")
  sleep(4)
  
  print("DEFESA - 50% DE CHANCE DE VOCÊ DEFENDER E RECUPERAR VIDA.")
  sleep(3)

  print("QUANTO MAIOR O NÚMERO DA ARMA, MAIOR SERÁ O SEU DANO. OS NÚMEROS VÃO DE 0 a 3.")
  sleep(5)

