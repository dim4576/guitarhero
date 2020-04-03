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

S = SU((wegth,hegth), FPS)

tablR = Tbline(wegth // 2 -80, (255,0,0), S.surf)
tablG = Tbline(wegth // 2, (0,255,0), S.surf)
tablB = Tbline(wegth // 2 +80, (0,0,255), S.surf)

def shar():
	PG.draw.rect(S.surf, WHITE, (firstLineX - 20, hegth - 40, 200, 30))
	PG.draw.line(S.surf, AZURE, [firstLineX, 0], [firstLineX, hegth], 3)
	PG.draw.line(S.surf, PURPLE, [secondLineX, 0], [secondLineX, hegth], 3)
	PG.draw.line(S.surf, YELLOW, [thredLineX, 0], [thredLineX, hegth], 3)
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
				tablR.kill_last()
			if i.key == PG.K_4:
				tablG.kill_last()
			if i.key == PG.K_5:
				tablB.kill_last()

S.setExecute(shar)

S.loop()
