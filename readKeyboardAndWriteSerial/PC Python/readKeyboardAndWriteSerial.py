import pygame
import time
import serial


def main():

    lastCode = 0
    code = 0
    
    radius = 15
    x = 30
    y = 30
    
    dx = 2;
    dy = 2 ;
    color = ( 255, 0, 0 )
    points = []

    left    = 0
    right   = 0
    forward = 0
    reverse    = 0

    port = "COM5"
    pygame.init()
    ser = serial.Serial( port, 115200, timeout=0.1)

    # open pygame window
    screen = pygame.display.set_mode((640, 480))
    
    # clear the screen
    screen.fill((0, 0, 0))

    clock = pygame.time.Clock()

    
    while True:
        for event in pygame.event.get():

            # determin if exit is requested
            if event.type == pygame.QUIT:
                ser.close()
                exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    ser.close()
                    exit(0)

                # movement keys 
                if event.key == pygame.K_LEFT:
                    left = 1                    
                if event.key == pygame.K_RIGHT:
                    right = 1                    
                if event.key == pygame.K_UP:
                    forward = 1                    
                if event.key == pygame.K_DOWN:
                    reverse = 1                    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    return
                
                # movement keys 
                if event.key == pygame.K_LEFT:
                    left = 0
                if event.key == pygame.K_RIGHT:
                    right = 0                    
                if event.key == pygame.K_UP:
                    forward = 0                    
                if event.key == pygame.K_DOWN:
                    reverse = 0                    

        if( left == right and left == 1 ) or ( forward == reverse and reverse == 1 ):
            print( 'Invalid command' )
        else :
            delX = dx*( right - left );
            delY = dy*( reverse - forward )
            
        pygame.draw.circle(screen, (0,0,0), (x, y), radius )
        x = x + delX;
        y = y + delY;
        pygame.draw.circle(screen, color, (x, y), radius )
        
        pygame.display.flip()

        code = chr ( 65 + 2**3*left + 2**2*right + 2**1*forward + 2**0*reverse );

        if ( lastCode != code ) :
            ser.write( code.encode() )
            lastCode = code

        time.sleep(0.1)

        clock.tick(60)
main()
