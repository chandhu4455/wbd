import xml.dom.minidom as FT
import xml.etree.ElementTree as ET
import math
from datetime import *
from tzlocal import *
import pytz
import datetime as dt
import os
import Angle
from math import degrees, radians, tan, sin, cos, asin, acos


class Fix():
    def __init__(self,logFile="log.txt"):                
        self.error = 0
        
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
            '''
            you can find your log.txt in workspace->test directory
            or you can use directory method
            file=open("C:\\Users\ChandrashekarChary\\Desktop\\fold\\log.txt","ab")
            '''
            fileFullPath = os.path.abspath(self.logFile)
            log="LOG: "+ self.TimeNow() + " Log file:" + "\t" + fileFullPath + "\n"
            self.file1.write(log)
            
        
    def setSightingFile(self,sightingFile):
        try:
            self.xmlFile=sightingFile 
            '''
            if you want to use directory method Uncomment these two lines 
            and comment below two lines  
            Filename=sightingFile.split("\\")
            log1="LOG:\t"+str(self.TimeNow())+":\t"+"Start of sighting file:\t"+Filename[-1]+"\n"
            '''
            "which will check the existance of file"
            xmlfile = open(self.xmlFile,'r')
            xmlfile.close()
            fileFullPath = os.path.abspath(self.xmlFile)
            log1="LOG: "+ self.TimeNow()+" Sighting file:" + "\t" + fileFullPath + "\n"
            self.file1.write(log1)
            return fileFullPath

        except:
            raise ValueError("File not exists")


    def TimeNow(self):
        now = dt.datetime.utcnow()
        time = datetime(now.year, now.month,now.day,now.hour,now.minute,now.second, tzinfo=pytz.utc)
        Zonetime=time.astimezone(get_localzone())
        return str(Zonetime)

    def setAriesFile(self, ariesFile=""):
        # setAriesFile method receives parameter ariesFile as string.
        # Sets the received text file as the aries file.

        # split filename with '.'
        actualFileName = ariesFile.split(".")[0]
        # checking filename without extension if < 1  than raise error: Received Filename is invalid.
        if (len(actualFileName)) < 1:
            self.error += 1
            raise (ValueError("Fix.setAriesFile:  Received Filename is invalid"))
        # set ariesfile as global.
        self.ariesFile = actualFileName + ".txt"
        # get full path of aries file.
        fileFullPath = os.path.abspath(self.ariesFile)
        # make a string of filename and file full path with current datetime.
        logEntry = ("LOG: " + self.TimeNow() + " Aries file:\t" + fileFullPath + " \n")
        # write a string in logfile.
        self.file1.write(logEntry)
        # checking ariesfile is exist or not.
        try:
            f = open(self.ariesFile, "r")
            f.close()
        except Exception as e:
            raise (ValueError("Fix.setAriesFile:  Aries file could not be opened"))
        # return full path of aries file.
        return fileFullPath


    def setStarFile(self, starFile=""):
        # setStarFile method receives parameter starFile as string.
        # Sets the received text file as the stars file.

        # split filename with '.'
        actualFileName = starFile.split(".")[0]
        # checking filename without extension if < 1  than raise error: Received Filename is invalid.
        if (len(actualFileName)) < 1:
            self.error += 1
            raise (ValueError("Fix.setStarFile:  Received Filename is invalid"))

        # set ariesfile as global.
        self.starFile = actualFileName + ".txt"
        # get full path of aries file.
        fileFullPath = os.path.abspath(self.starFile)
        # make a string of filename and file full path with current datetime.
        logEntry = ("LOG: " + self.TimeNow() + " Star file:\t" + fileFullPath + " \n")
        # write a string in logfile.
        self.file1.write(logEntry)
        # checking stars file is exist or not.
        try:
            f = open(self.starFile, "r")
            f.close()
        except Exception as e:
            raise (ValueError("Fix.setStarFile:  Stars file could not be opened"))
        # return full path of aries file.
        return fileFullPath

    def getSightings(self,assumedLatitude="0d0.0", assumedLongitude="0d0.0"):
        approximateLatitude = "0d0.0"            
        approximateLongitude = "0d0.0"
        dictList = []
        LatitudeLongitude = (approximateLatitude,approximateLongitude)
        ############
        sightings = FT.parse(self.xmlFile).documentElement.getElementsByTagName("sighting")
        #Which will check the root of the file(which should be 'fix' tag
        root = ET.parse(self.xmlFile).getroot()
        fileTag=root.tag
        self.errorString = ""

        assumedLatitudeObj = Angle.Angle()
        hemisphere = ""
        if "S" in assumedLatitude:
            hemisphere = "S"
            assumedLatitude = assumedLatitude.replace("S","")
            assumedLatitudeObj.setDegreesAndMinutes(assumedLatitude)
        elif "N" in assumedLatitude:
            hemisphere = "N"
            assumedLatitude = assumedLatitude.replace("N","")
            assumedLatitudeObj.setDegreesAndMinutes(assumedLatitude)


        assumedLongitudeObj = Angle.Angle()
        assumedLongitudeObj.setDegreesAndMinutes(assumedLongitude)
        assumedLongitude = assumedLongitudeObj.getDegrees()

        if hemisphere == "S":
            assumedLatitude = -(assumedLatitudeObj.getDegrees())
        else:
            assumedLatitude = assumedLatitudeObj.getDegrees()



        try:
            if(fileTag=='fix'):
                # sightingsNum used to know about which sighting we are in
                sightingsNum=1
                for i in sightings:
                    entryDict = {}
                    # Which searching body tag where sighting=sightingsNum
                    try:
                        body = i.getElementsByTagName('body')[0]
                        stringBody = body.childNodes[0].data
                        self.body = stringBody
                    except:
                        self.error += 1
                        self.errorString += "body tag is missing in sighting-"+str(sightingsNum) + "\n"
                        continue
                    # Which searching date tag where sighting=sightingsNum
                    try:
                        date = i.getElementsByTagName('date')[0]
                        stringDate=date.childNodes[0].data
                        self.date=stringDate
                    except:
                        self.error += 1
                        self.errorString += "date tag is missing in sighting-"+str(sightingsNum) + "\n"
                        continue
                    # Which searching time tag where sighting=sightingsNum
                    try:
                        time = i.getElementsByTagName('time')[0]
                        stringTime = time.childNodes[0].data
                        self.time = stringTime
                    except:
                        self.error += 1
                        # raise ValueError("time tag is missing in sighting-"+str(sightingsNum))
                        self.errorString += "time tag is missing in sighting-"+str(sightingsNum) + "\n"
                        continue
                    # Which searching observation tag where sighting=sightingsNum
                    try:
                        observation = i.getElementsByTagName('observation')[0]
                        x = observation.childNodes[0].data
                        DegreeMin = x
                        splitAnglestring = x.split("d")
                        deg = int(splitAnglestring[0])
                        Minutes = float(splitAnglestring[1])
                        angle1 = Angle.Angle()
                        angle1.setDegreesAndMinutes(DegreeMin)
                        observedAltitude = angle1.getDegrees()
                    except Exception as e:
                        self.error += 1
                        self.errorString += "observation tag is missing or invalid in sighting-"+str(sightingsNum) + "\n"
                        continue

                    # Here we are checking the observedAltitude valid or not(in the range or not)
                    if(0 <= deg < 90):
                        self.degrees=deg
                    else:
                        self.error += 1
                        self.errorString += "invalid observation altitude in sighting-"+str(sightingsNum) + "\n"
                        continue
                    if(0 <= Minutes < 60):
                        self.Minutes=Minutes
                    else:
                        self.error += 1
                        self.errorString += "invalid observation altitude in sighting-"+str(sightingsNum) + "\n"
                        continue

                    if(deg == 0):
                        if(Minutes<0.1):
                            self.error += 1
                            self.errorString += "invalid observation altitude in sighting-"+str(sightingsNum) + "\n"
                            continue

                    # Which searching height tag where sighting = sightingsNum
                    try:
                        height = i.getElementsByTagName('height')[0]
                        stringHeight=height.childNodes[0].data
                        self.height=stringHeight
                    except:
                        self.height=0.0
                        # continue

                    # Which searching temperature tag where sighting=sightingsNum
                    try:
                        temperature = i.getElementsByTagName('temperature')[0]
                        stringTemp=temperature.childNodes[0].data
                        if(-20<=int(stringTemp)<=120):
                            self.temperature=stringTemp
                        else:
                            self.temperature=72
                    except:
                        self.temperature=72
                        # continue

                    # Which searching pressure tag where sighting=sightingsNum
                    try:
                        pressure = i.getElementsByTagName('pressure')[0]
                        stringPressure=pressure.childNodes[0].data
                        if(100<=int(stringPressure)<1100):
                            self.pressure=stringPressure
                        else:
                            self.pressure=1010
                    except:
                        self.pressure=1010
                        # continue
                    # Which searching horizon tag where sighting=sightingsNum
                    try:
                        horizon = i.getElementsByTagName('horizon')[0]
                        x=horizon.childNodes[0].data
                        self.horizon = x
                    except:
                        self.horizon = 'natural'
                        # continue
                    if(self.horizon == "natural"):
                        dip = (-0.97 * math.sqrt(float(self.height ))) / 60
                    else:
                        dip = 0

                    # calculate refraction using pressure, temperature and oberservedAltitude.
                    try:
                        refraction = (-0.00452 * float(self.pressure)) / (273 + ((float((self.temperature))-32) * 5.0 / 9.0)) / tan(radians(observedAltitude))

                        # calculate adjusted Altitude.
                        adjustedAltitude = observedAltitude + dip + refraction
                        angle1.setDegrees(adjustedAltitude)
                        adjustedAltitudestring=angle1.getString()
                        # split time where received from sighting file and set hours, minutes and seconds.
                        hours = self.time.split(":")[0]
                        minutes = self.time.split(":")[1]
                        sec = self.time.split(":")[2]
                        # convert minutes in seconds
                        s = (int(minutes) * 60) + int(sec)

                        # converted sighting file date into aries file and star file date format.
                        formatedDate = datetime.strptime(self.date, '%Y-%m-%d').strftime('%m/%d/%y')
                        # open stars file in read mode.
                        starData = open(self.starFile, "r")
                        # use this flag while some tags are missing in sighting file.
                        bodyFlag = False
                        # create new Angle instance.
                        angle = Angle.Angle()
                        # read line from star file.
                    except:
                        self.error += 1
                        continue
                        
                    for line in starData:
                        line = line.strip()
                        # split line and take first element as name.
                        name = line.split("\t")[0]
                        # split line and take first element as date.
                        tempDt = line.split("\t")[1]
                        # searching in stars file.
                        if name == self.body and tempDt <= formatedDate:
                            # if name and date match than set variable by slit line and take third element.
                            self.SHAstar = angle.setDegreesAndMinutes(line.split("\t")[2])
                            # split line and take forth element and set latitude.
                            self.latitude = (line.split("\t")[3]).strip()
                            bodyFlag = True
                    # close stars file.
                    starData.close()
                    
                    # if name and date not found in stars file than return.
                    if(not bodyFlag):
                        self.error += 1
                        continue
                    # open aries file in read mode.
                    ariesData = open(self.ariesFile, "r")
                    # create a new instance of angle.
                    self.newAngle = Angle.Angle()
                    self.newAngle2 = Angle.Angle()
                    # read line form aries file.
                    for line in ariesData:
                        line = line.strip()
                        # split line and use first element as date
                        tempD = line.split("\t")[0]
                        # split line and use second element as hours
                        tempH = line.split("\t")[1]
                        # split line and use third element as observation.
                        obj = line.split("\t")[2]
                        # convert hour to integer.
                        hours = int(hours)
                        tempH = int(tempH)
                        # match sighting file data and hours to aries file data.
                        if tempD == formatedDate and tempH == hours:
                            # set return value of setDegreesAndMinutes method to variable.
                            self.GHAaries1 = self.newAngle.setDegreesAndMinutes(obj)
                            # read next line and split line, use third element as next observation.
                            nextObservation = next(ariesData).split("\t")[2]
                            # set return value of setDegreesAndMinutes method to variable.
                            self.GHAaries2 = self.newAngle2.setDegreesAndMinutes(nextObservation)
                            
                    # close aries file.
                    ariesData.close()
                    # calculate GHAaries.
                    self.GHAaries = self.GHAaries1 + (self.GHAaries2 - self.GHAaries1) * float(s)/3600
                    # calculate GHAobservation.
                    self.GHAobservation = self.GHAaries + self.SHAstar

                    # pass GHAobservation as degrees to setDegrees method.
                    angle.setDegrees(self.GHAobservation)
                    # set return value of getString method to GHAobservation.
                    self.GHAobservation = angle.getString()

                    LHAObj = Angle.Angle()
                    LHAObj.setDegreesAndMinutes(self.GHAobservation)
                    LHAObj.add(assumedLongitudeObj)
                    LHA = LHAObj.getDegrees()

                    latitudeObj = Angle.Angle()
                    latitudeObj.setDegreesAndMinutes(self.latitude)

                    sinlat1 = sin(radians(latitudeObj.getDegrees()))
                    sinlat2 = sin(radians(assumedLatitude))
                    sinlat = sin(radians(latitudeObj.getDegrees())) * sin(radians(assumedLatitude))

                    coslat1 = cos(radians(latitudeObj.getDegrees()))
                    coslat2 = cos(radians(assumedLatitude))
                    cosLHA = cos(radians(LHA))
                    coslat = coslat1 * coslat2 * cosLHA

                    interDistance = sinlat + coslat
                    correctedAltitude = degrees(asin(interDistance))

                    distanceAdjustment = int(round((correctedAltitude - angle1.getDegrees()) * 60, 0))
                    entryDict["distanceAdjustment"] = distanceAdjustment
                    coslat1 = cos(radians(assumedLatitude))
                    coslat2 = cos(radians(correctedAltitude))
                    numerator = sinlat1 - sinlat2 * interDistance
                    denominator = coslat1 * coslat2
                    azimuthAdjustment = degrees(acos(numerator / denominator))

                    azimuthAdjustmentObj = Angle.Angle()
                    azimuthAdjustmentObj.setDegrees(abs(azimuthAdjustment))
                    entryDict['azimuthAdjustment'] = azimuthAdjustment

                    entryDict['azimuthAdjustmentStr'] = ("-" if azimuthAdjustment < 0 else "") + azimuthAdjustmentObj.getString()

                    if hemisphere == "S":
                        entryDict['assumedLatitude'] = "S" + assumedLatitudeObj.getString()
                    else:
                        entryDict['assumedLatitude'] = assumedLatitudeObj.getString()
                    entryDict['assumedLongitude'] = assumedLongitudeObj.getString()

                    # populate data in dictionary
                    entryDict["body"] = self.body
                    entryDict["date"] = self.date
                    entryDict["time"] = self.time
                    entryDict["adjustedAltitude"] = adjustedAltitudestring
                    entryDict["latitude"] = self.latitude
                    entryDict["longitude"] = self.GHAobservation
                    entryDict["datetime"] = datetime.strptime(self.date + " " + self.time, "%Y-%m-%d %H:%M:%S")
                    # add dictionary in list
                    dictList.append(entryDict)
                # sort data by body and datetime
                dictList.sort(key=lambda k: k['body'])
                dictList.sort(key=lambda k: k['datetime'])

                sumLatPart = 0.0
                sumLongPart = 0.0
                for dictionaries in dictList:
                    sumLatPart += dictionaries['distanceAdjustment'] * cos(radians(dictionaries['azimuthAdjustment']))
                    sumLongPart += dictionaries['distanceAdjustment'] * sin(radians(dictionaries['azimuthAdjustment']))
                    # make a string by current datetime, body, sighting file date and time, adjusted altitude, latitude and longitude.
                    # self.txtFile.write(
                    # "LOG: " + str(local) + " " + data["body"] + "\t" + data["dt"] + "\t" + data["time"] + "\t"
                    # + data['degrees'] + "\t" + data['latitude'] + "\t" + data['longitude'] + "\t"
                    # + dataDict['assumedLatitude'] + "\t"
                    # + asLongObj.getString() + "\t" + data['azimuthAdjustment'] + "\t"
                    # + str(data['distanceAdjustment']) + "\n")
                    
                    altitudeString = ("LOG: " + self.TimeNow() + " " + dictionaries["body"] + "\t" + dictionaries["date"] + "\t" + dictionaries["time"] + "\t" + dictionaries["adjustedAltitude"] + "\t" + dictionaries["latitude"] + "\t" + dictionaries["longitude"] + "\t" + dictionaries['assumedLatitude'] + "\t" + dictionaries['assumedLongitude'] + "\t" + dictionaries['azimuthAdjustmentStr'] + "\t" + str(dictionaries['distanceAdjustment']) + "\n")
                    # write log entry to log file.
                    self.file1.write(altitudeString)

                approximateLatitude = assumedLatitude + sumLatPart / 60
                approximateLongitude = assumedLongitude + sumLongPart / 60

                approximateLatitudeObj = Angle.Angle()
                approximateLatitudeObj.setDegrees(abs(approximateLatitude))
                appLat = approximateLatitudeObj.getString()
                if approximateLatitude < 0:
                    appLat = "S" + appLat
                elif approximateLatitude > 0:
                    appLat = "N" + appLat
                approximateLongitudeObj = Angle.Angle()
                approximateLongitudeObj.setDegrees(approximateLongitude)
                appLong = approximateLongitudeObj.getString()

                sightingsNum=sightingsNum+1

                errLog = "LOG: " + self.TimeNow() + " Sighting errors:" + "\t" + str(self.error) + "\n"
                self.file1.write(errLog)
                
                apLatLongLog = "LOG: " + self.TimeNow() + " Approximate latitude:\t" + appLat + "\tApproximate longitude:\t" + appLong + "\n"
                self.file1.write(apLatLongLog)
                
                endLog = "LOG: " + self.TimeNow() + " End of sighting file " + self.xmlFile + "\n"
                self.file1.write(endLog)
            else:
                raise ValueError("Invalid fix file")
                
            # return approximateLatitude and approximateLongitude
            return (appLat, appLong)

        except Exception as e:
            # make a string of sighting file errors.
            endLog = "LOG: " + self.TimeNow() + " Sighting errors:" + "\t" + str(self.error) + "\n"
            # write string to logfile.
            self.file1.write(endLog)
            # close logfile.
            self.file1.close()
        finally:
            self.file1.close()
            

if __name__ == '__main__':
    fix = Fix()
    # fix.setSightingFile("sightings1.xml")
    fix.setSightingFile("sightings2.xml")
    fix.setAriesFile("aries.txt")
    fix.setStarFile("stars.txt")
    # fix.getSightings("N27d59.5", "85d33.4")
    fix.getSightings("S53d38.4", "74d35.3") # sightings2
