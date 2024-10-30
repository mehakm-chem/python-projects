import tree
import button
import graphics

def main():
    win = graphics.GraphWin("Fun Fire", 200, 200)
    win.setBackground("white")

    my_tree = tree.Tree(
        graphics.Point(100,100)
    )
    my_button = button.Button(
        graphics.Point(50,190),
        graphics.Point(150,150),
        "Burn!"
    )

    my_tree.draw(win)
    my_button.draw(win)

    click = win.getMouse()
    while not my_button.point_is_inside(click):
        click = win.getMouse() #if the click is not inside the button, ask for another click
    
    my_tree.burn_more(win)

    click = win.getMouse()
    while my_tree.is_on_fire():
        while not my_button.point_is_inside(click):
            click = win.getMouse()
        
        my_tree.burn_more(win)
        click = win.getMouse()

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()