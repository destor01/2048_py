#--------------------------------------------------
#----- Librerias importadas
#--------------------------------------------------
import platform
import os
import random
import time
#--------------------------------------------------
#----- Variables Globales
#--------------------------------------------------
M1 = [[" "," "," "," "], [" "," "," "," "], [" "," "," "," "], [" "," "," "," "]]
M2 = [[" "," "," "," "], [" "," "," "," "], [" "," "," "," "], [" "," "," "," "]]
R1 = [[" "," "," "," "], [" "," "," "," "], [" "," "," "," "], [" "," "," "," "]]
auxi1 = [[" "," "," "," "], [" "," "," "," "], [" "," "," "," "], [" "," "," "," "]]
auxi2 = [[" "," "," "," "], [" "," "," "," "], [" "," "," "," "], [" "," "," "," "]]
PunteoM1 = 0
PunteoM2 = 0
ModoJuego = 0
h = 1
#--------------------------------------------------
#----- PROCEDIMIENTO bienvenida
#----- Despliega datos e información de bienvenida
#--------------------------------------------------
def bienvenida():
  print("╔═════════════════════════════════════════╗")
  print("║                 ╔══════╗                ║")
  print("║                 ║ 2048 ║                ║")
  print("║                 ╚══════╝                ║")
  print("║   Ciencias de la Computacion I - 2023   ║")
  print("║               Sección BN                ║")
  print("║              Proyecto 2048              ║")
  print("╚═════════════════════════════════════════╝")
  print("╔═════════════════════════════════════════╗")
  print("║   Derek Tortola     | Carné: 23002939   ║")
  print("║   Edgar Cordón      | Carné: 09002387   ║")
  print("║   Gerardo Corado    | Carné: 23000175   ║")
  print("║   Leonel Hernández  | Carné: 23002991   ║")
  print("╚═════════════════════════════════════════╝")
  print("╔═════════════════════════════════════════╗")
  print("║                  \|||/                  ║")
  print("║                  (o o)                  ║")
  print("║         ------ooO-(_)-Ooo------         ║")
  print("║                                         ║")
  print("║        B  I  E  V  E  N  I  D O !       ║")
  print("║                                         ║")
  print("╚═════════════════════════════════════════╝")
  print()
#--------------------------------------------------
#----- Cabezal para juego 
#--------------------------------------------------
def sobrevive():
  print("╔═════════════════════════════════════════╗")
  print("║                 ╔══════╗                ║")
  print("║                 ║ 2048 ║                ║")
  print("║                 ╚══════╝                ║")
  print("║   Ciencias de la Computacion I - 2023   ║")
  print("║               Sección BN                ║")
  print("║              Proyecto 2048              ║")
  print("╚═════════════════════════════════════════╝")
  print("╔═════════════════════════════════════════╗")
  print("║                  \|||/                  ║")
  print("║                  (o o)                  ║")
  print("║         ------ooO-(_)-Ooo------         ║")
  print("║                                         ║")
  print("║        S  O  B  R  E  V  I  V E !       ║")
  print("║                                         ║")
  print("╚═════════════════════════════════════════╝")
  print()
#--------------------------------------------------
#----- Cabezal para Game Over
#--------------------------------------------------
def fin():
  print("╔═════════════════════════════════════════╗")
  print("║                 ╔══════╗                ║")
  print("║                 ║ 2048 ║                ║")
  print("║                 ╚══════╝                ║")
  print("║   Ciencias de la Computacion I - 2023   ║")
  print("║               Sección BN                ║")
  print("║              Proyecto 2048              ║")
  print("╚═════════════════════════════════════════╝")
  print("╔═════════════════════════════════════════╗")
  print("║                  \|||/                  ║")
  print("║                  (x x)                  ║")
  print("║         ------ooO-(-)-Ooo------         ║")
  print("║                                         ║")
  print("║        G  A  M  E  O  V  E  R ! !       ║")
  print("║                                         ║")
  print("╚═════════════════════════════════════════╝")
  print()
#--------------------------------------------------
#----- Cabezal para Game Over
#--------------------------------------------------
def win():
  print("╔═════════════════════════════════════════╗")
  print("║                 ╔══════╗                ║")
  print("║                 ║ 2048 ║                ║")
  print("║                 ╚══════╝                ║")
  print("║   Ciencias de la Computacion I - 2023   ║")
  print("║               Sección BN                ║")
  print("║              Proyecto 2048              ║")
  print("╚═════════════════════════════════════════╝")
  print("╔═════════════════════════════════════════╗")
  print("║                  \|||/                  ║")
  print("║                  (o o)                  ║")
  print("║         ------ooO-(w)-Ooo------         ║")
  print("║                                         ║")
  print("║                 W  I  N  ! !            ║")
  print("║                                         ║")
  print("╚═════════════════════════════════════════╝")
  print()
