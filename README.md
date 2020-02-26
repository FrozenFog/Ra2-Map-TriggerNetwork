# Packages
You'll need [pyecharts](https://github.com/pyecharts/pyecharts) before running this code.

# Usage
Run *main.py* with your map name, any maps that can be read by the game are available.

Map should be in same directory with the source code, or just type the full path of the destinated map.

The result will generate in source code dir, named with *render.html*.

Parameters:
* -w [width] __Set graph width(px), default=1920__
* -h [height] __Set graph height(px), default=1080__
* -r [repulsion] __Set repulsion, default=8000__
* -l __Show label on each node, default false__
* -d __Set each note is NOT dragable, default true__
* -i __Ignore isolated trigger, default false__

You may customize the symbol size in *globalvar.py*, further customize can be utilize in function **DrawWithPye** in *main.py*. 

# Example
    cmd python .\main.py
    >>>Map name(include ".map")
    Must in same directory!(or full path if not):
    <<<Testmap.map
    

    >>>Set parameters:
    -w [width]	  Set graph width, default=1920
    -h [height]	  Set graph height, default=1080
    -r [repulsion]	    Set repulsion, default=8000
    -l		  Show label on each node, default false
    -d		  Set each note is NOT dragable, default true
    -i		  Ignore isolated trigger, default false

    Leave it empty will run with default params:
    <<<-w 800 -h 600 -l
    >>>nodes 139
    links 137
    Finished. Press enter to exit.
    <<<

result in *render.html*:
![alt Result](https://github.com/FrozenFog/Ra2-Map-TriggerNetwork/blob/master/imgs/eg-result.png)
