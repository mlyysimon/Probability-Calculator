import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents = []
    
    # create a list of all the balls
    for key, value in kwargs.items():
      for i in range(value): # if more than 1 of  same color, print again
        self.contents.append(key)

  def draw(self, num_draw):
    # if the amount of balls to draw is greater than the amount of balls in the hat, return all the balls
    if num_draw > len(self.contents):
      return self.contents
    else:
      drawn_balls = []
      for num in range(num_draw):
        choice = random.choice(self.contents)
        self.contents.remove(choice) # remove the drawn balls from hat
        drawn_balls.append(choice) # create list of balls drawn

    return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  M = 0 # count of experiments resulting in expected balls
  for n in range(num_experiments):
    copy_hat = copy.deepcopy(hat) # create a copy of the hat contents
    drawn_balls = copy_hat.draw(num_balls_drawn)
    check = []
    # check if the drawn balls contain all of the expected balls
    for key, value in expected_balls.items():
      if drawn_balls.count(key) >= value:
        check.append(True)
      else:
        check.append(False)
    if all(check):
      M += 1
  return M / num_experiments # return probability