#This program is to calculate final mark of a module

#Prompt for Student Name
Student_Name = input("What is your name?")

#Prompt for CA marks
Ca_mark = input("What mark did you receive for your Continuous Assessment(CA) mark?")


#Prompt for Assignment marks
Assignment_mark = input("What mark did you receive for your Assignment?")


#Prompt for Common Test marks
CT_mark=input("What mark did you receive for you Common Test")

#Final mark(very messy)
print(Student_Name +"'s final mark is " + \
      str((0.4 * float(Ca_mark))+\
          (0.3 * float(Assignment_mark))+ \
          (0.3 * float(CT_mark))))

