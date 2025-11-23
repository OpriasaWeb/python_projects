contacts = {}

# -----------------------------
# 1. Add Contact
# -----------------------------
def add_contact():
  print("\n--- Add a New Contact ---")
  name = input("Enter name: ")
  phone = input("Enter phone number: ")
  email = input("Enter email: ")
  
   # Check if phone number already exists
  if phone in contacts:
    print("A contact with this phone number already exists.\n")
    return
  
  contacts[phone] = {"name": name, "email": email}
  
  print(contacts)
  
# -----------------------------
# 2. Update Contact
# -----------------------------
def update_contact():
  print("\n--- Update Contact ---")
  phone = input("Enter the phone number of the contact to update: ")
  
  if phone not in contacts:
    print("Contact not found.\n")
    return
  
  print(f"Current info: Name = {contacts[phone]['name']}, Email = {contacts[phone]['email']}")

  new_name = input("Enter new name (leave blank to keep current): ")
  new_email = input("Enter new email (leave blank to keep current): ")

  # Update only if provided
  if new_name:
      contacts[phone]["name"] = new_name
  if new_email:
      contacts[phone]["email"] = new_email

  print("Contact updated successfully!\n")

# -----------------------------
# 3. Delete Contact
# -----------------------------
def delete_contact():
  print("\n--- Delete Contact ---")
  phone = input("Enter the phone number of the contact to delete: ")

  if phone not in contacts:
      print("Contact not found.\n")
      return

  # Ask confirmation
  confirm = input(f"Are you sure you want to delete {contacts[phone]['name']}? (yes/no): ").lower()

  if confirm == "yes":
      del contacts[phone]
      print("Contact deleted successfully!\n")
  else:
      print("Deletion cancelled.\n")


# -----------------------------
# 4. View Contact
# -----------------------------
def view_contacts():
  print("\n--- Contact List ---")
  if not contacts:
      print("No contacts saved.\n")
      return

  for phone, info in contacts.items():
      print(f"Name: {info['name']} | Phone: {phone} | Email: {info['email']}")
  print()
  

# -----------------------------
# MAIN MENU
# -----------------------------
def main():
    while True:
        print("===== CONTACT BOOK MENU =====")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. View Contacts")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            view_contacts()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.\n")


# Run the program
main()