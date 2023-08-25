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

![Anchor model](https://github.com/Syrus212/Spritesheet_Rearranger/Anchor model.png)

Note : the sprites are order based on the upper-left hand corner of each sprite's bounding box. They are ordered from left to right and if two sprites have their corner on the same X coordinate from top to bottom.
