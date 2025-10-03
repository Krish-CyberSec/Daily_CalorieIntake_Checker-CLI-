import csv
from datetime import datetime
import os



#Name : Krish Kumar 
#Date : 03-10-2025
#Title: Daily calorie Tracker CLI Program !

print("\n✨ Welcome to the Daily Calorie Tracker CLI! ✨")
print("This tool helps you log your meals, calculate total and average calories,")
print("and check if you're staying within your daily calorie limit.\n")
print("Let's get started!\n")


Meal_Name=set() # To Prevent Dublicates used set
Meal_Cal=[]
result='' #Limit result
User_Data={} #store final data
N_user=input("Enter Your Name : ") # getting  the name of the user 
Cal_Limit=float(input("Enter the max amount of calories you want to maintain : "))
N_meal=int(input("\n How many Meals you want to add today? :  ")) # Checking how many meals the users wants to add today ?

for i in range(N_meal):
    M_Name=input(f"Enter the Meal name {i+1}  : ") #Getting the meal name from the user
    cal=float(input("Enter the amount of cal get : ")) #Getting the cal 
    Meal_Name.add(M_Name) #Storing it into the set
    Meal_Cal.append(cal) #Storing the cal
#Chekcing the Limit of Calories intaked is maintained or not
total_cal=sum(Meal_Cal)
if  total_cal==Cal_Limit:
    print("Hurray You maintained the calories intacke")
    result="Maintained"
elif total_cal <Cal_Limit:
    print(f"Not maintained the calories intacke , it is less than {Cal_Limit-total_cal}")
    result=f"Not Maintained the calories intake by, it is less than {Cal_Limit-total_cal} "
else:
    print(f"You exceeds the limit by {total_cal-Cal_Limit} ")
    result=f"Not Maintained by {total_cal-Cal_Limit}"



#Printing Formated CLI Output 
print("\n 📝 Summary of Your Meals:\n ")
print("Meal Name \t\tCalories")
print("-"*30)
for meal,cal in zip(Meal_Name,Meal_Cal):
    print(f"{meal:<16}\t{cal}")

print("-" * 30)
print(f"Total:\t\t\t{total_cal}")
print(f"Average:\t\t{(total_cal)/len(Meal_Cal)}")
print(f"Status:\t\t\t{result}")

#Checking if the user want to store the session or not 
save_log=input("\n💾 Do you want to save this session log to a file? (y/n): ").lower()
if save_log == 'y':
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y_%H-%M-%S")
    filename = f"{N_user}_calorie_log_{timestamp}.txt"

    with open(filename, "w",encoding="utf-8") as f:
        f.write("✨ Daily Calorie Tracker Log ✨\n")
        f.write(f"Name: {N_user}\n")
        f.write(f"Date: {now.strftime('%d-%m-%Y')}\n")
        f.write(f"Calorie Limit: {Cal_Limit}\n\n")
        f.write("Meal Name\t\tCalories\n")
        f.write("-" * 30 + "\n")
        for meal, cal in zip(Meal_Name, Meal_Cal):
            f.write(f"{meal:<16}\t{cal}\n")
        f.write("-" * 30 + "\n")
        f.write(f"Total:\t\t\t{total_cal}\n")
        f.write(f"Average:\t\t{(total_cal)/len(Meal_Cal)}\n")
        f.write(f"Status:\t\t\t{result}\n")

    print(f"\n✅ Session saved successfully to '{filename}'")
else:
    print("\n📂 Session not saved.")

print("\n👋 Thank you for using the Daily Calorie Tracker. Stay healthy!")





#checking If the user exist already or not !  ( will add some more functionality in future => for now i am leaving this )
# if N_user in User_Data:
#     print("User already exists. Do you want to update the details?")
#     choice = input("Press Y to update, N to keep old data: ").lower()
#     if choice == 'y':
#         User_Data[N_user] = {
#             "Meals": list(Meal_Name),
#             "Calories": Meal_Cal,
#             "limit":Cal_Limit,
#             "Toatal Calories": total_cal,
#             "Avg calories intake":(total_cal)/len(Meal_Cal),
#             "Result":result

#     }
#     else:
#         print("Old data kept unchanged.")
# else:
#      User_Data[N_user] = {
#             "Meals": list(Meal_Name),
#             "Calories": Meal_Cal,
#             "limit":Cal_Limit,
#             "Toatal Calories": total_cal,
#             "Avg calories intake":(total_cal)/len(Meal_Cal),
#             "Result":result
#         }