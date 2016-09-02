import json

import pygame

import SceneGameStart

def main():
    print "Starting game..."

    #Loads the configuration
    with open('config/config.json') as config_file:
        config = json.load(config_file)

    #temporary:
    global width, height
    screen_size =  width, height = config['screen']['width'], config['screen']['height']
    fps = config['fps']
    Debug = False
    pygame.init()
    screen = pygame.display.set_mode(screen_size)

    scene = SceneGameStart.SceneGameStart(screen, Debug)
    not_done = True
    while not_done:
        scene = scene.run()

if __name__ == "__main__":
    main()