#--------------------------------------------------
#----- PROCEDIMIENTO eliminar_archivos
#----- Eliminar los archivos utilizados para la opción de reply
#--------------------------------------------------
def eliminar_archivos():
  if os.path.exists("jugador1.txt"):
    os.remove("jugador1.txt")
  if os.path.exists("jugador2.txt"):
    os.remove('jugador2.txt')
#--------------------------------------------------
#----- PROCEDIMIENTO replay_bitacora
#----- Para escribir en un archivo.txt con la  bitacora de cada jugador
#--------------------------------------------------
def replay_bitacora(M, nom_archivo):
  archivo = open(nom_archivo,"a")
  #archivo = open(nom_archivo, "w")
  archivo.write(str(M)+'\n')
  archivo.close()
#--------------------------------------------------
#----- PROCEDIMIENTO replay_juego
#----- Para leer el archivo de la bitacora y mostrarlo en pantalla
#--------------------------------------------------
def replay_juego(nom_archivo):
  limpiar_pantalla()  
  archivo = open(nom_archivo+'.txt',"r")
  print('MOVIMIENTOS: ' + nom_archivo)
  c = 1
  for line in archivo.readlines():
    R1 = [[ " "," " ," " ," " ], [ " ", " ", " "," " ], [ " "," ", " ", " "], [ " "," " ," " ," " ]]
    line = line.replace(' ','')
    line = line.replace('[','')
    line = line.replace(']','')
    line = line.replace("'",'')
    line = line.replace("\n",'')
    line = line + ','
    cont = 0
    x = 0
    i = 0    
    j = -1
    while (cont < 16):
      n = ''
      while ((line[x]) != ','):         
        n = n + line[x]
        x = x + 1
      cont = cont + 1
      if (cont >= 1) and (cont <= 5): i = 0
      if (cont >= 5) and (cont <= 8): i = 1
      if (cont >= 9) and (cont <= 12): i = 2
      if (cont >= 13) and (cont <= 16): i = 3
      if (cont == 5) or (cont == 9) or (cont == 13): j = -1
      j = j + 1      
      R1[i][j] = n           
      x = x + 1
    #-----
    matrix_length = len(R1)
    
    print()
    print("Movimiento No. ", c)
    print('+------+------+------+------+')  
    for i in range(matrix_length):  
      fila = '|'
      for j in range(0, 4):
        n = R1[i][j]
        if (len(str(n)) == 0):
          fila = fila + '      |'
        if (len(str(n)) == 1):
          fila = fila + '    ' + str(n) + ' |'
        if (len(str(n)) == 2):
          fila = fila + '   ' + str(n) + ' |'
        if (len(str(n)) == 3):
          fila = fila + '  ' + str(n) + ' |'
        if (len(str(n)) == 4):
          fila = fila + ' ' + str(n) + ' |'
      print(fila)
      print('+------+------+------+------+') 
      #print()
    #-----
    c = c + 1
  archivo.close()
