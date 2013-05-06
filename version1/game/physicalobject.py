# -*- coding:utf-8 -*-
'''
Created on 2013-5-1

@author: Administrator
'''
import pyglet
import util

class PhysicalObject(pyglet.sprite.Sprite):
    '''
    各图形对象的父类
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super(PhysicalObject, self).__init__(*args, **kwargs)
        
        self.velocity_x, self.velocity_y = 0.0, 0.0 #速度
        
        self.dead = False #是否消失了
        self.new_objects = [] #新对象列表
        
        self.reacts_to_bullets = True #是否遇到子弹发生反应消失
        self.is_bullet = False #是否是子弹
        
        
        self.event_handlers = []
    
    #更新Sprite的位置    
    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt
        
        self.check_bounds()
    
    # 检查Sprite的x,y边界    
    def check_bounds(self):
        min_x = -self.image.width/2 
        min_y = -self.image.height/2
        max_x = 800 + self.image.width/2
        max_y = 600 + self.image.height/2 
        if self.x < min_x:
            self.x = max_x
        elif self.x > max_x:
            self.x = min_x
        if self.y < min_y:
            self.y = max_y
        elif self.y > max_y:
            self.y = min_y
    
    # 判断与另外一个Sprite是否发生碰撞        
    def collides_with(self, other_object):
        if not self.reacts_to_bullets and other_object.is_bullet:
            return False
        if self.is_bullet and not other_object.reacts_to_bullets:
            return False
            
        collision_distance = self.image.width*0.5*self.scale \
                                + other_object.image.width*0.5*other_object.scale
        actual_distance = util.distance(self.position, other_object.position)
        
        return (actual_distance <= collision_distance)
    
    # Sprite发生碰撞则消失
    def handle_collision_with(self, other_object):
        if self.__class__ == other_object.__class__:
            self.dead = False
        else:
            self.dead = True
        
        
        
        
        
        