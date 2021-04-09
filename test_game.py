
WIDTH = 800
HEIGHT = 600

alien = Actor('alien')
#alien.pos = 50,100
speed = 3
xs0 = 0
ys0 = 0
xs1 = 10
ys1 = 400
alien.pos = xs1, ys1

def draw():
    screen.blit('kosmos',(0,0))
    alien.draw()

def update():
        #alien.top += speed
        alien.left += speed
        if alien.top > HEIGHT:
            alien.pos = xs0, ys0
        if alien.left > WIDTH:
            alien.pos = xs1, ys1


def on_mouse_down(pos):
    if alien.collidepoint(pos):
        sounds.eep.play
