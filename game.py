import pygame as PG


class Surface ():
    def __init__(self, resolution, FPS):
        PG.init()
        self.surf = PG.display.set_mode(resolution)
        self.clk = PG.time.Clock()
        self.work = True
        self.FPS = FPS
        self.exec = self.void
        self.ivents = None
        pass

    def void(self):
        pass


    def setExecute(self, func):
        self.exec = func

    def loop(self):
        while self.work:
            self.clk.tick(self.FPS)
            PG.display.flip()
            self.surf.fill((0,0,0))
            self.ivents = PG.event.get()
            for i in self.ivents:
                if i.type == PG.QUIT:
                    self.work = False
                    PG.quit()
            self.exec()


if __name__ == "__main__":

    S = Surface((800,600), 60)

    def shar():
        PG.draw.circle(S.surf, (233,44,123), (50, 50), 30)
    
    S.setExecute(shar)
    S.loop()
    
