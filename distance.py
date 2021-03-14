import csv
import datetime
import main
import import_packages


# Open import files for distances
with open('./import/distance_table.csv', encoding='utf-8-sig') as distance_table:
    distance_table_csv = list(csv.reader(distance_table, delimiter=","))
with open('./import/address_list.csv', encoding='utf-8-sig') as address_list:
    address_list_csv = list(csv.reader(address_list, delimiter=","))

    # Time Complexity: O(N)
    def get_address_index(address):
        """
        Takes an address string passed in and looks for it in the address list
        If located in the list file the index is returned
        :param address:
        :return i:
        """
        for i, row in enumerate(address_list_csv):
            if address in row[0]:
                return i

    # Time Complexity: O(2) -> O(1)
    def get_distance(from_loc, to_loc):
        """
        Takes a from location and a to location
        Because the distance table is symmetrical the first level index must be greater than the second level index
        A conditional statement sets distance based on which value is larger
        Location values passed in are row/column indexes in the distance table file
        :param from_loc:
        :param to_loc:
        :return distance:
        """
        if from_loc > to_loc:
            distance = distance_table_csv[from_loc][to_loc]
            return distance
        elif to_loc > from_loc:
            distance = distance_table_csv[to_loc][from_loc]
        else:
            distance = 0
        return float(distance)


    def get_distances_list(package_list):
        """
        This algorithm starts at location 0 (WGUPS Hub) and a list of all packages being loaded onto the truck
        From the initial location, distances to all package addresses are read from the distance table and saved to
        a list. That list is sorted from shortest to longest distance using a lambda function. The first item in the
        list (shortest distance from current location) is added to the route list and is removed from the initial
        package list. The current location is set to that of the location just added to the route list.
        The algorithm repeats this process until there are no more packages left in the initial package list. Once
        this point is reached, the route list should be full populated with the shortest distances to each proceeding
        location. Once all packages have been handled, one final location is added to the route; the WGUPS Hub.
        This location has a package_id of None. The route list is then passed back to the caller.
        :param package_list:
        :return route_list:
        """
        curr = 0
        distance_list = []
        route_list = []

        # While there are packages to route
        # Time Complexity: O(N^2)
        # While loop is O(N) * internal for loop of O(N) -> O(N^2)
        while len(package_list) != 0:

            # For all IDs in temp_package list
            # Time Complexity: O(N)
            for package_id in package_list:

                # Get local copy of package
                package = import_packages.get_table().get_package(package_id)

                # Get address and distance
                package_loc_id = get_address_index(package.address)
                distance = get_distance(curr, package_loc_id)

                # Add package and distance to list
                distance_list.append(
                    {"package_id": package_id, "location": package_loc_id, "distance_from_last": distance})

            # Time Complexity: O(1)
            if len(distance_list) != 0:
                # Sort distances from current from shortest to longest
                sorted_distances = sorted(distance_list, key=lambda item: float(item["distance_from_last"]))

                # Add first (shortest distance) list item to route list
                route_list.append(
                    {"package_id": sorted_distances[0]["package_id"],
                     "distance": sorted_distances[0]["distance_from_last"]})

                # Change current location to that same address
                curr = sorted_distances[0]["location"]

                # Remove routed package from package_list
                package_list.remove(str(sorted_distances[0]["package_id"]))
                distance_list.clear()
                sorted_distances.clear()

        # Add hub to end of trip
        distance = get_distance(curr, 0)
        route_list.append({"package_id": None, "distance": distance})

        # Return list of packages in ordered route sequence
        return route_list
