import pygame
from pygame.locals import *

pygame.init()
infoObject = pygame.display.Info()
ekran = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("devre")
font = pygame.font.Font(None, 16)

# görseller
çıkışgörsel = font.render("x", True, (0, 0, 0))
vegörsel = pygame.image.load("and.png").convert_alpha()
notgörsel = pygame.image.load("not.png").convert_alpha()
norgörsel =pygame.image.load("nor.png").convert_alpha()
orgörsel = pygame.image.load("or.png").convert_alpha()
nandgörsel = pygame.image.load("nand.png").convert_alpha()
buffgörsel = pygame.image.load("buffer.png").convert_alpha()
xorgörsel = pygame.image.load("xor.png").convert_alpha()
xnorgörsel = pygame.image.load("xnor.png").convert_alpha()
giriş0görsel = pygame.Surface((30, 20))
giriş1görsel = pygame.Surface((30, 20))
giriş0görsel.fill((255, 255, 255))
giriş1görsel.fill((0, 0, 0))
sayı0 = font.render("0", True, (0, 0, 0))
sayı1 = font.render("1", True, (255, 255, 255))
alan0 = sayı0.get_rect(center=(10, 10))
alan1 = sayı1.get_rect(center=(10, 10))
giriş0görsel.blit(sayı0, alan0)
giriş1görsel.blit(sayı1, alan1)
led1görsel = pygame.Surface((30, 20))
led0görsel = pygame.Surface((30, 20))
led1görsel.fill((255, 255, 0))
led0görsel.fill((128, 128, 128))

mousex, mousey = 0, 0
seç = ""
soltık = False
sağtık = False
downx, downy = 0, 0
kapıindex = 0
ilkindex = ""
sonindex = ""
çıkışindex, girişindex = "", ""
simulasyon_çalıştır = False

#kapı sınıfları
class kapı:
    def __init__(self):
        self.x = mousex - 25
        self.y = mousey - 25
        self.type = seç
        self.index = kapıindex
        self.kapı_durum = 0

class andkapı(kapı):
    def __init__(self):
        super().__init__()
        self.çıkışlar = [["free", 25, 10]]
        self.girişler = [["free", 0, 10], ["free",0,10]]

    def draw(self):
        ekran.blit(vegörsel, (self.x, self.y))

    def checkOn(self):
        kapı_durum = 0
        for i in kabloList:
            if i.sonindex == self.index:
                if i.kapı_durum == 1:
                    kapı_durum += 1
        return kapı_durum == 2

class nandkapı(kapı):
    def __init__(self):
        super().__init__()
        self.çıkışlar = [["free", 25, 10]]
        self.girişler = [["free",0,10], ["free",0,10]]

    def draw(self):
        ekran.blit(nandgörsel, (self.x, self.y))  # Ekrana vegörsel'i çiz

    def checkOn(self):
        kapı_durum = 0  # Geçici sayaç değişkeni
        for i in kabloList:
            if i.sonindex == self.index:  # Eğer bir tel bu kapıda bitiyorsa
                if i.kapı_durum == 1:
                    kapı_durum += 1  # Eğer telin durumu 1 ise, kapı_durum'e ekle
        if kapı_durum == 2:
            return False  
        else:
            return True  
        
class xorkapı(kapı):
    def __init__(self):
        super().__init__()
        self.çıkışlar = [["free", 25, 10]]
        self.girişler = [["free",0,10], ["free",0,10]]

    def draw(self):
        ekran.blit(xorgörsel, (self.x, self.y))  # Ekrana vegörsel'i çiz

    def checkOn(self):
        kapı_durum = 0  # Geçici sayaç değişkeni
        for i in kabloList:
            if i.sonindex == self.index:  # Eğer bir tel bu kapıda bitiyorsa
                if i.kapı_durum == 1:
                    kapı_durum += 1  # Eğer telin durumu 1 ise, kapı_durum'e ekle
        if kapı_durum == 1:
            return True  
        else:
            return False  
        
class xnorkapı(kapı):
    def __init__(self):
        super().__init__()
        self.çıkışlar = [["free", 25, 10]]
        self.girişler = [["free",0,10], ["free",0,10]]

    def draw(self):
        ekran.blit(xnorgörsel, (self.x, self.y))  # Ekrana vegörsel'i çiz

    def checkOn(self):
        kapı_durum = 0  # Geçici sayaç değişkeni
        for i in kabloList:
            if i.sonindex == self.index:  # Eğer bir tel bu kapıda bitiyorsa
                if i.kapı_durum == 1:
                    kapı_durum += 1  # Eğer telin durumu 1 ise, kapı_durum'e ekle
        if kapı_durum == 0 or kapı_durum==2:
            return True  
        else:
            return False 
        
