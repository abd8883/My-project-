import pygame,random
from pygame.math import Vector2
import copy

pygame.mixer.init()
IN_Game   = True
out_of_game = False
win_the_game = False
GAME = True
SOCER = 0
DIC_UP = Vector2(0,-1) 
DIC_DOWN = Vector2(0,1)
DIC_RIGHT = Vector2(1,0)
DIC_LEFT =  Vector2(-1,0)   
random_dichr = [DIC_UP,DIC_DOWN,DIC_LEFT]
random_dichl =  [DIC_UP,DIC_DOWN,DIC_RIGHT]
random_dicvu = [DIC_DOWN,DIC_RIGHT,DIC_LEFT]  
random_dicvd = [DIC_UP,DIC_RIGHT,DIC_LEFT]  
MIN_POSITION = 3
MAX_POSITION = 12
SECOND_PORTION = 2
FIRST_PORTION = 1 
game_over = False
win_the_game_sound = pygame.mixer.Sound("goodresult-82807.mp3")
game_over_sound = pygame.mixer.Sound("negative_beeps-6008.mp3")
class MAIN: 
  def __init__(self):
    self.apple = APPLE()
    self.snake = SNAKE()
  def elements(self):
    self.apple.our_apple()
    self.snake.our_snake()
  def move(self):
    self.snake.move()
  def eaten(self):
    if self.apple.apples == self.snake.body[0]:
      self.apple.where_the_apple()
      self.snake.increes_size()
      self.snake.snake_sound.play()
    for block in self.snake.body[1:]:
      if block == self.apple.apples:
         self.apple.where_the_apple()
  def eat_self(self):
    for block in self.snake.body[1:]:
      if block == self.snake.body[0]:
         return True
  
  def directions(self):
    if self.snake.body[0].x < self.snake.body[1].x:
      return "left"
    elif self.snake.body[0].x > self.snake.body[1].x:
      return "right"
    elif self.snake.body[0].y < self.snake.body[1].y:
      return "up"
    else:
      return "down"
  def border(self):
      if self.snake.body[0].x > cell_num - 1 or self.snake.body[0].x < 0 or self.snake.body[0].y > cell_num - 1 or self.snake.body[0].y < 0:
          return True
   
  def score(self):
    font = pygame.font.SysFont('arial', 30)
    SOCER = font.render(f" Score : {len(self.snake.body) - 3}", True, pygame.Color('black'))
    screen.blit(SOCER,(10,10))
  def reset(self):
   self.snake.create_body()
  def game_over_instruction(self):
    screen.fill('white')
    font = pygame.font.SysFont('freesansbold', 30)
    font2 = pygame.font.SysFont('freesansbold', 50)
    game_over_surface = font2.render("Game Over", True, pygame.Color('red'))
    game_over_rect = game_over_surface.get_rect()
    game_over = font.render("Press c for continue and q for quit.", True, pygame.Color('red'))
    text_rect = game_over.get_rect()
    text_rect.center = (width/2, height/2)
    game_over_rect.center = (width/2, height/2 - text_rect.height/2 - 30)
    screen.blit(game_over, text_rect)
    screen.blit(game_over_surface, game_over_rect)
  def win(self):
    return len(self.snake.body) - 3 == 30
  def win_the_game_instruction(self):
    screen.fill('gray')
    font = pygame.font.SysFont('freesansbold', 30)
    font2 = pygame.font.SysFont('freesansbold', 50)
    win_the_game_surface = font2.render("You win !", True, pygame.Color('white'))
    win_the_game_rect = win_the_game_surface.get_rect()
    game_over = font.render("Press c for continue and q for quit.", True, pygame.Color('white'))
    text_rect = game_over.get_rect()
    text_rect.center = (width/2, height/2)
    win_the_game_rect.center = (width/2, height/2 - text_rect.height/2 - 30)
    trophy_rect = trophy.get_rect()
    trophy_rect.center = (win_the_game_rect.centerx, win_the_game_rect.centery - trophy_rect.height + 50)
    screen.blit(game_over, text_rect)
    screen.blit(win_the_game_surface, win_the_game_rect)
    screen.blit(trophy, trophy_rect)
      
