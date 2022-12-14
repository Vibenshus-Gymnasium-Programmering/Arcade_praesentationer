# [[file:10_OOP.org::*Så styr dog den bold - med keyboardet][Så styr dog den bold - med keyboardet:1]]
import arcade

SKAERMBREDDE = 640
SKAERMHOEJDE = 480
BOLDHASTIGHED = 3
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

    def draw(self):
        """ Tegner bolden som en simpel udfyldt cirkel vha arcade. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.farve)

class Vindue(arcade.Window):
    """ Vores nye vinduesklasse. """

    def __init__(self, bredde, hoejde, titel):
        """ Initialisator. """

        # Call the parent class's init function
        # Kalder forældreklasse(n/rnes) initialisatorer
        super().__init__(bredde, hoejde, titel)
        # Sætter baggrundsfarven én gang
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.setup()

    def setup(self):
        self.bold = Bold(100, 200, 0, 0, 5, arcade.csscolor.RED)

    def on_key_press(self, tast, modifikationstast):
        """ Kørers når brugeren trykker på en tast. """
        if tast == arcade.key.LEFT:
            self.bold.hastighed_x = - BOLDHASTIGHED
        elif tast == arcade.key.RIGHT:
            self.bold.hastighed_x = BOLDHASTIGHED
        elif tast == arcade.key.UP:
            self.bold.hastighed_y = BOLDHASTIGHED
        elif tast == arcade.key.DOWN:
            self.bold.hastighed_y = - BOLDHASTIGHED

    def on_key_release(self, tast, modifikationstast):
        """ Kørers når brugeren slipper en tast. """
        if tast == arcade.key.LEFT or tast == arcade.key.RIGHT:
            self.bold.hastighed_x = 0
        elif tast == arcade.key.UP or tast == arcade.key.DOWN:
            self.bold.hastighed_y = 0
            
    def update(self, delta_tid):
        self.bold.update()
        
    def on_draw(self):
        self.clear() # Man kunne også skrive arcade.start_render()
        self.bold.draw()

def main():
    vindue = Vindue(SKAERMBREDDE, SKAERMHOEJDE, "En bold styret med keyboardet")

    arcade.run()

main()
# Så styr dog den bold - med keyboardet:1 ends here
