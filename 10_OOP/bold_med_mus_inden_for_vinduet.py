# [[file:10_OOP.org::*Så styr dog den bold - med musen][Så styr dog den bold - med musen:1]]
import arcade

SKAERMBREDDE = 640
SKAERMHOEJDE = 480
BOLDHASTIGHED = 3


class Bold:
    """Denne klasse beskriver/styrer en bold, som hopper i vinduet på skærmen."""

    def __init__(self, position_x, position_y, hastighed_x, hastighed_y, radius, farve):
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.farve = farve

    def draw(self):
        """Tegner bolden som en simpel udfyldt cirkel vha arcade."""
        arcade.draw_circle_filled(
            self.position_x, self.position_y, self.radius, self.farve
        )


class Vindue(arcade.Window):
    """Vores nye vinduesklasse."""

    def __init__(self, bredde, hoejde, titel):
        """Initialisator."""

        # Call the parent class's init function
        # Kalder forældreklasse(n/rnes) initialisatorer
        super().__init__(bredde, hoejde, titel)
        # Sætter baggrundsfarven én gang
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.set_mouse_visible(False)
        self.setup()

    def setup(self):
        self.bold = Bold(self.width / 2, 25, 0, 0, 5, arcade.csscolor.RED)

    def on_mouse_motion(self, x, y, _botton, _modifiers):
        if x > self.bold.radius and x < self.width - self.bold.radius:
            self.bold.position_x = x
        if y > self.bold.radius and y < self.height - self.bold.radius:
            self.bold.position_y = y

    def on_draw(self):
        self.clear()  # Man kunne også skrive arcade.start_render()
        self.bold.draw()


def main():
    vindue = Vindue(SKAERMBREDDE, SKAERMHOEJDE, "En bold styret med musen")

    arcade.run()


main()
# Så styr dog den bold - med musen:1 ends here
