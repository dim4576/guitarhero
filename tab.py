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
			self.circle.move(0,1)
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
		self.weight, self.height = self.surf.get_size()
		self.colorR, self.colorG, self.colorB = self.color
		self.key_status = False


	def add(self):
		if self.tabs:
			if self.tabs[len(self.tabs) - 1].circle.posY < 30:
				return
		self.tabs.append(Tab(self.posX, self.color, self.surf))


	def drop(self):
		PG.draw.line(self.surf, 
					 (255, 255, 0), #yellow
					 [self.posX, 0], 
					 [self.posX, self.height], 
					 3)

		for i in range(len(self.tabs) ):
			if  not self.tabs[i].get_alive():
				self.tabs.pop(i)
				break

		for i in range(len(self.tabs) ):
			self.tabs[i].drop()

		PG.draw.circle(self.surf, 
					   (0,255,255),
					   (self.posX, self.height - 50),
					   34, 2)
		if self.key_status:
			PG.draw.circle(self.surf,
						   self.color,
						   (self.posX, self.height - 50),
						   20)
			PG.draw.circle(self.surf, 
					   (0,255,255),
					   (self.posX, self.height - 50),
					   24, 4)

	def set_stat(self, status_key):
		self.key_status = status_key

	def kill_tab(self):
		for i in range(len(self.tabs) ):
			x,y = self.tabs[i].circle.get_pos()
			if y > self.height - 110 and y < self.height + 10:
				self.tabs.pop(i)
				break

	def get_stat(self):
		return self.key_status


			
	def kill_last(self):
		if not self.tabs: return
		self.tabs.pop(0)