class APPLE:
  def __init__(self):
     self.where_the_apple()
     self.APPLES = pygame.image.load('APPLE.jpg').convert_alpha()
  def our_apple(self):
    apple = pygame.Rect(self.P1,self.P2,cell_size,cell_size)
    screen.blit(self.APPLES,apple)
  def where_the_apple(self):
     self.x = random.randint(0, cell_num - 1)                
     self.y = random.randint(0, cell_num - 1)    
     self.apples = Vector2(self.x,self.y)
     self.P1 = int(self.apples.x) *cell_size
     self.P2 = int(self.apples.y) *cell_size
 
    
    

class SNAKE:
  def __init__(self):
     self.horizontal_vertical = ['Horizontal','vertical']
     self.horizontal_vertical = random.choice(self.horizontal_vertical)
     self.y = random.randint(3,11)
     self.x = random.randint(3,11)
     self.create_body()
     self.BODY_BOTTOMLEFT = pygame.image.load('body_bottomlefty.jpg').convert_alpha()
     self.BODY_BOTTOMRIGHT = pygame.image.load('body_bottomrighty.jpg').convert_alpha()
     self.BODY_HORIZONTAL = pygame.image.load('body_horizontaly.jpg').convert_alpha()
     self.BODY_TOPLEFTY = pygame.image.load('body_toplefty.jpg').convert_alpha()
     self.BODY_TOPRIGHT = pygame.image.load('body_toprighty.jpg').convert_alpha()
     self.BODY_VIRTICAL = pygame.image.load('body_verticaly.jpg').convert_alpha()
     self.HEAD_DOWN = pygame.image.load('head_downy.jpg').convert_alpha()
     self.HEAD_LEFT = pygame.image.load('head_lefty.jpg').convert_alpha()
     self.HEAD_RIGHT = pygame.image.load('head_righty.jpg').convert_alpha()
     self.HEAD_UP = pygame.image.load('head_upy.jpg').convert_alpha()
     self.TAIL_DOWN = pygame.image.load('tail_downy.jpg').convert_alpha()
     self.TAIL_LEFT = pygame.image.load('tail_lefty.jpg').convert_alpha()
     self.TAIL_RIGHT = pygame.image.load('tail_righty.jpg').convert_alpha()
     self.TAIL_UP = pygame.image.load('tail_upy.jpg').convert_alpha()
     self.snake_sound = pygame.mixer.Sound('20279__koops__apple_crunch_16.wav')

  def our_snake(self):
    for block in self.body:
        self.snake_head()
        body_ = pygame.Rect(int(block.x) * cell_size,int(block.y) * cell_size ,cell_size,cell_size)
        if block == self.body[0]:
          screen.blit(self.head,body_)
        elif block == self.body[len(self.body) - 1]:
          self.snake_tail(block)
          screen.blit(self.tail,body_)
        else:
           index = self.body.index(block)
           front = self.body[index + 1] - block
           back = self.body[index - 1] - block
           if front.x == back.x:
             screen.blit(self.BODY_VIRTICAL,body_)
           elif front.y == back.y:
             screen.blit(self.BODY_HORIZONTAL,body_)
           elif back.x == -1 and front.y == -1 or back.y == -1 and front.x == -1:
             screen.blit(self.BODY_TOPLEFTY,body_)
           elif  back.y == -1 and front.x == 1 or back.x == 1 and front.y == -1:
             screen.blit(self.BODY_TOPRIGHT,body_)
           elif back.y == 1 and front.x == 1 or back.x == 1 and front.y == 1:
             screen.blit(self.BODY_BOTTOMRIGHT,body_)
           else:
              screen.blit(self.BODY_BOTTOMLEFT,body_)
        # pygame.draw.rect(screen,pygame.Color('red'),body_)
                 
               
  def move(self):  
      body = copy.deepcopy(self.body[:-1])
      self.body[0] += self.direction 
      self.body[1:] = body
      
      

  def increes_size(self):
      body = copy.deepcopy(self.body)
      self.body[0] += self.direction 
      self.body[1:] = body
  def create_body(self):   
    self.x_choose = random.randint(0,1)
    self.y_choose = random.randint(0,1)
    if self.horizontal_vertical == 'Horizontal' and self.x_choose == 0: 
        self.body = [Vector2(self.x + SECOND_PORTION,self.y),Vector2(self.x + FIRST_PORTION,self.y),Vector2(self.x,self.y)]
        self.direction = random.choice(random_dichl)
    elif self.horizontal_vertical == 'Horizontal' and self.x_choose == 1 :
        self.body = [Vector2(self.x,self.y),Vector2(self.x + FIRST_PORTION,self.y),Vector2(self.x + SECOND_PORTION,self.y)]   
        self.direction = random.choice(random_dichr)
    elif self.horizontal_vertical =='vertical ' and self.y_choose == 0:
        self.body = [Vector2(self.x,self.y + SECOND_PORTION),Vector2(self.x,self.y + FIRST_PORTION),Vector2(self.x,self.y)]
        self.direction = random.choice(random_dicvu)
    else:
        self.body = [Vector2(self.x,self.y),Vector2(self.x,self.y + FIRST_PORTION),Vector2(self.x,self.y + SECOND_PORTION)]
        self.direction = random.choice(random_dicvd)
  def snake_head(self):
    if self.body[0].x == self.body[1].x and self.body[0].y > self.body[1].y:
        self.head = self.HEAD_DOWN
    elif self.body[0].x == self.body[1].x and self.body[0].y < self.body[1].y:
       self.head = self.HEAD_UP
    elif self.body[0].y == self.body[1].y and self.body[0].x > self.body[1].x:
        self.head = self.HEAD_RIGHT
    else :
        self.head = self.HEAD_LEFT
        
        
  def snake_tail(self,block):
    if block.x == self.body[-2].x and block.y > self.body[-2].y:
        self.tail = self.TAIL_DOWN
    elif block.x == self.body[-2].x and block.y < self.body[-2].y:
       self.tail = self.TAIL_UP
    elif block.y == self.body[-2].y and block.x > self.body[-2].x:
        self.tail = self.TAIL_RIGHT
    else :
        self.tail = self.TAIL_LEFT
    

