import sys, copy, json, random
import pygame
import SceneGame
from pprint import *

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

    scene = SceneGame.SceneGame(screen, Debug)
    scene.initialize()
    not_done = True
    while not_done:
        not_done = scene.run()

if __name__ == "__main__":
    main()
