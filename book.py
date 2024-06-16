class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter contact's name: ")
        phone = input("Enter contact's phone number: ")
        email = input("Enter contact's email: ")
        address = input("Enter contact's address: ")
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
            return
        for contact in self.contacts:
            print(contact)

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone]
        if found_contacts:
            for contact in found_contacts:
                print(contact)
        else:
            print("Contact not found.")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        for contact in self.contacts:
            if contact.name == name:
                phone = input(f"Enter new phone number (current: {contact.phone}): ")
                email = input(f"Enter new email (current: {contact.email}): ")
                address = input(f"Enter new address (current: {contact.address}): ")
                contact.phone = phone if phone else contact.phone
                contact.email = email if email else contact.email
                contact.address = address if address else contact.address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    book = ContactBook()
    actions = {
        '1': book.add_contact,
        '2': book.view_contacts,
        '3': book.search_contact,
        '4': book.update_contact,
        '5': book.delete_contact,
    }
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '6':
            break
        
        action = actions.get(choice)
        
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
