
import numpy as np 
import pygame

pygame.init()
class formulas(pygame.sprite.Sprite):
    def __init__(self, deltat=0.1):
        super().__init__()
        self.color = (0, 0, 0)
        self.backcolor = None
        self.pos = (50, 50) 
        self.width = 400
        self.font = pygame.font.SysFont('Times New Roman', 30)
        self.active = False
        self.text = ""
        self.render_text()
        self.g = 0
        self.voX = 0
        self.voY = 0
        self.x = []
        self.y = []
        self.deltat = deltat 
        self.Xo = 0
        self.Yo = 0
        self.t = 60
        self.lista_nw = []
    
    def render_text(self):
        t_surf = self.font.render(self.text, True, self.color, self.backcolor)
        self.image = pygame.Surface((max(self.width, t_surf.get_width()+10), t_surf.get_height()+10), pygame.SRCALPHA)
        if self.backcolor:
            self.image.fill(self.backcolor)
        self.image.blit(t_surf, (5, 5))
        pygame.draw.rect(self.image, self.color, self.image.get_rect().inflate(-2, -2), 2)
        self.rect = self.image.get_rect(topleft = self.pos)

    def mov(self, event_list):
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and not self.active:
                self.active = self.rect.collidepoint(event.pos)
            if event.type == pygame.KEYDOWN and self.active:
                if event.key == pygame.K_RETURN:
                    lista_p = self.text.split(",")
                    for num in range(len(lista_p)):
                        self.lista_nw.append(float(lista_p[num]))
                    print(self.lista_nw)
                    self.g = self.lista_nw[0]
                    self.voX = self.lista_nw[1]
                    self.voY = self.lista_nw[2]
                    for m in np.arange(self.t//self.deltat):
                        vn = self.voY - self.g*self.deltat
                        yn = self.Yo + (self.voY * self.deltat) - (0.5 * self.g * self.deltat**2)
                        if yn<0:#cuando se defina un piso
                            #print("\nEl movimiento termino en {0} segundos".format(m))
                            break
                        self.y.append(600-(yn))
                        self.Yo = yn
                        self.voY = vn
                        xn = self.Xo + self.voX*self.deltat
                        self.x.append(100+(xn))
                        self.Xo = xn
                        self.voX = self.voX
                    return self.x, self.y
                    self.active = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.render_text() 
    
    def parejas(self):
        self.lista_n = []
        for a in range(len(self.x)):
            tupla = (self.x[a],self.y[a])
            self.lista_n.append(tupla)
        return self.lista_n
    
    def __str__(self):
        return "{0}".format(self.lista_n)