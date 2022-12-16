import arcade
import random
import math

SKAERMBREDDE = 640
SKAERMHOEJDE = 480
BOLDHASTIGHED = 3
BATHASTIGHED = 3
class Bold:
    """ Denne klasse beskriver/styrer en bold, som hopper i vinduet på skærmen. """

    def __init__(self, position_x, position_y, hastighed_x, hastighed_y, radius, farve):
        self.position_x = position_x
        self.position_y = position_y
        self.hastighed_x = hastighed_x
        self.hastighed_y = hastighed_y
        self.radius = radius
        self.farve = farve

    def update(self):
        self.position_x += self.hastighed_x
        self.position_y += self.hastighed_y

        # Bolden holdes inden for top og bund
        if self.position_y < self.radius or self.position_y > SKAERMHOEJDE - self.radius:
            self.hastighed_y *= -1

    def draw(self):
        """ Tegner bolden som en simpel udfyldt cirkel vha arcade. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.farve)

class Bat:
    """ Denne klasse repræsenterer battet i pong. """
    def __init__(self, center_x, center_y, hastighed_x, hastighed_y, bredde, hoejde, farve):
        self.center_x = center_x
        self.center_y = center_y
        self.hastighed_x = hastighed_x
        self.hastighed_y = hastighed_y
        self.bredde = bredde
        self.hoejde = hoejde
        self.farve = farve

    def update(self):
        self.center_x += self.hastighed_x
        self.center_y += self.hastighed_y

        # Holder battet inden for vinduet
        if self.center_x < self.bredde / 2:
            self.center_x = self.bredde / 2
        if self.center_x > SKAERMBREDDE - self.bredde / 2:
            self.center_x = SKAERMBREDDE - self.bredde / 2
        if self.center_y < self.hoejde / 2:
            self.center_y = self.hoejde/ 2
        if self.center_y > SKAERMHOEJDE - self.hoejde / 2:
            self.center_y = SKAERMHOEJDE - self.hoejde / 2
    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.bredde, self.hoejde, self.farve)

class Vindue(arcade.Window):
    """ Vores nye vinduesklasse. """

    def __init__(self, bredde, hoejde, titel):
        """ Initialisator. """

        # Kalder forældreklasse(n/rnes) initialisatorer
        super().__init__(bredde, hoejde, titel)
        # Sætter baggrundsfarven én gang
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_GREY)
        self.setup()

    def setup(self):
        self.bold = Bold(SKAERMBREDDE, SKAERMHOEJDE, 0, 0, 5, arcade.csscolor.RED)
        self.reset_bold(self.bold)
        self.spiller_venstre = Bat(20, SKAERMHOEJDE/2, 0, 0, 10, 60, arcade.csscolor.WHITE)
        self.spiller_hoejre= Bat(SKAERMBREDDE - 20, SKAERMHOEJDE/2, 0, 0, 10, 60, arcade.csscolor.WHITE)
        self.spiller_venstre_point = 0
        self.spiller_hoejre_point = 0
        self.spiller_venstre_pointtavle = arcade.Text("0", 20 , SKAERMHOEJDE-20, font_size = 20, anchor_x = "left", anchor_y = "top")
        self.spiller_hoejre_pointtavle = arcade.Text("0", SKAERMBREDDE - 20 , SKAERMHOEJDE-20, font_size = 20, anchor_x = "right", anchor_y = "top")

    def on_key_press(self, tast, modifikationstast):
        """ Kørers når brugeren trykker på en tast. """
        if tast == arcade.key.W:
            self.spiller_venstre.hastighed_y = BATHASTIGHED
        elif tast == arcade.key.S:
            self.spiller_venstre.hastighed_y = - BATHASTIGHED

        if tast == arcade.key.UP:
            self.spiller_hoejre.hastighed_y = BATHASTIGHED
        elif tast == arcade.key.DOWN:
            self.spiller_hoejre.hastighed_y = - BATHASTIGHED

    def on_key_release(self, tast, modifikationstast):
        """ Kørers når brugeren slipper en tast. """
        if tast == arcade.key.W or tast == arcade.key.S:
            self.spiller_venstre.hastighed_y = 0
        if tast == arcade.key.UP or tast == arcade.key.DOWN:
            self.spiller_hoejre.hastighed_y = 0
            
    def reset_bold(self, bold):
        bold.position_x = SKAERMBREDDE / 2
        bold.position_y = SKAERMHOEJDE / 2
        hastighed = random.randint(3,5)
        vinkel = random.uniform(0.1, math.pi/ 4)
        bold.hastighed_x = random.choice((-1, 1)) * hastighed * math.cos(vinkel)
        bold.hastighed_y = hastighed * math.sin(vinkel)
    def update(self, delta_tid):
        self.bold.update()
        self.spiller_venstre.update()
        self.spiller_hoejre.update()
        self.spiller_venstre_pointtavle.draw()

        # Bolden rammer venstre spiller
        if (self.bold.position_y < self.spiller_venstre.center_y + self.spiller_venstre.hoejde / 2 and
            self.bold.position_y > self.spiller_venstre.center_y - self.spiller_venstre.hoejde / 2 and
            self.bold.position_x - self.bold.radius < self.spiller_venstre.center_x + self.spiller_venstre.bredde / 2):
            self.bold.hastighed_x *= -1.1
        
        # Bolden rammer venstre spiller
        if (self.bold.position_y < self.spiller_hoejre.center_y + self.spiller_hoejre.hoejde / 2 and
            self.bold.position_y > self.spiller_hoejre.center_y - self.spiller_hoejre.hoejde / 2 and
            self.bold.position_x + self.bold.radius > self.spiller_hoejre.center_x - self.spiller_hoejre.bredde / 2):
            self.bold.hastighed_x *= -1.1

        # Bolden kommer forbi battene
        if self.bold.position_x < 0:
            self.spiller_hoejre_point += 1
            self.spiller_hoejre_pointtavle.text = str(self.spiller_hoejre_point)
        if self.bold.position_x > SKAERMBREDDE:
            self.spiller_venstre_point += 1
            self.spiller_venstre_pointtavle.text = str(self.spiller_venstre_point)
            
        if self.bold.position_x > SKAERMBREDDE:
            self.spiller_venstre_point += 1
        if self.bold.position_x < 0 or self.bold.position_x > SKAERMBREDDE:
            self.reset_bold(self.bold)
            
    def on_draw(self):
        self.clear() # Man kunne også skrive arcade.start_render()
        self.bold.draw()
        self.spiller_venstre.draw()
        self.spiller_hoejre.draw()
        self.spiller_venstre_pointtavle.draw()
        self.spiller_hoejre_pointtavle.draw()

def main():
    vindue = Vindue(SKAERMBREDDE, SKAERMHOEJDE, "PONG")

    arcade.run()

main()
