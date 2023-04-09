# WRITE YOUR FUNCTIONS HERE
#1
def get_pet_shop_name(cc_pet_shop):
    name=cc_pet_shop['name']
    return name
#2 
def get_total_cash(cc_pet_shop):
    sum=cc_pet_shop['admin']['total_cash']
    return sum
#3
def add_or_remove_cash(pet_shop,money):
    pet_shop['admin']['total_cash'] += money
    return pet_shop['admin']['total_cash']

#4
def add_or_remove_cash(pet_shop,money):
    pet_shop['admin']['total_cash'] += money
    return pet_shop['admin']['total_cash']

#5
def get_pets_sold(pet_shop):
    pets_sold=pet_shop['admin']['pets_sold']
    return pets_sold

#6
def increase_pets_sold(pet_shop,number_petsold):
    pet_shop['admin']['pets_sold']+=number_petsold
    return pet_shop['admin']['pets_sold']
#7
def get_stock_count(pet_shop):
    pets_stock=len(pet_shop['pets'])
    return pets_stock

#8/9
def get_pets_by_breed(pet_shop, breed_name):
    breed_sum=[]
    for pet in pet_shop['pets']:
        if breed_name==pet['breed']:
            breed_sum.append(pet['breed'])

    return breed_sum

#10 #11  note: loop in a loop 
def find_pet_by_name(pet_shop, pet_name):
    #note: possible that 2 pets has the same name?
    pets=[]
    for pet in pet_shop['pets']:
      if pet_name==pet['name']:
          pets.append(pet)
          for pet_info in pets:
           return pet_info
      else: 
        pass 
#note pass means if the pet_name is not in the dictionary, do nothing, in this case, pets=[] will be left empty.


# 12
def remove_pet_by_name(pet_shop, pet_name):
    pets=[]
    for pet in pet_shop['pets']:
      if pet_name==pet['name']:
         pet_shop['pets'].remove(pet) #-->note: to remove a dictionay in a group of dictionaries
#13
def  add_pet_to_stock(pet_shop, new_pet):
    pet_shop['pets'].append({'name':'new_pet'})
    return len(pet_shop['pets'])


def get_customer_cash(customer):
    return customer['cash']

#15
def remove_customer_cash(customer, remove_amount):
    customer['cash']=  customer['cash']-remove_amount


#16  
def get_customer_pet_count(customer):
    return len(customer['pets'])


#17
def add_pet_to_customer(customer, new_pet):
    customer['pets'].append(new_pet)
    return len(customer['pets'])

#18 # 19 #20
def customer_can_afford_pet(customer, new_pet):
     customer['cash']-=new_pet['price']
     if customer["cash"]>=0:
        return True
     else:
        return False

#21 22 23

# note: correct outcomes in zhu_test.py
# def  sell_pet_to_customer(pet_shop, pet_name, customer):
#     for pet in pet_shop['pets']:
#      if pet_name==pet['name']:
#         customer['pets'].append(pet_name)#-->['Arthur] 
#         pet_shop['admin']['pets_sold']+=1#-->1
#         customer['cash']-=pet['price']#-->100
#         pet_shop['admin']['total_cash']+=pet['price']#-->1900
       
#     return   len(customer['pets'])#-->1

#note try 2nd. 
#note: does it mean pet={} dictionary with "arthur"?

def  sell_pet_to_customer(pet_shop, pet_diction, customer):
    for pet in pet_shop['pets']:
     if pet_diction==pet and customer['cash']>=pet['price']:
        customer['pets'].append(pet_diction['name'])#-->['Arthur] 
        pet_shop['admin']['pets_sold']+=1#-->1
        customer['cash']-=pet['price']#-->100
        pet_shop['admin']['total_cash']+=pet['price']#-->1900
       
    return   len(customer['pets'])#-->1

#note: it works!!!