#--------------------------------------------------
#----- Maquina
#----- Lee toda la matriz y decide que movimiento hacer
#--------------------------------------------------
def maquina(M, no_jugador):
  if True:
    for i in range(0,4):
      for j in range(0,4):
        if i == 0:
          if j == 0:
            if M[i][j] == M[i][j+1]:
              l = ["a", "d"]
              l2 = random.choice(l)
              return l2
            elif M[i][j] == M[i+1][j]:
              l = ["w", "s"]
              l2 = random.choice(l)
              return l2
          elif j == 1 or j == 2:
            if M[i][j] == M[i][j-1] or M[i][j] == M[i][j+1]:
              l = ["a", "d"]
              l2 = random.choice(l)
              return l2
            elif M[i][j] == M[i+1][j]:
              l = ["w", "s"]
              l2 = random.choice(l)
              return l2
          elif j == 3:
            if M[i][j] == M[i][j-1]:
              l = ["a", "d"]
              l2 = random.choice(l)
              return l2
            elif M[i][j] == M[i+1][j]:
              l = ["w", "s"]
              l2 = random.choice(l)
              return l2
        elif i == 3:
          if j == 0:
            if M[i][j] == M[i][j+1]:
              l = ["a", "d"]
              l2 = random.choice(l)
              return l2
            elif M[i][j] == M[i-1][j]:
              l = ["w", "s"]
              l2 = random.choice(l)
              return l2
          elif j == 1 or j == 2:
            if M[i][j] == M[i][j-1] or M[i][j] == M[i][j+1]:
              l = ["a", "d"]
              l2 = random.choice(l)
              return l2
            elif M[i][j] == M[i-1][j]:
              l = ["w", "s"]
              l2 = random.choice(l)
              return l2
          elif j == 3:
            if M[i][j] == M[i][j-1]:
              l = ["a", "d"]
              l2 = random.choice(l)
              return l2
            elif M[i][j] == M[i-1][j]:
              l = ["w", "s"]
              l2 = random.choice(l)
              return l2
        elif i == 1 or i == 2:
          if j == 0:
            if M[i][j] == M[i][j+1]:
              l = ["a", "d"]
              l2 = random.choice(l)
              return l2
            elif M[i][j] == M[i+1][j] or M[i][j] == M[i-1][j]:
              l = ["w", "s"]
              l2 = random.choice(l)
              return l2
          elif j == 3:
            if M[i][j] == M[i][j-1]:
              l = ["a", "d"]
              l2 = random.choice(l)
              return l2
            elif M[i][j] == M[i+1][j] or M[i][j] == M[i-1][j]:
              l = ["w", "s"]
              l2 = random.choice(l)
              return l2
          elif j == 1 or j == 2:
            if M[i][j] == M[i][j-1] or M[i][j] == M[i][j+1]:
              l = ["a", "d"]
              l2 = random.choice(l)
              return l2
            elif M[i][j] == M[i+1][j] or M[i][j] == M[i-1][j]:
              l = ["w", "s"]
              l2 = random.choice(l)
              return l2
  else:
    l = ["a", "s", "d", "w"]
    l2 = random.choice(l)
    return l2
#--------------------------------------------------
#----- Suma los iguales en la matriz arriba
#--------------------------------------------------
def sumaarriba(M, no_jugador):
  global M1, M2
  global PunteoM1, PunteoM2
  if no_jugador == 1:
    auxi1 = M
  if no_jugador == 2:
    auxi2 = M
  aux = M
  x=0
  while x <= 2:
    for c in range(0,4):
      if x != 3:
        if aux[x][c] != " ":
          if aux[x+1][c] == aux[x][c]:
            aux[x][c] = aux[x][c] + aux[x+1][c]
            aux[x+1][c] = " "
            if no_jugador == 1: PunteoM1 = PunteoM1 + 2
            if no_jugador == 2: PunteoM2 = PunteoM2 + 2
    x = x + 1
  aux = movarriba(aux)
  if no_jugador == 1:
    M1 = aux
  elif no_jugador == 2:
    M2 = aux
  return aux
#--------------------------------------------------
#----- Mueve la Matriz hacia arriba
#--------------------------------------------------
def movarriba(M):
  aux = M
  x=0
  while x <= 2:
    if x == 0:
      for c in range(0,4):
        if aux[x][c] == " ":
          if M[x+1][c] != " ":
            M[x][c]=M[x+1][c]
            M[x+1][c] = " "
          elif M[x+2][c] != " ":
            M[x][c]=M[x+2][c]
            M[x+2][c] = " "
          elif M[x+3][c] != " ":
            M[x][c]=M[x+3][c]
            M[x+3][c] = " "
    elif x == 1:
      for c in range(0,4):
        if aux[x][c] == " ":
          if M[x+1][c] != " ":
            M[x][c]=M[x+1][c]
            M[x+1][c] = " "
          elif M[x+2][c] != " ":
            M[x][c]=M[x+2][c]
            M[x+2][c] = " "
    elif x == 2:
      for c in range(0,4):
        if aux[x][c] == " ":
          if M[x+1][c] != " ":
            M[x][c]=M[x+1][c]
            M[x+1][c] = " "
    x = x + 1
  return aux
#--------------------------------------------------
#----- Suma los iguales en la matriz abajo
#--------------------------------------------------
def sumaabajo(M, no_jugador):
  global M1, M2
  global PunteoM1, PunteoM2
  if no_jugador == 1:
    auxi1 = M
  if no_jugador == 2:
    auxi2 = M
  aux = M
  x=3
  while x >= 1:
    for c in range(0,4):
      if x != 0:
        if aux[x][c] != " ":
          if aux[x-1][c] == aux[x][c]:
            aux[x][c] = aux[x][c] + aux[x-1][c]
            aux[x-1][c] = " "
            if no_jugador == 1: PunteoM1 = PunteoM1 + 2
            if no_jugador == 2: PunteoM2 = PunteoM2 + 2
            
    x = x - 1
  aux = movabajo(aux)
  if no_jugador == 1:
    M1 = aux
  elif no_jugador == 2:
    M2 = aux
  return aux
