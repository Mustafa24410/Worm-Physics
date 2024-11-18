import pygame

# Color Constants
BLACK = (20, 20, 20)
WHITE = (210, 210, 210)
GREY = (125, 125, 125)

# Initaization
pygame.init()
clock = pygame.time.Clock()
run = True

# Screen
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Worm Physics')
h = screen.get_height()
w = screen.get_width()

# Worm Class
class Worm():
    def __init__(self, start_pos, nodes, length):

        # Error catching for obvious purposes
        if nodes <= 0:
            raise Exception('Nodes cannot be less than or equal to 0')
        else:
            self.nodes = nodes

        self.length = length
        self.nodes = []

        # self.nodes[0]   -->  Head of Worm
        # self.nodes[-1]  -->  Tail of Worm
        # Adjacent elements are connected with segmet of length self.length
        # Initialization orientation is a straight line with head at start_pos

        for i in range(nodes):
            self.nodes.append(pygame.FRect([start_pos[0]-i*self.length, start_pos[1]], [15, 15]))
    
    def draw(self, node_color, segment_color):

        # First draw segments then nodes cuz then it looks goofy ahh

        for i in range(1, len(self.nodes)):
            pygame.draw.line(screen, segment_color, self.nodes[i].center, self.nodes[i-1].center, 7)
        for i in range(len(self.nodes)):
            pygame.draw.circle(screen, node_color, self.nodes[i].center, self.nodes[i].w/2)
    
    def update(self, speed):
        
        # The most IMPORTANT function of them worm
        # This function makes the worm all wiggly and jiggly

        for i in range(1, len(self.nodes)):
            vector = pygame.Vector2(self.nodes[i-1].centerx-self.nodes[i].centerx, self.nodes[i-1].centery-self.nodes[i].centery)
            if self.length*1.1 >= int(vector.length()) >= self.length/1.1:
                continue
            if int(vector.length()) > self.length:
                self.nodes[i].center += vector.normalize()*speed
            elif int(vector.length()) < self.length:
                self.nodes[i].center -= vector.normalize()*speed

worm = Worm([w/2, h/2], 10, 25)
speed = 4
mov_vect = pygame.Vector2(0, 0)

while run:
    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mov_vect = pygame.math.Vector2([0, 0])
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        mov_vect.x += speed
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        mov_vect.x -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        mov_vect.y += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        mov_vect.y -= speed
    if abs(mov_vect.x) == abs(mov_vect.y) and mov_vect.length() != 0:
        mov_vect = mov_vect.normalize()*speed
    worm.nodes[0].center += mov_vect

    screen.fill(BLACK)
    worm.draw(WHITE, GREY)
    worm.update(speed)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()