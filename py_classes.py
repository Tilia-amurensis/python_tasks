class Things:
    pass
class Inanimate(Things):
    pass
class Animate(Things):
    pass
class Sidewalks(Inanimate):
    pass
class Animals(Animate):
    def breathe(self):
        print('he breathes')
    def move(self):
        print('he moves')
    def eat_food(self):
        print('he eats')
    def left_foot_forward(self):
        print('left foot in front')
    def left_foot_backward(self):
        print('left food in back')
    def right_foot_forward(self):
        print('right foot in front')
    def right_foot_backward(self):
        print('right foot in back')
class Mammals(Animals):
    def feed_young_with_milk(self):
        print('he feeds baby')
class Giraffes(Mammals):
    def __init__(self,spots):
        self.giraffe_spots = spots
    def eat_leaves_from_trees(self):
        self.eat_food()
    def find_food(self):
        self.move()
        print("I find food")
        self.eat_food()
    def dance_jig(self):
        self.move()
        self.move()
        self.move()
    def dance(self):
        self.left_foot_forward()
        self.left_foot_backward()
        self.right_foot_backward()
        self.right_foot_forward()
    



reginald = Giraffes(150)
reginald.move()
reginald.eat_leaves_from_trees()

harold =  Giraffes(125)

reginald.eat_leaves_from_trees()
harold.feed_young_with_milk()

reginald.dance_jig()
harold.find_food()

osvald = Giraffes(100)
print(osvald.giraffe_spots)

harold.dance()
reginald.right_foot_forward()



