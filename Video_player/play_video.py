import pygame, sys
from video_player import Video


def Play(option=1):
    pygame.init()
    ## Enter your Video actuall path or relative path
    if(option==1):     
        pygame.display.set_caption("pal tu pal")
        vid = Video("Video\\Pal tu pal.mp4")
    elif(option==2):     
        pygame.display.set_caption("Phenix")
        vid = Video("Video\\Phenix.mp4")
    elif(option==3):     
        pygame.display.set_caption("Suna Hai")
        vid = Video("Video\\Suna Hai.mp4")
    elif(option==4):     
        pygame.display.set_caption("Symphony")
        vid = Video("Video\\Symphony.mp4")
    elif(option==5):     
        pygame.display.set_caption("Ghost")
        vid = Video("Video\\Ghost.mp4")
    elif(option==6):     
        pygame.display.set_caption("kaise hua")
        vid = Video("Video\\kaise hua.mp4")
    elif(option==7):     
        pygame.display.set_caption("CONTROL")
        vid = Video("Video\\CONTROL.mp4")
    elif(option==8):     
        pygame.display.set_caption("Stronger")
        vid = Video("Video\\Stronger.mp4")
    elif(option==9):     
        pygame.display.set_caption("Aigiri Nandini")
        vid = Video("Video\\Aigiri Nandini.mp4")
    elif(option==0):     
        pygame.display.set_caption("Deva Shree Ganesha")
        vid = Video("Video\\Deva Shree Ganesha.mp4")
    else:     
        pygame.display.set_caption("Shiv Tandav")
        vid = Video("Video\\Shiv Tandav.mp4")


    #* play the selected video 
    WIDTH, HEIGHT = 936, 637
    # pWIDTH, pHEIGHT = WIDTH, HEIGHT
    vol = 0.2
    on_volume = True

    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT),pygame.RESIZABLE)
    while True:
        
        if(on_volume):
            vid.set_volume(vol)
            on_volume=False
        vid.draw(SCREEN, (0, 0))
        vid.set_size((WIDTH, HEIGHT))
        pygame.display.update()
        WIDTH, HEIGHT = pygame.display.get_window_size()
        
        
        for event in pygame.event.get():
            if(vid.finish()):
                vid.close()
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.toggle_pause()
        ## checking if you press the X symbol of window
            if event.type == pygame.QUIT:
                vid.close()
                pygame.quit()
                sys.exit()
            
		## checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:
			
                if event.key == pygame.K_BACKSPACE:
                    vid.close()
                    pygame.quit()
                    return
                    
                if event.key == pygame.K_r:
                    vid.restart()
                    on = True
			
                if event.key == pygame.K_j:
                    vid.seek(-10)
                if event.key == pygame.K_k or event.key == pygame.K_SPACE:
                    vid.toggle_pause()    
                if event.key == pygame.K_l:
                    vid.seek(+10)
                
                if event.key == pygame.K_h:
                    vol += 0.05
                    on_volume =True
                if event.key == pygame.K_n:
                    vol -= 0.05
                    on_volume = True
                if event.key == pygame.K_m:
                    if(vol>0):
                        vol=0
                    else:
                        vol=0.3
                    on_volume = True


                if event.key == pygame.K_o:
                    vid.get_playback_data()
                    print(pygame.display.get_window_size())
                    
                # if event.key == pygame.K_f:       # issue fix on Video player
                #     if((WIDTH,HEIGHT) != (1536, 937)):
                #         SCREEN = pygame.display.toggle_fullscreen()
                #         pWIDTH, pHEIGHT = WIDTH, HEIGHT
                #         WIDTH, HEIGHT = 1536, 937
                #     else:
                #         WIDTH, HEIGHT = pWIDTH, pHEIGHT
                        
                    
                    
                
                

                
