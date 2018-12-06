import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.y = pyxel.height / 2
        self.vy = 8
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_A):
            self.x = (self.x - 1) % pyxel.width
        if pyxel.btn(pyxel.KEY_D):
            self.x = (self.x + 1) % pyxel.width
        if pyxel.btn(pyxel.KEY_W):
            self.y -= 1
            self.vy = -8

        if self.y < pyxel.height / 2:
            self.y += self.vy
        else:
            self.y = pyxel.height / 2

        if self.vy <= 8:
            self.vy += 1
        print(self.vy)
        print(self.y)

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, self.x + 7, self.y + 7, 9)

App()
