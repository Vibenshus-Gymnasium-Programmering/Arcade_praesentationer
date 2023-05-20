# [[file:10_OOP.org::*Sprites][Sprites:1]]
import arcade
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 50
PADDLE_SPEED = 5
BALL_SPEED = 5
BALL_RADIUS = 5


class Paddle(arcade.SpriteSolidColor):
    def __init__(self, center_x, center_y, width, height, color=arcade.color.WHITE):
        super().__init__(width, height, color)
        self.center_x = center_x
        self.center_y = center_y

    def on_update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y


class Ball(arcade.SpriteCircle):
    def __init__(self, center_x, center_y, radius, color=arcade.color.RED):
        super().__init__(radius, color)
        self.center_x = center_x
        self.center_y = center_y

    def reset(self):
        self.position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        angle = random.uniform(0, 1.4)
        sign = random.choice([1.0, -1.0])
        self.change_x = sign * math.cos(angle) * BALL_SPEED
        self.change_y = sign * math.sin(angle) * BALL_SPEED

    def on_update(self, delta_time):
        self.center_x += self.change_x
        self.center_y += self.change_y


class PongGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.paddle_list = None
        self.paddle_left = None
        self.paddle_right = None
        self.ball_list = None
        self.ball = None

    def setup(self):
        self.paddle_list = arcade.SpriteList()
        self.paddle_left = Paddle(
            1.5 * PADDLE_WIDTH, self.height / 2, PADDLE_WIDTH, PADDLE_HEIGHT
        )
        self.paddle_list.append(self.paddle_left)
        self.paddle_right = Paddle(
            self.width - 1.5 * PADDLE_WIDTH,
            self.height / 2,
            PADDLE_WIDTH,
            PADDLE_HEIGHT,
        )
        self.paddle_list.append(self.paddle_right)
        self.ball_list = arcade.SpriteList()
        self.ball = Ball(self.width / 2, self.height / 2, BALL_RADIUS)
        self.ball.reset()
        self.ball_list.append(self.ball)

    def on_update(self, delta_time):
        self.ball_list.on_update()
        self.paddle_list.on_update()

        if self.ball.top > self.height or self.ball.bottom < 0:
            self.ball.change_y *= -1.0

        if self.ball.right < 0 or self.ball.left > self.width:
            self.ball.reset()

        collisions_list = arcade.check_for_collision_with_list(
            self.ball, self.paddle_list
        )
        for paddle in collisions_list:
            change_direction(self.ball, paddle)

    def on_draw(self):
        self.clear()
        self.paddle_list.draw()
        self.ball_list.draw()

    def on_key_press(self, key, _modifiers):
        if key == arcade.key.W:
            self.paddle_left.change_y = PADDLE_SPEED
        elif key == arcade.key.S:
            self.paddle_left.change_y = -PADDLE_SPEED
        if key == arcade.key.UP:
            self.paddle_right.change_y = PADDLE_SPEED
        elif key == arcade.key.DOWN:
            self.paddle_right.change_y = -PADDLE_SPEED

    def on_key_release(self, key, _modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            self.paddle_left.change_y = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.paddle_right.change_y = 0


def change_direction(ball, item):
    if (ball.top > item.bottom and ball.center_y < item.bottom) or (
        ball.bottom < item.top and ball.center_y > item.top
    ):
        ball.change_y *= -1.0
    if (ball.left < item.right and ball.center_x > item.right) or (
        ball.right > item.left and ball.center_x < item.left
    ):
        ball.change_x *= -1.0


def main():
    pong_game = PongGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Pong with sprites")
    pong_game.setup()

    arcade.run()


main()

# Sprites:1 ends here
