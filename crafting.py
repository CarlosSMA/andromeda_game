def craftar(qttMaterial,arma):
  print("qttMaterial:",qttMaterial)
  print("arma:",arma)
  global resposta
  resposta=" "
# MOSTRAR ARMAS DISPONÍVEIS (O JOGO CRAFTA A MELHOR DISPONÍVEL)
  if (qttMaterial >= 5 and qttMaterial < 10) and arma == 0:
    resposta = input("Você deseja craftar um arco e flecha por 5 materiais[S/N]? ")
  # ANALISAR RESPOSTA DO USUÁRIO  
    if resposta == "S":
      arma = 1
      qttMaterial-=5
    elif resposta == "N":
      arma = arma
    else:
      while (resposta != "N" and resposta != "S" and resposta != " "):
        resposta = input("Resposta inválida. Você deseja craftar um arco e flecha por 5 materiais[S/N]? ")

  elif (qttMaterial >= 10 and qttMaterial < 20) and (arma == 0 or arma == 1):
    resposta = input("Você deseja craftar uma espada por 10 materais[S/N]? ")

   # ANALISAR RESPOSTA DO USUÁRIO 
    print("resposta",resposta)
    if resposta == "S":
      arma = 2
      qttMaterial-=10
    elif resposta == "N":
      arma = arma
    else:
      while (resposta != "N" and resposta != "S" and resposta != " "):
       resposta = input("Resposta inválida. Você deseja craftar uma espada por 10 materiais[S/N]? ")

  elif qttMaterial >= 20 < 60 and (arma == 0 or arma == 1 or arma == 2): 
    resposta = input(" Você deseja craftar uma pistola por 20 materiais? S/N")
 
    # ANALISAR RESPOSTA DO USUÁRIO  
    if resposta == "S":
      arma = 3
      qttMaterial-=20
    elif resposta == "N":
      arma = arma
    else:
      while (resposta != "N" and resposta != "S" and resposta != " "):
       resposta = input("Resposta inválida. Você deseja craftar uma pistola por 25 materiais[S/N]? ")
  elif qttMaterial >= 60:
    reposta = input("Você deseja craftar o traje por 60 materiais?")
  
  return [qttMaterial,arma]