class notkapı(kapı):
    def __init__(self):
        kapı.__init__(self)
        self.çıkışlar=[["free", 25, 10],["Full",0,0]]
        self.girişler=[["free",0,10]]
    def draw(self):
        ekran.blit(notgörsel,(self.x,self.y))
    def checkOn(self):
        kapı_durum = 0
        for i in kabloList:
            if i.sonindex==self.index:
                if i.kapı_durum==1:
                    return False
                else:
                    return True

class Norkapı(kapı):
    def __init__(self):
        kapı.__init__(self)
        self.çıkışlar = [["free", 25, 10]]
        self.girişler = [["free",0,10], ["free",0,10]]
    def draw(self):
        ekran.blit(norgörsel,(self.x,self.y))
    def checkOn(self):
        kapı_durum=0
        for i in kabloList:
            if i.sonindex==self.index:
                if i.kapı_durum==1:
                    kapı_durum+=1
        if kapı_durum>=1:
            return False
        else:
            return True
        
class orkapı(kapı):
    def __init__(self):
        kapı.__init__(self)
        self.çıkışlar = [["free", 25, 10]]
        self.girişler = [["free",0,10], ["free",0,10]]
    def draw(self):
        ekran.blit(orgörsel,(self.x,self.y))
    def checkOn(self):
        kapı_durum=0
        for i in kabloList:
            if i.sonindex==self.index:
                if i.kapı_durum==1:
                    kapı_durum+=1
        if kapı_durum>=1:
            return True
        else:
            return False
        
class bufferkapı(kapı):
    def __init__(self):
        kapı.__init__(self)
        self.çıkışlar = [["free", 5, 10]]
        self.girişler = [["free",0,10], ["free",0,10]]
    def draw(self):
        ekran.blit(buffgörsel,(self.x,self.y))
    def checkOn(self):
        kapı_durum=0
        for i in kabloList:
            if i.sonindex==self.index:
                if i.kapı_durum==1:
                    return True
                else:
                    return False
                
class çıkışkapı(kapı):
    def __init__(self):
        kapı.__init__(self)
        self.çıkışlar = [["Full", 0, 0]]
        self.girişler = [["free",0,10]]
        self.bağlantı = False 

    def draw(self):
        giriş_kapı_durumu = None 

        for i in kabloList:
            if i.sonindex == self.index:
                self.bağlantı = True
                giriş_kapı_durumu = i.kapı_durum
                break
        else:
            self.bağlantı = False

        # Bağlı değilse 'X' yazdır
        if not self.bağlantı:
            x_surface = font.render("X", True, (0, 0, 0))  # X'i siyah renkte render edin
            ekran.blit(x_surface, (self.x + 2, self.y + 2))
            return

        # Bağlı ve giriş durumu varsa 0 veya 1 yazdır
        if giriş_kapı_durumu is not None:
            if giriş_kapı_durumu == 1:
                ekran.blit(giriş1görsel, (self.x , self.y))
            else:
                ekran.blit(giriş0görsel, (self.x , self.y))
                
class düğme(kapı):
    def __init__(self):
        kapı.__init__(self)
        self.çıkışlar = [["free", 20, 10], ["Full", 0, 0]]
        self.girişler = [["Full", 15,15 ]]
        self.kapı_durum = 0

    def draw(self):
        if self.kapı_durum == 1:
            ekran.blit(giriş1görsel, (self.x, self.y))
        else:
            ekran.blit(giriş0görsel, (self.x, self.y))

    def checkOn(self):
        if self.kapı_durum == 1:
            return True
        else:
            return False

class led(kapı):
    def __init__(self):
        kapı.__init__(self)
        self.çıkışlar = [["Full", 0, 0]]
        self.girişler = [["free",0,10]]

    def draw(self):
        for i in kabloList:
            if i.sonindex == self.index and i.kapı_durum == 1:
                ekran.blit(led1görsel, (self.x, self.y))
                return
        ekran.blit(led0görsel, (self.x, self.y))

