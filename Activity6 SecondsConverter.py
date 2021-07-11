#This is a program that accepts time in seconds as input
#and converts it into hours, minutes and seconds

#input: prompt seconds
#processing: import the math , calculate the hour min and sec
#output:display teh hours minutes and seconds

#Prompt seconds
_scd=int(input("Enter time to be converted(in secs):  "))

#import math
import math

#Calculate the sec
f_sec = (_scd %60)

#Calculate the hour
f_hour= int((_scd //60)/60)


#Calculate the min
f_min = (_scd //60)-(f_hour *60)


#Display the hours , minutes and seconds
print("Time: %s hrs, %s min, %s sec" %(f_hour, f_min ,f_sec))


