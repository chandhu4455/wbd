"""
Created on August 30,2016
@author: Chandrashekar Chary Vadla
"""
from test.test_socket import try_address
from math import degrees
from macpath import split

class Angle():
    
    def __init__(self):
        "Creates an instance of Angle  "
        #self.angle = ...       set to 0 degrees 0 minutes
        self.degrees = 0
        self.minutes = 0.0
    ""     
    def setDegrees(self,degrees=None):
        """degrees is the number of degrees (and portions of degrees).It is a numeric value (integer or float). 
        Optional, defaults to zero if missing."""
        degreeString=str(degrees) #degreeString is input string degrees>whic is used for splitting used in line 23
        if(degrees is int or float):        
            if('.' not in degreeString):#if its not a float value
                degrees=degrees%360
                self.degrees=degrees
                self.minutes=0                 
            else:
                degreeSplit=degreeString.split(".")#if length of degreeSplit[1])>1 then its having more than one decimal gives error
                if len(degreeSplit[1])>1:
                    raise ValueError("error: minutes having more than one decimal")
                else:
                    degrees= degrees%360
                    degreeString1=str(degrees)
                    degreeSplit1=degreeString1.split(".")
                    #degreeSplit1 is string of degrees
                    #make sense assigning values to degreees and minutes 

                    self.degrees=int(degreeSplit1[0])
                    self.minutes=(int(degreeSplit1[1])*60)/10
        else:
            raise ValueError("error: degrees is not a integer/float")       
        return degrees   
    def setDegreesAndMinutes(self, angleString=None):
        if ('d' in angleString):#valid string having 'd' in it,so im checking d first
            splitAnglestring=angleString.split("d")#used to split anglestring
            if(int(splitAnglestring[0])):#splitAnglestring[0] should be integer value otherwise returns error
                splitAnglestring[0]=int(splitAnglestring[0])
                degrees=self.setDegrees(splitAnglestring[0])
            else:
                raise ValueError("invalid angleString")
            #checks the splitAnglestring[1]  is int or float 
            if('.' in splitAnglestring[1] or float(splitAnglestring[1]) or int(splitAnglestring[1])):
                splitAnglestringMin=splitAnglestring[1].split(".")
                if(len(splitAnglestringMin)>2):#if decimal more than 2 gives error?
                    raise ValueError("Invalid angleString please give valid input")
                else:
                    if(float(splitAnglestring[1])>60):
                        Minutes=round(float(splitAnglestring[1])/60,1)
                        if(int(splitAnglestring[0])<0):
                            degrees=degrees-Minutes                     
                        else:
                            degrees=degrees+Minutes 
                    else:
                        Minutes= float(splitAnglestring[1])%60
                        Minutes=round(float(Minutes/60),1)
                        if(int(splitAnglestring[0])<0):
                            degrees=degrees-Minutes                     
                        else:
                            degrees=degrees+Minutes
                return degrees
    
        else:
            raise ValueError("Invalid angleString please give valid input")
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
        minutes=str(self.minutes)
        string=degrees+"d"+minutes
        return string#gives the output of degrees in string mode means: Example:240d35
    
    def getDegrees(self):
        Minute=round(float(self.minutes)/60,1)
        Degrees= Minute+self.degrees
        Degrees=Degrees%360
        return Degrees