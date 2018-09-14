class parent():
    def __init__(self , last_name , eye_color):
        print "Parent constructor called"
        self.last_name = last_name
        self.eye_color = eye_color

class child(parent):
    #for the child constructor we rewrite the variables of parent class and add the new variables
    def __init__(self , last_name , eye_color, number_of_toys):
        print "child constructor called"
        #now we call the parent construcor
        parent.__init__(self , last_name , eye_color)
        self.number_of_toys = number_of_toys
        
# now observe the results
miley_cyrus = child ("Cyrus" , "Blue" , 5)

print miley_cyrus.last_name
print miley_cyrus.number_of_toys
