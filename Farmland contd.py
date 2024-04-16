
def add_equipment_rental(equipment_name, start_date, end_date, farmer_id):
    query = "INSERT INTO equipment_rental (equipment_name, start_date, end_date, farmer_id) VALUES (%s, %s, %s, %s)"
    values = (equipment_name, start_date, end_date, farmer_id)

    print("Equipment rental added successfully!")

    
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
            

        elif choice == "2":
            name = input("Enter crop name: ")
            planting_date = input("Enter planting date (YYYY-MM-DD): ")
            harvest_date = input("Enter harvest date (YYYY-MM-DD): ")
            
            

        elif choice == "3":
            name = input("Enter poultry name: ")
            quantity = int(input("Enter quantity: "))
            
            

        elif choice == "4":
            name = input("Enter animal product name: ")
            quantity = int(input("Enter quantity: "))
            
            

        elif choice == "5":
            name = input("Enter farm owner name: ")
            email = input("Enter farm owner email: ")
            phone = input("Enter farm owner phone: ")
            

        elif choice == "6":
            equipment_name = input("Enter equipment name: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            farmer_id = int(input("Enter farmer/owner ID: "))
            add_equipment_rental(equipment_name, start_date, end_date, farmer_id)

        elif choice == "7":
            break