#--------------------------------------------------
#----- Mueve la Matriz hacia abajo
#--------------------------------------------------
def movabajo(M):
  aux = M
  x=3
  while x >= 1:
    if x == 3:
      for c in range(0,4):
        if aux[x][c] == " ":
          if M[x-1][c] != " ":
            M[x][c]=M[x-1][c]
            M[x-1][c] = " "
          elif M[x-2][c] != " ":
            M[x][c]=M[x-2][c]
            M[x-2][c] = " "
          elif M[x-3][c] != " ":
            M[x][c]=M[x-3][c]
            M[x-3][c] = " "
    elif x == 2:
      for c in range(0,4):
        if aux[x][c] == " ":
          if M[x-1][c] != " ":
            M[x][c]=M[x-1][c]
            M[x-1][c] = " "
          elif M[x-2][c] != " ":
            M[x][c]=M[x-2][c]
            M[x-2][c] = " "
    elif x == 1:
      for c in range(0,4):
        if aux[x][c] == " ":
          if M[x-1][c] != " ":
            M[x][c]=M[x-1][c]
            M[x-1][c] = " "
    x = x - 1
  return aux
#--------------------------------------------------
#----- Suma los iguales en la matriz derecha
#--------------------------------------------------
def sumaderecha(M, no_jugador):  
  global M1, M2
  global PunteoM1, PunteoM2
  if no_jugador == 1:
    auxi1 = M
  if no_jugador == 2:
    auxi2 = M
  aux = M
  x=3
  while x >= 1:
    for c in range(0,4):
      if x != 0:
        if aux[c][x] != " ":
          if aux[c][x-1] == aux[c][x]:
            aux[c][x] = aux[c][x] + aux[c][x-1]
            aux[c][x-1] = " "
            if no_jugador == 1: PunteoM1 = PunteoM1 + 2
            if no_jugador == 2: PunteoM2 = PunteoM2 + 2
    x = x - 1
  aux = movderecha(aux)
  if no_jugador == 1:
    M1 = aux
  elif no_jugador == 2:
    M2 = aux
  return aux
#--------------------------------------------------
#----- Mueve la Matriz hacia derecha
#--------------------------------------------------
def movderecha(M):
  aux = M
  x=3
  while x >= 1:
    if x == 3:
      for c in range(0,4):
        if aux[c][x] == " ":
          if M[c][x-1] != " ":
            M[c][x]=M[c][x-1]
            M[c][x-1] = " "
          elif M[c][x-2] != " ":
            M[c][x]=M[c][x-2]
            M[c][x-2] = " "
          elif M[c][x-3] != " ":
            M[c][x]=M[c][x-3]
            M[c][x-3] = " "
    elif x == 2:
      for c in range(0,4):
        if aux[c][x] == " ":
          if M[c][x-1] != " ":
            M[c][x]=M[c][x-1]
            M[c][x-1] = " "
          elif M[c][x-2] != " ":
            M[c][x]=M[c][x-2]
            M[c][x-2] = " "
    elif x == 1:
      for c in range(0,4):
        if aux[c][x] == " ":
          if M[c][x-1] != " ":
            M[c][x]=M[c][x-1]
            M[c][x-1] = " "
    x = x - 1
  return aux
#--------------------------------------------------
#----- Suma los iguales en la matriz izquierda
#--------------------------------------------------
def sumaizquierda(M, no_jugador):
  global M1, M2
  global PunteoM1, PunteoM2
  if no_jugador == 1:
    auxi1 = M
  if no_jugador == 2:
    auxi2 = M
  aux = M
  x=0
  while x <= 2:
    for c in range(0,4):
      if x != 3:
        if aux[c][x] != " ":
          if aux[c][x+1] == aux[c][x]:
            aux[c][x] = aux[c][x] + aux[c][x+1]
            aux[c][x+1] = " "
            if no_jugador == 1: PunteoM1 = PunteoM1 + 2
            if no_jugador == 2: PunteoM2 = PunteoM2 + 2  
            
    x = x + 1
  aux = movizquierda(aux)
  if no_jugador == 1:
    M1 = aux
  elif no_jugador == 2:
    M2 = aux
  return aux
