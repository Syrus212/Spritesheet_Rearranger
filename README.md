# Spritesheet_Rearranger

You must have Python installed. It can be downloaded [here](https://www.python.org).

You must first install some packages before using this tool : open command prompt and type those commands :<br />
<br />
```pip3 install opencv-python```<br />
```pip3 install pillow```<br />
```pip3 install tk```<br />
```pip3 install numpy```<br />

If these commands do not work, try replacing ```pip3```with simply ```pip```.

Make sure both ```.py```files are in the same directory.

Double click the ```main.py```file and select the spritesheet you want to clean up. The rearranged spritesheet will be called ```Result.png```and will be placed in the same directory as the source file.

Anchor model :

WIP

Note : the sprites are order based on the upper-left hand corner of each sprite's bounding box. They are ordered from left to right and if two sprites have their corner on the same X coordinate from top to bottom.
