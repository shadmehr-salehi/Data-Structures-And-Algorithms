#Skip List Class in python 
# For more info visit : https://en.wikipedia.org/wiki/Skip_list
# ---- A Drunk Man Will Find His Way Home but a Drunk Bird May Get Lost Forever =) ----
import random

class Node(object):
	def __init__(self, key, level):
		self.key = key
		self.forward = [None]*(level+1)

class SkipList(object):
	def __init__(self, max_lvl = 3, P = 0.5):
		self.MAXLVL = max_lvl
		self.P = P
		self.header = self.createNode(self.MAXLVL, -1)
		self.level = 0
	
	def createNode(self, lvl, key):
		n = Node(key, lvl)
		return n
	
	def randomLevel(self): 
		lvl = 0
		while random.random()<self.P and lvl<self.MAXLVL:lvl += 1
		return lvl

	def add(self, key):
		update = [None]*(self.MAXLVL+1)
		current = self.header

		for i in range(self.level, -1, -1):
			while current.forward[i] and \
				current.forward[i].key < key:
				current = current.forward[i]
			update[i] = current

		current = current.forward[0]

		if current == None or current.key != key:
			rlevel = self.randomLevel()

			if rlevel > self.level:
				for i in range(self.level+1, rlevel+1):
					update[i] = self.header
				self.level = rlevel
			n = self.createNode(rlevel, key)
			for i in range(rlevel+1):
				n.forward[i] = update[i].forward[i]
				update[i].forward[i] = n

	def erase(self, search_key):

		update = [None]*(self.MAXLVL+1)
		current = self.header

		for i in range(self.level, -1, -1):
			while(current.forward[i] and current.forward[i].key < search_key):	
				current = current.forward[i]
			update[i] = current
		current = current.forward[0]

		if current != None and current.key == search_key:
			for i in range(self.level+1):
				if update[i].forward[i] != current:
					break
				update[i].forward[i] = current.forward[i]

			while(self.level>0 and self.header.forward[self.level] == None):
				self.level -= 1

	def search(self, key) -> bool:
		current = self.header
		for i in range(self.level, -1, -1):
			while(current.forward[i] and current.forward[i].key < key):
				current = current.forward[i]
		current = current.forward[0]

		if current and current.key == key:
			return True
		return False




def main():
    lst = SkipList()
    lst.add(1)
    lst.add(2)
    lst.add(3)
    lst.add(4)
    lst.erase(3)
    print(lst.search(3))
    
main()
