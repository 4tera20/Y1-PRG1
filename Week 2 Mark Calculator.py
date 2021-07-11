#This program is to calculate final mark of a module

#Prompt for Student Name
Student_No = int(input("Enter in your StudentNo:"))

#Prompt for CA marks
Ca_mark = int(input("Enter in your Continuous Assessment(CA) mark:"))


#Prompt for Assignment marks
A_mark = int(input("Enter in your Assignment results:"))


#Prompt for Common Test marks
CT_mark=int(input("Enter in your Common Test results:"))

#Calculation of Final Mark
F_Mark=str((0.4 * float(Ca_mark))+\
          (0.3 * float(A_mark))+ \
          (0.3 * float(CT_mark)))

#Print row one
print("{:<10s}{:10s}{:10s}{:10s}{:s}".format("StudentNo","Test","Assign","CA","Final"))

#Print row two
print("{:<10d}{:<10d}{:<10d}{:<10d}{:<10s}".format(Student_No,CT_mark,A_mark,Ca_mark,F_Mark))
