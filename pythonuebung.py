import random
#ferris1="@"
#ferris2="T"
class Monster(object):
    def __init__(self,symbol,x,y):
        self.symbol=symbol
        self.x=x
        self.y=y
        
    def dance(self):
        self.x+=random.randint(-1,1)
        self.y+=random.randint(-1,1)
    
    def check(self,xmin=1,xmax=39,ymin=2,ymax=11):
        if self.x<xmin:
            self.x=xmin
        if self.x>xmax:
            self.x=xmax
        if self.y<ymin:
            self.y=ymin
        if self.y>ymax:
            self.y=ymax
        


def blit(screen,monsters):
    """print all monsters on the screen"""
    o=""
    y=0
    for line in screen.splitlines():
        line=list(line)
        for monster in monsters:
            if monster.y==y:
                line[monster.x]=monster.symbol
        # fertig mit monstern
        for char in line:
            o+=char
        o+="\n"  # enter
        y+=1
    return o
    
    

def main():
    print ("hallo welt")
    meinemonster=[ferris,paolo]
    while True:
         paolo.dance()
         paolo.check()
         ferris.check()
         print(blit(s1,meinemonster))
         action=input("hääää?? (wasdq)")
         if action.lower()=="q":
             break
         elif action.lower()=="w":
             ferris.y-=1
         elif action.lower()=="a":
             ferris.x-=1
         elif action.lower()=="d":
             ferris.x+=1
         elif action.lower()=="s":
             ferris.y+=1
         elif action.lower()=="x":
             ferris.dance()
    
    return 0

ferris=Monster("@",12,9)
paolo=Monster("Ö",15,7)
s1="""
+---------------------------------------+
|                                       |
|                                       |
|                                       |
|                                       |
|    B              B            B      |
|   BBBB           BBBB        BBB      |
|  BBBBBB        BBBBBBB      BBBBB     |
|BBBBBBBBBB   BBBBBBBBBBBBBBBBBBBBB   BB|
|BBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBB|
|BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|
+---------------------------------------+
"""

if __name__ == '__main__':
    main()

