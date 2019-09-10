#pehla khel upgradation2
'''update:'''


def main():
    import pygame
    import sys
    import random
    import time
    def detect_collision1(p_position,e_position1):
        p_x=p_position[0]
        p_y=p_position[1]
        e_x=e_position1[0]
        e_y=e_position1[1]
        if(p_x>e_x and e_x+e_size>p_x) or (e_x>p_x and p_x+p_size>e_x):
            if (p_y>e_y and e_y+e_size>p_y) or (e_y>p_y and p_y+p_size>e_y):
                return 0
        return 1
    def detect_collision2(p_position,e_position2):
        p_x = p_position[0]
        p_y = p_position[1]
        e_x2 = e_position2[0]
        e_y2 = e_position2[1]
        if (p_x > e_x2 and e_x2 + e_size > p_x) or (e_x2 > p_x and p_x + p_size > e_x2):
            if (p_y > e_y2 and e_y2 + e_size > p_y) or (e_y2 > p_y and p_y + p_size > e_y2):
                return 0
        return 1

    def detect_collision3(p_position,e_position3):
        p_x = p_position[0]
        p_y = p_position[1]
        e_x3 = e_position3[0]
        e_y3 = e_position3[1]
        if (p_x > e_x3 and e_x3 + e_size > p_x) or (e_x3 > p_x and p_x + p_size > e_x3):
            if (p_y > e_y3 and e_y3 + e_size > p_y) or (e_y3 > p_y and p_y + p_size > e_y3):
                return 0
        return 1
    def drop_e(e_list1,e_list2,e_list3):
        delay=random.random()
        if len(e_list1)<4 and delay<0.08:
            x_pos=random.randint(0,width-e_size)
            y_pos=0
            e_list1.append([x_pos,y_pos])
        if len(e_list2)<4 and delay<0.08:
            x_pos2=random.randint(0,width-e_size)
            y_pos2=0
            e_list2.append([x_pos2,y_pos2])
        if len(e_list3)<1 and delay<0.01:
            x_pos3 = random.randint(0, width - e_size)
            y_pos3 = 0
            e_list3.append([x_pos3,y_pos3])

    def draw_e(e_list1,e_list2,e_list3):
        delay=random.random()
        for e_position1 in e_list1:
            pygame.draw.rect(screen, blue, (e_position1[0], e_position1[1], e_size, e_size))
        for e_position2 in e_list2:
            pygame.draw.rect(screen, green, (e_position2[0], e_position2[1], e_size, e_size))
        for e_position3 in e_list3:
            if delay<0.5:
                pygame.draw.rect(screen, ((0,222,113)), (e_position3[0], e_position3[1], e_size, e_size))
            else:
                pygame.draw.rect(screen, ((71,19,134)), (e_position3[0], e_position3[1], e_size, e_size))
    def update_e_position(e_list1,e_list2,e_list3):
       for index,e_position1 in enumerate(e_list1):
        if e_position1[1]>=0 and e_position1[1]<height:
            e_position1[1]+=speed
        else:
            e_list1.pop(index)
       for index,e_position2 in enumerate(e_list2):
        if e_position2[1]>=0 and e_position2[1]<height:
            e_position2[1]+=speed
        else:
            e_list2.pop(index)
       for index,e_position3 in enumerate(e_list3):
        if e_position3[1]>=0 and e_position3[1]<height:
            e_position3[1]+=speed
        else:
            e_list3.pop(index)
    def collision_checker(e_list1,p_position):
        for e_position1 in e_list1:
            if detect_collision1(p_position,e_position1)==0:
                return 0
        return 1




    pygame.init()
    width=800
    height=600
    white_p=((200,200,200))
    blue=((225,0,0))
    yellow=((255,73,177))
    green=((0,225,0))
    b_color=(0,0,0)
    p_size=50
    e_size=50
    speed=10
    score=0
    clock=pygame.time.Clock()
    e_position1=[random.randint(0,width-e_size),0]
    e_position2=[random.randint(0,width-e_size),0]
    e_position3=[random.randint(0,width-e_size),0]
    p_position=[width/2,height-2*p_size]
    e_list1=[e_position1]
    e_list2=[e_position2]
    e_list3=[e_position3]
    myFont=pygame.font.SysFont("monospace",35)
    myFont1=pygame.font.SysFont("arial",100)
    myFont2=pygame.font.SysFont("arial",50)
    screen=pygame.display.set_mode((width,height))
    game_over=True
    pygame.mixer.music.load("castle.mp3")
    pygame.mixer.music.play(-1)
    while game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    if p_position[0]>0:
                        p_position[0]-=p_size
                elif event.key==pygame.K_RIGHT:
                    if p_position[0]<=700:
                        p_position[0]+=p_size
        screen.fill(b_color)

        clock.tick(30)
        drop_e(e_list1,e_list2,e_list3)
        update_e_position(e_list1,e_list2,e_list3)
        for e_position3 in e_list3:
            if detect_collision3(p_position,e_position3)==0:
                score+=10
        for e_position2 in e_list2:
            if detect_collision2(p_position,e_position2)==0:
                score+=1
        text= "SCORE : " + str(score)
        label=myFont.render(text,1,yellow)
        screen.blit(label,(width-250,height-40))
        if collision_checker(e_list1,p_position)==0:
            pygame.mixer.music.stop()
            x = pygame.mixer.Sound("game_over.wav")
            x.play()
            time.sleep(1)
            label1 = myFont1.render("GAME OVER", 1,(100, 100, 100))
            screen.blit(label1, (width - 700, height - 300))
            pygame.display.update()
            time.sleep(3)
            screen.fill((200, 200, 200))
            label2=myFont2.render("PRESS 'Y' TO PLAY AGAIN",True,((69,69,69)))
            screen.blit(label2, (width-700,height-300))
            pygame.display.update()
            khatam = True
            while khatam is True:
                for e in pygame.event.get():
                    if e.type is pygame.KEYDOWN:
                        if e.key == pygame.K_y:
                            main()
                        if e.key == pygame.K_n:
                            game_over=False
                            khatam=False


            break
        draw_e(e_list1, e_list2,e_list3)
        pygame.draw.rect(screen, white_p, (p_position[0], p_position[1], p_size, p_size))
        pygame.display.update()

main()