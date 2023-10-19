#https://replit.com/join/xrvgluelyl-nery-eduardoedu
#inputs
age=int(input("Introduce your age: "))
weight=float(input("Introduce your weight: "))
height=float(input("Introduce your Height: "))
print("Options: ")
print("Sedentary")
print("Moderate")
print("Active")
PA=str(input("Introduce your Physical Activity: "))
BMI=weight/(height**2)
#if´s
if age<=18:
  print("High carbohydrate diet recommended")
elif age>=18 and age<35:
  print("High protein annd lower carbohydrate diet reccomended")
elif age>35:
  print("low sugar diet reccomended") 
if(age>=18and age<=30)and(PA=="Sedentary" or PA=="Moderate" ):
  print("You need aerobic exercises")
if BMI<18 and PA=="Sedentary":
  print("Consult nutrisionist")
  print("Increase physical activity")
elif (BMI>18 and BMI<25) and (PA=="Moderate" or PA=="Active"):
  print("You're in good condition")
elif BMI>25 and PA=="Sedentary":
  print("Consult a nutrisionits")
  print("Increase Physical Activity")
  print("Decrease weight")
print("Your BMI is: ",BMI)
