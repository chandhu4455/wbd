import math

class Angle():
    def __init__(self):
        """This is constructor. This will initialize the Angle object."""

        self.degrees = 0.0 # default value
        self.minutes = 0.0 # default value
        self.isNegative = False

    def setDegrees(self, degrees=0.0):
        """Sets degrees and minutes for the object.
        
        Args:
            degrees: degrees as floating point number.
            
        Returns:
            degrees as floating point number.
        """
        
        try:
            self.minutes, self.degrees = math.modf(float(degrees))
        except Exception as e:
            try:
                self.degrees, self.minutes = int(degrees), 0
            except Exception as e:
                raise ValueError("Angle.setDegrees:  Invalid parameter value for degrees.")

        sum = float((self.degrees % 360) + self.minutes)
        sum = sum % 360
        frac, whole = math.modf(sum)
        self.degrees = whole
        self.minutes = frac
        return sum

    def setDegreesAndMinutes(self, angleString):
        """Sets degrees and minutes for the object.
        
        Args:
            angleString: degrees and minutes as string.
            
        Returns:
            degrees as floating point number.
        """
        
        deg = None
        min = None
        self.isNegative = False
        
        # check received string is blank or not
        if angleString == "":
            raise ValueError("Angle.setDegreesAndMinutes:  Invalid angleString.")

        # check separator exists or not
        if "d" not in angleString:
            raise ValueError("Angle.setDegreesAndMinutes:  Invalid angleString.")

        # spit string with separator
        degreesAndMinutes = angleString.split("d")

        if len(degreesAndMinutes) != 2:
            raise ValueError("Angle.setDegreesAndMinutes:  Invalid angleString.")

        deg = degreesAndMinutes[0]
        min = degreesAndMinutes[1]
            
        if "." in deg:
            raise ValueError("Angle.setDegreesAndMinutes:  Invalid angleString.")

        try:
            deg = int(deg)
            min = float(min)
        except Exception as e:
            raise ValueError("Angle.setDegreesAndMinutes:  Invalid angleString.")

        if min < 0:
            raise ValueError("Angle.setDegreesAndMinutes:  Invalid angleString.")

        if len(str(min).split(".")[1]) > 1:
            raise ValueError("Angle.setDegreesAndMinutes:  Invalid angleString.")

        if deg < 0:
            self.isNegative = True
            deg = 360 - deg - (int(min % 60) if min > 60 else 0)

        self.degrees = (deg + (int(min % 60) if min > 60 else 0)) % 360
        self.minutes = (min % 60) / 60

        if self.isNegative:
            return 360 - float(self.degrees + self.minutes)
        else:
            return float(self.degrees + self.minutes)

    def add(self, angle=None):
        """Adds degrees from received angle.
        
        Args:
            angle: An object of Angle
            
        Returns:
            degrees as floating point number.
        """
        
        if not isinstance(angle, Angle):
            raise ValueError("Angle.add:  Invalid angle.")

        if angle.isNegative:
            temp = (float(self.degrees + self.minutes) - float(angle.degrees + angle.minutes)) % 360
        else:
            temp = (float(self.degrees + self.minutes) + float(angle.degrees + angle.minutes)) % 360

        frac, whole = math.modf(temp)
        self.degrees = whole
        self.minutes = frac
        self.isNegative = False

        return temp

    def subtract(self, angle=None):
        """Subtracts degrees of angle.
        
        Args:
            angle: An object of Angle
            
        Returns:
            degrees as floating point number.
        """
        
        if not isinstance(angle, Angle):
            raise ValueError("Angle.add:  Invalid angle.")

        if angle.isNegative:
            temp = (float(self.degrees + self.minutes) + float(angle.degrees + angle.minutes)) % 360
        else:
            temp = (float(self.degrees + self.minutes) - float(angle.degrees + angle.minutes)) % 360

        frac, whole = math.modf(temp)
        self.degrees = whole
        self.minutes = frac
        self.isNegative = False

        return temp

    def compare(self, angle=None):
        """Compares current angle with received angle.
        
        Args:
            angle: An object of Angle
            
        Returns:
            * -1 if current angle is less than received angle
            * 0 if both the angles are same
            * 1 if current angle is greater than received angle
        """
        
        if not isinstance (angle, Angle):
            raise ValueError("Angle.add:  Invalid angle.")

        if self.getDegrees() > angle.getDegrees():
            return 1
        elif self.getDegrees() < angle.getDegrees():
            return -1
        else:
            return 0
            
    def getString(self):
        """Converts and returns the angle as a string.
        
        Returns:
            Current angle object as a string
        """
        
        return str(int(self.degrees)) + "d" + str(round(self.minutes * 60, 1))

    
    def getDegrees(self):
        """Returns the angle as a floating point value.
        
        Returns:
            Current angle as a floating point value
        """
        
        temp = float(self.degrees + round(self.minutes * 60.0, 1) / 60.0) % 360
        return ((360 - temp) if self.isNegative else temp)