#--------------------------------------------------
#----- Mueve la Matriz hacia derecha
#--------------------------------------------------
def movizquierda(M):
  aux = M
  x=0
  while x <= 2:
    if x == 0:
      for c in range(0,4):
        if aux[c][x] == " ":
          if M[c][x+1] != " ":
            M[c][x]=M[c][x+1]
            M[c][x+1] = " "
          elif M[c][x+2] != " ":
            M[c][x]=M[c][x+2]
            M[c][x+2] = " "
          elif M[c][x+3] != " ":
            M[c][x]=M[c][x+3]
            M[c][x+3] = " "
    elif x == 1:
      for c in range(0,4):
        if aux[c][x] == " ":
          if M[c][x+1] != " ":
            M[c][x]=M[c][x+1]
            M[c][x+1] = " "
          elif M[c][x+2] != " ":
            M[c][x]=M[c][x+2]
            M[c][x+2] = " "
    elif x == 2:
      for c in range(0,4):
        if aux[c][x] == " ":
          if M[c][x+1] != " ":
            M[c][x]=M[c][x+1]
            M[c][x+1] = " "
    x = x + 1
  return aux
#--------------------------------------------------
#----- maximo_numero
#--------------------------------------------------
def maximo_numero(M, no_jugador):
  max = 0
  for i in range(len(M)):
    for j in range(0, 4):
      if M[i][j] != " ":
        if max < M[i][j]: max = M[i][j]
  return(max)  
#--------------------------------------------------
#----- Agrega un 2 o 4 en la matriz 
#--------------------------------------------------
def agregaral(M, no_jugador):
  global M1, M2
  c = True
  cont = 0
  mx = maximo_numero(M, no_jugador)
  if mx < 2048:
    for x in range(0,4):
      for y in range(0,4):
        if M[x][y] == " ":
          cont += 1
    if cont > 0:
      while c == True:
        num = [2, 4]
        azar = random.choice(num)
        azar1 = random.randint(0, 3)
        azar2 = random.randint(0, 3)
        if M[azar1][azar2] == " ": 
          M[azar1][azar2] = azar 
          if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
          if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
          return M
    else:
      if ModoJuego == 1:
        limpiar_pantalla()
        fin()
        print("Su punteo Máximo es de:")
        print("                 ╔════════╗                ")
        print("                   Punteo                 ")
        print("                    ",PunteoM1,"                   ")
        print("                 ╚════════╝                ")
        num = maximo_numero(M, no_jugador)
        print("Su número Máximo es de:")
        print("                 ╔════════╗                ")
        print("                   Número                 ")
        print("                    ",num,"                   ")
        print("                 ╚════════╝                ")
      if (ModoJuego == 2) or (ModoJuego == 3):
        limpiar_pantalla()
        fin()
        print("Su punteo Máximo es de:")
        print("                 Jugador: 1","                 Jugador: 2")
        print("                 ╔════════╗","                 ╔════════╗")
        print("                   Punteo  ","                   Punteo  ")
        print("                    ",PunteoM1,"                        ",PunteoM2)
        print("                 ╚════════╝","                 ╚════════╝")
        print()
        print()
        num1 = maximo_numero(M1, 1)
        num2 = maximo_numero(M2, 2)
        print("Su número Máximo es de:")
        print("                 Jugador: 1","                 Jugador: 2")
        print("                 ╔════════╗","                 ╔════════╗")
        print("                   Número  ","                   Número  ")
        print("                    ",num1,"                        ",num2)
        print("                 ╚════════╝","                 ╚════════╝")
        print()
        print()
      input("Presione Enter para regresar al menú")
      c = False
      main()
  else:
    if ModoJuego == 1:
      limpiar_pantalla()
      win()
      print("Su punteo Máximo es de:")
      print("                 ╔════════╗                ")
      print("                   Punteo                 ")
      print("                    ",PunteoM1,"                   ")
      print("                 ╚════════╝                ")
      num = maximo_numero(M, no_jugador)
      print("Su número Máximo es de:")
      print("                 ╔════════╗                ")
      print("                   Número                 ")
      print("                    ",num,"                   ")
      print("                 ╚════════╝                ")
    if (ModoJuego == 2) or (ModoJuego == 3):
      limpiar_pantalla()
      win()
      print("Su punteo Máximo es de:")
      print("                 Jugador: 1","                 Jugador: 2")
      print("                 ╔════════╗","                 ╔════════╗")
      print("                   Punteo  ","                   Punteo  ")
      print("                    ",PunteoM1,"                        ",PunteoM2)
      print("                 ╚════════╝","                 ╚════════╝")
      print()
      print()
      num1 = maximo_numero(M1, 1)
      num2 = maximo_numero(M2, 2)
      print("Su número Máximo es de:")
      print("                 Jugador: 1","                 Jugador: 2")
      print("                 ╔════════╗","                 ╔════════╗")
      print("                   Número  ","                   Número  ")
      print("                    ",num1,"                        ",num2)
      print("                 ╚════════╝","                 ╚════════╝")
      print()
      print()
    input("Presione Enter para regresar al menú")
    c = False
    main()
