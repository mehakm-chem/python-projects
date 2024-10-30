# tree.py -- William Bailey -- 2023
# 
from graphics import *

class Tree:
    '''
    Represents an individual tree. Starts as an unburned tree, and can be burned through
    repeated calls to object method Tree.burn_more(). Please ensure that the accompanying 
    files are in the same directory as this file:
        0_tree.png
        1_little_burn.png
        2_lot_burn.png
        3_charcoal.png
    '''
    # I know these dimensions from the outset.
    img_width = 29
    img_height = 29
    tree_images = [
        "0_tree.png",
        "1_little_burn.png",
        "2_lot_burn.png",
        "3_charcoal.png"
    ]
    for i in range(len(tree_images)):
        tree_images[i] = os.path.join(os.path.dirname(__file__), tree_images[i])


    def __init__(self, anchor_pt: Point):
        '''
        Creates a unburned Tree object centered at anchor_pt. 
        '''
        self.burn_level = 0
        self.tree_img = Image(anchor_pt, self.tree_images[0])


    def __str__(self) -> str:
        '''
        Returns a string representation of the calling object. 
        This is the string type conversion function, str().
        '''
        return (f'{self.tree_images[self.burn_level]} at '
            + f'({self.tree_img.getAnchor.getX()}, '
            + f'{self.tree_img.getAnchor.getX()})')


    def __repr__(self) -> str:
        '''
        Return a code-like string representation of the calling object.
        This is the representation function, repr().
        '''
        return f'Tree({repr(self.tree_img.getAnchor())})'


    def getAnchorPoint(self) -> Point:
        '''
        Returns the Point at which the calling object is centered.
        '''
        return self.tree_img.getAnchor()


    def draw(self, win:  GraphWin) -> None:
        '''
        Draws the Tree object to the graphics window win.
        '''
        self.tree_img.draw(win)


    def undraw(self) -> None:
        '''
        Removes the Tree object from the graphics window win.
        '''
        self.tree_img.undraw()


    def burn_more(self, win: GraphWin) -> None:
        '''
        Moves the calling Tree object to the next burn state.
        If the calling Tree object is in the final burn state, it is not modified.
        '''
        if self.burn_level >= len(self.tree_images)-1:
            return

        self.burn_level += 1
        self.tree_img.undraw()
        self.tree_img = Image(self.tree_img.getAnchor(), self.tree_images[self.burn_level])
        self.tree_img.draw(win)


    def is_on_fire(self) -> bool:
        '''
        Returns True if the calling Tree object is on fire, False otherwise.
        '''
        return 0 < self.burn_level < len(self.tree_images) - 1


    def point_is_inside(self, point: Point) -> bool:
        '''
        Returns True if point is within the bounds of the calling object.
        '''
        return (abs(self.getAnchorPoint().getX() - point.getX()) < Tree.img_width 
            and abs(self.getAnchorPoint().getY() - point.getY()) < Tree.img_height)
