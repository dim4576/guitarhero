import pygame as PG
from game import Surface as SU
from tab import Tab, Tbline
import random

wegth = 300
hegth = 600
FPS = 60
distansX = 80
firstLineX = wegth // 2 -distansX
secondLineX = wegth // 2
thredLineX = wegth // 2 +distansX
WHITE = 255,255,255
AZURE = 0,255,255
PURPLE = 255,0,255
YELLOW = 255,255,0
RED = 255,0,0
GREEN = 0,255,0
BLUE = 0,0,255

S = SU((wegth,hegth), FPS)

tablR = Tbline(firstLineX, RED, S.surf)
tablG = Tbline(secondLineX, GREEN, S.surf)
tablB = Tbline(thredLineX, BLUE, S.surf)

def shar():
	PG.draw.rect(S.surf, WHITE, (firstLineX - 20, hegth - 40, 200, 30))
	tablR.drop()
	tablG.drop()
	tablB.drop()
	if random.randint(0,100) > 99:
		tablR.add()
	if random.randint(0,100) > 99:
		tablG.add()
	if random.randint(0,100) > 99:
		tablB.add()
	for i in S.ivents:
		if i.type == PG.KEYDOWN:
			if i.key == PG.K_3:
				tablR.set_stat(True)
			if i.key == PG.K_4:
				tablG.set_stat(True)
			if i.key == PG.K_5:
				tablB.set_stat(True)
			if i.key == PG.K_RIGHTBRACKET or i.key == PG.K_LEFTBRACKET:
				if tablR.get_stat():
					tablR.kill_tab()
				if tablG.get_stat():
					tablG.kill_tab()
				if tablB.get_stat():
					tablB.kill_tab()
		if i.type == PG.KEYUP:
			if i.key == PG.K_3:
				tablR.set_stat(False)
			if i.key == PG.K_4:
				tablG.set_stat(False)
			if i.key == PG.K_5:
				tablB.set_stat(False)

S.setExecute(shar)

S.loop()
