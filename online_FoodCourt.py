import fontstyle
welcome = fontstyle.apply(" Welcome to the online food court ", "white/GREEN_BG")
print(welcome)
print()
food1 = {"pasta":12, "noodles":3, "burger":5, "sandwitch":6, "veg_roll":7}
price1 = {"pasta":200, "noodles":150, "burger":350, "sandwitch":250, "veg_roll":70}
class restaurent:
    global food1
    global price1
    def __init__(self):
        self.food = food1
        self.price = price1
        self.total_price = 0
    def order_taken(self, food_nm, quantity):
        self.total_price += self.price[food_nm]*quantity
        if(self.food[food_nm] == 0):
            return (0, self.total_price)
        elif(self.food[food_nm] >= quantity):
            self.food[food_nm] -= quantity
            return (1, self.total_price)
        elif(self.food[food_nm] <= quantity):
            return (2, self.total_price)
obj = restaurent()
class customer:
    global food1
    global price1
    def __init__(self, nm, food_nm, quantity, location):
        self.name = nm
        self.foodn = food_nm
        self.foodq = quantity
        self.location = location.lower()
        self.bill2 = 0
    def order_given(self):
        order = obj.order_taken(self.foodn, self.foodq)
        if(order[0] == 0):
            return f"Sorry, the {self.foodn} is finished.", 0
        elif(order[0] == 1):
            bill2 = self.total_bill(order[1])
            self.bill2 = bill2
            return f"Order recieve successfully, and the total price is {bill2}.", 1
        elif(order[0] == 2):
            return f"Sorry, we cannot give you the quantity you want.\nWe can give {food1[self.foodn]} {self.foodn}(s).", 2
    def total_bill(self, p):
        bill = p
        if(self.location == "dhaka"):
            bill += 70
        else:
            bill += 120
        return bill
    def details(self):
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print(fontstyle.apply("$    Your Total Bill     $", "bold/black/Italic"))
        print(f"Customer Name: {self.name.upper()}")
        print(f"Ordered Food: {self.foodn.upper()}")
        print(f"Ordered Food Quantity: {self.foodq}")
        print(f"The total bill including delivery charge: {self.bill2}")
        print(f"Thank you for purchasing food. Have a nice day.")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n")

# ==============================================================================
sum1 = sum(food1.values())
while(sum1 != 0):
    name = input("Pleaase, enter your name: ")
    foodnm = input("Please enter the food you want: ").lower()
    q = input("Please, enter the quantity you want: ")
    location = input("please, enter you location: ")
    customer1 = customer(name, foodnm, int(q), location)
    sum1 = sum(food1.values())
    orderg = customer1.order_given()
    print(orderg[0])
    print()
    if(orderg[1] == 1):
        customer1.details()
    elif(orderg[1] == 0):
        break
    obj.total_price = 0