#--------------------------------------------------
#----- PROCEDIMIENTO limpiar_pantalla
#----- Limpia la pantalla
#--------------------------------------------------
def limpiar_pantalla():
  if platform.system() == 'windows':
      os.system('cls')
  else:
      os.system('clear')
#--------------------------------------------------
#----- inicializar_matrices
#--------------------------------------------------
def inicializar_matrices():
  global M1, M2
  M1 = [[" "," "," "," "], [" "," "," "," "], [" "," "," "," "], [" "," "," "," "]]
  M2 = [[" "," "," "," "], [" "," "," "," "], [" "," "," "," "], [" "," "," "," "]]
  global PunteoM1, PunteoM2
  PunteoM1 = 0
  PunteoM1 = 0
  eliminar_archivos()
#--------------------------------------------------
#----- Instrucciones
#--------------------------------------------------
def instruc():
  limpiar_pantalla()
  bienvenida()
  
  print('2048 es un juego que se practica en un tablero de 4x4 casillas, en cada casilla se van a guardar números potencias de 2. Estos números se van sumando hasta que en alguna de las casillas de el numero 2048. \n')
  input('\n\n\nPresione ENTER para continuar...\n\n\n')
  
  print('   * El tablero inicia con un 2 o un 4 en 2 casillas.\n')
  print('   * Usted puede hacer 4 movimientos (arriba, abajo, izquierda y derecha)')
  print('   * Cuando usted mueva hacia algún lado, todos los números en el tablero se moverán hacia la dirección a donde usted decidió moverse. Algunos de los números se pueden sumar.')
  input('\n\n\nPresione ENTER para continuar...\n\n\n') 
  
  print('   * Cuando se hace un movimiento, algunas casillas pueden sumar sus valores y convertirse en una sola casilla. Las reglas para realizar las sumas son las siguientes:\n\n\n')
  print('   * Si dos casillas tienen el mismo número se pueden sumar si son iguales y estan en la casilla consecutiva siguiente, sea fila o columna. Por ejemplo: \n\n\n')
  input('\n\n\nPresione ENTER para continuar...\n\n\n') 
  
  print('   Estos tableros si se pueden sumar y que resulte solo una casilla con la suma de las 2.\n\n')
  
  print('   +------+------+------+------+               +------+------+------+------+')
  print('   |      |      |      |      |               |      |      |      |      |')
  print('   +------+------+------+------+               +------+------+------+------+')
  print('   |      |  4   |      |      |               |      |      |      |      |')
  print('   +------+------+------+------+               +------+------+------+------+')
  print('   |      |  4   |      |      |               |      |  2   |   2  |      |')
  print('   +------+------+------+------+               +------+------+------+------+')
  print('   |      |      |      |      |               |      |      |      |      |')
  print('   +------+------+------+------+               +------+------+------+------+')
  
  print('\n\n\n   * En el caso del tablero izquierdo, solo se pueden unir si el movimiento es hacia arriba o hacia abajo.')
  print('\n   * En el tablero del lado derecho solo se pueden unir si el movimiento es hacia la izquierda o hacia la derecha.')
  print('   * En este caso la casilla que queda con el valor sumado es la mas cercana al valor del movimiento.\n\n\n')
  
  input('\n\n\nPresione ENTER para continuar...\n\n\n') 
  
  print('   Estos tableros no se pueden sumar y no se convierten en una sola casilla:\n\n')
  
  print('   +------+------+------+------+               +------+------+------+------+')
  print('   |      |      |      |      |               |      |      |  2   |      |')
  print('   +------+------+------+------+               +------+------+------+------+')
  print('   |      |  4   |      |      |               |      |      |      |      |')
  print('   +------+------+------+------+               +------+------+------+------+')
  print('   |      |      |   4  |      |               |      |      |      |      |')
  print('   +------+------+------+------+               +------+------+------+------+')
  print('   |      |      |      |      |               |  2   |      |      |      |')
  print('   +------+------+------+------+               +------+------+------+------+')
  
  
  print('   Solo es posible sumar 2 casillas consecutivas, si hay 3 números consecutivos, solo 2 de ellos se van a sumar y el otro se queda igual. En el caso de que hayan 4 números consecutivos se sumarían en pares.')
  print('   Si se pueden sumar varias casillas en una sola línea, se van a asumir la las casillas que están en la dirección del movimiento.')      

  input('\n\n\nPresione ENTER para continuar...\n\n\n') 
  limpiar_pantalla()
  bienvenida()
