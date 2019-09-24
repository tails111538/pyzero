
alien = Actor('alien')


start_level = 400, 400
alien.topleft = start_level

WIDTH = 1300
HEIGHT = 700

def is_brick(row, col):
    if row <= 13:
        if row == 3 and col >= 3 and col <= 7:
            return False
        if row == 4 and col >= 3 and col <= 11:
            return False
        if row == 5 and col >= 3 and col <= 7:
            return False
        return True
    return False

def draw():
    screen.clear()
    for row in range(7):
        cols = []
        for col in range(13):
            if is_brick(row, col):
                screen.blit('brick', (col * 100, row * 100))

    alien.draw()

def update():
    if keyboard.left and alien.left > 0:
        print(int(alien.top / 100))
        print(int(alien.left / 100))
        if not is_brick(int(alien.top / 100), int(alien.left / 100)):
            alien.x -= 10
    elif keyboard.right and alien.right < WIDTH:
        alien.x += 10
    elif keyboard.up and alien.top > 0:
        alien.y -= 10
    elif keyboard.down and alien.bottom < HEIGHT:
        alien.y += 10

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()


def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'