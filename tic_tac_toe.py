import os
os.environ['SDL_VIDEODRIVER']='windib'
import pygame
pygame.init
pygame.font.init()
pygame.mixer.init()


window = pygame.display.set_mode((1200, 800))

pygame.display.set_caption("Tic Tac Toe")

font = pygame.font.SysFont("Arial Black", 100)
font2 = pygame.font.SysFont("ALGERIAN", 100)
font3 = pygame.font.SysFont("Times New Roman", 40)
font4 = pygame.font.SysFont("Copperplate Gothic Bold", 40)
pygame.mixer.music.load('Megaman X- Spark Mandrill Theme.mp3')
pygame.mixer.music.play()

black = (0,0,0)
white = (255, 255, 255)
orange = (255, 140, 0)
background = pygame.image.load("wood.jpeg")
board = pygame.image.load("board.gif")
hline = pygame.image.load("hline.gif")
vline = pygame.image.load("vline.gif")
dline1 = pygame.image.load("dline1.gif")
dline2 = pygame.image.load("dline2.gif")
x = pygame.image.load("x.gif")
o = pygame.image.load("o.gif")
playButton = pygame.image.load('playButton.png')

moveb = 0
b = 100
movea = 0
a = 850
t = 0
play = False

def oddTurn(turn):
    if turn%2 == 1:
        return True
    else:
        return False