#--------------------------------------------------
#----- Modalidad Normal
#--------------------------------------------------
def modnor(M, no_jugador):
  limpiar_pantalla()
  global M1, M2, h, auxi1, auxi2
  if no_jugador == 1:
    M = M1
    #PunteoM = PunteoM1
  elif no_jugador == 2:
    M = M2
    #PunteoM = PunteoM2
  matrix_length = len(M1)
  global c, ModoJuego
  c = True
  while c == True:
    sobrevive()
    if h != 1:
      M = agregaral(M, 1)
    if ModoJuego == 1: print("Modalidad Normal")
    if ModoJuego == 2: print("Jugador vs Jugador")
    if ModoJuego == 3: print("Jugador vs Maquina")
    print("Jugador ", no_jugador ,":")
    print('+------+------+------+------+')  
    for i in range(matrix_length): 
      fila = '|'
      for j in range(0, 4):
        n = M[i][j]
        if (len(str(n)) == 1):
          fila = fila + '    ' + str(n) + ' |'
        if (len(str(n)) == 2):
          fila = fila + '   ' + str(n) + ' |'
        if (len(str(n)) == 3):
          fila = fila + '  ' + str(n) + ' |'
        if (len(str(n)) == 4):
          fila = fila + ' ' + str(n) + ' |'
      print(fila)
      print('+------+------+------+------+') 
    print("                 ╔════════╗                ")
    print("                   Punteo                 ")
    #print("                    ",PunteoM,"                   ")
    if no_jugador == 1: print("                    ",PunteoM1,"                   ")
    if (no_jugador == 2) or (no_jugador ==3): print("                    ",PunteoM2,"                   ")
    print("                 ╚════════╝                ")
    print()
    if ModoJuego == 1:
      print('Letra "W" para el movimiento hacia arriba')
      print('Letra "S" para el movimiento hacia abajo')
      print('Letra "A" para el movimiento hacia la izquierda')
      print('Letra "D" para el movimiento hacia la derecha') 
    if ModoJuego == 2:
      print('Letra "W" para el movimiento hacia arriba')
      print('Letra "S" para el movimiento hacia abajo')
      print('Letra "A" para el movimiento hacia la izquierda')
      print('Letra "D" para el movimiento hacia la derecha') 
    if ModoJuego == 3:
      if no_jugador == 1:
        print('Letra "W" para el movimiento hacia arriba')
        print('Letra "S" para el movimiento hacia abajo')
        print('Letra "A" para el movimiento hacia la izquierda')
        print('Letra "D" para el movimiento hacia la derecha') 
    if (ModoJuego == 2) or (ModoJuego == 3): print('Letra "Y" para cambiar de jugador')
    if no_jugador == 1:
      if M != auxi1:
        print('Letra "U" para regresar 1 movimiento')
    if no_jugador == 2:
      if M != auxi2:
        print('Letra "U" para regresar 1 movimiento')
    print('Letra "R" para mostrar las jugadas que se han hecho en el juego') 
    print('Letra "Q" para salir') 
    if ModoJuego == 3 and no_jugador == 2:
      print("Enter para realizar el siguiente movimiento")
    print()
    p = True
    if ModoJuego != 3:
      while p == True:
        x = input("Ingrese el siguiente movimiento:")
        if x == "w":
#--Derek
          if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
          if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
          h = 0
          M = sumaarriba(M, no_jugador)
          p = False
        elif x == "s":
#--Derek
          if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
          if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
          h = 0
          M = sumaabajo(M, no_jugador)
          p = False
        elif x == "d":
#--Derek
          if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
          if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
          h = 0
          M = sumaderecha(M, no_jugador)
          p = False
        elif x =="a":
#--Derek
          if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
          if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
          h = 0
          M = sumaizquierda(M, no_jugador)
          p = False
        elif x == "y":
          if ModoJuego == 2:
            if no_jugador == 1:
              h = 1
              modnor(M2, 2)
              no_jugador = 2
            if no_jugador == 2:
              h = 1
              modnor(M1, 1)
              no_jugador == 1
        elif x =="r":            
          if no_jugador == 1: replay_juego("jugador1")
          if no_jugador == 2: replay_juego("jugador2")
          input("Presione enter para continuar")
          p = False
