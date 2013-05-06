# -*- coding:utf-8 -*-
'''
Created on 2013-5-1

@author: Administrator
'''
import math, pyglet

from pyglet.window import key

import physicalobject
import resources
import bullet

class Player(physicalobject.PhysicalObject):
    '''
    classdocs
    '''

    def __init__(self, *args, **kwargs):
        '''
        Constructor
        '''
        super(Player, self).__init__(img=resources.player_image, 
                                     *args, **kwargs)
        # 创建引擎火焰
        self.engine_sprite = pyglet.sprite.Sprite(img=resources.engine_image,
                                                  *args, **kwargs)
        
        self.engine_sprite.visible = False
                
        self.thrust = 300.0
        self.rotate_speed = 200.0
        self.bullet_speed = 700.0
        
        # 是否与子弹发生反应
        self.reacts_to_bullets = False
        
        # 把事件处理告诉游戏处理器
        self.key_handler = key.KeyStateHandler()
        self.event_handlers = [self, self.key_handler]
        
    def on_key_press(self, symbol, modifiers):
        if symbol == key.SPACE:
            self.fire()
            
    def update(self, dt):
        super(Player, self).update(dt)
        
        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotate_speed * dt
        if self.key_handler[key.UP]:
            # 设置移动速度
            angle_radians =  -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
            
            # 更新引擎火焰位置
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y
            self.engine_sprite.visible = True
        else:
            self.engine_sprite.visible = False
            
    def fire(self):
        # 设置发射角度
        angle_radians = -math.radians(self.rotation)
            
        # 创建子弹对象
        ship_radius = self.image.width/2
        bullet_x = self.x + math.cos(angle_radians) * ship_radius    
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)
        
        # 设置子弹速度
        bullet_vx = self.velocity_x + math.cos(angle_radians) * self.bullet_speed
        bullet_vy = self.velocity_y + math.sin(angle_radians) * self.bullet_speed
        new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy
        
        # 添加子弹对象到新对象列表
        self.new_objects.append(new_bullet)    
        
        # 播放子弹声音
        resources.bullet_sound.play()
            
    def delete(self):
        # 删除引擎火焰和飞船对象
        self.engine_sprite.delete()
        super(Player, self).delete()
        
        
        