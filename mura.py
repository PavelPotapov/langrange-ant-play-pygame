import play
from random import randint
ylines = []
terrain = []
WIDTH_CELLS = 20
HEIGHT_CELLS = 20
WIDTH_SCREEN = 1024
HEIGHT_SCREEN = 640
xlines = []
def grid():
    k1 = 0
    k2 = 0
    global WIDTH_CELLS,HEIGHT_CELLS,WIDTH_SCREEN,HEIGHT_SCREEN
    for i in range(HEIGHT_SCREEN//HEIGHT_CELLS):
        line = play.new_line(
                color='black', 
                x=-WIDTH_SCREEN/2, 
                y=-HEIGHT_SCREEN/2+i*HEIGHT_CELLS, 
                length=WIDTH_SCREEN, 
                angle=0, 
                thickness=1, 
                x1=None, 
                y1=None
            )
        ylines.append(line)
        k1 += 1
    for i in range(WIDTH_SCREEN//WIDTH_CELLS):
        line = play.new_line(
                color='black', 
                x=-WIDTH_SCREEN/2+i*WIDTH_CELLS,
                y=HEIGHT_SCREEN/2,
                length=HEIGHT_SCREEN, 
                angle=-90, 
                thickness=1, 
                x1=None, 
                y1=None
            )
        xlines.append(line)
        k2 += 1
    print(k2,k1)
grid()
ant = play.new_box(
        color='red',
        x=-1,
        y=29,
        width=WIDTH_CELLS-WIDTH_CELLS/10+1,
        height=HEIGHT_CELLS-HEIGHT_CELLS/10+1,
        border_color="light blue",
        border_width=0
    )
def randomcellplace():
    cellplacer = play.new_box(
        color='red',
        x=1*(-(WIDTH_SCREEN//WIDTH_CELLS)/2)*WIDTH_CELLS+WIDTH_CELLS/2-1,
        y=29*11-HEIGHT_CELLS/2,
        width=WIDTH_CELLS-WIDTH_CELLS/10+1,
        height=HEIGHT_CELLS-HEIGHT_CELLS/10+1,
        border_color="light blue",
        border_width=0)
randomcellplace()
@play.repeat_forever
async def do():
    a = False
    for i in terrain:
        if i.is_touching(ant):
            i.hide()
            terrain.remove(i)
            ant.turn(-90)
            ant.move(WIDTH_CELLS)
            a = True
    if a == False:
        ant.turn(+90)
        terrain.append(play.new_box(
            x=ant.x,
            y=ant.y,
            width=ant.width,
            height=ant.height
        ))
        ant.move(WIDTH_CELLS)
    await play.timer(0.3)
play.start_program()