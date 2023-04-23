from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
chosenBlock = 1
def update():
    class Sky(Entity):
        def __init__(self):
         super().__init__(
        parent=scene,
        model="sphere",
        texture="sky_default",
        scale=150,
            )
    global chosenBlock
    if held_keys["1"]:
        chosenBlock = 1
        print("beyaz seçildi")

    if held_keys["2"]:
        chosenBlock = 2
        print("çimen renk seçildi")
    if held_keys["3"]:
        chosenBlock = 2
        print("taş seçildi")


class Block(Button):
    def __init__(self, position=(0, 0, 0), texture="grass"):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            texture=texture,
            color=color.white,
            origin_y=.5,
            highlight_color=color.lime)

    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                if chosenBlock == 1:
                    block = Block(position=self.position + mouse.normal, texture="white_cube")
                if chosenBlock == 2:
                    block = Block(position=self.position + mouse.normal, texture="grass")

                if chosenBlock == 3:
                    block = Block(position=self.position + mouse.normal, texture="blue_cube")

            if chosenBlock == 4:
                block = Block(position=self.position + mouse.normal, texture="pink_cube")
            if key == "left mouse down":
                destroy(self)


app = Ursina()
sky = Sky()
player = FirstPersonController()
for x in range(30):
    for y in range(30):
        block = Block(position=(x, 0, y))
app.run()