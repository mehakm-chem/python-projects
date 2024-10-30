from graphics import *

class Button(Rectangle):
    '''
    Represents a rectangular, clickable button. Has built-in functions which determine if a 
    Point object is within the boundary of the Button.
    '''
    def __init__(self, pt1, pt2, text, box_fill="blanched almond"):
        super().__init__(pt1, pt2)
        self.setFill(box_fill)
        self.text = Text(Point((pt1.getX()+pt2.getX())/2, (pt1.getY()+pt2.getY())/2), text)


    def point_is_inside(self, point):
        '''
        Returns True if point is within the bounds of the calling Button object, False otherwise.
        '''
        pts = [self.getP1(), self.getP2()]
        xs = [pts[0].getX(), pts[1].getX()]
        ys = [pts[0].getY(), pts[1].getY()]

        xs.sort()
        ys.sort()

        return ( xs[0] <= point.getX() <= xs[1] and ys[0] <= point.getY() <= ys[1])


    def draw(self, win):
        '''
        Draws the calling Tree object to the window win.
        '''
        super().draw(win)
        self.text.draw(win)


    def undraw(self):
        '''
        Removes the calling Tree object from the window win.
        '''
        self.text.undraw()
        super().undraw()

