# -*- coding:utf-8 -*-
'''
Created on 2013-4-28

@author: Administrator
'''
import math

import pyglet,random

import resources
import asteroid
from util import distance


def asteroids(num_asteroids, player_position, batch=None):
    # 产生小行星，随机设置行星的位置、速度，并且不让行星靠近飞船
    asteroids = []
    for i in xrange(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, batch=batch)
        
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random()*40
        new_asteroid.velocity_y = random.random()*40
        asteroids.append(new_asteroid)
    return asteroids
        

def player_lives(num_icons, batch=None):
    # 飞船的生命
    player_lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image,
                                          x=785-i*30, y=585,
                                          batch=batch)
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives







