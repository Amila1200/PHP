fname = input("Enter your first_name : ")
lname = input("Enter your last_name : ")
ad = input("Enter your permanent address : ")
tp = input("Enter your mobile number : ")
p1 = float(input("Enter the price 01 : "))
p2 = float(input("Enter the price 02 : "))
p3 = float(input("Enter the price 03 : "))
dis1 = float(input("Enter the discount as percentage : "))
np = p1 + p2 + p3
dis = np * (dis1/100)
newprice = np - dis
print("Full name is                  : ",fname + "" + lname)
print("Address                       : ",ad)
print("Telophone Number              : ",tp)
print("Price                         : ",np)
print("Discount as percentage        : ",dis1 + "" + "%")
print("Discount                      : ",dis)
print("Net Price                     : ",newprice)

