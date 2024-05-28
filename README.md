# CS50x - Final Project - Simple PyGame Project
___
#### Video Demo: <URL HERE> url
___
#### *README.md* was created via GitHub, as such, images were linked with that format in mind. See GitHub Repo link to view as intended
___
## Description:
For my final project in CS50x, I went out online and found some courses that taught how to make 2d pixel games
in PyGame for Python. The course I ended up working through and using my projects from as a reference was "Learn Python
by making games" by Christian Koch via [udemy.com](https://www.udemy.com). The class specifically can be found [here](
https://www.udemy.com/course/learn-python-by-making-games/?couponCode=KEEPLEARNING
). The game itself is incredibly simple as this is something I am still actively intending on learning more of, but didn't
want the scope of this final project to get so large that it started to become unmanageable at my current skill level.
In it's current version, the game contains, at it's core a few things; a folder with all the code that I wrote referencing
what I learn from the aforementioned udemy course, a folder with split pixel graphics from a tilesheet that I used from a 
royalty-free game asset pack on [itch.io](https://itch.io) found [here](https://pixel-boy.itch.io/ninja-adventure-asset-pack) courtesy of 
itch.io user "pixel boy", and a map that I made in an application called Tiled using the previously mentioned asset pack. ([Link to Tiled](https://www.mapeditor.org/))

___

![Screenshot of the game, running at 480x480](/game_screenshot.PNG)

## Process:
This project began (after taking the PyGame course on Udemy) by firstly, looking on itch.io for an asset pack that was simple enough to use and was also within ability to use. The one I decided on using 
was call "Ninja Adventure Asset Pack" by Pixel Boy.

___

![[Ninja Adventure Asset Pack](https://pixel-boy.itch.io/ninja-adventure-asset-pack)](/ninja_adventure_pack_pic.PNG)

___

After picking out the characters I wanted to use, I then had to figure out how to split up the sprite sheets for all the 
characters I intended to use. Luckily I found a website that allowed users to upload a sprite sheet and it would split the
frames based on the number of columns and rows and applying that over the resolution of the image which resulted in perfectly cut sprite sheets/frames. ([ezgif.com](https://ezgif.com/sprite-cutter))  was used for this) The only downside I experienced was that the assets were all very small and were intended to be used with a proper engine such as Unity and not necessarily PyGame, so the final resolution was quite small at 480x480.

___

![Spritesheets before cutting](/sprite_sheet.PNG)

___

The next step was using the Tiled application to create my map and add object/entity layers.

___

![Tiled Map Editor](/tiled_screenshot.PNG)
___

After finally having the map and all the assets ready to be imported, I could finally begin coding the project. Because the CS50.dev VSCode environment was based on a server, I could not use it for dedicated windows in the way a game would require. For this, I decided to use PyCharm as I already had familiarity with it from other online Python courses.

___
![PyCharm with this project open](/pycharm_screenshot.PNG)
___
### Game Controls
|Key Input|Action|
|---------|------|
|Up Arrow|Move Up|
|Down Arrow|Move Down|
|Left Arrow|Move Left|
|Right Arrow|Move Right|
|Space Bar|Attack|
___
## Issues during development
All in all this project was fairly straight-forward and the course I took prior to beginning this project set me up very well for success. Most of the bugs I encountered were usually typos. That being said, there was only one issue that hung me up for a little bit but I was eventually able to figure it out after referencing some of the material from the course I took.
The issue I was facing was when the player would attack an enemy ninja, when the enemy ninja "died", ALL of the enemy ninjas would die at the same time. This was because all enemies are put into a `pygame.sprite.Group()` so when something happens to one, unless the developr is interating through the sprites in that group during some sort of event loop, the game will treat them all as a single entity. To fix this, I was able to iterate over the sprite group with a `for` loop, and using PyGame's built in sprite collision method, `pygame.sprite.spritecollide()` I was able to get the enemy sprites to "die" independetly of each other. This method takes the sprite calling the method (`self`), the group of sprites it's interacting with, and then a boolean for a "dokill" parameter to delete the sprite. After a few test runs making sure the logic was implemented properly, I felt the game was in a decent enough state and was an appropriately sized project that it was ready for submission. I learned a LOT with this project and the taste I've gotten for simple 2D game development has definitely piqued my curiosity to dive deeper in to pixel/2D game development for future passion projects.

# Sources/Resources
- Asset pack - [Ninja Adventure Asset Pack](https://pixel-boy.itch.io/ninja-adventure-asset-pack) by Pixel Boy
- Course - [Learn Python by making games](https://www.udemy.com/course/learn-python-by-making-games/) By Christian Koch AKA Clear Code on YouTube
- IDE/PyCharm - [PyCharm](https://www.jetbrains.com/pycharm/)
- Tileset based map editor - [Tiled Map Editor](https://www.mapeditor.org/)
- Sprite sheet cutter - [ezgif.com](https://ezgif.com/sprite-cutter)
