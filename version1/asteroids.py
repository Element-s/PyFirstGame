# -*- coding:utf-8 -*-
'''
Created on 2013-4-28

@author: Administrator
'''
import pyglet

from game import load
from game import player
from game import asteroid
from game import bullet

# 创建游戏窗口
game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()

# 设置游戏初始分数以及窗口标题
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="My Firs Game", 
                                x=400, y=575, anchor_x='center', batch=main_batch)

game_over_label = pyglet.text.Label(text="Game Over",x=400, y=-300,
                                    anchor_x='center', batch=main_batch,
                                    font_size=48)

counter = pyglet.clock.ClockDisplay()

player_ship = None
player_lives = []
game_objects = []
num_asteroids = 3
score = 0

event_stack_size = 0

def init():
    # 初始化游戏状态
    global score, num_asteroids
    
    score = 0
    score_label.text = "Score:" + str(score)
    
    num_asteroids = 3
    reset_level(2)
    
# 重置游戏
def reset_level(num_lives=2):
    global player_ship, player_lives, game_objects, event_stack_size
    
    # 清除事件栈
    while event_stack_size > 0:
        game_window.pop_handlers()
        event_stack_size -= 1
    
    for life in player_lives:
        life.delete()
        
    # 初始化飞船
    player_ship = player.Player(x=400, y=300, batch=main_batch)
    
    # 初始化飞船生命
    player_lives = load.player_lives(num_lives, batch=main_batch)
    
    # 初始化小行星
    asteroids = load.asteroids(num_asteroids, player_ship.position, batch=main_batch)
    
    # 保存所有对象
    game_objects = [player_ship] + asteroids
    
    # 添加所有对象的事件到游戏事件栈中
    for obj in game_objects:
        for handler in obj.event_handlers:
            game_window.push_handlers(handler)
            event_stack_size += 1

@game_window.event
def on_draw():
    # 绘制所有的图形对象
    game_window.clear()
    main_batch.draw()
    counter.draw()
    
def update(dt):
    global score, num_asteroids
    
    player_dead = False
    victory = False
    
    for i in xrange(len(game_objects)):
        for j in xrange(i+1, len(game_objects)):
            obj_1 = game_objects[i]
            obj_2 = game_objects[j]
            
            if not obj_1.dead and not obj_2.dead:
                if obj_1.collides_with(obj_2):
                    obj_1.handle_collision_with(obj_2)
                    obj_2.handle_collision_with(obj_1)
    
                    
    to_add = []        
    
    asteroids_remaining = 0
    
    for obj in game_objects:
        obj.update(dt)
        to_add.extend(obj.new_objects)
        obj.new_objects = []
    
        if isinstance(obj, asteroid.Asteroid):
            asteroids_remaining += 1
    
    if asteroids_remaining == 0:
        victory = True
            
        
    for to_remove in [obj for obj in game_objects if obj.dead]:
        if to_remove == player_ship:
            player_dead = True
        
        to_add.extend(to_remove.new_objects)
        to_remove.delete()
        
        game_objects.remove(to_remove)
        
        if isinstance(to_remove, asteroid.Asteroid):
            score += 1
            score_label.text = "Score:" + str(score)
    
    game_objects.extend(to_add)
        
    if player_dead:
        if len(player_lives) > 0:
            reset_level(len(player_lives) - 1)
        else:
            game_over_label.y = 300
    elif victory:
        num_asteroids += 1
        player_ship.delete()
        score += 10
        reset_level(len(player_lives))


if __name__ == '__main__':
    init()
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
    
    
    
    
    