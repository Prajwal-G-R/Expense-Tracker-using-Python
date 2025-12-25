#Pythone code for Expense Tracker CLI
user_data = [10 , 20] 
print("Welcome to Expense Tracker")
while True:
 print(" 1. Add Expense \n 2. View Expense \n 3. Show Total \n 4. Exit ")

 user_input = int(input("Please enter your option from the abouce menue "))

 if user_input==1:
   User_input = int(input("Enter the amount of your expense"))
   user_data.append(User_input)
   print("You expense is added succesfully")

 if user_input==2:
   print(user_data)

 if user_input==3:
   i = 0 
   sum = 0 
   while i < len(user_data):
     sum += user_data[i]
     i = i + 1 

   print(sum)

 if user_input==4:
   print("Exit")
   break

