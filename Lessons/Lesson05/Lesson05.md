<div>

<p>
<img align=left src="images/ckcslogo.png">
</p>

---

<p>
<H1 align=left><a href="http://www.coolkidscodingschool.com">Cool Kids Coding School</a></H1>
<H2 align=left>Course: <strong>Game Programming</strong></H1>
<H3 align=left>Lesson 5: <strong>Working with Sprites</strong></H3>
</p>

</div>

---


> 1.0 Overview

In this lesson we are going to start discussing the use of sprites in our game development.  The term "sprite" is a holdover from older computer and game machines. These older computers were unable to draw and erase graphics fast enough for them to work as games. These machines had special hardware to handle game like objects that needed to animate very quickly. These objects were called "sprites" and had special limitations, but could be drawn and updated very fast. These days computers have become generally fast enough to handle sprite like objects without dedicated hardware.

> 2.0 Review

In the last lesson we discussed the following, lets review.  

+ We talked about the problems of representing complicated data structures, Students and ClassSubjects  
+ We discussed how python introduced the concept of a class that allows us to create custom data types.
+ We discussed how the class is the blueprint used when python created an object, or an instance, of this class.
+ We showed how these data types can have attributes that represent the attributes of the object we are trying to model.
+ We then discussed how objects aside from having attributes also can have methods, or functions that belong to a class.  These methods give our class the ability to have a certain behavior.
+ Finally we discussed how classes are allowed to inherit attributes and methods from a parent.

> 3.0 The Classes

In python the sprite module comes with two main classes.  The first is the Sprite which should be used as a base class for all our game objects.  This class has several methods to help manage the game object.  The other type of class is the Group class.  The Group class is a container (like a list) for different Sprite objects.  This is all there really is to it.  We'll start with a description of what each type of class does, and then discuss the proper ways to use these classes.

> 4.0 What is a sprite?

A sprite is a computer graphics term for any object on the screen that can move around. When you play any 2D game, all the objects you see on the screen are sprites. Sprites can be animated, they can be controlled by the player, and they can even interact with each other.

We will take care of updating and drawing our sprites in the UPDATE and DRAW sections of our game loop. But you can probably imagine, if your game has a large number of sprites then these sections of your game loop could get very long and complicated. Fortunately, Pygame has a good solution for this: the sprite group.

A sprite group is just a collection of sprites that you can act on all at the same time. Let’s make a sprite group to hold all the sprites in our game:

```python
clock = pygame.time.Clock()
 all_sprites = pygame.sprite.Group()
```

Now we can take advantage of the group by adding the following in our game loop:

```python
    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
```

Now for every sprite that we create we just make sure we add it to the all_sprites group, and it will automatically be drawn on the screen and updated each time through the loop.

> 4.1 Creating a sprite

Now we’re ready to make our first sprite. In Pygame, sprites are objects. We start by defining our new sprite:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect() 
```

class tells Python we’re defining a new object, which is going to be our player sprite, and its type is pygame.sprite.Sprite, which means it will be based on Pygame’s pre-defined Sprite class.

The first bit of code we need in a class definition, is the special __init__() function, which defines what code will run whenever a new object of this type is created. There are also two properties that every Pygame sprite must have: an image and a rect:

The first line, pygame.sprite.Sprite.__init__(self) is required by Pygame - it runs the built-in Sprite classes initializer. Next, we define the image property - in this case, we’re just creating a simple 50 x 50 square and filling it with the color GREEN. Later we’ll learn how to make the sprite’s image be something fancier, like a character or spaceship, but a solid square is good enough for now.

Next, we must define the sprite’s rect, which is short for “rectangle”. Rectangles are used all over the place in Pygame to keep track of an object’s coordinates. the get_rect() command just looks at the image and calculates the rectangle that will enclose it.

We can use the rect to put the sprite wherever we want it on the screen. Let’s start with the sprite in the center:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
 ```

Now that we’ve defined our Player sprite, we need to create it by making an instance of the Player class. We also need to make sure we add the sprite to the all_sprites group:

```python
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
```

> 4.2 Sprite Movement

