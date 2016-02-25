import random
from random import randint

help = 'this is a list of all commands: i, print inventory n, go north s, go south w, go west e, go east, to travel a set of directions multiple times: type direcion(s) pf trabel of the same line (up to four) e.g -nssn- craft, craft item sell, sell item buy, buy item equip, equip weapon attack, attack enemy heal, heals player hp +10, potion/ ether/ red pot/ blue pot: + 5/+15 per turn/+20/+50 y or n, answer question prompt'

global map
map = []

global gold
gold = 999

def gamestart():
        global x
        x = raw_input('Welcome to Grimgar, what is your name travaler? ')
        if x.isalpha():
                print 'I see, you are %s' % (x)
                v = raw_input('is this correct? ')
                if v == 'n':
                        gamestart()
                elif v == 'y':
                        pass
                else:
                        gamestart()

gamestart()

global inv
inv = {'wood':4, 'feather':8, 'stone':5, 'dagger':7, 'cheese':4 }

class char():
        def mainchar(self, hp, atk):
                global inv
                self.hp = hp
                self.atk = atk
                print 'hp: ', hp
                print 'atk: ', atk

        def heal(self, hp):
                self.hp += 10

        def potheal(self, hp):
                if 'potion' in inv:
                        self.hp += 5

        def cure(self, hp):
                if 'ether' in inv:
                        if enemy.attack == False:
                                self.hp += 15

class enemy():
        def enemy(self, hpe, atke):
                self.hpe = hpe
                self.atke = atke
                print 'hp: ', hpe
                print 'atk: ', atke

def quest2():
        global gold
        print 'there is a '

def quest1():
        global gold
        print 'i need you to find my necklace, its an ancient familt heirloom'
        x = raw_input('accept quest? ')
        if x == 'y':
                q = True
                while q == True:
                        print 'find jeffs necklace'
                        break
                if 'necklace' in inv:
                        q = False
        if q == False:
                print 'quest completed'
                inv['necklace'] -= 1
                print 'inv: ', inv
                gold += 150



def NPC():
        l = ['jeff', 'sauon', 'minato', 'yamada', 'tsuki', 'araragi', 'kitsune', 'kairi', 'namine', 'okabe', 'kero', 'yousuke', 'john smith', 'dean', 'sam', 'carrot', 'keith', 'sameul vimes', 'navidson', 'ivan', 'daru', 'watanuki', 'yuko', 'shinji', 'asuka', 'langley', 'gendou', 'ritsuko', 'rei', 'mirai', 'touka', 'ken', 'haise', 'urie', 'washu', 'eto', 'kanto', 'natani', 'raine', 'ginko', 'doumeki', 'saria', 'nimakaze', 'narita']
        x = raw_input('talk? ')
        if x == 'y':
                talk = True
                if talk == True:
                        print l
                        x = raw_input('to whom? ')
                        if x == 'jeff':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'minato':
                                name = x
                                text = ['If you have specific items in your inventory, you can craft them to make special items that you otherwise wouldnot be able to buy at the shop. ']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'yamada':
                                name = x
                                text = ['I know what youre thinking *what a common name*, but let me tell you, it runs in the family. ']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'tsukineko':
                                name = x
                                text = ['oh thank you, not many people think "moon-cat" is a cute name']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'araragi':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'kitsune':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'kairi':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'namine':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'okabe':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'kero':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'yousuke':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'john smith':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'dean':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'sam':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'keith':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'samuel vimes':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'navidson':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'ivan':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'daru':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'watanuki':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        if x == 'yuko':
                                name = x
                                text = ['hello']
                                name = name
                                print '%s: ' % (name), text
                        elif x == 'shinji':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                quest1()
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'asuka':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'langley':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'gendou':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'ritsuko':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'rei':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'mirai':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'touka':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'ken':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'haise':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'urie':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'washu':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'eto':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'kanto':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'natani':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'raine':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'ginko':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'doumeki':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'saria':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'nimakaze':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                        elif x == 'narita':
                                name = x
                                text = ['i have a favor to ask']
                                name = name
                                print '%s: ' % (name), text
                                
                                quest1()
                                
                                x = raw_input('end convo? ')
                                if x == 'y':
                                                talk = False
                elif talk == False:
                                pass
        elif x == 'n':
                        pass


