#This program is to display the Surface area of the cylinder
#input= radius, height,pi
#process = import pi , calculate the surface area of the cylinder
#output = display the surface area of the cylinder

#Import math
import math

#Prompt input of radius
rd= float((input("Enter the radius of the cylinder in cm: ")))

#Prompt input of height
height = float(input("Enter the height of the cylinder in cm: "))

#Calculation of Surface Area
def calculate_surface_area_cylinder(rd,height):
    S_A = float((2* (math.pi)*rd *height) + (2*(math.pi)*(rd ** 2)))
    return(S_A)

print("The surface area of the cylinder is " + \
      str(calculate_surface_area_cylinder(rd,height)))
