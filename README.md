# Spritesheet_Rearranger

You must have Python installed. It can be downloaded [here](https://www.python.org).

You must first install some packages before using this tool : open command prompt and type those commands :<br />
<br />
```pip3 install opencv-python```<br />
```pip3 install pillow```<br />
```pip3 install tk```<br />
```pip3 install numpy```<br />
```pip3 install easygui```<br />

If these commands do not work, try replacing ```pip3```with simply ```pip```.

Make sure both ```.py```files are in the same directory.

Right click the ```main.py```file and click _Edit with Idle_. Then from the top menu click _Run_ and choose _Run Module_. Select the spritesheet you want to clean up. The rearranged spritesheet will be called ```Result.png```and will be placed in the same directory as the source file.

Anchor model :

![Anchor model](https://github.com/Syrus212/Spritesheet_Rearranger/blob/main/Anchor%20model.png)

Note 1 : the sprites are ordered based on the upper-left hand corner of each sprite's bounding box. They are ordered from left to right and if two sprites have their corner on the same X coordinate from top to bottom.

Note 2 : for spritesheets with multiple rows (like color variations, eyes...), create the spritesheet for each row separately and then assemble the full spritesheet by hand. This tool can't guess which sprites are supposed to be on a row and which sprites aren't.

Troubleshooting : if you don't get the expected result, try adding a layer below the sprites, adding a plain background color and then erasing it before flattening the image. If black sprites don't seem to show up correctly, try lightening them by a small amount. Pitch black sprites will not work with this tool. If you still encounter issues, try and see if there is any non transparent pixel in the image (each group of at least 1 pixel adjacent to other pixels is considered its own sprite and could mess up the program).
