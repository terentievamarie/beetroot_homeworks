import unittest
from operations_with_dict import add_new_entries, search_by_first_name, update_entry
from phones import return_result
import json

with open(r'/Users/apple/Documents/python_beetroot/unittests/phones.json') as file:
    data = json.load(file)

class TestPhones(unittest.TestCase):


    def test_add_new_entries(self):
        phones_list = []
        result = add_new_entries(phones_list, "Maria","Terentieva", "+34005043","Kiev")
        self.assertEqual(result, [{"Maria Terentieva":{'phone':"+34005043",'city':"Kiev"}}])


    def test_search_by_name(self):
        result = search_by_first_name(data, "Lu Ran Ran")
        self.assertEqual(result, 
    [{
        "Lu Ran Ran": {
            "phone": "+1893",
            "city": "Athens"
        }
    }])

  
    def test_return_result(self):
        result = return_result()
        self.assertEqual(result, "Done. ")

if __name__ == '__main__':
    unittest.main()