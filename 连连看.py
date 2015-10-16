# -*- coding: UTF-8 -*-
from random import randrange
from graphics import*
import math
import time
import copy
import winsound
import thread
class Draw:#画框的类
    def __init__(self,a,b):
        self.p1=Point(50*a-25,50*b-25)
        self.p2=Point(50*a+25,50*b-25)
        self.p3=Point(50*a+25,50*b+25)
        self.p4=Point(50*a-25,50*b+25)
    def circle(self):
        self.c=Polygon(self.p1,self.p2,self.p3,self.p4)
        self.c.setOutline("blue")
        self.c.draw(win)
        return c
    def m(self):
        self.c=Polygon(self.p1,self.p2,self.p3,self.p4)
        self.c.setFill("white")
        self.c.setOutline("white")
        self.c.draw(win)
    def undraw(self):
        self.c.undraw()
        
def play_time():#同步记时
    global playtime,playtime_text
    
    playtime_text=Text(Point(200,0),playtime)
    playtime_text.draw(win)
    playtime_text2=Text(Point(150,0),"时间:").draw(win)
    while playtime>0:
        time.sleep(1)
        playtime=playtime-1
        playtime_text.setText(playtime)
    
def drawline(a,b,c,d,e,f,g,h):#画线
    global playtime,cl1,cl2,playtime_text
    l1=Line(Point(a*50,b*50),Point(c*50,d*50))
    l1.setOutline("red")
    l1.draw(win)
    l2=Line(Point(c*50,d*50),Point(e*50,f*50))
    l2.setOutline("red")
    l2.draw(win)
    l3=Line(Point(e*50,f*50),Point(g*50,h*50))
    l3.setOutline("red")
    l3.draw(win)
    tt=Text(Point(300,0),"+2 seconds")
    tt.draw(win)
    playtime=playtime+2
    playtime_text.setText(playtime)
    time.sleep(0.5)
    tt.undraw()
    l1.undraw()
    l2.undraw()
    l3.undraw()
    cl1.undraw()
    cl2.undraw()
    
def prepare():#前期工作
    global position,win,wash,playtime,click,picture_left,\
           po1,xo1,xo2,yo1,yo2,wait_time,c,wash_text,t
    position=[[0 for i in range(10)] for k in range(10)]
    win=GraphWin('game interface',600,600)
    win.setCoords(-100,500,500,-75)
    back=Image(Point(200,212.5),'pictures\\0.gif').draw(win)
    for i in range (1,17):
        k=0
        while k<4:
            x=randrange(1,9)
            y=randrange(1,9)
            if position[x][y]==0:
                k=k+1
                position[x][y]=i
                point=Point(x*50,y*50)
                picture=Image(point,'pictures\\%s.gif'%i).draw(win)
    wash=2
    wash_text=Text(Point(175,460),"你还有%s次洗牌机会"%wash)
    wash_text.draw(win)
    close=Polygon(Point(375,10),Point(450,10),Point(450,-25),Point(375,-25))
    close.draw(win)
    close_text=Text(Point(412,-12),"关闭声音").draw(win)
    playtime=50
    thread.start_new_thread(play_time,())      
    picture_left=64
    click=0
    po1=(0,0)
    xo1=0
    yo1=0
    xo2=0
    yo2=0
    wait_time=0
    c=0
    t=True
    
def win_lose():#判断输赢
    global picture_left,playtime,t
    if playtime<=1:
        fail=Text(Point(225,475),"you fail,click anywhere to restart")
        fail.draw(win)
        win.getMouse()
        time.sleep(1)
        t=False
    if picture_left==0:
        ach=Text(Point(225,475),"you win,click anywhere to restart")
        ach.draw(win)
        playtime=0
        win.getMouse()
        time.sleep(1)
        t=False

def wash1():#洗牌
    global click,wash,position
    if click==1:
        cl1.undraw()
    elif click==2:
        cl1.undraw()
        cl2.undraw()
    click=0
    wash=wash-1
    wash_text.setText("你还有%s次洗牌机会"%wash)
    positiona=copy.deepcopy (position)
    positionb=copy.deepcopy (position)
    for i in range (1,9):
        for k in range(1,9):
            if positiona[i][k]!=0:
                while 1:
                    x=randrange(1,9)
                    y=randrange(1,9)
                    if positionb[x][y]!=0:
                        position[x][y]=positiona[i][k]
                        positionb[x][y]=0
                        a=position[x][y]
                        p=Point(x*50,y*50)
                        picture=Image(p,'pictures\\%s.gif'%a)
                        picture.draw(win)
                        break

