import pygame as PG
from game import Surface as SU
from tab import Tab, Tbline

wegth = 300
hegth = 750

S = SU((wegth,hegth), 60)

tablR = Tbline(wegth // 2 -80, (255,0,0), S.surf)
tablG = Tbline(wegth // 2, (0,255,0), S.surf)
tablB = Tbline(wegth // 2 +80, (0,0,255), S.surf)

def shar():
	PG.draw.line(S.surf, (0,255,255), [wegth // 2 -80, 0], [wegth // 2 -80, hegth], 3)
	PG.draw.line(S.surf, (255,0,255), [wegth // 2, 0], [wegth // 2, hegth], 3)
	PG.draw.line(S.surf, (255,255,0), [wegth // 2 +80, 0], [wegth // 2 +80, hegth], 3)
	tablR.drop()
	tablG.drop()
	tablB.drop()
	for i in S.ivents:
		if i.type == PG.KEYDOWN:
			if i.key == PG.K_3:
				tablR.add()
			if i.key == PG.K_4:
				tablG.add()
			if i.key == PG.K_5:
				tablB.add()

S.setExecute(shar)

S.loop()
