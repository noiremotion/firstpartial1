#https://replit.com/join/arbqenzpzt-nery-eduardoedu
cost=int(input("Enter the purchase amount: "))
memberC=str(input("Do you have a membership card?: (Y/N)"))
if cost>=100:
  discount=10
  promotion1="Yes"
else:
  promotion1="No"
if cost<=100 and memberC=="Y":
  discount=5
else:
  promotion2="No"
  price2=cost
price2=cost-(cost*(discount/100))
print("The discount amount is: ",discount,"%")
print("The cost is: ",cost)
print("The state of your membership card is: ",memberC)
print("Therefore your promotions state is: ")
print("Promo 1: ",promotion1)
print("Promo 2: ",promotion2)
print("Full payment: ",price2)
