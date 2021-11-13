from pycsim import CSim, common
import time

class level1:
    def __init__(self,body)
        self.body=body

        def move_forward(timeout)
            while timeout > 10
                rl = self.body.right_length()
                ll = self.body.left_length()
                if 0.01 < rl  < 10:
                    self.body.rotate_left()
                elif 0.01 < ll < 10:
                    self.body.rotate_right()
                else 
                    self.body.move_forward()
