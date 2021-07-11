
def calculatebmi(weight,height):

    bmi =weight/(height * height)
    print ("BMI:", bmi)
    return bmi

#Prompts for weight
weight = int(input("What is your weight in kg?"))

#Prompts for height
height = float(input("What is your height in m?"))

calculatebmi(weight,height)

