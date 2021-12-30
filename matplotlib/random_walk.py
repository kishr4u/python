from random import choice

class RandomWalk:
    def __init__(self,num_points=5000):
        self.num_points=num_points
        self.x_values=[0]
        self.y_values=[0]
    
    def fill_walk(self):
        while len(self.x_values) < self.num_points:
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1,-1])
            y_distance=choice([0,1,2,3,4])
            y_step= y_distance*y_direction
             
            print(x_direction,y_direction)
            
            if x_step == 0 and y_step == 0:
                continue
            
            #here -1 means the last character in opython, -2 means last but one
            #so basically take last value and keep adding
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
        
        