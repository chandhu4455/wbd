#from Navigation.test import angle1Degrees
#from Navigation.test import angle1Degrees, addangle1
from test.test_socket import try_address
from math import degrees
from macpath import split

class Angle():
    
    def __init__(self):
        #self.angle = ...       set to 0 degrees 0 minutes
       self.degrees = 0
       self.minutes = 0.0
           
    def setDegrees(self,degrees=None): 
        x= degrees
        degrees=str(degrees)
        
        if(degrees is int or float):        
            if('.' not in degrees):#
               # x= int(degrees)#            
                #if(x==degrees):#5.6==5
                x=x%360
                self.degrees=x
                self.minutes=0
                    #self.degrees=x 
                    
            else:
                mysplit=degrees.split(".")
                if len(mysplit[1])>1:
                    raise ValueError("error: minutes having more than one decimal")
                else:
                    #x=float(x)
                    x= x%360
                    x=str(x)
                    degreeSplit=x.split(".")
                    
                    self.degrees=int(degreeSplit[0])
                    
                    self.minutes=(int(degreeSplit[1])*60)/10
                    print "gg",self.minutes
                    
                        #self.minutes=y 
                        #print y 
        else:
            raise ValueError("error: degrees is not a integer/float")
            
       
                
        return x
        
   
        
        
    def setDegreesAndMinutes(self, angleString=None):
        
        #X=str(angleString)
        if ('d' in angleString):
            splitAnglestring=angleString.split("d")
           # print "jj",splitAnglestring
        #print "gg",len(y)
            if(int(splitAnglestring[0])):
                splitAnglestring[0]=int(splitAnglestring[0])
                degrees=self.setDegrees(splitAnglestring[0])
            #return t
                #print t
        
            #print "uu",splitAnglestring[1]
            if('.' in splitAnglestring[1] or float(splitAnglestring[1]) or int(splitAnglestring[1])):
            
                splitAnglestringMin=splitAnglestring[1].split(".")
                if(len(splitAnglestringMin)>2):
                    ValueError("Invalid angleString please give valid input")
                else:
                    #print splitAnglestring[1]
                    if(float(splitAnglestring[1])>60):
                        Minutes=round(float(splitAnglestring[1])/60,1)
                    #i=int(i)
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
                        #print 'ddd less 60' 
                #z= float(y[1])%60
                #z=z*60/100
                return degrees
    
        else:
            ValueError("Invalid angleString please give valid input")
               # m1 = m1%60
                #return t1
            
            
            
        
        
        
        
        #return angle11,t
        
       

            """
            if('.' in splitAnglestring[1] and float(splitAnglestring[1])):  
                splitAnglestring=str(splitAnglestring)
                splitAnglestringMin=splitAnglestring[1].split(".")
                if(len(splitAnglestringMin)>2):
                    ValueError("Invalid angleString please give valid input")
                else:
                    print splitAnglestring[1]
                    if(float(splitAnglestring[1])>60):
                        Minutes=float(splitAnglestring[1])/60
                    #i=int(i)
                        if(int(splitAnglestring[0])<0):
                            degrees=degrees-Minutes                     
                        else:
                            degrees=degrees+Minutes 
                    else:
                        Minutes= float(splitAnglestring[1])%60
                        Minutes=float(Minutes/60)
                        if(int(splitAnglestring[0])<0):
                            degrees=degrees-Minutes                     
                        else:
                            degrees=degrees+Minutes
                        print 'ddd less 60' 
                #z= float(y[1])%60
                #z=z*60/100
            elif(int(splitAnglestring[1])):
                if(int(splitAnglestring[1])>60):
                    Minutes= int(splitAnglestring[1])%60
                    Minutes=float(Minutes/60)
                    if(int(splitAnglestring[0])<0):
                        degrees=degrees-Minutes                     
                    else:
                        degrees=degrees+Minutes
                        """
                
          
            
            
            
        
        
        
        
        #return angle11,t
        
       
       
       
    
    def add(self, angle=None):
        #self.x=[]
        #angle=angle1Degrees
        #x=[]
        #x=angle1Degrees.angle11
        #c=4+x
        # return c
        #print angle
        #angle=angle+angle
        # x.append(angle)
        #return angle
        
        #print "ki",x
        degrees=angle.split("d")
        self.degrees +=int(degrees[0])
        self.minutes +=float(degrees[1])
        
        Minute=self.minutes
        Minute=round(float(self.minutes/60),1)
        Degrees= Minute+self.degrees
        Degrees=Degrees%360
        return Degrees
        
        """
        
        getDegree= self.getDegrees(angle)#t43.4
        print getDegree
        getMinutes= self.getDegrees(angle)
        sum= getDegree+getMinutes
        print "su=",sum
        """
    
    
    def subtract(self, angle):
        degrees=angle.split("d")
        self.degrees -=int(degrees[0])
        self.minutes -=float(degrees[1])
        
        Minute=self.minutes
        Minute=round(float(self.minutes/60),1)
        Degrees= Minute+self.degrees
        Degrees=Degrees%360
        return Degrees
    
    def compare(self, angle):
        
        compDegree=self.getDegrees()
        print "hhh",compDegree
        #degrees= angle
        #compDegree2 = angle.getDegrees()
        
        degrees=angle.split("d")
        self.degrees =int(degrees[0])
        self.minutes =float(degrees[1])
        Minute=self.minutes
        Minute=round(float(self.minutes/60),1)
        Degrees= Minute+self.degrees
        Degrees=Degrees%360
        print Degrees
        if(compDegree>Degrees):#1.5 25
            return -1
        elif(compDegree==Degrees):
            return 0
        else:
            return 1
        pass
    
    def getString(self):
        degrees=str(self.degrees)
        minutes=str(self.minutes)
        string=degrees+"d"+minutes
       # return string
        print string
        return string
        pass
    
    def getDegrees(self):
        Minute=round(float(self.minutes)/60,1)
        print "p",Minute
        Degrees= Minute+self.degrees
        Degrees=Degrees%360
        print "jj",Degrees
        return Degrees
        
        
        
    

    
    
         
        
        