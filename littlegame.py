# -*- coding: utf-8 -*-
"""
Created on Sat Feb 23 17:50:30 2019

@author: SXQ
"""

# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


class Creat_Role():
    def __init__(self,name,hp,att,speed):
        self.name=name
        self.hp=hp
        self.att=att
        self.speed = speed


# In[3]:


class Battle():
    def __init__(self, role1, role2):
        self.role1 = role1
        self.role2 = role2
        self.bar = pd.DataFrame()
        self.role1_list = [x.name for x in role1]
        self.role2_list = [x.name for x in role2]
        self.result = 2
        self.lenbar = 100
        
    def timelist(self):
        for r in self.role1:
            att_time = np.arange(1, r.speed + 1) * (self.lenbar/r.speed)
            bar_role = pd.DataFrame()
            bar_role['att_time'] = att_time
            bar_role['role'] = r.name
            self.bar = pd.concat([self.bar,bar_role])
        for r in self.role2:
            att_time = np.arange(1, r.speed + 1) * (self.lenbar/r.speed)
            bar_role = pd.DataFrame()
            bar_role['att_time'] = att_time
            bar_role['role'] = r.name
            self.bar = pd.concat([self.bar,bar_role])
    
    def sort(self):
        self.bar.sort_values(by='att_time', ascending = True, inplace = True)
        self.bar.reset_index()
        self.bar.drop('index', inplace = True)
    
    def start(self):
        for i in range(self.bar.shape[0]):
            row = self.bar.iloc[i]
            if row['role'] in self.role1_list:
                role = self.role1[self.role1_list.index(row['role'])]
                self.role2[0].hp -= role.att
                print('{}对{}造成了{}点伤害'.format(role.name,self.role2[0].name,str(role.att)))
                if self.role2[0].hp <= 0:
                    print('{}死亡了'.format(self.role2[0].name))
                    del self.role2[0]
                    del self.role2_list[0]
                    if len(self.role2) == 0:
                        self.result = 1
                        print('战斗胜利')
                        break
            
            if row['role'] in self.role2_list:
                role = self.role2[self.role2_list.index(row['role'])]
                self.role1[0].hp -= role.att
                print('{}对{}造成了{}点伤害'.format(role.name,self.role1[0].name,str(role.att)))
                if self.role1[0].hp <= 0:
                    print('{}死亡了'.format(self.role1[0].name))
                    del self.role1[0]
                    del self.role1_list[0]
                    if len(self.role1) == 0:
                        self.result = 0
                        print('战斗失败')
                        break
            
    def run(self):
        self.timelist()
        self.sort()
        self.start()


# In[4]:
        
major1 =  Creat_Role('HERO1', 100, 20, 20)
major2 =  Creat_Role('HERO2', 100, 20, 20)
major3 =  Creat_Role('HERO3', 100, 20, 20)

guai1 =  Creat_Role('LaJi1', 100, 15, 20)
guai2 =  Creat_Role('LaJi2', 100, 15, 20)
guai3 =  Creat_Role('LaJi3', 100, 15, 20)

battle1 = Battle([major1,major2,major3], [guai1,guai2,guai3])

battle1.run()