class düğüm:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.index = kapıindex
        self.kapı_durum = 0
        self.girişler = [["free",0,0]]
        self.çıkışlar = [["free",0,0]]

    def draw(self):
        pygame.draw.circle(ekran, (0, 0, 0), (self.x, self.y), 5)
        if self.kapı_durum == 1:
            pygame.draw.circle(ekran, (0, 255, 0), (self.x, self.y), 3)
        else:
            pygame.draw.circle(ekran, (255, 0, 0), (self.x, self.y), 3)

    def checkOn(self):
        for i in kabloList:
            if i.sonindex == self.index:
                if i.kapı_durum == 1:
                    return True
        return False

class kablo:
    def __init__(self, ilk_x, ilk_y, endx, endy):
        self.ilk_x = ilk_x
        self.ilk_y = ilk_y
        self.endx = endx
        self.endy = endy
        self.ilkindex = ilkindex
        self.sonindex = sonindex
        self.kapı_durum = 0

    def draw(self):
        if self.kapı_durum == 0:
            pygame.draw.line(ekran, (0, 0, 0), (self.ilk_x, self.ilk_y), (self.endx, self.endy), 4)
            pygame.draw.line(ekran, (255, 255, 255), (self.ilk_x, self.ilk_y), (self.endx, self.endy), 2)
        else:
            pygame.draw.line(ekran, (0, 0, 0), (self.ilk_x, self.ilk_y), (self.endx, self.endy), 4)
            pygame.draw.line(ekran, (0, 255, 0), (self.ilk_x, self.ilk_y), (self.endx, self.endy), 2)

        for i in kapıList:
            if i.index == self.ilkindex:
                self.kapı_durum = i.checkOn()

# Initialize lists
kapıList = []
kabloList = []
kapılistkopya, kaplolistkopya = [], []

def collide(checkx, checky, x, y, w, h):
    return x < checkx < x + w and y < checky < y + h

