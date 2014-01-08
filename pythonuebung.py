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
    
    def check(self, xmax,ymax,xmin=1,ymin=2):
        if self.x<xmin:
            self.x=xmin
        if self.x>xmax:
            self.x=xmax
        if self.y<ymin:
            self.y=ymin
        if self.y>ymax:
            self.y=ymax
        
def get(screen,x,y):
    """return the char at x,y"""
    lines=screen.splitlines()
    char=lines[y][x]
    return char
    
def get_level_size(screen):
    """return xmax,ymax"""
    lines=screen.splitlines()
    xmax=len(lines[1])
    ymax=len(lines)
    print(xmax,ymax)
    return xmax-2,ymax-2    

def blit(screen,monsters):
    """print all monsters on the screen"""
    output=""
    y=0
    for line in screen.splitlines():
        line=list(line)
        for monster in monsters:
            if monster.y==y:
                line[monster.x]=monster.symbol
        # fertig mit monstern
        for char in line:
            output+=char
        output+="\n"  # enter
        y+=1
    return output
    
def generate_level():
    width=random.randint(10,80)
    height=random.randint(10,20)
    y=0
    level=""
    line=" "*width
    while y<height:
        y+=1
        x=0
        level+="\n"
        line=level.splitlines()[-1]
        while x<width:
            x+=1
           
            chance=0.1
            print("line:",line)
            if len(line)>x and line[x]!=" ":
                chance=0.75
            if len(line)>2:
                if x >1 and line[x-1]!=" ":
                    chance+=0.1
                if len(line) > x+1 and line[x+1]!=" ":
                    chance+=0.1
            if random.random()<chance:
                level+="B"
            else:
                level+=" "
    return level

    

def main():
    actual=0
    print ("hallo welt")
    meinemonster=[ferris,paolo]
    while True:
         paolo.dance()
         xmax,ymax=get_level_size(levels[actual])
         paolo.check(xmax,ymax)
         ferris.check(xmax,ymax)
         char= get(levels[actual],ferris.x,ferris.y)
         if char=="n":
            actual+=1
            print("next level")
         elif char=="p":
              actual-=1
         xmax,ymax=get_level_size(levels[actual])
         paolo.check(xmax,ymax)
         ferris.check(xmax,ymax)
         print(blit(levels[actual],meinemonster))
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
         elif action.lower()=="i":
             ferris.x+=0
         #useless action
    
    return 0

ferris=Monster("@",12,9)
paolo=Monster("Ö",15,7)
levels=[]
levels.append("""
+---------------------------------------+
|                                       |
|                                       |
|                                       |
|                                       |
|    B              B            B      |
|   BBBB           BBBB        BBB      |
|n  BBBBBB        BBBBBBB      BBBBB    |
|  BBBBBBBB   BBBBBBBBBBBBBBBBBBBBB  nBB|
|BBBBBBBBBBB BBBBBBBBBBBBBBBBBBBBBBBBBBB|
|BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|
+---------------------------------------+
""")  # levesls[0]     
levels.append("""
+---------------------------------------+
|                                       |
|             BBBB                      |
|           BBBBBBBB                    |
|         BBBBBBBBB                     |
|        BBBBBBBBB                      |
|       BBBBBBBBB          BBB         n|
|pBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|
|BBBBBBBBBBBBBBBBBBBB   BBBBBBBBBBBBBBBB|
|BBBBBBBBBBBBBBBBBB       BBBBBBBBBBBBBB|
+---------------------------------------+
""")   #levels[1]
levels.append("""
+---------------------------------------+
|                                       |
|                                       |
|            BBBBBBBBBBBBB              |
|         BBBBBBBBBBBBBBBB              |
|      BBBBBBBBBBBBBBBBBBBBBB           |
|    BBBBBBBBBBBBBBBBBBBBBBBBB          |
|  BBBBBBBBBBBB     BBBBBBBBBBB         |
|  BBBBBBBBBBBBBB      BBBBBBBBBB      n|
| BBBBBBBBBBBBBBBBBB     BBBBBBBBBBBBBBB|
|BBBBBBBBBBBBBBBBBBBBB        pBBBBBBBBB|
|BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|
|BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|
|BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|
|BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB|
+---------------------------------------+
""")
levels.append(generate_level())
if __name__ == '__main__':
    main()

