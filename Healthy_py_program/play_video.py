import pygame, sys
from video_player import Video
pygame.init()
WIDTH, HEIGHT = 900, 600


def Play(option=1):
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    vol = 0.3
    if(option==1):     
        pygame.display.set_caption("pal tu pal")
        vid = Video("C:\\Users\\debra\Videos\\Editing video\\Pal tu pal AMV - Made with Clipchamp.mp4")
        vid.set_size((WIDTH, HEIGHT))
    elif(option==2):
        pygame.display.set_caption("Suna Hai")
        vid = Video("C:\\Users\\debra\Videos\\Editing video\\Suna Hai AMV - Made with Clipchamp.mp4")
        vid.set_size((WIDTH, HEIGHT))
    else:
        pygame.display.set_caption("Stronger")
        vid = Video("C:\\Users\\debra\Videos\\Editing video\\Stronger_my_editing_soguna - Made with Clipchamp.mp4")
        vid.set_size((WIDTH, HEIGHT))
    vid.set_volume(vol)
    #* play the selected video 
    while True:
        vid.draw(SCREEN, (0, 0))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.toggle_pause()
        ## checking if you press the X symbol of window
            if event.type == pygame.QUIT:
                vid.close()
                pygame.quit()
                return
		## checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:
			
			# checking if key "A" was pressed
                if event.key == pygame.K_k:
                    vid.toggle_pause()
                
                if event.key == pygame.K_BACKSPACE:
                    vid.close()
                    pygame.quit()
                    return
                    
                if event.key == pygame.K_r:
                    vid.restart()
			
                if event.key == pygame.K_j:
                    vid.seek(5)
                    
                if event.key == pygame.K_l:
                    vid.seek(-5)
                
                if event.key == pygame.K_h:
                    vol += 0.1
                    vid.set_volume(vol)
                
                if event.key == pygame.K_m:
                    vol -= 0.1
                    vid.set_volume(vol)
                
                if event.key == pygame.K_o:
                    vid.get_playback_data()
    
    
        
# sys.exit()