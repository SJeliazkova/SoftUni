type_fuel = input()
quantity_fuel = float(input())

if quantity_fuel >= 25:
    if type_fuel == "Diesel":
        print(f"You have enough diesel.")
    elif type_fuel == "Gasoline":
            print(f"You have enough gasoline.")
    elif type_fuel == "Gas":
        print(f"You have enough gas.")
    else:
        print("Invalid fuel!")

else:
    if type_fuel == "Diesel":
        print(f"Fill your tank with diesel!")

    elif type_fuel == "Gasoline":
        print(f"Fill your tank with gasoline!")

    elif type_fuel == "Gas":
        print(f"Fill your tank with gas!")
    else:
        print("Invalid fuel!")