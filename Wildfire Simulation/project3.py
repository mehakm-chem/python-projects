'''
mittal_project3.py -- Mehak Mittal -- December 5 2023
A graphical python program which allows the user to observe the way fire spreads, 
in addition to automatically computing statistics about the fire, 
including how much of the forest was destroyed, and how long the fire burned. 
The program allows the user to enter different probabilities of fire spreading.
'''
import random
import time
import tree
import graphics
from graphics import *

TREE_SIZE = 29


class Forest:
    def __init__(self, breadth = 15, height = 10) -> None:
        '''
        creating a 2D List of the forest
        '''
        self.forest = []
        for i in range(breadth):
            row = []
            for j in range(height):
                anchorPoint = Point(
                    TREE_SIZE/2 * (i+1) + TREE_SIZE/2 * i,
                    TREE_SIZE/2 * (j+1) + TREE_SIZE/2 * j)
                row.append(Tree(anchorPoint))
            self.forest.append(row)
        
        #making a bool forest
        #initializing all the trees at False
        self.bool_forest = []
        for i in range(breadth):
            row = []
            for j in range(height):
                row.append(False)
            self.bool_forest.append(row)
            
    def isForestonFire(self):
        '''
        checks whether the forest is on fire by checking
        if any tree is on fire
        '''
        isOnFire = False
        for row in self.forest:
            for tree in row:
                if tree.is_on_fire():
                    isOnFire = True
        return isOnFire #returns bool whether any tree is on fire or not

                    
    def burnForest(self, win, probability):
        '''
        traverses through the bool forest, followed by the
        main forest to check which tree will catch fire
        or burn further
        '''
        #traverses through the main forest to 
        #check which tree will burn 
        for row in range(len(self.forest)):
            for col in range(len(self.forest[row])):
                tree = self.forest[row][col]
                if tree.is_on_fire():
                    for ROW in range(
                        max(0, row-1),
                        min(len(self.forest), row+2)
                        ):
                        for COL in range(
                            max(0, col-1),
                            min(len(self.forest[row]), col+2)
                            ):
                            if random.random() < probability:
                                #update the bool forest value for
                                #the tree to catch fire to True
                                self.bool_forest[ROW][COL] = True

        #in the bool forest, everything that is true - burn it
        #in the main forest
        for row in range(len(self.bool_forest)):
            for col in range(len(self.bool_forest[row])):
                if self.bool_forest[row][col]:
                    self.forest[row][col].burn_more(win)            
        
    def undrawForest(self):
        '''
        erases the entire forest
        '''
        for row in range(len(self.forest)):
            for col in range(len(self.forest[row])):
                self.forest[row][col].undraw()

    def drawForest(self, win):
        '''
        redraws the entire forest
        '''
        for row in self.forest:
            for tree in row:
                tree.draw(win)


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

def work_with_buttons(button_RS, 
                      button_CS, 
                      button_S, 
                      my_forest, 
                      click_point, 
                      win, 
                      probability):
    '''
    a function that gives the flow of prgram
    based on which one fo the provided buttons
    is clicked
    '''
    #random start
    if button_RS.point_is_inside(click_point):
        #locate a random tree in the forest
        RandomTree_loc = [random.randint(1,14), random.randint(1,9)]
        RandomTree = my_forest.forest[RandomTree_loc[0]][RandomTree_loc[1]]
        #burn the randomn tree
        RandomTree.burn_more(win)

        count_sim = 0 #counts the discrete steps
        while my_forest.isForestonFire():
            my_forest.burnForest(win, probability)
            count_sim += 1
            time.sleep(0.1)
        
        
        prompt_point1 = Point(50, 140)
        prompt_point2 = Point(350, 180)
        prompt_text = f"Fire subsided in {count_sim} steps. Click anywhere to close"
        prompt = Button(prompt_point1, prompt_point2, prompt_text)
        prompt.draw(win)

        win.getMouse()
        prompt.undraw()
        
    #click to start
    elif button_CS.point_is_inside(click_point):
        selectTree = win.getMouse()
        select_row, select_col = -1, -1
        
        #finding the selected tree in forest:
        for row in range(len(my_forest.forest)):
            for col in range(len(my_forest.forest[row])):
                if my_forest.forest[row][col].point_is_inside(selectTree):
                    select_row, select_col = row, col
        
        #validating the selection
        if select_row != -1 and select_col != -1:
            selectedTree = my_forest.forest[select_row][select_col]
            selectedTree.burn_more(win)
        
            count_sim = 0 #counts discrete steps
            while my_forest.isForestonFire():
                my_forest.burnForest(win, probability)
                count_sim += 1
                time.sleep(0.1)
        
        prompt_point1 = Point(50, 140)
        prompt_point2 = Point(350, 180)
        prompt_text = f"Fire subsided in {count_sim} steps. Click anywhere to close"
        prompt = Button(prompt_point1, prompt_point2, prompt_text)
        prompt.draw(win)

        win.getMouse()
        prompt.undraw()
    
    #reset simulation
    elif button_S.point_is_inside(click_point):
        #erase the forest
        my_forest.undrawForest()
        #create a new forest object
        my_forest = Forest()
        #draw the forest in the new instance
        my_forest.drawForest(win)
    
    return True, my_forest

