from copy import deepcopy


# Time Complexity: O(1)
def print_package(package):
    """
    Prints all details for package passed in in formatted line item
    Takes 3 lines including separator space after each iteration
    :param package:
    :return:
    """
    print('%-18s'%f'Package ID: {package.package_id}' + '%-20s'%f'Status: {package.status}' +
          '%-75s'%f'Address: {package.address}, {package.city}, {package.zip_code}')
    if package.status == "Delivered":
        print('%-48s'%f'  Weight: {package.weight} - Delivery Deadline: {package.deadline}' +
              '%-75s'%f'Delivery Time: {package.delivered_time}')
    else:
        print('%-48s'%f'  Weight: {package.weight} - Delivery Deadline: {package.deadline}')

    print()


class HashTable:

    # Time Complexity: O(1)
    def __init__(self, size=10):
        """Initialize hash table and default table with 10 buckets"""
        self.table = []
        self.default = []
        for bucket in range(size):
            self.table.append([])
            self.default.append([])

    # Time Complexity: O(1)
    def set_default(self):
        """Create deep copy of current table to default table"""
        self.default = deepcopy(self.table)

    # Time Complexity: O(1)
    def reset(self):
        """Reset table with default table data using deep copy to overwrite changes"""
        self.table = deepcopy(self.default)

    # Time Complexity: O(1)
    def get_hash(self, key):
        """
        Generate a hash key value
        :param key:
        :return: hash key
        """
        return int(key) % len(self.table)

    # Time Complexity: O(N)
    def add(self, package):
        """
        Append a package item to the table
        :param package:
        :return: True or False
        """
        index = self.get_hash(package.package_id)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item.package_id is package.package_id:
                    return True
            self.table[index].append(package)
            return True
        else:
            self.table[index].append(package)
            return True

    # Time Complexity: O(N)
    def update(self, package):
        """
        Update a package item in the hash table
        :param package:
        :return: True or False
        """
        index = self.get_hash(package.package_id)
        if self.table[index] is not None:
            for i, item in enumerate(self.table[index]):
                if item.package_id is package.package_id:
                    self.table[index][i] = package
                    return True
        else:
            print(f'Could not locate package with ID {package.package_id}. Package was not updated.')
            return False

    # Time Complexity: O(N)
    def remove(self, package):
        """
        Remove a package item from the hash table
        :param package:
        :return: True or False
        """
        index = self.get_hash(package.package_id)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item.package_id is package.package_id:
                    self.table[index].remove(item)
                    return True
        else:
            print(f'Could not locate package with ID {package.package_id}. Package was not removed.')
            return False

    # Time Complexity: O(N)
    def get_package(self, package_id):
        """
        Takes a package ID passed in and locates it within the hash table
        Package item is returned to the caller
        :param package_id:
        :return:
        """
        index = self.get_hash(package_id)
        if self.table[index] is not None:
            for item in self.table[index]:
                if item.package_id == package_id:
                    return item
        else:
            print(f'Could not locate package with ID {package_id}.')
            return None

    # Time Complexity: O(N)
    def print_all(self):
        """Sends each item in the hash table to print_package() method"""
        index = 0
        for list_item in self.table:
            for item in list_item:
                print_package(item)
