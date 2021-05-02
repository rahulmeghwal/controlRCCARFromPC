import pygame
import time
import serial


def main():

    lastCode = 0
    code = 0
    # Just draw a circle on screen to see of out key movements are being captured by python or not
    # circle features
    x = 30
    y = 30
    radius = 15
    color  = ( 255, 0, 0 )
    
    # speed of circle
    dx = 2;
    dy = 2;

    # variable for keys pressed
    left    = 0
    right   = 0
    forward = 0
    reverse = 0

    # You will have to change this to the port where arduino is connected
    port = "COM5"
    # open serial port
    ser = serial.Serial( port, 115200, timeout=0.1)
    
    # Intialize pygame
    pygame.init()
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
        # Draw black circle(since background is black) at last location    
        pygame.draw.circle(screen, (0,0,0), (x, y), radius )
        x = x + delX;
        y = y + delY;
        
        # Draw red circle at new location    
        pygame.draw.circle(screen, color, (x, y), radius )
        
        pygame.display.flip()

        code = chr ( 65 + 2**3*left + 2**2*right + 2**1*forward + 2**0*reverse );
        
        # write to serial - if there is a change in the state of keys
        if ( lastCode != code ) :
            ser.write( code.encode() )
            lastCode = code

        time.sleep(0.1)

        clock.tick(60)
main()
