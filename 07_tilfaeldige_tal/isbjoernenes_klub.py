import arcade
import arcade.key
import arcade.csscolor
import random

# Størrelsen på øjnene skaleres desværre ikke efter
class Terning:
    def __init__(self, x, y, size = 100):
        self.x = x
        self.y = y
        self.size = size
        self.dot_size = self.size // 10 if self.size // 10 else 1
        self.side = 6
        self.slaa()

    def _tegn_baggrund(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.size, self.size, arcade.csscolor.WHITE)
   
    def _tegn_1(self):
        arcade.draw_circle_filled(self.x, self.y, self.dot_size, arcade.csscolor.BLACK)

    def _tegn_2(self):
        arcade.draw_circle_filled(self.x-self.size*2/7, self.y+self.size*2/7, self.dot_size, arcade.csscolor.BLACK)
        arcade.draw_circle_filled(self.x+self.size*2/7, self.y-self.size*2/7, self.dot_size, arcade.csscolor.BLACK)

    def _tegn_3(self):
        self._tegn_1()
        self._tegn_2()

    def _tegn_4(self):
        self._tegn_2()
        arcade.draw_circle_filled(self.x+self.size*2/7, self.y+self.size*2/7, self.dot_size, arcade.csscolor.BLACK)
        arcade.draw_circle_filled(self.x-self.size*2/7, self.y-self.size*2/7, self.dot_size, arcade.csscolor.BLACK)
        
    def _tegn_5(self):
        self._tegn_4()
        self._tegn_1()

    def _tegn_6(self):
        self._tegn_4()
        arcade.draw_circle_filled(self.x+self.size*2/7, self.y, self.dot_size, arcade.csscolor.BLACK)
        arcade.draw_circle_filled(self.x-self.size*2/7, self.y, self.dot_size, arcade.csscolor.BLACK)
        
    def _tegn_centrum(self):
        arcade.draw_circle_filled(self.x, self.y, 5, arcade.csscolor.RED)
    def slaa(self):
        self.side = random.randint(1, 6)
    def vis_side(self):
        self._tegn_baggrund()
        # I stedet for en lang række med if og elif bruges udnyttes her et dictionary
        muligheder = {1: self._tegn_1, 2: self._tegn_2, 3: self._tegn_3, 4: self._tegn_4, 5:self._tegn_5, 6:self._tegn_6}
        muligheder[self.side]()
        
class Main_window(arcade.Window):
    def __init__(self, bredde, hoejde, titel):
        super().__init__(bredde, hoejde, titel)
        arcade.set_background_color(arcade.csscolor.BLUE)

        self.antal_rul = 1

        self.terninger = list()
        for j in range(2):
            for i in range(5):
                # Størrelse og placering af terninger er hardcoded til vinduets størrelse
                self.terninger.append(Terning(150+i*2*100,(j + 1) * 150, 100))

        # Liste til senere nemmere opdatering
        self.tekstelementer = list()

        # Overskriften
        self.tekst = arcade.Text("Hvor mange isbjørne er der her?", 200, self.height - 100, font_size = 24)
        self.tekst.anchor_x = "center"
        self.tekst.x = self.width / 2

        self.tekstelementer.append(self.tekst)

        # Viser antallet af rul
        self.antal_rul_tekst = arcade.Text(f"Antal rul = {self.antal_rul}", 200, self.height - 150, font_size = 24)
        self.antal_rul_tekst.anchor_x = "center"
        self.antal_rul_tekst.x = self.width / 2
        
        self.tekstelementer.append(self.antal_rul_tekst)

        # Info om Q
        self.key_info_q = arcade.Text("Q: Luk", 20, 20, font_size = 18)
        self.tekstelementer.append(self.key_info_q)
        # Info om SPACE
        self.key_info_space = arcade.Text("SPACE: Rul igen", self.width - 20, 20, font_size = 18)
        self.key_info_space.anchor_x = "right"
        self.tekstelementer.append(self.key_info_space)

    def on_draw(self):
        arcade.start_render()
        # Tegner teksten
        for tekst in self.tekstelementer:
            tekst.draw()
        # Tegner terningerne
        for terning in self.terninger:
            terning.vis_side()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.antal_rul += 1
            self.antal_rul_tekst.text = f"Antal rul = {self.antal_rul}"
            for terning in self.terninger:
                terning.slaa()
            
        elif key == arcade.key.Q:
            self.close()
def main():
    main_window = Main_window(1100, 600, "Isbjørnenes klub")
    arcade.run()

main()
