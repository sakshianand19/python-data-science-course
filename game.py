import pgzrun

music.play('wallpaper')
music.set_volume(50)

b = Actor('icecream', (50,50))
vx, vy = 3, 2

def draw():
    screen.fill('aqua')
    b.draw()

def update():
    global vx, vy
    b.x += vx
    b.y += vy
    if b.right > 800 or b.left < 0:
        vx = -vx
        sounds.s1.play()
    if b.bottom > 600 or b.top < 0:
        vy = -vy
        sounds.s1.play()    

pgzrun.go() 