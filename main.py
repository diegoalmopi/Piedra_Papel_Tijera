import random
from os import system

def jugar(user, pc, w, l):
    
    if (user == "piedra" and pc == "tijera") or (user == "papel" and pc == "piedra") or (user == "tijera" and pc == "papel"):
        print("🙋 Ganaste!")
        w += 1 
    elif user == pc:
        print("🤝 Empate")        
    else:
        print("🤖 Te gané!")
        l += 1
    return w,l
   
def run():    
    victorias = 0
    derrotas = 0
    opciones = ("piedra","papel","tijera")
    while(victorias < 2 and derrotas < 2):        
        
        pc = random.randint(1,3)
        jugador = input("Piedra 🪨, papel 📄 o tijera ✂️ : ")
        jugador = jugador.lower() #Convierte la cadena de caracteres en minúsulas
        if not jugador in opciones:
            print("Elige una opción válida")
            continue
        
        system("clear")
        pc = random.choice(opciones)
        
        print(f"Elegiste ------------> {jugador.upper()}")
        print(f"Computadora eligió --> {pc.upper()}")
        victorias,derrotas = jugar(jugador,pc,victorias,derrotas)
        print(f"Tú: {victorias}"," vs ",f"PC: {derrotas}")
                   
    print("El juego ha terminado!")

if __name__ == '__main__':
    run()