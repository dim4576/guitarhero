import pygame as PG
from game import Surface as SU
from circle import Circle as CI

class Tab():
	def __init__(self, posX, color, surface):
		self.startPosX = posX
		self.startColor = color
		self.surf = surface
		self.circle = CI(color, 30, (posX,-30), surface)
		self.alive = True

	def drop(self):
		if self.alive:
			self.circle.move(0,3)
			self.circle.show()
			self.howU()

	def howU(self):
		x,y = self.circle.get_pos()
		Xmax, Ymax = self.circle.surf.get_size()
		if y > Ymax + 30:
			self.alive = False

	def get_alive(self):
		return self.alive

	def rebuild(self):
		self.__init__(self.startPosX, self.startColor, self.surf)

class Tbline():
	def __init__(self, posX, color, surface):
		self.posX = posX
		self.color = color
		self.surf = surface
		self.tabs = list()

	def add(self):
		if self.tabs:
			if self.tabs[len(self.tabs) - 1].circle.posY < 30:
				return
		self.tabs.append(Tab(self.posX, self.color, self.surf))

	def drop(self):
		for i in range(len(self.tabs) ):
			if  not self.tabs[i].get_alive():
				self.tabs.pop(i)
				break

		for i in range(len(self.tabs) ):
			self.tabs[i].drop()
			
	def kill_last(self):
		if not self.tabs: return
		self.tabs.pop(0)