gameLoop = True
while gameLoop:
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            gameLoop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            print pygame.mous.get_pos()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                play = True
            if event.key == pygame.K_KP7 and s1 and oddTurn(turn):
                ax=True
                column1 += 1
                row1 += 1
                diagonal1 += 1  
                turn += 1
            if event.key == pygame.K_KP8 and s2 and oddTurn(turn):
                bx=True
                column2 += 1
                row1 += 1    
                turn += 1
            if event.key == pygame.K_KP9 and s3 and oddTurn(turn):
                cx=True
                column3 += 1
                row1 += 1
                diagonal2 += 1   
                turn += 1
            if event.key == pygame.K_KP4 and s4 and oddTurn(turn):
                dx=True
                column1 += 1
                row2 += 1   
                turn += 1
            if event.key == pygame.K_KP5 and s5 and oddTurn(turn):
                ex=True
                column2 += 1
                row2 += 1
                diagonal1 += 1
                diagonal2 += 1 
                turn += 1
            if event.key == pygame.K_KP6 and s6 and oddTurn(turn):
                fx=True
                column3 += 1
                row2 += 1  
                turn += 1
            if event.key == pygame.K_KP1 and s7 and oddTurn(turn):
                gx=True   
                column1 += 1
                row3 += 1
                diagonal2 += 1 
                turn += 1
            if event.key == pygame.K_KP2 and s8 and oddTurn(turn):
                hx=True 
                column2 += 1
                row3 += 1  
                turn += 1
            if event.key == pygame.K_KP3 and s9 and oddTurn(turn):
                ix=True 
                column3 += 1
                row3 += 1
                diagonal1 += 1  
                turn += 1
            
            if event.key == pygame.K_q and s1 and not oddTurn(turn):
                ao=True
                column1 += 5
                row1 += 5
                diagonal1 += 5    
                turn += 1
            if event.key == pygame.K_w and s2 and not oddTurn(turn):
                bo=True
                column2 += 5
                row1 += 5    
                turn += 1
            if event.key == pygame.K_e and s3 and not oddTurn(turn):
                co=True
                column3 += 5
                row1 += 5
                diagonal2 += 5 
                turn += 1
            if event.key == pygame.K_a and s4 and not oddTurn(turn):
                do=True
                column1 += 5
                row2 += 5     
                turn += 1
            if event.key == pygame.K_s and s5 and not oddTurn(turn):
                eo=True
                column2 += 5
                row2 += 5
                diagonal1 += 5
                diagonal2 += 5  
                turn += 1
            if event.key == pygame.K_d and s6 and not oddTurn(turn):
                fo=True
                column3 += 5
                row2 += 5    
                turn += 1
            if event.key == pygame.K_z and s7 and not oddTurn(turn):
                go=True 
                column1 += 5
                row3 += 5
                diagonal2 += 5  
                turn += 1
            if event.key == pygame.K_x and s8 and not oddTurn(turn):
                ho=True 
                column2 += 5
                row3 += 5 
                turn += 1
            if event.key == pygame.K_c and s9 and not oddTurn(turn):
                io=True
                column3 += 5
                row3 += 5
                diagonal1 += 5   
                turn += 1
            if event.key == pygame.K_DOWN:
                moveb+=7
            if event.key == pygame.K_UP:
                moveb-=7
            if event.key == pygame.K_LEFT:
                movea-=7    
            if event.key == pygame.K_RIGHT:
                movea+=7               
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                moveb=0  
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                movea=0
            
                   
    window.fill(orange)
    name = font.render("TIC TAC TOE", 1, white)
    textPlay = font2.render("PLAY", 1, black)
    infoPlay = font3.render("Press Enter to Play", 1, black)
    window.blit(name, (55,20))
    production = font4.render("CREATED BY: SHEHAN", 1, black)
    player1Wins = font4.render("PLAYER 1 WINS!", 1, black)
    player2Wins = font4.render("PLAYER 2 WINS!", 1, black)
    draw = font4.render("DRAW!", 1, black)
    
    if not play:
        ax=False
        bx=False
        cx=False
        dx=False
        ex=False
        fx=False
        gx=False
        hx=False
        ix=False
        
        ao=False
        bo=False
        co=False
        do=False
        eo=False
        fo=False
        go=False
        ho=False
        io=False
        
        s1 = True
        s2 = True
        s3 = True
        s4 = True
        s5 = True
        s6 = True
        s7 = True
        s8 = True
        s9 = True
        
        turn = 1
        column1 = 0
        column2 = 0
        column3 = 0
        row1 = 0
        row2 = 0
        row3 = 0
        diagonal1 = 0
        diagonal2 = 0        
        window.blit(pygame.transform.scale(playButton, (400,400)), (190,240))
        window.blit(textPlay, (255,360))
        window.blit(infoPlay, (243,460))
        window.blit(production, (a,b)) 
    
    if play:
        window.blit(pygame.transform.scale(board, (500,500)), (150,200))
        window.blit(pygame.transform.scale(x, (100,100)), (800,275))
        player1 = font3.render("Player 1", 1, black)
        window.blit(player1, (925,300))
        window.blit(pygame.transform.scale(o, (100,100)), (800,525))
        player2 = font3.render("Player 2", 1, black)
        window.blit(player2, (925,550))
        if ax:
            window.blit(pygame.transform.scale(x, (100,100)), (185,230))
            s1 = False
        if bx:
            window.blit(pygame.transform.scale(x, (100,100)), (353,230))
            s2 = False
        if cx:
            window.blit(pygame.transform.scale(x, (100,100)), (521,230)) 
            s3 = False
        if dx:
            window.blit(pygame.transform.scale(x, (100,100)), (185,400)) 
            s4 = False
        if ex:
            window.blit(pygame.transform.scale(x, (100,100)), (353,400))    
            s5 = False
        if fx:
            window.blit(pygame.transform.scale(x, (100,100)), (521,400))  
            s6 = False
        if gx:
            window.blit(pygame.transform.scale(x, (100,100)), (185,560)) 
            s7 = False
        if hx:
            window.blit(pygame.transform.scale(x, (100,100)), (353,560))  
            s8 = False
        if ix:
            window.blit(pygame.transform.scale(x, (100,100)), (521,560))
            s9 = False
        
        if ao:
            window.blit(pygame.transform.scale(o, (100,100)), (185,230))
            s1 = False       
        if bo:
            window.blit(pygame.transform.scale(o, (100,100)), (353,230))
            s2 = False    
        if co:
            window.blit(pygame.transform.scale(o, (100,100)), (521,230))  
            s3 = False       
        if do:
            window.blit(pygame.transform.scale(o, (100,100)), (185,400))  
            s4 = False       
        if eo:
            window.blit(pygame.transform.scale(o, (100,100)), (353,400))
            s5 = False      
        if fo:
            window.blit(pygame.transform.scale(o, (100,100)), (521,400)) 
            s6 = False     
        if go:
            window.blit(pygame.transform.scale(o, (100,100)), (185,560)) 
            s7 = False      
        if ho:
            window.blit(pygame.transform.scale(o, (100,100)), (353,560))
            s8 = False       
        if io:
            window.blit(pygame.transform.scale(o, (100,100)), (521,560)) 
            s9 = False     
        
        if row1 == 3:
            window.blit(pygame.transform.scale(hline, (630,240)), (75,160))
            window.blit(player1Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False
                
        if row2 == 3:
            window.blit(pygame.transform.scale(hline, (630,240)), (75,330))
            window.blit(player1Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False            
        if row3 == 3:
            window.blit(pygame.transform.scale(hline, (630,240)), (75,490))
            window.blit(player1Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False            
        if column1 == 3:
            window.blit(pygame.transform.scale(vline, (240,630)), (116,130))
            window.blit(player1Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False            
        if column2 == 3:
            window.blit(pygame.transform.scale(vline, (240,630)), (284,130))
            window.blit(player1Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False            
        if column3 == 3:
            window.blit(pygame.transform.scale(vline, (240,630)), (452,130)) 
            window.blit(player1Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False            
        if diagonal1 == 3:
            window.blit(pygame.transform.scale(dline1, (1000,1000)), (-80,-40))
            window.blit(player1Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False            
        if diagonal2 == 3:
            window.blit(pygame.transform.scale(dline2, (1000,1000)), (-80,-70))
            window.blit(player1Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False            
        
        if row1 == 15:
            window.blit(pygame.transform.scale(hline, (630,240)), (75,160))
            window.blit(player2Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False            
        if row2 == 15:
            window.blit(pygame.transform.scale(hline, (630,240)), (75,330))
            window.blit(player2Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False             
        if row3 == 15:
            window.blit(pygame.transform.scale(hline, (630,240)), (75,490))
            window.blit(player2Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False             
        if column1 == 15:
            window.blit(pygame.transform.scale(vline, (240,630)), (116,130))
            window.blit(player2Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False             
        if column2 == 15:
            window.blit(pygame.transform.scale(vline, (240,630)), (284,130))
            window.blit(player2Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False             
        if column3 == 15:
            window.blit(pygame.transform.scale(vline, (240,630)), (452,130))
            window.blit(player2Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False             
        if diagonal1 == 15:
            window.blit(pygame.transform.scale(dline1, (1000,1000)), (-80,-40))
            window.blit(player2Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False             
        if diagonal2 == 15:
            window.blit(pygame.transform.scale(dline2, (1000,1000)), (-80,-70))
            window.blit(player2Wins, (290,730))
            if t<500:
                t += 1
            else:
                play = False   
        if turn == 10:
            window.blit(draw, (355,730))
            if t<500:
                t += 1
            else:
                play = False              

    b+=moveb
    a+=movea
    pygame.display.flip()
    pygame.display.update()
pygame.quit()