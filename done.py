import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="local_host",
    user="root",
    database="farm_management"
)

# Create a cursor
cursor = db.cursor()

def add_farm(name, location, size):
    query = "INSERT INTO farm (name, location, size) VALUES (%s, %s, %s)"
    values = (name, location, size)
    cursor.execute(query, values)
    db.commit()
    print("Farm added successfully!")

# Function to add a new crop to a specific farm
def add_crop(name, planting_date, harvest_date, farm_id):
    query = "INSERT INTO crop (name, planting_date, harvest_date, farm_id) VALUES (%s, %s, %s, %s)"
    values = (name, planting_date, harvest_date, farm_id)
    cursor.execute(query, values)
    db.commit()
    print("Crop added successfully!")

def add_poultry(name, quantity, farm_id):
    query = "INSERT INTO poultry (name, quantity, farm_id) VALUES (%s, %s, %s)"
    values = (name, quantity, farm_id)
    cursor.execute(query, values)
    db.commit()
    print("Poultry added successfully!")

# Function to add a new animal product to a specific farm
def add_animal_product(name, quantity, farm_id):
    query = "INSERT INTO animal_product (name, quantity, farm_id) VALUES (%s, %s, %s)"
    values = (name, quantity, farm_id)
    cursor.execute(query, values)
    db.commit()
    print("Animal product added successfully!")

# Function to add a new farm owner to a specific farm
def add_farm_owner(name, email, phone, farm_id):
    query = "INSERT INTO farm_owner (name, email, phone, farm_id) VALUES (%s, %s, %s, %s)"
    values = (name, email, phone, farm_id)
    cursor.execute(query, values)
    db.commit()
    print("Farm owner added successfully!")

# Function to add a new equipment rental by a farmer
def add_equipment_rental(equipment_name, start_date, end_date, farmer_id):
    query = "INSERT INTO equipment_rental (equipment_name, start_date, end_date, farmer_id) VALUES (%s, %s, %s, %s)"
    values = (equipment_name, start_date, end_date, farmer_id)
    cursor.execute(query, values)
    db.commit()
    print("Equipment rental added successfully!")

# Modify the main program to include the equipment rental option
if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Add a new farm")
        print("2. Add a new crop")
        print("3. Add poultry")
        print("4. Add animal product")
        print("5. Add farm owner")
        print("6. Add equipment rental")
        print("7. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter farm name: ")
            location = input("Enter farm location: ")
            size = float(input("Enter farm size (acres): "))
            add_farm(name, location, size)

        elif choice == "2":
            name = input("Enter crop name: ")
            planting_date = input("Enter planting date (YYYY-MM-DD): ")
            harvest_date = input("Enter harvest date (YYYY-MM-DD): ")
            farm_id = int(input("Enter farm ID: "))
            add_crop(name, planting_date, harvest_date, farm_id)

        elif choice == "3":
            name = input("Enter poultry name: ")
            quantity = int(input("Enter quantity: "))
            farm_id = int(input("Enter farm ID: "))
            add_poultry(name, quantity, farm_id)

        elif choice == "4":
            name = input("Enter animal product name: ")
            quantity = int(input("Enter quantity: "))
            farm_id = int(input("Enter farm ID: "))
            add_animal_product(name, quantity, farm_id)

        elif choice == "5":
            name = input("Enter farm owner name: ")
            email = input("Enter farm owner email: ")
            phone = input("Enter farm owner phone: ")
            farm_id = int(input("Enter farm ID: "))
            add_farm_owner(name, email, phone, farm_id)

        elif choice == "6":
            equipment_name = input("Enter equipment name: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            farmer_id = int(input("Enter farmer/owner ID: "))
            add_equipment_rental(equipment_name, start_date, end_date, farmer_id)

        elif choice == "7":
            break
