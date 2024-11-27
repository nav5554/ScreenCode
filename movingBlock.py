#This code makes a 5x5 blue block that bounces off the walls


#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class GraphicsTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(GraphicsTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        red = graphics.Color(0, 255, 0);
        
        while(j == 0):
          #Every iteration of the for loop the block shifts one pixel
          #Goes up to 26 because screen is 32 pixels wide but block is 5 pixels wide so 32-5 = 27
          #Blocks are created with 5 DrawLine() methods making a 5x5 block
             for i in range(27):
                 graphics.DrawLine(canvas, 0, i, 5, i, red)
                 graphics.DrawLine(canvas, 0, i+1, 5, i+1, red)
                 graphics.DrawLine(canvas, 0, i+2, 5, i+2, red)
                 graphics.DrawLine(canvas, 0, i+3, 5, i+3, red)
                 graphics.DrawLine(canvas, 0, i+4, 5, i+4, red)
                 graphics.DrawLine(canvas, 0, i+5, 5, i+5, red)
                 time.sleep(0.05)
                 canvas.Clear()
            #Sample thing as above except it moves in the other direction
             for i in range(27):
                 graphics.DrawLine(canvas, 0, 32-i, 5, 32-i, red)
                 graphics.DrawLine(canvas, 0, 32-(i+1), 5, 32-(i+1), red)
                 graphics.DrawLine(canvas, 0, 32-(i+2), 5, 32-(i+2), red)
                 graphics.DrawLine(canvas, 0, 32-(i+3), 5, 32-(i+3), red)
                 graphics.DrawLine(canvas, 0, 32-(i+4), 5, 32-(i+4), red)
                 graphics.DrawLine(canvas, 0, 32-(i+5), 5, 32-(i+5), red)
                 time.sleep(0.05)
                 canvas.Clear()




# Main function
if __name__ == "__main__":
    graphics_test = GraphicsTest()
    if (not graphics_test.process()):
        graphics_test.print_help()
