nombre1= input("inserte nombre de jugador 1:")
nombre2= input("inserte nombre de jugador 2:")
jugador1 = input("hola jugador 1, que elegis? piedra,papel o tijera?: ")
jugador2 = input("hola jugador 2, que elegis? piedra,papel o tijera?: ")

if jugador1== jugador2:
  print("empate")
elif (jugador1 =="piedra" and jugador2=="tijeras" ) or (jugador1 == "papel" and jugador2=="piedra") or (jugador1 == "tijeras" and jugador2== "papel"):
  print("ah ganado:", nombre1)
else:
    print ("ah ganado:", nombre2)