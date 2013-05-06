# -*- coding:utf-8 -*-
'''
Created on 2013-5-5

@author: Elem
'''
import random

import physicalobject, resources

class Asteroid(physicalobject.PhysicalObject):
    '''
    小行星类，小行星消失之前被一点点分割
    '''


    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super(Asteroid, self).__init__(resources.asteroid_image, *args, **kwargs)
        self.rotate_speed = random.random() * 100.0 - 50.0
        
    def update(self, dt):
        # 更新行星速度以及旋转状态
        super(Asteroid, self).update(dt)
        self.rotation += self.rotate_speed * dt
    
    def handle_collision_with(self, other_object):
        super(Asteroid, self).handle_collision_with(other_object)
        
        # 行星被击中一次并且尺寸大于0.25时，重新创建行星对象
        if self.dead and self.scale > 0.25:
            num_asteroids = random.randint(2, 3)
            for i in xrange(num_asteroids):
                new_asteroid = Asteroid(x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.velocity_x = random.random()*70 + self.velocity_x
                new_asteroid.velocity_y = random.random()*70 + self.velocity_y
                new_asteroid.scale = self.scale*0.5
                self.new_objects.append(new_asteroid)
        
        
        
        
        
        