NPC()


mnchr = char()
global x
print '%s' % (x)
def gold_count():
        global gold
        if gold >= 0:
                print'gold: ', gold

gold_count()
mnchr.mainchar(100, 10)
enemy = enemy()



def shop1():
        global gold
        global inv
        print 'shop:'
        print '[stock: dagger(4atk, 5g) necklace(+7 mana, +2 atk, 28g), sword(+15atk, 20g), axe(+52atk, 35g), kunai(+3atk), shuriken(+2atk), metal(12g), katana(+20atk, 44g)]'
        global stock1
        stock1 = {'dagger':100, 'necklace':25, 'sword':100, 'axe':100, 'kunai':100, 'shuriken':100, 'metal':60, 'katana':100}
        print stock1
        x = raw_input('buy or sell item? ')
        if x == 'buy':
                b = raw_input('buy which item? ')
                if b == 'dagger':
                        if 'dagger' in inv:
                                gold -= 5
                                inv['dagger'] += 1
                                stock1['dagger'] -= 1
                        print 'inv: ', inv
                        print 'stock: ', stock1
                        gold_count()
                        if 'dagger' not in inv:
                                gold -= 5
                                inv['dagger'] = 1
                                stock1['dagger'] -=1
                        print 'inv: ', inv
                        print 'stock: ', stock1
                        gold_count()
                elif b == 'axe':
                        if 'axe' in inv:
                                gold -= 35
                                inv['axe'] += 1
                                stock1['axe'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'axe' not in inv:
                                gold -= 35
                                inv['axe'] = 1
                                stock1['axe'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'shuriken':
                        if 'shuriken' in inv:
                                gold -= 3
                                inv['shuriken'] += 1
                                stock1['shuriken'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'shuriken' not in inv:
                                gold -= 3
                                inv['shuriken'] = 1
                                stock1['shuriken'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'kunai':
                        if 'kunai' in inv:
                                gold -= 5
                                inv['kunai'] += 1
                                stock1['kunai'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'kunai' not in inv:
                                gold -= 5
                                inv['kunai'] = 1
                                stock1['kunai'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'metal':
                        if 'metal' in inv:
                                gold -= 15
                                inv['metal'] += 1
                                stock1['metal'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'metal' not in inv:
                                gold -= 15
                                inv['metal'] = 1
                                stock1['metal'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'katana':
                        if 'katana' in inv:
                                gold -= 44
                                inv['katana'] += 1
                                stock1['katana'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'katana' not in inv:
                                gold -= 44
                                inv['katana'] = 1
                                stock1['katana'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'sword':
                        if 'sword' in inv:
                                gold -= 20
                                inv['sword'] += 1
                                stock1['sword'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'sword' not in inv:
                                gold -= 20
                                inv['sword'] = 1
                                stock1['sword'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'necklace':
                        if 'necklace' in inv:
                                gold -= 28
                                inv['necklace'] += 1
                                stock1['necklace'] -=1
                        print 'inv: ', inv
                        print 'stock: ', stock1
                        gold_count()
                        if 'necklace' not in inv:
                                gold -= 28
                                inv['necklace'] = 1
                                stock1['necklace'] -=1
                        print 'inv: ', inv
                        print 'stock: ', stock1
                        gold_count()
                else:
                        pass
        elif x == 'sell':
                print 'shop:'
                print 'stock: dagger(4atk, 5g) necklace(+7 mana, +2 atk, 28g), sword(+15atk, 20g), axe(+52atk, 35g), kunai(+3atk), shuriken(+2atk), metal(12g), katana(+20atk, 44g), upgrade weapon]'
                print stock1
                print 'inv: ', inv
                s = raw_input('sell which item? ')
                if b == 'dagger':
                        if 'dagger' in inv:
                                gold += 5
                                inv['dagger'] += 1
                                stock1['dagger'] -= 1
                        print 'inv: ', inv
                        print 'stock: ', stock1
                        gold_count()
                        if 'dagger' not in inv:
                                gold += 5
                                inv['dagger'] = 1
                                stock1['dagger'] -=1
                        print 'inv: ', inv
                        print 'stock: ', stock1
                        gold_count()
                elif b == 'axe':
                        if 'axe' in inv:
                                gold += 35
                                inv['axe'] += 1
                                stock1['axe'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'axe' not in inv:
                                gold += 35
                                inv['axe'] = 1
                                stock1['axe'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'shuriken':
                        if 'shuriken' in inv:
                                gold += 3
                                inv['shuriken'] += 1
                                stock1['shuriken'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'shuriken' not in inv:
                                gold += 3
                                inv['shuriken'] = 1
                                stock1['shuriken'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'kunai':
                        if 'kunai' in inv:
                                gold += 5
                                inv['kunai'] += 1
                                stock1['kunai'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'kunai' not in inv:
                                gold += 5
                                inv['kunai'] = 1
                                stock1['kunai'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'metal':
                        if 'metal' in inv:
                                gold += 15
                                inv['metal'] += 1
                                stock1['metal'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'metal' not in inv:
                                gold += 15
                                inv['metal'] = 1
                                stock1['metal'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'katana':
                        if 'katana' in inv:
                                gold += 44
                                inv['katana'] += 1
                                stock1['katana'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'katana' not in inv:
                                gold += 44
                                inv['katana'] = 1
                                stock1['katana'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'sword':
                        if 'sword' in inv:
                                gold += 20
                                inv['sword'] += 1
                                stock1['sword'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                        if 'sword' not in inv:
                                gold += 20
                                inv['sword'] = 1
                                stock1['sword'] -= 1
                                print 'inv: ', inv
                                print 'stock: ', stock1
                                gold_count()
                elif b == 'necklace':
                        if 'necklace' in inv:
                                gold += 28
                                inv['necklace'] += 1
                                stock1['necklace'] -=1
                        print 'inv: ', inv
                        print 'stock: ', stock1
                        gold_count()
                        if 'necklace' not in inv:
                                gold += 28
                                inv['necklace'] = 1
                                stock1['necklace'] -=1
                        print 'inv: ', inv
                        print 'stock: ', stock1
                        gold_count()
        else:
                pass



def craft():
        global inv
        x = raw_input('craft item? ')
        if x == 'y':
                x = raw_input('which item? ')
                if x == 'arrow':
                        if 'wood' in inv and 'feather' in inv and 'stone' in inv:
                                inv['arrow'] = 1
                                inv['wood'] -= 2
                                inv['feather'] -= 4
                                inv['stone'] -= 1
                                print inv
                        if 'wood' in inv and 'feather' in inv and 'stone' not in inv:
                                print 'you lack the neccecary items to craft this'
                elif x == 'stew':
                        if 'meat' and 'bowl' and 'spoon' and 'cauliflower' and 'beans' and 'carrots' and 'soup' in inv:
                                inv['stew'] = 1
                                inv['meat'] -= 2
                                inv['spoon'] -= 1
                                inv['cauliflower'] -= 3
                                inv['beans'] -= 6
                                inv['soup'] -= 1
                                print inv
                        if 'meat' and 'bowl' and 'spoon' and 'cauliflower' and 'beans' and 'carrots' and 'soup' not in inv:
                                print 'you lack the neccecary items to craft this'
                elif x == 'soup':
                        if 'broth' and 'vegetables' in inv:
                                inv['soup'] = 1
                                inv['broth'] -= 2
                                inv['vegetables'] -= 4
                                print inv
                        if 'broth' and 'vegetables' not in inv:
                                print 'you lack the neccecary items to craft this'
                elif x == 'crystal sword':
                        if 'quartz' and 'metal' and 'binding stone' in inv:
                                inv['crystal sword'] = 1
                                inv['metal'] -= 2
                                inv['quartz'] -= 7
                                inv['binding stone'] -= 1
                                print inv
                        if 'quartz' and 'metal' and 'binding stone' not in inv:
                                print 'you lack the neccecary items to craft this'
                elif x == 'osidian arrow':
                        if 'obsidian' and 'feather' and 'wood' in inv:
                                inv['wood'] -= 2
                                inv['obsidian'] -= 2
                                inv['festher'] -= 4
                                inv['obsidian arrow'] = 1
                                print inv
                        if 'obsidian' and 'feather' and 'wood' not in inv:
                                print 'you lack the neccecary items to craft this'
        elif x == 'n':
                pass



def unlock():
        l = ['door unlocked', 'door locked']
        x = raw_input('> ')
        if x == 'key':
                return random.choice(l)
                if random.choice(l) == 'door unlocked':
                        print 'door inlocked'
                elif random.choice(l) == 'door locked':
                        print 'door locked'
                        unlock()



def chest1():
        global inv
        chest = {'cheese':3, 'key':8, 'cactus':1}
        print 'chest: ', chest
        print 'cheese: heals 5 hp, key: opens doors, cactus: the most tsundere of plants'
        x = raw_input('take items? ')
        if x == 'y':
                if 'cheese' and 'key' and 'cactus' in inv:
                        a = raw_input('which item? ')
                        if a == 'cheese':
                                inv['cheese'] += 3
                                chest['cheese'] -=3
                        if a == 'key':
                                inv['key'] += 8
                                chest['key'] -= 8
                        print 'inv: ', inv
                        print 'chest: ', chest
                elif 'cheese' and 'key' and 'cactus' not in inv:
                        l = raw_input('which item? ')
                        if l == 'cheese':
                                inv['cheese'] = 3
                        elif l == 'key':
                                inv['key'] = 8
                        print 'inv: ', inv
                        print 'chest: ', chest

def is_equipped():
        global inv
        x = raw_input('equip bow and arrow? ')
        if x == 'y':
                if 'bow' in inv:
                        x = raw_input('which arrow? ')
                        if x == 'obsisian arrow':
                                if 'obsidian arrow' in inv:
                                        mnchr.atk += 4
        x = raw_input('equip weapon? ')
        if x == 'y':
                x = raw_input('which? ')
                print inv
                if x == 'dagger':
                        if 'dagger' in inv:
                                mnchr.atk += 4
                elif x == 'sword':
                        if 'sword' in inv:
                                mnchr.atk += 15
                elif x == 'katana':
                        if 'katana' in inv:
                                mnchr.atk += 20
                elif x == 'axe':
                        if 'axe' in inv:
                                mnchr.atk += 52
                elif x == 'soul sword':
                        if 'soul sword' in inv:
                                mnchr.atk += 36
                elif x == 'bankai':
                        if 'bankai' in inv:
                                mnchr.atk += 78
                elif x == 'fire sword':
                        if 'fire sword' in inv:
                                mnchr.atk += 32
                elif x == 'ice sword':
                        if 'ice sword' in inv:
                                mnchr.atk += 34
                elif x == 'crystal sword':
                        if 'crystal sword' in inv:
                                mnchr.atk += 666
                elif x == 'shuriken':
                        if 'shuriken' in inv:
                                mnchr.atk += 2
                elif x == 'kunai':
                        if 'kunai' in inv:
                                mnchr.atk += 3
                elif x == 'void of existensial anguish sword':
                        if 'void of existensial anguish sword' in inv:
                                mnchr.atk += 999

                else:
                        pass
        elif x == 'n':
                pass
#oelete the following note
#obsisian, amethyst, emerald, quartz, opal



def specitem():
        global inv
        x = raw_input('wear item? ')
        if x == 'y':
                x = raw_input('which item? ')
                if x == 'blue crystal necklace':
                        while 'blue crystal necklace' in inv:
                                mnchr.hp += 7
                                print mnchr.hp
                                break
                                if 'blue crystal necklace' not in inv:
                                        mnchr.hp -= 7
        elif x == 'n':
                pass

        x = raw_input('eat food? ')
        if x == 'y':
                x = raw_input('which food? ')
                if x == 'cheese':
                        while 'cheese' in inv:
                                mnchr.hp += 5
                                print 'hp + 5', mnchr.hp
                                break
                        if 'cheese' not in inv:
                                        mnchr.hp -= 5
                elif x == 'soup':
                        while 'soup' in inv:
                                mnchr.hp += 8
                                print 'hp + 8', mnchr.hp
                                break

                elif x == 'stew':
                        while 'stew' in inv:
                                mnchr.hp += 15
                                break


def encounter():
        global gold
        global inv
        encounter = True
        l = ['snek', 'floof', 'boop', 'dragon', 'rabbit', 'crab', 'lamb', 'moose', 'poof', 'enole']
        print random.choice(l)
        if random.choice(l) == 'floof':
                e = enemy.enemy(50, 100)
                print e
        elif random.choice(l) == 'snek':
                e = enemy.enemy(20, 35)
                print e
        elif random.choice(l) == 'boop':
                e = enemy.enemy(5, 12)
                print e
        elif random.choice(l) == 'dragon':
                e = enemy.enemy(150, 40)
                print e
        elif random.choice(l) == 'rabbit':
                e = enemy.enemy(13, 7)
                print e
        elif random.choice(l) == 'crab':
                e = enemy.enemy(3, 5)
                print e
        elif random.choice(l) == 'lamb':
                e = enemy.enemy(6, 8)
                print e
        elif random.choice(l) == 'moose':
                e = enemy.enemy(50, 14)
                print e
        elif random.choice(l) == 'enole':
                e = enemy.enemy(2, 4)
                print e
        elif random.choice(l) == 'poof':
                e = enemy.enemy(43, 65)
                print e
        else:
                pass


        while encounter == True:
                x = raw_input('attack? ')
                if x == 'y':
                        if 'dagger' or 'crystal sword' or 'bankai' or 'soul sword' or 'axe' or 'fire sword' or 'ice sword' or 'kunai' or 'shuriken' or 'katana' or 'sword' or 'blade of existencial crisis' or 'obsodian arrow' in inv:
                                is_equipped()
                                enemy.hpe -= mnchr.atk
                                print 'hp: ', enemy.hpe

                        if 'dagger' or 'crystal sword' or 'bankai' or 'soul sword' or 'axe' or 'fire sword' or 'ice sword' or 'kunai' or 'shuriken' or 'katana' or 'sword' or 'blade of existencial crisis' or 'obsisian arrow' not in inv:
                                enemy.hpe -= mnchr.atk
                                print 'hp: ', enemy.hpe

                if enemy.hpe <= 0:
                                encounter = False

                if x == 'n':
                        print 'you got away safely'
                        encounter = False

        if encounter == False:
                print 'enemy slain'
                gold += randint(0, 50)
                gold_count()





def over_world():
        global map
        print 'you are outside'
        x = raw_input('> ')
        if x == 'n':
                print 'you go north'
        elif x == 'n' 's' 's' 's':
                print 'you go north, south, south, south'
                map.append('nsss = 1st shop')
                shop1()
                print map
        elif x == 'n' 's' 'e' 'w':
                encounter()
        elif x == 'n' 's' 'w' 'w':
                chest1()

over_world()

def main_command():
        x = raw_input('> ')
        if x == 'map':
                print map
        elif x == 'i':
                print inv
        elif x == 'help':
                print help
        elif x == 'heal':
                mnchr.heal()
        elif x == 'cure':
                mnchr.cure()
        elif x == 'craft':
                craft()



over_world()



                     
