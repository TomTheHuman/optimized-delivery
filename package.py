class Package:

    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, flag, flag_description):
        # Initialize package object for adding to data structure
        # Set self values with imported data
        self.package_id = package_id  # The package ID
        self.address = address  # Package shipping address
        self.city = city  # City of shipping address
        self.state = state  # State of shipping address
        self.zip_code = zip_code  # Zip code of shipping address
        self.deadline = deadline  # Delivery date/time deadline
        self.weight = weight  # Weight of package
        self.flag = flag  # Flag for packages with special notes
        self.flag_description = flag_description  # Description of flag

        # Set default values
        if flag == "delayed":
            self.status = "Delayed"  # Status of package
        else:
            self.status = "At the Hub"
        self.delivered_time = None  # Time of delivery


