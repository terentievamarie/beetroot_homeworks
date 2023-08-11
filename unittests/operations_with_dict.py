def add_new_entries(phones_list,first_name,second_name,phone,city):
    name=first_name+' '+ second_name
    phones_list.append({name:{'phone':phone,'city':city}})
    return phones_list

def search_by_first_name(phones_list, first_name):
    output_list = []
    for el in phones_list:
        for key in el.keys():
            if first_name in key:
                output_list.append(el)
                break
    return output_list

def search_by_last_name(phones_list,  last_name):
    output_list = []
    for el in phones_list:
        for key in el.keys():
            if last_name in key:
                output_list.append(el)
                break
    return output_list

def search_by_full_name(phones_list,full_name):
    output_list=[]
    for el in phones_list:
        for key in el.keys():
            if key==full_name:
                output_list.append(el)
                break
    return output_list

def update_entry(phones_list, phone, new_key, new_value):
    for item in phones_list:
        for value in item.values():
            if value["phone"] == phone:
                value[new_key] = new_value
                return phones_list
            
def delete_entry(phones_list, phone):
    for item in phones_list:
        for value in item.values():
            if value['phone']==phone:
                phones_list.remove(item)
    return phones_list

def search_by_location(phones_list,city):
    output_list=[]
    for item in phones_list:
        for el in item.values():
            if el.get('city')==city:
                output_list.append(item)
    return output_list

def search_by_telephone_number(phones_list,phone):
    output_list=[]
    for item in phones_list:
        for el in item.values():
            if el.get('phone')==phone:
                output_list.append(item)
    return output_list