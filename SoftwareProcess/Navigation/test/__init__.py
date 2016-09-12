import Navigation.prod.Angle as Angle
angle1 = Angle.Angle()
angle2 = Angle.Angle()
angle3 = Angle.Angle()
angle4 = Angle.Angle()
#angle1Degrees = angle1.setDegreesAndMinutes("52d10")   #angle1Degrees should be 45.0        
angle2Degrees = angle2.setDegrees(degrees=50.5)

#angle3Degrees = angle3.setDegrees(19.43)        #angle2Degrees should be 340.5        
#angle3Degrees = angle3.setDegreesAndMinutes("36d5")   #angle3Degrees should be 0.5 
#angle4Degrees = angle4.setDegreesAndMinutes("15d5")     
#addangle1=angle1.add("43d4")
#addangle2=angle2.add("15d0") 
#subangle1=angle2.subtract("-386d30")
#anglestring1=angle2.getString()
 
#print angle3Degrees
print angle2Degrees
compAngle1=angle2.compare("25d3")
print compAngle1

#print addangle2
#print subangle1

#angle1Degrees=angle1Degrees+angle2Degrees

#print angle1Degrees
#print addangle2


