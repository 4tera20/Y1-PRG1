#This program calculates the total cost of an item with GST

#Prompting for price of item
price_of_item = input("What was the price of the item in dollars?")
 

#Prompting for GST
gst_item=input("What was the percentage of GST chargable on the item?")


#Calculation of Total Percentage Chargable
total_percentage= int(gst_item)/100 + 1
total_cost = (total_percentage * float(price_of_item))

#Display of the total cost
print(total_cost)
