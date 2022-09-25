from random import randrange

def get_numbers_ticket(min, max, quantity):
    my_list=list()
    if min<1 or max>1000 or quantity not in (range(min+1,max)):
        return my_list
    else:
        while quantity>0:
            item=randrange(min,max+1)
            print(f'{item},{item  in my_list}') 
            if item not in my_list:
                my_list.append(item)
                quantity-=1
        my_list.sort()
        return my_list

print(get_numbers_ticket(1, 10,7))