def error_label(win):
    '''
    creates an error label that pops up
    everytime there is an invalid input
    in the probability box
    '''
    error_point1 = Point(50, 140)
    error_point2 = Point(350, 180)
    error_text = f"Input valid. Click anywhere to close"
    error = Button(error_point1, error_point2, error_text)
    error.draw(win)

    win.getMouse()
    error.undraw()

def main():

    #creating a window
    win = graphics.GraphWin("Wildfire", 700, 290)
    win.setBackground("lightgrey")

    #creating the forest using the class Forest()
    my_forest = Forest()
    my_forest.drawForest(win)
    
    #burn probability
    burn_prob = Text(Point(570, 100), "Burn Probability:")
    burn_prob.setStyle("bold")
    burn_prob.setTextColor("black")

    burn_prob.draw(win)

    #input box
    inputbox = Entry(Point(570, 130), 15)
    inputbox.draw(win)

    #creating buttons

    #Run (Random Start)
    point1_RS = Point(510, 150)
    point2_RS = Point(630, 180)
    text_RS = "Run (Random Start)"
    button_RS = Button(point1_RS, point2_RS, text_RS)
    
    #Run (Click to Start)
    point1_CS = Point(510, 185)
    point2_CS = Point(630, 215)
    text_CS = "Run (Click to Start)"
    button_CS = Button(point1_CS, point2_CS, text_CS)

    #Reset Simulation
    point1_S = Point(510, 220)
    point2_S = Point(630, 250)
    text_S = "Reset Simulation"
    button_S = Button(point1_S, point2_S, text_S)

    #Exit Button
    point1_E = Point(680, 0)
    point2_E = Point(700, 20)
    text_E = "X"
    button_E = Button(point1_E, point2_E, text_E)
    button_E.setFill("red")

    button_RS.draw(win)
    button_CS.draw(win)
    button_S.draw(win)
    button_E.draw(win)

    click_point = win.getMouse()

    #the click needs to be in one of the button
    while not (
        button_RS.point_is_inside(click_point) or
        button_CS.point_is_inside(click_point) or
        button_S.point_is_inside(click_point)
        ):
        click_point = win.getMouse()

    #input validation loop
    continueVar = True
    while continueVar:
        try:
            probability = float(inputbox.getText())
            if probability > 0:
                continueVar = False

        except ValueError:
            error_label(win)
            win.getMouse()
            continue
        
    
    button_press, my_forest = work_with_buttons(button_RS, button_CS,
                                                button_S, my_forest,
                                                click_point, win, probability)

    while button_press:
        click_point = win.getMouse()

        if button_E.point_is_inside(click_point):
            win.close()

        try:
            probability = float(inputbox.getText())
            
        except ValueError:
            error_label(win)
            win.getMouse()
        
        button_press, my_forest = work_with_buttons(button_RS, button_CS,
                                                    button_S, my_forest,
                                                    click_point, win, probability)

if __name__ == "__main__":
    main()