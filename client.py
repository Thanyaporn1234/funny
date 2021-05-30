import pygame
from network import Network
pygame.font.init()
import os

width = 500
height = 500
n = Network()
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Game")

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "BG.jpg")), (width, height))
BG_wait = pygame.transform.scale(pygame.image.load(os.path.join("assets", "gameBG.jpg")), (width, height))

# Player player
bird1 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "b1.png")), (100,80))
bird2 = pygame.transform.scale(pygame.image.load(os.path.join("assets", "b3.png")), (100,80))

class Player():
    def __init__(self,x,y,width,height,image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = (x,y,width,height)
        self.vel = 3
        self.ready = False 
        self.image = image
        
       
        
    def draw(self,win):
        win.blit(self.image, (self.x, self.y))
        #pygame.draw.rect(win, self.color , self.rect)
 
        
    def move(self):
        self.x += self.vel
        self.update()
        
            
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
        
    def get_width(self):
        return self.image.get_width()
        
    
    
        
def read_pos(str):
    str = str.split(",")
    return int(str[0]) , int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def read_check(str):
    if str == "True":
        return True
    else:
        return False
               
def redrawWindow(win,player,player2):
    win.blit(BG_wait, (0,0))

    if not(player.ready and player2.ready):
        wait = pygame.transform.scale(pygame.image.load(os.path.join("assets", "waiting.png")), (300,250))
        win.blit(wait, (width/2 - wait.get_width()/2, height/2 - wait.get_height()/2))
    else:
        player.draw(win)
        player2.draw(win)
        
    pygame.display.update()
    
def main():
    run = True
    startPos = read_pos(n.getPos())
    p = Player(startPos[0],startPos[1],100,100,bird1)
    p2 = Player(0,0,100,100,bird2)
    p.ready = True
    clock = pygame.time.Clock()
    print("Hellooo")
    print(n.getP())
   

    while run:
        clock.tick(60)
        p2.ready = read_check(n.send(str(p.ready)))
        p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    p.move()
        redrawWindow(win ,p , p2)
        
        #มันยังรันไม่ออกตรงนี้แต่มันไม่แอเร่อ พยยจะทำเส้นชัยแต่ไม่ออกงับ
        if p.x + p.get_width() > width: 
            font = pygame.font.SysFont("comicsans", 60)
            u_win = font.render("You're Winner.", 1, (255,0,0))
            win.blit(u_win, (100,200))
        elif p2.x + p2.get_width() > width:
            font = pygame.font.SysFont("comicsans", 60)
            u_win1 = font.render("You're Winner.", 1, (255,0,0))
            win.blit(u_win1, (100,200))    
        


def menu():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.blit(BG, (0,0))
        font = pygame.font.SysFont("comicsans", 60)
        start = pygame.image.load(os.path.join("assets", "start.png"))
        win.blit(start, (10,70))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False                  
    main()
        

while True:
    menu()