pygame.init()

# display surface of my game
cell_num,cell_size = 15,40
width = cell_num * cell_size
height = cell_num * cell_size
display = (width, height)
screen = pygame.display.set_mode(display)
pygame.display.set_caption('Snake Game')
# def our_grid():
clock_rate = pygame.time.Clock()

main = MAIN()

trophy = pygame.image.load('trophy-png-30577.png').convert_alpha()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,100) 


while GAME:
    while out_of_game:
      for event in pygame.event.get():
            # checks if the current event is a QUIT event
              if event.type == pygame.QUIT:
                 out_of_game = False  
                 GAME = False
              if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                  out_of_game = False  
                  GAME = False
                elif event.key == pygame.K_c:
                  out_of_game = False  
                  IN_Game = True
      main.game_over_instruction()
      pygame.display.update()
      clock_rate.tick(30)
      

    while win_the_game:
         for event in pygame.event.get():
            # checks if the current event is a QUIT event
              if event.type == pygame.QUIT:
                 win_the_game = False  
                 GAME = False
              if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                  win_the_game = False  
                  GAME = False
                elif event.key == pygame.K_c:
                  win_the_game = False  
                  IN_Game = True    
         main.win_the_game_instruction()
         pygame.display.update()
         clock_rate.tick(30)  
    while IN_Game:  
        for event in pygame.event.get():
            # checks if the current event is a QUIT event
              if event.type == pygame.QUIT:
                  #out from program
                  GAME = False
              if event.type == SCREEN_UPDATE:
                    main.move()   
              if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_UP and not main.directions() == 'down':
                    main.snake.direction = DIC_UP  
                  elif event.key == pygame.K_DOWN and not main.directions() =='up':
                    main.snake.direction = DIC_DOWN
                  elif event.key == pygame.K_RIGHT and not main.directions() =='left':
                      main.snake.direction = DIC_RIGHT  
                  elif event.key == pygame.K_LEFT and not main.directions() == 'right':
                      main.snake.direction = DIC_LEFT
    
        screen.fill('white')
        main.elements()
        main.eaten()
        if main.border():
           main.reset()
           game_over_sound.play()
           IN_Game = False
           out_of_game = True
        if main.eat_self():
          main.reset()
          game_over_sound.play()
          IN_Game = False
          out_of_game = True
        if main.win():
          main.reset()
          win_the_game_sound.play()
          IN_Game = False
          win_the_game = True
        main.score()
        pygame.display.update()
        clock_rate.tick(30)

    