def judge():##判断是否符合消去要求
    global link
    if x1==x2 and y1!=y2:
        i=-1
        link=1
        if yma!=ymi+1:
            for k in range(ymi+1,yma):
                if position[x1][k]!=0:
                    link=0
        if link==1:
            drawline(x1,y1,x2,y2,x1,y1,x2,y2)
        while i<9 and link==0:
            i=i+1
            link=1
            for k in range(min(xmi,i),max(xmi,i)+1):
                 if k!=x1:
                    if position[k][ymi]!=0:
                        link=0
                    if position[k][yma]!=0:
                        link=0
            for k in range(ymi,yma+1):
                if position[i][k]!=0:
                    link=0
            if link==1:
                z=i
                drawline(x1,y1,z,y1,z,y2,x1,y2)
    elif x1!=x2 and y1==y2:
                    
        i=-1
        link=1
        if xma!=xmi+1:
            for k in range(xmi+1,xma):
                if position[k][y1]!=0:
                    link=0
        if link==1:
            drawline(x1,y1,x2,y2,x1,y1,x2,y2)
        while i<9 and link==0:
            i=i+1
            link=1
            for k in range(min(y1,i),max(y1,i)+1):
                if k!=y1:
                    if position[xmi][k]!=0:
                        link=0
                    if position[xma][k]!=0:
                        link=0
            for k in range(xmi,xma+1):
                if position[k][i]!=0:
                    link=0
            if link==1:
                z=i
                drawline(xmi,y11,xmi,z,xma,z,xma,y22)
    elif x1!=x2 and y1!=y2:
        i=-1
        link=0
        while i<9 and link==0:
            i=i+1
            link=1
            if y11!=i:
                for k in range(min(y11,i),max(y11,i)+1):
                    if k!=y11:
                        if position[xmi][k]!=0:
                            link=0
            if y22!=i:
                for k in range(min(y22,i),max(y22,i)+1):
                    if k!=y22:
                        if position[xma][k]!=0:
                            link=0
            for k in range(xmi+1,xma):
                if position[k][i]!=0:
                    link=0
            if link==1:
                z=i
                drawline(xmi,y11,xmi,z,xma,z,xma,y22)
        i=-1
        while i<9 and link==0:
            i=i+1
            link=1
            if xmi!=i:
                for k in range(min(xmi,i),max(xmi,i)+1):
                    if k!=xmi:
                        if position[k][y11]!=0:
                            link=0
            if xma!=i:
                for k in range(min(xma,i),max(xma,i)+1):
                    if k!=xma:
                        if position[k][y22]!=0:
                            link=0
            for k in range(ymi+1,yma):
                if position[i][k]!=0:
                    link=0
            if link==1:
                z=i
                drawline(xmi,y11,z,y11,z,y22,xma,y22)
                
def clicks():#获取鼠标点击
    global po2,xo1,xo2,yo1,yo2,click,p1,x1,x2,y1,y2,cl1,cl2
    po2=win.getMouse()
    xo2=int((po2.getX()+25)/50)
    yo2=int((po2.getY()+25)/50)
    if po2.getX()>375 and po2.getX()<450 and po2.getY()>-25 and\
        po2.getY()<10:
        winsound.PlaySound('pictures\\2', winsound.SND_ASYNC)
    elif po2.getX()>-96 and po2.getX()<30 and po2.getY()>444 and\
        po2.getY()<481 and wash>0:
        wash1()
    while (xo1!=xo2 or yo1!=yo2)and(xo2>0 and xo2<9 and yo2>0 and yo2<9)\
            and position[xo2][yo2]!=0:
        if click==0:
            click=1
            p1=po2
            x1=xo2
            y1=yo2
            xo1=xo2
            yo1=yo2
            cl1=Draw(x1,y1)
            cl1.circle()
            break
        if click==1:
            click=2
            p2=po2
            x2=xo2
            y2=yo2
            xo1=xo2
            yo1=yo2
            cl2=Draw(x2,y2)
            cl2.circle()
            break
        
def game_main():#两次点击后根据是否可以消去执行相关步骤
    global click,xma,xmi,xo1,yo1,cl1,cl2,y11\
            ,y1,y2,yma,ymi,link,picture_left,y22,y11
    if click==2:
        click=0
        xma=max(x1,x2)
        xmi=min(x1,x2)
        a=position[x1][y1]
        b=position[x2][y2]
        if a!=b:
            xo1=0
            yo1=0
            cl1.undraw()
            cl2.undraw()
        elif a==b:
            if x1>x2:
                y11=y2
                y22=y1
            elif x1<x2:
                y11=y1
                y22=y2
            yma=max(y1,y2)
            ymi=min(y1,y2)
            judge()
            if link==1:
                position[x1][y1]=0
                position[x2][y2]=0
                c=Draw(x1,y1)
                c.m()
                c=Draw(x2,y2)
                c.m()
                picture_left=picture_left-2
            elif link==0:
                xo1=0
                yo1=0
                cl1.undraw()
                cl2.undraw()

def main():#运行游戏
    winsound.PlaySound('pictures\\1', winsound.SND_ASYNC)#播放背景音乐
    while 1:
        prepare()#前期准备工作
        while t:
            clicks()#获取鼠标点击
            game_main()#主模块，判断是否可以消去，并执行相关步骤
            win_lose()#判断输赢
        win.close()
main()
