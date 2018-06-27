import math

class vectors:

    def __init__(self,x,y):
        '''
        this is the constructor class
        '''
        self.x = x
        self.y = y

    def __str__(self):
        '''
        Method that return a string
        args:
            self object
        output:
            x as string
        '''
        return str(self.x)

    def __add__(self,vector):
        '''
        method that adds vectors 
        arg:
            a vector in the form of a set i.e (x,y)
        operation:
            a new vector that add the given vector to the self object
        output:
            vector in the form of a set (x,y)
        '''
        return (self.x+vector[0],self.y+vector[1])

    def __sub__(self,vector):
        '''
        method that substracts vectors 
        arg:
            a vector in the form of a set i.e (x,y)
        operation:
            a new vector that subtracts the given vector to the self object
        output:
            vector in the form of a set (x,y)
        '''
        return (self.x-vector[0],self.y-vector[1])

    def __mul__(self,multiplication_factor):
        '''
        Method that multiplies the vector by given parameter
        args:
            integer e.g 4 or vector i.e (x,y)
        process:
            multiply the vector by the given multiplication factor
        output:
             vector in the form of a set (x,y)
        '''
        if isinstance(multiplication_factor,int):
            return (self.x*multiplication_factor,self.y*multiplication_factor)
        else:
            return (self.x*multiplication_factor[0] + self.y*multiplication_factor[1])

    def magnitude(self):
        '''
        method that finds the magnitude of a vector
        arg:
            self
        process:
            square x and y and  find the squareroot of their sum
        output:
            magnitude as a float
        '''
        var1=self.x**2+self.y**2
        print(float(math.sqrt(var1)))




# this are the tests

#this tests __add__ method
ins_vec = vectors(1,2)
vector4 = ins_vec.__add__((1,3))
print(vector4)
#this tests __sub__ method
vector5 = ins_vec.__sub__((1,3))
print(vector5)

#this tests __mul__ method
vector6 = ins_vec.__mul__((1,3)) # when the input is a vector
print(vector6)

vector7 = ins_vec.__mul__(5) # when the input is a scalar
print(vector7)

#this tests magnitude method
vector8 = ins_vec.magnitude()
print(vector8)

        


