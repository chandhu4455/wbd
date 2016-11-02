"""
Created on August 30,2016
@author: Chandrashekar Chary Vadla
"""
# from test.test_socket import try_address
from math import degrees
from macpath import split

class Angle():
    
    def __init__(self):
        "Creates an instance of Angle  "
        #self.angle = ...       set to 0 degrees 0 minutes
        self.degrees = 0
        self.minutes = 0.0

    def setDegrees(self,degrees=None):
        """degrees is the number of degrees (and portions of degrees).It is a numeric value (integer or float). 
        Optional, defaults to zero if missing."""
        if degrees==None:
            degrees=0
      
        try:  
            degreeString=str(degrees) #degreeString is input string degrees>whic is used for splitting used in line 23
            if(degrees is int or float):        
                if('.' not in degreeString):#if its not a float value
                    degrees=float(degrees)%360
                    self.degrees=degrees
                    self.minutes=0.0                
                else:
                    #degreeSplit=degreeString.split(".")#if length of degreeSplit[1])>1 then its having more than one decimal gives error
                    degrees= degrees%360
                    #print "greee",degrees
                    degreeString1=str(degrees)
                    degreeSplit1=degreeString1.split(".")
                    #degreeSplit1 is string of degrees
                    #make sense assigning values to degreees and minutes
                    #print "lokl",degreeSplit1[1]
                    min = float("0."+degreeSplit1[1])
                    min=min
                    
                    #print degreeSplit1[0]
                   # min = str(min)
                    #x=min.split(".")
                    
                    self.degrees=int(degreeSplit1[0])
                    #print "splitted",degreeSplit1[1]
                    
                    self.minutes=min*60
                    #print "min",self.minutes
                    #print self.degrees
        except:
            raise ValueError("Angle.setDegrees: degrees is not a integer/float")       
        #print degrees
        return degrees

    
    def setDegreesAndMinutes(self, angleString=None):
        if(angleString=="0d0" or angleString=="0d0.0"):
            degrees=0.0
            return degrees
        try:
            if ('d' in angleString):#valid string having 'd' in it,so im checking d first
                splitAnglestring=angleString.split("d")#used to split anglestring
                if(int(splitAnglestring[0])):#splitAnglestring[0] should be integer value otherwise returns error
                    degree1=int(splitAnglestring[0])
                    
                    self.degrees=self.setDegrees(degree1)
                else:
                    raise ValueError("invalid angleString")
                #checks the splitAnglestring[1]  is int or float 
                if('.' in splitAnglestring[1]):
                    splitAnglestringMin=splitAnglestring[1].split(".")
                    if float(splitAnglestring[1])<0:
                        raise ValueError("invalid anglestring")
                    else:
                        self.minutes = float(splitAnglestring[1])
                    
                    if(len(splitAnglestringMin)>2):#if decimal more than 2 gives error?
                        raise ValueError("Invalid angleString please give valid input")
                    else:
                        self.minutes = float(splitAnglestring[1])
                    
                    # if(float(splitAnglestring[1])>=60):
                    #     Minutes=float(splitAnglestring[1])%60
                    #     self.minutes=Minutes/60
                    #     if(int(splitAnglestring[0])<0):
                    #         degrees=degrees-self.minutes
                    #     else:
                    #         degrees=degrees+Minutes
                    # else:
                    #     Minutes= float(splitAnglestring[1])%60
                    #     self.minutes=float(Minutes/60)
                    #     if(int(splitAnglestring[0])<0):
                    #         degrees=degrees-self.minutes
                    #     else:
                    #         degrees=degrees+Minutes
                    
                else:
                    self.minutes = float(splitAnglestring[1])
                #     if(int(splitAnglestring[1])>=60):
                #         Minutes=float(splitAnglestring[1])%60
                #         Minutes=Minutes/60
                #         if(int(splitAnglestring[0])<0):
                #             degrees=degrees-Minutes
                #         else:
                #             degrees=degrees+Minutes
                #     else:
                #         Minutes= float(splitAnglestring[1])%60
                #         Minutes=float(Minutes/60)
                #         if(int(splitAnglestring[0])<0):
                #             degrees=degrees-Minutes
                #         else:
                #             degrees=degrees+Minutes
                #print "entiii",degrees
                return (self.degrees + (self.minutes / 60)) % 360
        except:
            raise ValueError("Angle.setDegreesAndMinutes: Invalid angleString please give valid input")
    """
    takes the input angle into degrees string
    checks the if the  int(degrees[0]) and int(degrees[1])) or float(degrees[1]) or gives error
    for add subtraction and compare
    """
    def add(self, angle=None):
        
        degrees=angle.split("d")
        try:
            if(int(degrees[0])):
               
                self.degrees +=int(degrees[0])
                self.minutes +=float(degrees[1])
    
                Minute=self.minutes
                Minute=round(float(self.minutes/60),1)
                Degrees= Minute+self.degrees
                Degrees=Degrees%360
                return Degrees#returns sum of degrees
        except:
            raise ValueError("invalid adding angle in instance add")
    def subtract(self, angle):
        degrees=angle.split("d")
        try:
            if(int(degrees[0])):
                self.degrees -=int(degrees[0])
                self.minutes -=float(degrees[1])
        
                Minute=self.minutes
                Minute=round(float(self.minutes/60),1)
                Degrees= Minute+self.degrees
                Degrees=Degrees%360
                return Degrees#returns subtraction of degrees
        except:
            raise ValueError("invalid adding angle in instance subtract")
        """
        compDegree is takes angle1
        degrees takes input angle by method
        compares the angles,return 1(if its greater compDegree )
        return 0 (if its equal angles)
        return -1 ( (if its lesser compDegree )
        """
    def compare(self, angle): 
        compDegree=self.getDegrees()
        degrees=angle.split("d")
        try:
            if(int(degrees[0])):
                self.degrees =int(degrees[0])
                self.minutes =float(degrees[1])
                Minute=self.minutes
                Minute=round(float(self.minutes/60),1)
                Degrees= Minute+self.degrees
                Degrees=Degrees%360
                if(compDegree>Degrees):
                    return -1
                elif(compDegree==Degrees):
                    return 0
                else:
                    return 1
       
        except:
            raise ValueError("invalid adding angle in instance subtract")
        
    def getString(self):
        degrees=str(self.degrees)
        minutes=float(self.minutes)
        string=degrees+"d"+ str(round(minutes,1))
        return string#gives the output of degrees in string mode means: Example:240d35
    
    def getDegrees(self):
        #print "min",self.minutes
        min=str(self.minutes)
        y=round(self.minutes,1)
        x=min.split('.')
        Minute=round(y/60,1)

    #round(0.01/60 + 10.46/60,4)
        #print "hey",Minute
        #print self.degrees
        Degrees= Minute+self.degrees
        
        Degrees=Degrees%360
        return Degrees

if __name__ == "__main__":
    f = Angle()
    f.setDegreesAndMinutes("015d4.9")
    # f.setDegrees(45.15)
    print f.getString()
    print f.minutes
