import turtle
import math
import time


#ciala w ukladzie
class CelestialBody(turtle.Turtle):

    minimal_size = 7
    display_log_base = 1.1

    def __init__(
            self,
            solarsystem,  #uklad słoneczny do którego należy ciało
            mass,
            position=(0, 0),
            velocity=(0, 0),
            body_color = ""
    ):
        super().__init__()
        self.mass = mass
        self.setposition(position)
        self.velocity = velocity
        self.size = max(math.log(self.mass, self.display_log_base), self.minimal_size,)
        self.body_color = body_color
        self.penup()
        self.hideturtle()
        solarsystem.add_celestialbody(self)



    ''' slonca maja ogromna mase, aby objekty na symulacji prezentowaly sie ladnie uzyjemy
        skali logarytmicznej o podstawie 1,1 ktora z malych x zwraca liczby podobne do x,
        a z wielkich liczb duzo mniejsze '''
    def draw(self):
        size = int(self.size)
        self.clear()
        #self.dot(math.log(size,1.1))
        self.dot(self.size)

    def movement(self):
        self.setx(self.xcor() + self.velocity[0])
        self.sety(self.ycor() + self.velocity[1])


class Star(CelestialBody):
    def __init__(
            self,
            solarsystem,  # uklad słoneczny do którego należy ciało
            mass,
            position=(0, 0),
            velocity=(0, 0),
            body_color="orange",
    ):
        super().__init__(solarsystem, mass, position, velocity, body_color)
        self.color(self.body_color)

class Planet(CelestialBody):

    def __init__(
            self,
            solarsystem,  # uklad słoneczny do którego należy ciało
            mass,
            position=(0, 0),
            velocity=(0, 0),
            body_color="blue",
    ):
        super().__init__(solarsystem, mass, position, velocity, body_color)
        self.color(self.body_color)


class Moon(CelestialBody):

    def __init__(
            self,
            solarsystem,  # uklad słoneczny do którego należy ciało
            mass,
            position=(0, 0),
            velocity=(0, 0),
            body_color="white",
    ):
        super().__init__(solarsystem, mass, position, velocity, body_color)
        self.color(self.body_color)


# uklad sloneczny
class SolarSystem:
    def __init__(self,screen_height, screen_width, screen_color):
        self.SolarSystem = turtle.Screen()
        self.SolarSystem.setup(screen_height, screen_width)
        self.SolarSystem.tracer(0)
        self.SolarSystem.bgcolor(screen_color)
        self.CelestialBodies = []

    def add_celestialbody(self, celestialbody):
        self.CelestialBodies.append(celestialbody)

    def rmvcelestialbody(self, celestialbody):
        celestialbody.clear()
        self.CelestialBodies.remove(celestialbody)

    def cel_body_movement(self):
        for celestialbody in self.CelestialBodies:
            celestialbody.movement()
            celestialbody.draw()
            self.SolarSystem.update()


    @staticmethod
    def accelerate_due_to_gravity(body1, body2):
        force = body1.mass*body2.mass/(body1.distance(body2)**2)
        angle = body1.towards(body2)
        reverse = 1
        for body in body1, body2:
            acceleration = force / body.mass
            acceleration_x = acceleration * math.cos(math.radians(angle))
            acceleration_y = acceleration * math.sin(math.radians(angle))
            body.velocity = (
                body.velocity[0] + (reverse * acceleration_x),
                body.velocity[1] + (reverse * acceleration_y),
            )
            reverse = -1

    def check_collision(self, body1, body2):
        if isinstance(body1, Planet) and isinstance(body2, Planet):
            return
        if body1.distance(body2) < body1.size/3 + body2.size/3:
            for body in body1, body2:
                if isinstance(body, Planet):
                    self.rmvcelestialbody(body)


    def calculate_all_body_interactions(self):
        CelestialBodies_copy = self.CelestialBodies.copy()
        for idx, body1 in enumerate(CelestialBodies_copy):
            for body2 in CelestialBodies_copy[idx + 1:]:
                self.accelerate_due_to_gravity(body1, body2)
                self.check_collision(body1, body2)


class Simulation:
    @staticmethod
    def uklad_sloneczny_sim(screen_h, screen_w, buffer_time, screen_clr):
        uklad_sloneczny = SolarSystem(screen_h,screen_w, screen_clr)
        slonce = Star(uklad_sloneczny, 15891, (0, 0), (0, 0))
        ziemia = Planet(uklad_sloneczny, 100, (0, 400), (-6, 0), "green")
        ksiezyc = Moon(uklad_sloneczny,3, (0, 369), (-8, 0))
        wenus = Planet(uklad_sloneczny, 48, (0, 220), (-8, 0), "LightPink")
        mars = Planet(uklad_sloneczny, 60, (0, 540), (-5, 0), "red")
        merkury = Planet(uklad_sloneczny, 3, (0, 150), (-9, 0), "DarkGrey")

        while True:
            time.sleep(buffer_time)
            uklad_sloneczny.cel_body_movement()
            uklad_sloneczny.calculate_all_body_interactions()

    @staticmethod
    def uklad_binarny_sim(screen_h, screen_w, buffer_time, screen_clr):
        uklad_sloneczny = SolarSystem(screen_h, screen_w, screen_clr)
        slonce1 = Star(uklad_sloneczny, 11000, (0, 200), (-3, 0))
        slonce2 = Star(uklad_sloneczny, 11000, (0, -200), (3, 0))
        planeta1 = Planet(uklad_sloneczny, 6, (0, 0), (-10, 0), "green")
        planeta2 = Planet(uklad_sloneczny, 20, (0, 350), (10, 0), "CornflowerBlue")
        planeta3 = Planet(uklad_sloneczny, 10, (0, -320), (-12, 0), "cyan")
        while True:
            time.sleep(buffer_time)
            uklad_sloneczny.cel_body_movement()
            uklad_sloneczny.calculate_all_body_interactions()

