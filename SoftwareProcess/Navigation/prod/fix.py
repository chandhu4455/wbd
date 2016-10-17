"""
Created on October 8,2016
@author: Chandrashekar Chary Vadla
"""

import xml.dom.minidom as FT
import xml.etree.ElementTree as ET
from xml.dom.minidom import *
import math
from datetime import *
from tzlocal import *
import pytz
import datetime as dt

import Angle as Angle
from math import degrees
class Fix():
    def __init__(self,logFile="log.txt"):                
        #logFile=str(logFile)
        #print logFile
        
        self.logFile=logFile
        if(logFile==None):
            raise ValueError("Fix.__init__Fix:string is empty")
        if(logFile==" "):
            raise ValueError("Fix.__init__Fix:string invalid")
        if(len(logFile)<1):
            raise ValueError("Fix.__init__Fix:string invalid")
        if(len(logFile)>=1):
            file1=open(logFile,"a")
            self.file1=file1
            #print "open"
            '''
            you can find your log.txt in workspace->test directory
            or you can use directory method
            file=open("C:\\Users\ChandrashekarChary\\Desktop\\fold\\log.txt","ab")
            '''
            log="LOG:\t"+str(self.TimeNow() )+":\tStart of Log\n"
            self.file1.write(log)
            
        
    def setSightingFile(self,sightingFile):  
        try:
            self.xmlFile=sightingFile 
            #x=self.TimeNow() 
            '''
            if you want to use directory method Uncomment these two lines 
            and comment below two lines  
            Filename=sightingFile.split("\\")
            log1="LOG:\t"+str(self.TimeNow())+":\t"+"Start of sighting file:\t"+Filename[-1]+"\n"
            '''
            "which will check the existance of file"
            xmlfile=open(self.xmlFile,'r')
            print "file exists"
            xmlfile.close()
            log1="LOG:\t"+str(self.TimeNow())+":\t"+"Start of sighting file:\t"+sightingFile+"\n"
            #print log1
            self.file1.write(log1)
            return(False)
        except:
            raise ValueError("File not exists")
            return(True)
    def TimeNow(self):
        now = dt.datetime.utcnow()
        time = datetime(now.year, now.month,now.day,now.hour,now.minute,now.second, tzinfo=pytz.utc)
        Zonetime=time.astimezone(get_localzone())
        return Zonetime
    def getSightings(self):
        approximateLatitude = "0d0.0"            
        approximateLongitude = "0d0.0"
        LatitudeLongitude = (approximateLatitude,approximateLongitude);
        ############
        sightings = FT.parse(self.xmlFile).documentElement.getElementsByTagName("sighting")
        #Which will check the root of the file(which should be 'fix' tag
        root = ET.parse(self.xmlFile).getroot()
        fileTag=root.tag
        #print fileTag
      
        if(fileTag=='fix'): 
            #sightingsNum used to know about which sighting we are in
            sightingsNum=1
            for i in sightings:
                #Which searching body tag where sighting=sightingsNum
                try:
                    body = i.getElementsByTagName('body')[0]
                    stringBody=body.childNodes[0].data
                    self.body=stringBody   
                except:
                    raise ValueError("body tag is missing in sighting-"+str(sightingsNum))
                
                #Which searching date tag where sighting=sightingsNum
                try:
                    date = i.getElementsByTagName('date')[0]
                    stringDate=date.childNodes[0].data
                    self.date=stringDate
                except:
                    raise ValueError("date tag is missing in sighting-"+str(sightingsNum))
                
                #Which searching time tag where sighting=sightingsNum
                try:
                    time = i.getElementsByTagName('time')[0]
                    stringTime=time.childNodes[0].data
                    self.time=stringTime
                except:
                    raise ValueError("time tag is missing in sighting-"+str(sightingsNum))
                
                #Which searching observation tag where sighting=sightingsNum
                try:
                    observation = i.getElementsByTagName('observation')[0]
                    x=observation.childNodes[0].data
                    DegreeMin=x
                    splitAnglestring=x.split("d")
                    degrees=int(splitAnglestring[0])
                    Minutes=float(splitAnglestring[1])
                    angle1=Angle.Angle()
                    observedAltitude=angle1.setDegreesAndMinutes(DegreeMin)
                    #print observedAltitude
                except:
                    raise ValueError("observation tag is missing in sighting-"+str(sightingsNum))
                
                #Here we are checking the observedAltitude valid or not(in the range or not)
                if(0<=degrees<90):
                    self.degrees=degrees
                else:
                    raise ValueError("invalid observation altitude in sighting-"+str(sightingsNum))   
                if(0<=Minutes<60):
                    self.Minutes=Minutes
                else:
                    raise ValueError("invalid observation altitude in sighting-"+str(sightingsNum))
                if(degrees==0):
                    if(Minutes<0.1):
                        raise ValueError("invalid observation altitude in sighting-"+str(sightingsNum)) 
                
                #########
                #Which searching height tag where sighting=sightingsNum
                try:
                    height = i.getElementsByTagName('height')[0]
                    stringHeight=height.childNodes[0].data
                    self.height=stringHeight   
                except:
                    self.height=0.0
                    
                #Which searching temperature tag where sighting=sightingsNum
                try:
                    temperature = i.getElementsByTagName('temperature')[0]
                    stringTemp=temperature.childNodes[0].data
                    if(-20<=int(stringTemp)<=120):
                        self.temperature=stringTemp
                        #print self.temperature
                    else:
                        self.temperature=72
                        #print self.temperature   
                except:
                    self.temperature=72
                    #print self.temperature
                    
                #Which searching pressure tag where sighting=sightingsNum
                try:
                    pressure = i.getElementsByTagName('pressure')[0]
                    stringPressure=pressure.childNodes[0].data
                    if(100<=int(stringPressure)<1100):
                        self.pressure=stringPressure
                        #print self.pressure
                    else:
                        self.pressure=1010
                        #print self.pressure    
                except:
                    self.pressure=1010
                    
                #Which searching horizon tag where sighting=sightingsNum
                try:
                    horizon = i.getElementsByTagName('horizon')[0]
                    x=horizon.childNodes[0].data
                    self.horizon=x
                    #print self.horizon   
                except:
                    self.horizon='Natural'
                    #print self.horizon
                if(len(self.body)>7):
                    logEntry="LOG:\t" + str(self.TimeNow()) + "\t" +str(self.body) + "\t" +str(self.date) + "\t" +str(self.time) + "\t" + str(observedAltitude) + "\n"
                    #print logEntry
                    self.file1.write(logEntry)
                    #self.__init__Fix(logEntry)
                else:
                    logEntry="LOG:\t" + str(self.TimeNow()) + "\t" +str(self.body) + "\t\t" +str(self.date) + "\t" +str(self.time) + "\t" 
                    self.file1.write(logEntry)  
                if(self.horizon=="Natural"):
                    dip = (-0.97 * math.sqrt(float(self.height ))) / 60 
                    #print dip           
                else:
                    dip=0
                    
                
                refraction = ( -0.00452 * float(self.pressure )) / ( 273 + ((float((self.temperature))-32)*5)/9) / math.atan(observedAltitude)            
                #print "refra",refraction
                adjustedAltitude = observedAltitude + dip + refraction 
                adjustedAltitude=round(adjustedAltitude,3)  
                splitAltitude=str(adjustedAltitude).split(".")
                
                adjustedAltitudestring=splitAltitude[0]+"d"+splitAltitude[1]
                
                altitudeString=str(adjustedAltitudestring) + "\n"
                self.file1.write(altitudeString)
                #print "adjusted",adjustedAltitude
                print "================================"
                print "Body=",self.body 
                print "Horizon= ",self.horizon               
                print "dip=",dip         
                print "Adjusted altitude",adjustedAltitude
                print "================================"
                
                sightingsNum=sightingsNum+1
            if(sightingsNum==1):
                raise ValueError("No sightings found in inputFile")
            endLog="LOG:\t"+str(self.TimeNow())+":\t"+"End of sighting file:\t"+self.xmlFile+"\n"
            self.file1.write(endLog)
            self.file1.close()
        else:
            raise ValueError("Invalid fix file")
        return LatitudeLongitude