def menu():
    global seç, kapıList, kabloList, kapılistkopya, kaplolistkopya, ekran

    font = pygame.font.Font(None, 16)
    buton_en = 80
    buton_yükseklik = 30
    buton_buşluk = 20

    buton_x = 20
    buton_y = 20
    buton_sayı = 14

    for i in range(buton_sayı):
        butonlar = ["AND", "not","or","nor","xor","xnor","nand","buff","düğme","çıkış", "led", "kablolar", "düğüm", "Mouse"][i]
        buton_yüzeyi = font.render(butonlar, True, (0, 0, 0))
        buton_alan = pygame.Rect(buton_x, buton_y, buton_en, buton_yükseklik)

        if buton_alan.collidepoint(mousex, mousey):
            pygame.draw.rect(ekran, (150, 150, 150), buton_alan)
        else:
            pygame.draw.rect(ekran, (200, 200, 200), buton_alan)

        text_x = buton_alan.centerx - buton_yüzeyi.get_width() // 2
        text_y = buton_alan.centery - buton_yüzeyi.get_height() // 2
        ekran.blit(buton_yüzeyi, (text_x, text_y))

        if soltık and buton_alan.collidepoint(mousex, mousey):
            seç = butonlar.lower()

        buton_x += buton_en + buton_buşluk

    if seç == "and":
        ekran.blit(vegörsel, (mousex-25, mousey-25))
    elif seç == "nand":
        ekran.blit(nandgörsel, (mousex-25, mousey-25))
    elif seç == "not":
        ekran.blit(notgörsel, (mousex-25, mousey-25))
    elif seç == "xor":
        ekran.blit(xorgörsel, (mousex-25, mousey-25))
    elif seç == "xnor":
        ekran.blit(xnorgörsel, (mousex-25, mousey-25))
    elif seç == "or":
        ekran.blit(orgörsel, (mousex-25, mousey-25))
    elif seç == "nor":
        ekran.blit(norgörsel, (mousex-25, mousey-25))
    elif seç == "buff":
        ekran.blit(buffgörsel, (mousex-25, mousey-25))
    elif seç == "düğme":
        ekran.blit(giriş0görsel, (mousex-25, mousey-25))
    elif seç == "led":
        ekran.blit(led0görsel, (mousex-25, mousey-25))
    elif seç == "çıkış":
        ekran.blit(çıkışgörsel, (mousex-25, mousey-25))
    elif seç == "düğüm":
        pygame.draw.circle(ekran, (0, 0, 0), (mousex, mousey), 5)
    if seç == "and" and sağtık:
        print("ve doğruluk tablosu \n"
                   "| A | B | çıkış |\n" 
                   "---------------\n" 
                   "| 0 | 0 | 0   |\n" 
                   "| 0 | 1 | 0   |\n" 
                   "| 1 | 0 | 0   |\n" 
                   "| 1 | 1 | 1   |\n" 
                   "---------------")
    elif seç == "nand"and sağtık:
                print("nand doğruluk tablosu \n"
                   "| A | B | çıkış |\n"
                   "---------------\n" 
                   "| 0 | 0 | 1   |\n" 
                   "| 0 | 1 | 1   |\n" 
                   "| 1 | 0 | 1   |\n" 
                   "| 1 | 1 | 0   |\n" 
                   "---------------")
    elif seç == "not"and sağtık:
                print("not doğruluk tablosu \n"
                   "| A | çıkış|\n" 
                   "------------\n"
                   "| 0 | 1    |\n" 
                   "| 1 | 0    |\n" 
                   "------------")
    elif seç == "xor"and sağtık:
                print("xor doğruluk tablosu \n"
                   "| A | B | çıkış |\n" 
                   "---------------\n" 
                   "| 0 | 0 | 0   |\n" 
                   "| 0 | 1 | 1   |\n" 
                   "| 1 | 0 | 1   |\n" 
                   "| 1 | 1 | 0   |\n" 
                   "---------------")
    elif seç == "xnor"and sağtık:
        print("xnor doğruluk tablosu \n"
                   "| A | B | çıkış |\n" 
                   "---------------\n" 
                   "| 0 | 0 | 1   |\n" 
                   "| 0 | 1 | 0   |\n" 
                   "| 1 | 0 | 0   |\n" 
                   "| 1 | 1 | 1   |\n" 
                   "---------------")
    elif seç == "or"and sağtık:
        print("or doğruluk tablosu \n"
                   "| A | B | çıkış |\n" 
                   "---------------\n" 
                   "| 0 | 0 | 0   |\n" 
                   "| 0 | 1 | 1   |\n" 
                   "| 1 | 0 | 1   |\n" 
                   "| 1 | 1 | 1   |\n" 
                   "---------------")
    elif seç == "nor"and sağtık:
        print("nor doğruluk tablosu \n"
                   "| A | B | çıkış |\n" 
                   "---------------\n" 
                   "| 0 | 0 | 1   |\n" 
                   "| 0 | 1 | 0   |\n" 
                   "| 1 | 0 | 0   |\n" 
                   "| 1 | 1 | 0   |\n" 
                   "---------------")
    elif seç == "buff"and sağtık:
        print("buffer doğruluk tablosu \n"
                   "| A | çıkış|\n" 
                   "------------\n"
                   "| 1 | 1    |\n" 
                   "| 0 | 0    |\n" 
                   "------------")
    sim_butunlar = [("Çalıştır", (20, 70)), ("Reset", (120, 70)), ("Durdur", (220, 70))]

    for text, poz in sim_butunlar:
        buton_alan = pygame.Rect(poz[0], poz[1], buton_en, buton_yükseklik)
        buton_yüzeyi = font.render(text, True, (0, 0, 0))

        if buton_alan.collidepoint(mousex, mousey):
            pygame.draw.rect(ekran, (150, 150, 150), buton_alan)
        else:
            pygame.draw.rect(ekran, (200, 200, 200), buton_alan)

        text_x = buton_alan.centerx - buton_yüzeyi.get_width() // 2
        text_y = buton_alan.centery - buton_yüzeyi.get_height() // 2
        ekran.blit(buton_yüzeyi, (text_x, text_y))

        if soltık and buton_alan.collidepoint(mousex, mousey):
            if text == "Çalıştır":
                sim_çalıştır()
            elif text == "Reset":
                sim_reset()
            elif text == "Durdur":
                sim_durdur()

def sim_çalıştır():
    global simulasyon_çalıştır, kapılistkopya, kaplolistkopya
    simulasyon_çalıştır = True
    kapılistkopya = [kapı for kapı in kapıList]
    kaplolistkopya = [kablo for kablo in kabloList]

def sim_durdur():
    global simulasyon_çalıştır
    simulasyon_çalıştır = False

def sim_reset():
    global kapıList, kabloList, kapılistkopya, kaplolistkopya, simulasyon_çalıştır
    kapıList = kapılistkopya.copy()
    kabloList = kaplolistkopya.copy()
    simulasyon_çalıştır = False

