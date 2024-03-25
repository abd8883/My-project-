# Snake Game

## Video Demo: <https://youtu.be/4DIRjJdpe3g?si=VHrBWymKegKCCpLr>

### Description

My project is a simple snake game written in Python using pygame library where when a snake eats an apple it gets longer and your score increases. If your snake hits any part of its body it will die.

pygame is a library that handles the backend of the game it reduces the complexity for the developer to write code for the game.

#### steps of my code

1. import the pygame module,random module, copy module and Vector2 from pygame library:

   - Vector2: is a two-dimensional vector that is used to represent the different parts of the snake body.

       - **simple example of how Vector2 represent the parts of the snake body is shown below:**
       `self.body = [Vector2(40,50),Vector2(39,50),Vector2(38,50)]` this code represent the snake body as a list of Vector2 objects where `Vector2(40,50)` represent the head, the snakehead direction to the left, `Vector2(39,50)` represent the middle part of the snake and `Vector2(38,50)` represent the tail of the snake body.

       - why I am using Vector2 :
          - I am using Vector2 because it is easy to manipulate and it supports mathematical operations      between vector objects this will help me to change the direction of the snake and its length.

2. implement main class,snake class and apple class:
I am using class to make my code tidy, convenient to read hide the complexity of certain operations, and provide a simple interface for users or other parts of the program.

   - MAIN class:

     - have several methods :

          1- `__init__` to create apple and snake object

          2- `elements` method to draw the snake,apple by calling the method of the snake and apple class.

          3- `move` method to move the snake by calling move methods in snake class.

          4- `eaten` method to check if the snake ate the apple the logic of this method is to check if the head of the snake is equal to the apple's position.

          5 - `eat_self` method to check if the head of the snake is equal to any part's position of the snake.

          6 - `directions` method to return the direction of the snake by comparing the first element of a snake with the second one. simple example to understand what I mean: the head element is the first element of the list of vectors when the x coordinate of the head less than the x coordinate of the second element means that the head is to the left of the second element which means snake in the left direction.

          7 -  `border` method to check if the head of the snake is touching the border of the screen. a simple example to understand how the method is working: `self.snake.body[0].x > cell_num - 1` cell_num is the number of cells in the screen I subtract the cell_num by one because the index starts from zero when `self.snake.body[0].x` which is the head be more than the cell_num - 1 which mean the head touches the right border of the screen and the same logic for the other borderes.

          8 - `score` method to increase the score each time the snake eats the apple and view the result on the screen. the score is the length of the snake minus three the reason why I am subtracting by three is that the length starts from 3 vectors so each time the snake eats the apple the length will increase and because the score is equal to length minus three the score will increase by one each time the snake eat the apple.

          9 - `reset` method to create a new body of the snake this method is used when the player wins or loses to ensure that when a player wants to play the game again the snake length is 3 which is the initial length of the snake.

          10 - `game_over_instruction` method to display the game over  screen when the snake hits the wall or hits itself.

          11 - `win` method returns if the score reaches the maximum score which is 30.

          12 - `win_the_game_instruction` method to display the win screen when a player reaches the maximum score.
   - APPLE class:
     - have several methods:
        
          1 - `__init__`  in the init method, I call the where_the_apple() method which randomly chooses a position of the apple and I load an image of my apple.

          2 - `our_apple` method to draw the apple on the screen by first creating an apple object by giving an apple-specific location on the screen and then drawing an image of the apple which I loaded in the `__init__` method in the specific location.

          3 - `where_the_apple` method to randomly choose a position of the apple on the screen.
   - SNAKE class:
      - have several methods:
              1 - `__init__` in the init method, I define horizontal_vertical which randomly chooses a vertical or horizontal direction for the snake also I define x and y coordinates which I will use to choose the initial direction of the snake and I call the create_body method which creates a list of vectors that represents snake body, I load all images of the snake body of the snake has more than one images to represent all possible movement of the snake last thing in the `__init__` method I load a sound represents the sound of the snake when eating the apple.    
              2-`move` the method changes the direction of the snake in each movement by copying all part of the snake except the last element to a new list then changing the head direction to the new direction then adding the new head to the new list this give the illusion of movement.
              3-`increes_size` this method increases the size of the snake each time it eats an apple it works with the same logic as the move method except that the new list we created is equal to all elements plus the head.
              4 - `our_snake`  method to drawing the snake this method works by seeing first the direction of the snake and then drawing a body with images that represent this specific direction of the snake.

              simple example of how our_snake method works:
              first, the program looping through all vectors of the list which represents the body of the snake.

              supposed self. body equal to [Vector2(10,10), Vector2(11,10), Vector2(12,10), Vector2(13,10), Vector2(13,9)] the length of this snake is 5 so the head is Vector2(10,10) first of all we call the snake_head method which returns the Optimal head image with this head Vector by compare first Vector with the second Vector in our case the head is to the left of the second Vector so the Snake_head will return image of the snake head looking to the left.
              
              after that block will equal the second element of the list which is Vector2(11,10) in this case we create two Vectors the first one equal to Vector following the Vector2(11,10) which is Vector2(12,10) and the second one equal to Vector behind Vector2(11,10) which is equal to the head's  Vector (10,10) if the y coordinate of the new Vectors is equal to each other this means the optimal image of Vector2(11,10) is BODY_VIRTICAL which is true in this case .

              at last  all block work at same way except the last block will work as same of head logic.

              The rest of the methods explanations are implicit in the previous explanation.               
  
 3.  The main loop of the game which devied in three parts as follows:
  
      - game over loop: this loop is used to display the game over screen when the snake hits the wall or hits itself.
  
      - win loop: this loop is to display the screen when the player wins the game.
      - game loop : this loop is for the game itself for example when the user press the left key it decides   where the snake goes or when the snake eats an apple all of that will happen all of this in a game loop.

