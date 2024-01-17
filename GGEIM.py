import arcade,random,time

WIDTH=1600
HEIGHT=800
class Cactys(arcade.Sprite):
    def __init__(self,image):
        super().__init__(image,hit_box_algorithm="Detailed")

class Dino(arcade.Sprite):
    def __init__(self,det):
        super().__init__(det,hit_box_algorithm="Detailed")
        self.textures.append(arcade.load_texture("images/dino2.png"))
        self.textures.append(arcade.load_texture("images/dino3.png"))
        self.texture=self.textures[1]
        self.time=time.time()
        self.fly=False

class Over(arcade.Sprite):
    def __init__(self,image):
        super().__init__(image)

class Window(arcade.Window):
    def __init__(self,ret,ter):
        super().__init__(ret,ter)
        self.bg=arcade.load_texture("images/bg.png")
        self.dino=Dino("images/dino1.png")
        self.dino.set_position(200,250)
        
        self.ser=0
        self.cactys=Cactys("images/cactus1.png")
        self.cactys.set_position(1500,235)
        self.cactys.change_x=7
        self.statys=True
        self.over=Over("Remove-bg.ai_1705505032552.png")
        self.over.center_x=WIDTH/2
        self.over.center_y=HEIGHT/2
    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.statys==False:
            self.statys=True
            self.cactys.center_x=1650+random.randint(0,100)
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.SPACE:
           if self.dino.fly==False:
            self.dino.change_y=15
            self.dino.fly=True
        
        if symbol==arcade.key.R:
           self.statys=True
           self.cactys.center_x=1650+random.randint(0,100)
    def on_draw(self):
        self.clear((200,4,80))
        arcade.draw_texture_rectangle(WIDTH/2,HEIGHT/2,WIDTH,HEIGHT,self.bg)
        self.dino.draw()
        self.cactys.draw()
        self.dino.draw_hit_box()
        self.cactys.draw_hit_box()
        if self.statys==False:
            arcade.draw_texture_rectangle(WIDTH/2,HEIGHT/2,WIDTH,HEIGHT,arcade.load_texture("images/game_over.png"))
            self.over.draw()

    def update(self,delta_time):
        if self.statys==True:
            if time.time()-self.dino.time>0.2:
                self.dino.time=time.time()
                self.dino.texture=self.dino.textures[self.ser]
                self.ser+=1
                if self.ser==3:
                    self.ser=0
               
                    

        
            self.cactys.center_x-=self.cactys.change_x
            if self.cactys.center_x<-50:
                self.cactys.center_x=1650+random.randint(0,100)
            self.dino.center_y+=self.dino.change_y
            if self.dino.center_y<250:
                self.dino.center_y=250
                self.dino.fly=False
            self.dino.change_y-=0.5
            

            hit=arcade.check_for_collision(self.dino,self.cactys)
            if hit==True:
                self.statys=False
            print(self.dino.fly)

game=Window(WIDTH,HEIGHT)
arcade.run()