#--Derek2        
        elif x =="q":
          p = False
          c = False
          main()
        elif x == "u":
          if no_jugador == 1: 
            M1 = auxi1
            M = auxi1
          if no_jugador == 2: 
            M2 = auxi2
            M = auxi2
          p = False
        else:
          h = 1
          print("Favor ingrese un comando correcto")
      limpiar_pantalla()
    elif ModoJuego == 3:
      if no_jugador == 1:
        while p == True:
          x = input("Ingrese el siguiente movimiento:")
            
          if x == "w":
#--Derek
            if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
            if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
            h = 0
            M = sumaarriba(M, no_jugador)
            p = False
          elif x == "s":
#--Derek
            if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
            if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
            h = 0
            M = sumaabajo(M, no_jugador)
            p = False
          elif x == "d":
#--Derek
            if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
            if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
            h = 0
            M = sumaderecha(M, no_jugador)
            p = False
          elif x =="a":
#--Derek
            if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
            if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
            h = 0
            M = sumaizquierda(M, no_jugador)
            p = False
          elif x == "y":
            if ModoJuego == 3:
              if no_jugador == 1:
                h = 1
                modnor(M2, 2)
                no_jugador = 2
              if no_jugador == 2:
                h = 1
                modnor(M1, 1)
                no_jugador == 1
          elif x =="r":
            if no_jugador == 1: replay_juego("jugador1")
            if no_jugador == 2: replay_juego("jugador2")          
            p = False
#--Derek2          
          elif x =="q":
            p = False
            c = False
            main()
          elif x == "u":
            if no_jugador == 1: 
              M1 = auxi1
              M = auxi1
            if no_jugador == 2: 
              M2 = auxi2
              M = auxi2
            p = False
          else:
            h = 1
            print("Favor ingrese un comando correcto")
      elif no_jugador == 2:
        while p == True:
          x = input("Ingrese el siguiente movimiento:")
          if x == "y":
            if ModoJuego == 3:
              if no_jugador == 1:
                h = 1
                modnor(M2, 2)
                no_jugador = 2
              if no_jugador == 2:
                h = 1
                modnor(M1, 1)
                no_jugador == 1
          elif x =="r":
            if no_jugador == 1: replay_juego("jugador1")
            if no_jugador == 2: replay_juego("jugador2")
            p = False
#--Derek2          
          elif x == "q":
            p = False
            c = False
            main()
          elif x == "u":
            if no_jugador == 1: 
              M1 = auxi1
              M = auxi1
            if no_jugador == 2: 
              M2 = auxi2
              M = auxi2
            p = False
          else:
            t = maquina(M, no_jugador)
            if t == "w":
#--Derek
              if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
              if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
              h = 0
              M = sumaarriba(M, no_jugador)
              p = False
            elif t == "s":
#--Derek
              if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
              if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
              h = 0
              M = sumaabajo(M, no_jugador)
              p = False
            elif t == "d":
#--Derek
              if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
              if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
              h = 0
              M = sumaderecha(M, no_jugador)
              p = False
            elif t =="a":
#--Derek
              if no_jugador == 1: replay_bitacora(M1, "jugador1.txt")
              if no_jugador == 2: replay_bitacora(M2, "jugador2.txt")
              h = 0
              M = sumaizquierda(M, no_jugador)
              p = False
      limpiar_pantalla()
#--------------------------------------------------
#----- MENU 
#--------------------------------------------------
def main():
  global ModoJuego, M1, M2, auxi1, auxi2
  inicializar_matrices()
  limpiar_pantalla()
  inicializar_matrices()
  bienvenida()
  c = True
  while c == True:
    p = True
    while p == True:
      print("1. Modalidad Normal")
      print("2. Jugador vs Jugador")
      print("3. Jugador vs Maquina")
      print("4. Instrucciones")
      print("5. Salir")
      x = input("Ingrese el numero del modo que desea jugar:")
      if x == "1":
        ModoJuego = 1
        inicializar_matrices()
        agregaral(M1, 1)
        agregaral(M1, 1)
        modnor(M1, 1)
      elif x == "2":        
        ModoJuego = 2
        inicializar_matrices()
        agregaral(M1, 1)
        agregaral(M1, 1)
        agregaral(M2, 2)
        agregaral(M2, 2)
        modnor(M1, 1)
      elif x == "3":
        ModoJuego = 3
        inicializar_matrices()
        agregaral(M1, 1)
        agregaral(M1, 1)
        agregaral(M2, 2)
        agregaral(M2, 2)
        modnor(M1, 1)
      elif x == "4":
        instruc()
      elif x == "5":
        print("Saliendo...")
        exit()
      else:
        print("No valido!!")
        time.sleep(2)
        
      limpiar_pantalla()
      bienvenida()
main()