Remember, in the game loop, we have the all_sprites.update(). This means that for every sprite in the group, Pygame will look for an update() function and run it. So to get our sprite to move, we just need to define its update rules:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
```

This means that every time through the game loop, we increase the x coordinate of the sprite by 5 pixels. Go ahead and run it and you’ll see the sprite head off the right side of the screen.

Let’s fix that by making the sprite wrap around - whenever it reaches the right side of the screen, we will move it to the left side. We can do this easily by using one of the convenient “handles” on the sprite’s rect:

[rect]: ./images/rect_handles.png
![alt text][rect]

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
```

Go ahead and experiment - notice that anything you put in the update() method of the sprite will happen every frame. Try making the sprite move up and down (change the y coordinate) or making it bounce off the wall (reverse the direction when the rect reaches the edge).

> 5.0 Moving to graphical sprites

Next we’ll show how to use art for your sprite - changing it from a plain square into an animated character.

Colored rectangles are fine - they’re a great way to start and make sure you have the basics of your game working, but sooner or later you’re going to want to use a cool spaceship image or character for your sprite. This leads us to the first issue: where do you get your game graphics.

> 5.1 Where to find art

When you need art for your game, you have 3 choices:

+ Draw it yourself
+ Find an artist to draw it for you
+ Use pre-existing art from the Internet

1 and 2 are fine if you or your friends are artistically inclined, but for most programmers, creating nice-looking art is not in our skill set.  Fortunately, there’s a good solution: OpenGameArt.org. This website is loaded with tons of art, sound, music, and more - and it’s all generously licensed by the artists for you to use in your games. One of the best artists you can find there is named Kenney (just put his name in the search box).

The reason I love to use Kenney’s art (besides the fact that it’s very high quality) is that he likes to release it in packs. This means that you can get sets of art that will all match in style, instead of trying to mix and match images from multiple artists.

We’re going to use the image “p1_jump.png”:

[alien]: ./images/p1_jump.png
![alt text][alien]

> 5.2 Organizing game assets

First we need a folder to hold our assets, which is a term game developers use to refer to things like art and sound. I called the folder “image”, and I put the player image into it.

To use this image in our game, we need to tell Pygame to load the picture file, which means we need our program to know where the file is located. Depending on what kind of computer you are using, this can be different, and we want to be able to run our program on any computer, so we need to load a Python library called os, and then specify where our game is located:

```python
 import pygame
 import random
 import os

 # set up asset folders
 game_folder = os.path.dirname(__file__)
 ```

The special Python variable ```__file__``` refers to whatever folder your game code is saved in, and the command os.path.dirname figures out the path to that folder.
Different operating systems use different ways of describing where things are located on the computer. By using the os.path command, we can let the computer figure out what the right path is (whether to use “/” or “\” for example.)

Now, we can specify our “image” folder:

```python
 import pygame
 import random
 import os

 # set up asset folders
 game_folder = os.path.dirname(__file__)
 img_folder = os.path.join(game_folder, 'image')
 player_img = pygame.image.load(os.path.join(img_folder, 'p1_jump.png')).convert()
```

Now we’ve loaded our image by using pygame.image.load() and we’ve made sure to use convert(), which will speed up Pygame’s drawing by converting the image into a format that will be faster to draw on the screen. Now we’re ready to replace the plain green square in our sprite with our fancy player image:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
```

Notice we’ve deleted the self.image.fill(GREEN) commmand - we don’t need it to be filled with a solid color anymore. get_rect() will still work just fine, because it looks at whatever self.image is to figure out what the bounding rectangle should be.  

Now if you run the program, you should see a nice little cartoon alien running across the screen. But we have a problem - one we can’t see because the background is currently black. Change the screen.fill() command at the bottom to something else - I decided to use BLUE. Now you can see the issue:

When you have an image file on the computer, that file is always a rectangular grid of pixels. No matter what shape you’ve drawn, there’s still a border of pixels filling the “background” of your image. What we need to do is tell Pygame to ignore the pixels in the image that we don’t care about. In this image, those pixels happen to be black, so we can add the following:

```python
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
```

set_colorkey() just tells Pygame that when we draw the image we want to ignore any pixels of the specified color. Now our image looks much better:

Congratulations, you have now learned the basics of working with Pygame! Next class we will start making a real game.

---

## **Any Questions?**

### **for any questions contact hw_help@coolkidscodingschool.com**
