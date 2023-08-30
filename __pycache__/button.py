import pygame as p
import setting as s
import loadimg as l


# this class define the normal button
class Button:
    isStartGame = False
    def __init__(self, x, y, width, height,type,img, onClickFunction =None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onClickFunction = onClickFunction
        self.img = {
            'normal': img[0],
            'hover': img[1],
            'pressed': img[2],
            'active': img[3]
        }
        self.state = 'normal'
        self.isPress = False
        self.active = False
        self.type = type
    def process(self, screen, gs):
        pos = p.mouse.get_pos()
        if self.type =='re':
            if gs.moveLog ==[]:
                self.state = 'normal'
            else:
                self.state = 'active'
        elif self.type =='ne':
            if gs.store == []:
                self.state = 'normal'
            else:
                self.state = 'active'
        elif self.type =='ex':
            if gs.moveLog ==[]:
                self.state = 'normal'
            else:
                self.state = 'active'
        elif self.type == 'st':
            if gs.moveLog ==[]:
                self.state = 'normal'
            else:
                self.state = 'active'
        elif self.type == 'pa':
            if gs.moveLog !=[]:
                self.state = 'normal'
            else:
                self.state = 'active'      
        if self.state =='active' or self.type =='st' or self.type =='pa' or self.type =='ex':
            if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
                self.state = 'hover'
                if p.mouse.get_pressed()[0] and not self.isPress:
                    self.state = 'pressed'
                    self.isPress =True
                    self.onClickFunction()
                    if self.type == 'st':
                        self.active = True
                        Button.isStartGame = True
                else:
                    self.isPress = False
        if self.type == 'st' and self.active:
            return
        if self.type == 'pa' and self.state == 'active':
            return
        if self.type == 'ex' and self.state == 'active':
            return

        if self.type == 'st' and self.state == 'active':
            return
        if self.state != None:
            
            screen.blit(self.img[self.state], (self.x, self.y))


#this class define a special button like the start game button
class SButton(Button):
    def __init__(self, x, y, width, height,type,img, onClickFunction =None):
        super().__init__( x, y, width, height,type,img, onClickFunction)
    def process(self, screen, gs):
        pos = p.mouse.get_pos()

        if self.type =='ex':
            if gs.moveLog ==[]:
                self.state = 'normal'
            else:
                self.state = 'active'
        elif self.type == 'st':
            if gs.moveLog ==[]:
                self.state = 'normal'
            else:
                self.state = 'active'
        elif self.type == 'pa':
            if gs.moveLog !=[]:
                self.state = 'normal'
            else:
                self.state = 'active'
        if self.state == 'active': return
        
        if self.x <= pos[0] <= self.x + self.width and self.y <= pos[1] <= self.y + self.height:
            self.state = 'hover'
            if p.mouse.get_pressed()[0] and not self.isPress:
                self.state = 'pressed'
                self.isPress =True
                self.onClickFunction()
                if self.type == 'st':
                    self.active = True
                    Button.isStartGame = True
            else:
                self.isPress = False
        if self.state != None:
            screen.blit(self.img[self.state], (self.x, self.y))