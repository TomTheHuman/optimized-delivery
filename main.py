# Author: Thomas Shaw
# Student ID: 001425966

import hash_table
import truck
import delivery
import import_packages
import distance
from datetime import *

if __name__ == '__main__':
    """
    Trucks are initialized and loaded
    User is presented with a CLI for managing packages and routes based on their input time
    CLI uses a looping main menu
    Upon looping the packages hash table is reset
    Every time an option is selected all routes are ran and data is populated for packages based on the given input
    time. Package or truck data is then displayed depending on the option selected. 
    """

    # Time Complexity: O(1)
    def print_truck_mileage():
        """Prints individual and total truck mileage in readable format"""
        print(f'Truck mileage for {tod_string}')
        print(f'  Truck #1: %.2f miles'%truck1.mileage)
        print(f'  Truck #2: %.2f miles'%truck2.mileage)
        print(f'  Truck #3: %.2f miles'%truck3.mileage)
        print(f'  TOTAL MILEAGE: %.2f miles\n'%(truck1.mileage + truck2.mileage + truck3.mileage))


    # Time Complexity: O(1)
    def run_routes():
        """
        Sets truck depart times
        Based on user's entered time_of_day trucks will have their route initiated
        Once truck 1 or 2 return, the earlier arrival time between them is used as truck 3's depart time
        """
        # Set depart time
        truck1.depart = time(8, 0)
        truck2.depart = time(9, 30)
        truck3.depart = time(23, 59)

        # Run routes
        if truck1.depart <= time_of_day:
            delivery.run_route(truck1, time_of_day)
        if truck2.depart <= time_of_day:
            delivery.run_route(truck2, time_of_day)

        if truck1.arrive is not None and truck2.arrive is not None:
            if truck1.arrive <= truck2.arrive:
                truck3.depart = truck1.arrive
            else:
                truck3.depart = truck2.arrive

        if truck3.depart <= time_of_day:
            delivery.run_route(truck3, time_of_day)


    # Time Complexity: O(1)
    def handle_incorrect_address(package_id, address, city, state, zip_code):
        """
        Takes passed in parameters to update the package with incorrect data
        :param package_id:
        :param address:
        :param city:
        :param state:
        :param zip_code:
        :return:
        """
        # Update package with incorrect address
        package = import_packages.get_table().get_package(package_id)
        package.address = address
        package.city = city
        package.state = state
        package.zip_code = zip_code

    # User interface menu
    choice = 0
    print('========================================')
    print('=       WGUPS MANAGEMENT SYSTEM        =')

    # Time Complexity: O(N)
    while choice != '4':
        # Initialize variables
        truck1 = truck.Truck(1)
        truck2 = truck.Truck(2)
        truck3 = truck.Truck(3)
        import_packages.get_table().reset()

        # Load Trucks
        delivery.load_truck(truck1, ['1', '4', '5', '7', '13', '14', '15', '16', '20', '21', '29', '30', '31', '34', '37', '40'])
        delivery.load_truck(truck2,
                   ['2', '3', '6', '10', '17', '18', '22', '23', '24', '25', '26', '28', '32', '33', '36', '38'])
        delivery.load_truck(truck3, ['8', '9', '11', '12', '19', '27', '35', '39'])

        # Present menu options
        print('========================================')
        print('Choose an option from the list:')
        print('  1. View all packages')
        print('  2. Find a package')
        print('  3. View truck mileage')
        print('  4. Exit\n')
        choice = input('Option: ')
        if choice == '4':
            print('Goodbye')
            exit()
        # Time Complexity: O(N)
        while choice not in ['1', '2', '3', '4']:
            choice = input('Invalid entry! Please enter an option from the list: ')
        print()

        # Collect time of day
        print('Enter time of day (ex. 2:30 PM)...')
        hour = input('Hour: ')
        while len(hour) == 0 or int(hour) < 0 or int(hour) > 12:
            hour = input('Enter a valid hour (0 - 12): ')
        minute = input('Minute: ')
        while len(minute) == 0 or int(minute) < 0 or int(minute) > 59:
            minute = input('Enter a valid minute value (0 - 59): ')
        am_pm = input('AM or PM: ')
        while len(am_pm) == 0 or am_pm.lower() != 'am' and am_pm.lower() != 'pm':
            am_pm = input('Enter AM or PM (not case-sensitive): ')
        print()

        # Set time of day
        if am_pm.lower() == 'pm':
            if hour == '12':
                hour_val = int(hour)
            else:
                hour_val = int(hour) + 12
        else:
            hour_val = int(hour)
        minute_val = int(minute)
        time_of_day = time(hour_val, minute_val)
        tod_string = time_of_day.strftime("%I:%M %p")

        # Correct package address if 10:20 AM or later
        if time_of_day == time(10, 20):
            print('Please confirm corrected address for package ID #9:')
            print('  Incorrect: 300 State St., Salt Lake City, UT, 84103')
            print('  Correct: 410 S State St., Salt Lake City, UT, 84111\n')
            print('   1. Confirm address')
            print('   2. Exit\n')
            correction_choice = input('Option: ')

            # Time Complexity: O(N)
            while correction_choice not in ['1', '2']:
                correction_choice = input('Invalid option! Please enter 1 or 2: ')
            if correction_choice == '1':
                handle_incorrect_address('9', "410 S State St", "Salt Lake City", "UT", "84111")
            elif correction_choice == '2':
                print('Goodbye')
                exit()
        if time_of_day > time(10, 20):
            print('Address for package ID #9 was corrected at 10:20 AM:')
            print('  Incorrect: 300 State St, Salt Lake City, UT, 84103')
            print('  Correct: 410 S State St, Salt Lake City, UT, 84111\n')
            handle_incorrect_address('9', "410 S State St", "Salt Lake City", "UT", "84111")

        # Run routes based on time of day
        run_routes()

        # Perform tasks based on options
        if choice == '1':
            print(f'Displaying all packages for {tod_string}...\n')
            import_packages.get_table().print_all()
        elif choice == '2':
            # Collect package ID
            package_id = input('Enter a package ID: ')

            # Print results
            print(f'Displaying package ID {package_id} for {tod_string}...\n')
            package = import_packages.get_table().get_package(package_id)
            if package is not None:
                hash_table.print_package(package)
        elif choice == '3':
            print_truck_mileage()




