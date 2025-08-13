import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    asteriodfield = AsteroidField()
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        updatable.update(dt)

        
        for obj in drawable:
            obj.draw(screen)
        
        for obj in asteroids:
            if obj.collisions(player):
                print("Game Over")
                exit()
        
        for obj in asteroids:
            for shot in shots:
                if shot.collisions(obj):
                    shot.kill()
                    obj.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
if __name__ == "__main__":
    main()
