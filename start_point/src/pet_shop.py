# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(get_name):
    return get_name["name"]

def get_total_cash(cash_total):
    return cash_total["admin"]["total_cash"]

def add_or_remove_cash(cash_total, cash_change):
    cash_total["admin"]["total_cash"] += cash_change
    
def get_pets_sold(amount_sold):
    return amount_sold["admin"]["pets_sold"]

def increase_pets_sold(amount_sold, new_sold):
     amount_sold["admin"]["pets_sold"] += new_sold

def get_stock_count(stock_count):
    return len(stock_count["pets"])

def get_pets_by_breed(pet_shop_list, breed):
    new_list = []
    for pet in pet_shop_list["pets"]:
        if pet["breed"] == breed:
            new_list.append(pet)
    return new_list

def find_pet_by_name(pet_shop_list, name):
    for pet in pet_shop_list["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(pet_shop_list, name):
    for pet in pet_shop_list["pets"]:
        if pet["name"] == name:
            pet_shop_list["pets"].remove(pet)
 
def add_pet_to_stock(pet_shop_list, new_pet):
        pet_shop_list["pets"].append(new_pet)
        
def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, cash):
    customer["cash"] -= cash

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
     customer["pets"].append(1)














































    # current_total = cash_total["admin"]["total_cash"]
    # cash_added = cash_change
    # return current_total += cash_added













 


