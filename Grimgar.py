import random
from random import randint

help = 'this is a list of all commands: i, print inventory n, go north s, go south w, go west e, go east, to travel a set of directions multiple times: type direcion(s) pf trabel of the same line (up to four) e.g -nssn- craft, craft item sell, sell item buy, buy item equip, equip weapon attack, attack enemy heal, heals player hp +10, potion/ ether/ red pot/ blue pot: + 5/+15 per turn/+20/+50 y or n, answer question prompt'

global map
map = []
		
global gold
gold = 0

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
inv = {'wood':4, 'feather':8, 'stone':5, 'dagger':7}

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
	print '[stock: dagger(4atk, 5g) necklace(+7 mana, +2 atk, 28g), steel plated armor(+5 def, 8g), sword, axe, kunai, shuriken, metal, ]'
	global stock1
	stock1 = {'dagger':6, 'necklace':2, 'steel plated armor':4}
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
		elif b == 'necklace':
			if 'necklace' in inv:
				gold -= 28
				inv['necklace'] += 1
				stock1['necklace'] -=1
			print 'inv: ', inv
			print 'inv: ', inv
			gold_count()
			if 'necklace' not in inv:
				gold -= 28
				inv['necklace'] = 1
				stock1['necklace'] -=1
			print 'inv: ', inv
			print 'stock: ', stock1
			gold_count()
		elif b == 'steel plated armor':
			if 'steel plated armor' in inv:
				gold -= 8
				inv['steel plated armor'] += 1
				stock1['steel plated armor'] -= 1
			print 'inv: ', inv
			print 'stock: ', stock1
			gold_count()
			if 'steel plated armor' not in inv:
				gold -= 8
				inv['steel plated armor'] = 1
				stock1['steel plated armor'] -= 1
			print 'inv: ', inv
			print 'stock: ', stock1
			gold_count()
		else:
			pass
	elif x == 'sell':
		print 'stock: dagger(4atk, 5g) necklace(+7 mana, +2 atk, 28g), steel plated armor(+5 def, 8g)'
		print stock1
		print 'inv: ', inv
		s = raw_input('sell which item? ')
		if s == 'dagger':
			if 'dagger' in inv:
				gold += 5
				inv['dagger'] -= 1
				stock1['dagger'] += 1
			print 'inv: ', inv
			print 'stock: ', stock1
			gold_count()
		elif s == 'necklace':
			if 'necklace' in inv:
				gold += 28
				inv['necklace'] -= 1
				stock1['necklace'] +=1
			print 'inv: ', inv
			print 'stock: ', stock1
			gold_count()
		elif s == 'steel plated armor':
			if 'steel plated armor' in inv:
				gold += 8
				inv['steel plated armor'] -= 1
				stock1['steel plated armor'] += 1
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
	chest = {'cheese':3, 'key':8}
	print chest
	x = raw_input('take items? ')
	if x == 'y':
		if 'cheese' and 'key' in inv:
			a = raw_input('which item? ')
			if a == 'cheese':
				inv['cheese'] += 3
				chest['cheese'] -=3
			if a == 'key':
				inv['key'] += 8
				chest['key'] -= 8
			print 'inv: ', inv
			print 'chest: ', chest
		elif 'cheese' and 'key' not in inv:
			l = raw_input('which item? ')
			if l == 'cheese':
				inv['cheese'] = 3
			elif l == 'key':
				inv['key'] = 8
			print 'inv: ', inv
			print 'chest: ', chest
			
def is_equipped():
	global inv
	x = raw_input('equip weapon? ')
	if x == 'y':
		x = raw_input('which? ')
		if x == 'dagger':
				mnchr.atk += 4
		elif x == 'sword':
			mnchr.atk += 15
		elif x == 'katana':
			mnchr.atk += 20
		elif x == 'axe':
			mnchr.atk += 52
		elif x == 'soul sword':
			mnchr.atk += 36
		elif x == 'bankai':
			mnchr.atk += 78
		elif x == 'fire sword':
			mnchr.atk += 32
		elif x == 'ice sword':
			mnchr.atk += 34
		elif x == 'crystal sword':
			mnchr.atk += 666
		elif x == 'shuriken':
			mnchr.atk += 2
		elif x == 'kunai':
			mnchr.atk += 3
		elif x == 'blade of existencial crisis':
			mnchr.atk += 999
		else:
			pass
	elif x == 'n':
		pass
	
				

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
	text = ['hello']
	x = raw_input('talk? ')
	if x == 'y':
		talk = True
		if talk == True:
			print 'jeff: ', text
			if 'i have a favor to ask' in text:
				quest1()
			if 'i have a favor to ask' not in text:
				x = raw_input('end convo? ')
				if x == 'y':
					talk = False
		elif talk == False:
				pass
	elif x == 'n':
		pass
		
def specitem():
	while 'blue crystal necklace' in inv:
		mnchr.hp += 7
		if 'blue crystal necklace' not in inv:
			mnchr.hp -=7
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
			if 'dagger' or 'crystal sword' or 'bankai' or 'soul sword' or 'axe' or 'fire sword' or 'ice sword' or 'kunai' or 'shuriken' or 'katana' or 'sword' or 'blade of existencial crisis' in inv:
				is_equipped()
				enemy.hpe -= mnchr.atk
				print 'hp: ', enemy.hpe
			
			if 'dagger' or 'crystal sword' or 'bankai' or 'soul sword' or 'axe' or 'fire sword' or 'ice sword' or 'kunai' or 'shuriken' or 'katana' or 'sword' or 'blade of existencial crisis' not in inv:
				enemy.hpe -= mnchr.atk
				print 'hp: ', enemy.hpe
				
		if enemy.hpe <= 0:
				encounter = False
			
		if x == 'n':
			print 'you got away safely'
		
	if encounter == False:
		print 'enemy slain'
		gold += randint(0, 50)
		gold_count()
		if random.choice(l) == 'snek':
			inv['snake skin'] = 1
			print inv
	
encounter()

		
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
	elif x == 'n' 's' 'e' 'w':
		encounter()
		
		

	
	
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
		
		

	
	

	

	

	
		
	