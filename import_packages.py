import csv
from hash_table import HashTable
from package import Package
import datetime


with open('./import/package_file.csv', encoding='utf-8-sig') as in_file:
    in_file.seek(0)
    read_file = csv.reader(in_file, delimiter=",")

    package_table = HashTable()

    # Time Complexity: O(N)
    for row in read_file:
        package_id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip_code = row[4]
        deadline = row[5]
        weight = f'{row[6]} kgs'
        flag_description = row[7]

        if "Can only be" in row[7]:
            flag = "truck_specific"
        elif "Delayed" in row[7]:
            flag = "delayed"
        elif "Wrong address" in row[7]:
            flag = "wrong_address"
        elif "Must be delivered" in row[7]:
            flag = "deliver_with"
        else:
            flag = None

        package = Package(package_id, address, city, state, zip_code, deadline, weight, flag, flag_description)
        package_table.add(package)

    package_table.set_default()


    # Time Complexity: O(1)
    def get_table():
        """Returns package hash table initialized from import file"""
        return package_table