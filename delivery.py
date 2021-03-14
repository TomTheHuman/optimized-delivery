import main
import distance
from datetime import timedelta, time, datetime
import import_packages


# Time Complexity: O(1)
def load_truck(truck, package_list):
    """
    Saves local copy of ordered delivery route list
    Copies local delivery route list to the truck instance passed
    :param truck:
    :param package_list:
    :return:
    """
    ordered_list = distance.get_distances_list(package_list).copy()
    truck.route = ordered_list.copy()


# Time Complexity: O(2N) -> O(N)
def run_route(truck, time_of_day):
    """
    Using the time of day passed in this function processes each package on the truck
    If the calculated delivered time for each package is before the time of day the package will be updated
    Packages with a delivery time later than the time of day will be skipped and left in their previous status
    Using each package's distance value a time delta is calculated to generate delivery times
    Delivered packages have their status and delivery time updated
    When the last item in the route list is reached the truck's arrival time is set
    :param truck:
    :param time_of_day:
    :return:
    """
    # Local copy of variables
    route_data = truck.route.copy()
    depart = truck.depart

    # Time Complexity: O(N)
    for item in route_data:
        if item["package_id"] is not None:
            package = import_packages.get_table().get_package(item["package_id"])
            package.status = "En Route"

    # Time Complexity: O(N)
    for item in route_data:
        # Calculate time of delivery
        delta = timedelta(minutes=((float(item["distance"])/truck.mph)*60))
        dt = datetime.combine(datetime.today(), depart) + delta
        depart = dt.time()

        if dt.time() <= time_of_day:
            # Remove package from truck and update mileage
            truck.mileage += float(item["distance"])

            if item["package_id"] is not None:
                # Update package data in table
                package = import_packages.get_table().get_package(item["package_id"])
                package.status = "Delivered"
                package.delivered_time = dt.time().strftime("%I:%M %p")
                import_packages.get_table().update(package)
            elif item["package_id"] is None:
                truck.arrive = dt.time()
        else:
            return



