from SolarSystemSim import  Star, Moon, Planet, SolarSystem, Simulation
import time

def create_system():
    height = input("wprowadz wysokosc ekranu: ")
    width = input("wprowadz szerokosc ekranu: ")
    color = input("wprowadz kolor tla (najlepiej wypada 'black'):  ")
    return SolarSystem(int(height), int(width), color)


def add_body(ss_name, type):
    mass = int(input("wprowadz mase: "))
    xpos = int(input("wprowadz koordynat x: "))
    ypos = int(input("wprowadz koordynat y: "))
    xvel = int(input("wprowadz wartosc x wektora predkosci: "))
    yvel = int(input("wprowadz wartosc y wektora predkosci: "))
    color = input("wprowadz kolor ciala: ")
    if type == "star":
        return Star(ss_name, mass, (xpos, ypos), (xvel, yvel), color)
    elif type == "planet":
        return Planet(ss_name, mass, (xpos, ypos), (xvel, yvel), color)
    elif type == "moon":
        return Moon(ss_name, mass, (xpos, ypos), (xvel, yvel), color)


def sim_creator():
    system = create_system()
    stars = []
    planets = []
    moons = []
    print("Jak dodac ciala aby nie rozbily sie o siebie od razu?\n1.Gwiazde umiescic w punkcie (0,0) i nadac predkosc (0,0)\n2.Cialom niebieskim nadac na jednym koordynacie 0 i na dugim odleglosc, predkosc nadac na przeciwnym miejscu wektora aby cialo zaczelo sie obracac wokol gwiazdy\nPo opanowaniu tych dwoch aspektow zachecam do eksperymentacji z ilosciami, polozeniami i predkosciami cial!!!")
    status = True
    while status:
        choice = int(input("1.Dodaj gwiazde\n2.Przejdz dalej\n"))
        if choice == 1:
            stars.append(add_body(system, 'star'))
        else:
            status = False
    status = True
    while status:
        choice = int(input("1.Dodaj planete\n2.Przejdz dalej\n"))
        if choice == 1:
            stars.append(add_body(system, 'planet'))
        else:
            status = False
    status = True
    while status:
        choice = int(input("1.Dodaj ksiezyc\n2.Przejdz dalej\n"))
        if choice == 1:
            stars.append(add_body(system, 'moon'))
        else:
            status = False

    while True:
        time.sleep(0.02)
        system.cel_body_movement()
        system.calculate_all_body_interactions()


def menu():
    select = int(input("Wybor Symulacji\n1.Uklad Sloneczny\n2.Uklad z dwoma gwiazdami\n3.Wlasny uklad\n"))
    if select == 1:
        height = int(input("wprowadz wysokosc ekranu: "))
        width = int(input("wprowadz szerokosc ekranu: "))
        color = input("wprowadz kolor tla (najlepiej wypada 'black'):  ")
        Simulation.uklad_sloneczny_sim(height, width,0.02, color)
    elif select == 2:
        height = int(input("wprowadz wysokosc ekranu: "))
        width = int(input("wprowadz szerokosc ekranu: "))
        color = (input("wprowadz kolor tla (najlepiej wypada 'black'):  "))
        Simulation.uklad_binarny_sim(height, width, 0.02, color)
    elif select == 3:
        sim_creator()



menu()