def öğeyerleştir():
    global kapıindex, ilkindex, sonindex, çıkışindex, girişindex, kapıList, kabloList
    for i in kapıList:
        pygame.draw.rect(ekran, (0, 0, 0), (i.x, i.y, 30,20), 1)

    if soltık and mousey > 110:
        if seç == "and":
            kapıList.append(andkapı())
            kapıindex += 1
        elif seç == "not":
            kapıList.append(notkapı())
            kapıindex += 1
        elif seç == "nand":
            kapıList.append(nandkapı())
            kapıindex += 1
        elif seç == "or":
            kapıList.append(orkapı())
            kapıindex += 1
        elif seç == "xor":
            kapıList.append(xorkapı())
            kapıindex += 1
        elif seç == "xnor":
            kapıList.append(xnorkapı())
            kapıindex += 1
        elif seç == "nor":
            kapıList.append(Norkapı())
            kapıindex += 1
        elif seç == "buff":
            kapıList.append(bufferkapı())
            kapıindex += 1
        elif seç == "düğme":
            kapıList.append(düğme())
            kapıindex += 1
        elif seç == "led":
            kapıList.append(led())
            kapıindex += 1
        elif seç == "çıkış":
            kapıList.append(çıkışkapı())
            kapıindex += 1
        elif seç == "düğüm":
            kapıList.append(düğüm(mousex, mousey))
            kapıindex += 1
        elif seç == "mouse":
            for i in kapıList:
                if collide(mousex, mousey, i.x, i.y, 50, 50):
                    i.kapı_durum = not i.kapı_durum


def kabloyerleştir():
    global ilkindex, sonindex, çıkışindex, girişindex, kabloList, kapıList

    if seç == "kablolar":
        if soltık:
            if ilkindex == "":
                for i in kapıList:
                    if collide(mousex, mousey, i.x, i.y, 50, 50):
                        çıkışindex = 0
                        ilkindex = i.index
            else:
                for i in kapıList:
                    if collide(mousex, mousey, i.x, i.y, 50, 50):
                        giriş_sayı = 0
                        for giriş in i.girişler:
                            if giriş[0] == "free":
                                girişindex = giriş_sayı
                                sonindex = i.index
                            giriş_sayı += 1

                if sonindex != "":
                    isayı = 0
                    for i in kapıList:
                        if i.index == ilkindex:
                            tsayısı = 0
                            for t in kapıList:
                                if t.index == sonindex:
                                    kabloList.append(kablo(kapıList[isayı].x + kapıList[isayı].çıkışlar[çıkışindex][1], kapıList[isayı].y + kapıList[isayı].çıkışlar[çıkışindex][2], kapıList[tsayısı].x + kapıList[tsayısı].girişler[girişindex][1], kapıList[tsayısı].y + kapıList[tsayısı].girişler[girişindex][2]))
                                    ilkindex = ""
                                    sonindex = ""
                                    çıkışindex = ""
                                    girişindex = ""
                                    return
                                tsayısı += 1
                        isayı += 1

        if ilkindex != "":
            sayı = 0
            for i in kapıList:
                if i.index == ilkindex:
                    pygame.draw.line(ekran, (0, 0, 0), (kapıList[sayı].x + kapıList[sayı].çıkışlar[çıkışindex][1], kapıList[sayı].y + kapıList[sayı].çıkışlar[çıkışindex][2]), (mousex, mousey), 4)
                    pygame.draw.line(ekran, (255, 255, 255), (kapıList[sayı].x + kapıList[sayı].çıkışlar[çıkışindex][1], kapıList[sayı].y + kapıList[sayı].çıkışlar[çıkışindex][2]), (mousex, mousey), 2)
                sayı += 1
    else:
        ilkindex = ""
        sonindex = ""


def nesneler():
    for i in kabloList:
        i.draw()
    for i in kapıList:
        i.draw()

son_x, son_y = 0, 0


while True:
    ekran.fill((255, 255, 255))
    nesneler()
    menu()
    if not simulasyon_çalıştır:
        öğeyerleştir()
        kabloyerleştir()
    else:
        pass

    soltık = False
    sağtık = False
    son_x, son_y = mousex, mousey
 

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEMOTION:
            mousex, mousey = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            mousex, mousey = event.pos
            if event.button == 1:
                soltık = True
            elif event.button == 3:
                sağtık = True
            mouseDown = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
            downx, downy = event.pos
    pygame.display.update()