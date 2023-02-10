import random
from os import system

def jugar(user, pc, w, l):
    
    if (user == "piedra" and pc == "tijera") or (user == "papel" and pc == "piedra") or (user == "tijera" and pc == "papel"):
        print("Ganaste!")
        w += 1 
    elif user == pc:
        print("Empate")        
    else:
        print("Perdiste")
        l += 1
    return w,l
def eleccion(opcion):
    
    match opcion:
        case "piedra" | "1":
            return "piedra"            
        case "papel" | "2":
            return "papel"            
        case "tijera" | "3":
            return "tijera"            
        case _:
            print("Elije una opción válida")
   
def run():    
    victorias = 0
    derrotas = 0
    while(victorias < 2 and derrotas < 2):        
        
        pc = random.randint(1,3)
        jugador = input("Piedra (1), papel (2) o tijera (3): ")
        jugador = jugador.lower() #Convierte la cadena de caracteres en minúsulas
        system("clear")
        pc = eleccion(str(pc))
        jugador = eleccion(jugador)
        print(f"Elegiste ------------> {jugador.upper()}")
        print(f"Computadora eligió --> {pc.upper()}")
        victorias,derrotas = jugar(jugador,pc,victorias,derrotas)
        print(f"Tú: {victorias}"," vs ",f"PC: {derrotas}")
                   
    print("El juego ha terminado")

if __name__ == '__main__':
    run()