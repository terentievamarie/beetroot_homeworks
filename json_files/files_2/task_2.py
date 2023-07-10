import json
from operations_with_dict import add_new_entries,search_by_first_name,search_by_last_name,search_by_full_name,update_entry,delete_entry,search_by_location,search_by_telephone_number


try:
    with open(r'/Users/apple/Documents/python_beetroot/json_files/files_2/phones.json') as file:
        data=json.load(file)
except FileNotFoundError:
    raise FileNotFoundError
def writer_1():
    try:
        with open(r"/Users/apple/Documents/python_beetroot/json_files/files_2/phones.json", "w+") as file:
            json.dump(data, file)
    except FileNotFoundError:
        raise FileNotFoundError
    
result=input('what would you like to do? you can do these steps: a(add new entries),sbfn(search by first name),sbln(search by last name),sbfnm(search by full name,ue(update entry),de(delete entry),sbl(search by location),sbt(search by telephone number)')
if result.lower()=='a':
    add_new_entries(data,input('Please,enter your first name: '),input('Please,enter your last name: '),input('Please,enter your phone: '),input('Please,enter your city: '))
    writer_1()
elif result.lower()=='sbfn':
    search_by_first_name(data,input('Please,enter your first name: '))
    writer_1()
elif result.lower()=='sbln':
    search_by_last_name(data,input('Please,enter your last name: '))
    writer_1()
elif result.lower()=='sbfn':
    search_by_full_name(data,input('Please,enter your full name: '))
    writer_1()
elif result.lower()=='ue':
    update_entry(data,input('Please,enter your phone: '),input('Please,enter your field: '),input('Please,enter your value: '))
    writer_1()
elif result.lower()=='de':
    delete_entry(data,input('Please,enter your phone: '))
    writer_1()
elif result.lower()=='sbl':
    search_by_location(data,input('Please,enter your city: '))
    writer_1()
elif result.lower()=='sbt':
    search_by_telephone_number(data,input('Please,enter your phone: '))
    writer_1()
else:
    print("Enter the correct name of the operation!")