Important stuff that pygame provides to us:

1. `pygame.init` function that initializes all things that we need to use pygame from functions to objects without it we can't build a game by pygame so we need to call this function before we start using pygame.
2. `pygame.display.set_mode((width, height))`: it returns a surface object which is a window that we draw every element of the game like a snake or apple on it.
3. `clock_rate = pygame. time.Clock()` creates an object called clock_rate, which has several methods to control the time in the game in my example I am using `clock_rate.tick(30)` which means that the game will run at 30 frames per second to ensure that every computer is suitable to run the game in the same speed.  
4. `pygame.display.set_caption('Snake Game')` This method gives my game a title.
5. `pygame.image.load('trophy-png-30577.png').convert_alpha()` `loading an image in my program.
6. `SCREEN_UPDATE = pygame.USEREVENT` creating my event.
7. `pygame.time.set_timer(SCREEN_UPDATE,100) ` this code sends my event every 100 ms to the event queue.
8. `for event in pygame.event.get()` loop through all events in the queue.
9. `if event.type == pygame.any_event` any_event is not a real event I created it to explain how this code works this code checks if the event is equal to any_event if it is true then the compiler executes the code inside the if statement.
10. `pygame. KEYDOWN` type of event to check if the player presses any keyboard key.
11. ` if event.key == pygame.K_q` This code checks if the player presses the q key and this code is inside the `if event.type == pygame.KEYDOWN:` in conclusion, this code checks if the user presses any key and then looks at which key the player pressed.
12. `pygame.display.update()` This code updates the screen every loop to check the new change of the game appears on the screen .
13. ` screen.fill('white')` this code fills the screen with white color.

**All variables I  used in my game**:

1. `IN_Game` : boolean variable if it's true which means my game now runs and the user does not win or lose but still plays.
2. `out_of_game`: boolean variable if it's true which means the user has lost the game by hitting the border of the screen or hitting itself.
3. `win_the_game`: boolean variable if it's true which means the user earns 30 scores.
4. `GAME` :boolean variable if it's true which means the game is running regardless if the player won or lost or still plays this main loop of the game.
5. these variables equal the value that will be assigned to `self. direction` to change the direction of the snake when the player presses any key from the (up, down, right, left) keys in the keyboard.
```
DIC_UP = Vector2(0,-1) 
DIC_DOWN = Vector2(0,1)
DIC_RIGHT = Vector2(1,0)
DIC_LEFT =  Vector2(-1,0) 
```
6. these listes equal to all possible randoms direction when the game start. these lists equal to all possible random directions when the game starts that are assigned to `self. direction`.
```
random_dichr = [DIC_UP,DIC_DOWN,DIC_LEFT]
random_dichl =  [DIC_UP,DIC_DOWN,DIC_RIGHT]
random_dicvu = [DIC_DOWN,DIC_RIGHT,DIC_LEFT]  
random_dicvd = [DIC_UP,DIC_RIGHT,DIC_LEFT]  
```

