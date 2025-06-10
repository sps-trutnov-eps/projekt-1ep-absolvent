import pygame
keys = pygame.key.get_pressed()        
            if keys[pygame.K_KP8]:
                
                x-=1
                print(x)
            if keys[pygame.K_KP2]:
                x+=1
                print(x)
            if keys[pygame.K_KP4]:
                y-=1
                print(y)
            if keys[pygame.K_KP6]:
                y+=1
                print(y)
