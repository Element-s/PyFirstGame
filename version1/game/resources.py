'''
Created on 2013-4-28

@author: Elem
'''
import pyglet
import util

pyglet.resource.path = ['../resources']
pyglet.resource.reindex()
    

player_image = pyglet.resource.image('player.png')
util.center_image(player_image)

bullet_image = pyglet.resource.image('bullet.png')
util.center_image(bullet_image)

asteroid_image = pyglet.resource.image('asteroid.png')
util.center_image(asteroid_image)

engine_image = pyglet.resource.image('engine_flame.png')
engine_image.anchor_x = engine_image.width * 1.5
engine_image.acnhor_y = engine_image.height / 2

bullet_sound = pyglet.resource.media('bullet.wav', streaming=False)

