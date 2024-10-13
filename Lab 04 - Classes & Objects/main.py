# Authors: Sophia Ngo, Melanie Lopez, Sara Tfaili
# Date: 2/19/2024
# Description: This program allows the user to view, search, and modify a contant list.

import contact
import check_input


def read_file():
  """Read each contact, construct a Contact object, store in contacts list, sort, return list."""
  contacts = []

  file = open("addresses.txt")
  for item in file:
    data = item.strip().split(",")
    contact_object = contact.Contact(data[0], data[1], data[2], data[3],
                                     data[4], data[5])
    contacts.append(contact_object)

  file.close()
  contacts.sort()
  return contacts


def write_file(contacts):
  """Passes in list of contacts, loops through the list, writes each contact to file and on new line."""
  file = open("addresses.txt", "w")
  for item in contacts:
    file.write(repr(item) + "\n")
  file.close()


def get_menu_choice():
  """Displays menu and returns user's valid input."""
  print(
      "\nRolodex Menu:\n1. Display Contacts\n2. Add Contact\n3. Search Contacts\n4. Modify Contact\n5. Save and Quit"
  )
  return check_input.get_int_range(" ", 1, 5)


def modify_contact(con):
  """Passes in a contact, displays the contact, prompts the user to change information, updates the contact, and returns the modified contact."""
  while True:
    modify_menu = "\nModify Menu:\n1. First name\n2. Last name\n3. Phone\n4. Address\n5. City\n6. Zip\n7. Save"
    print(modify_menu)

    choice = check_input.get_int_range(" ", 1, 7)

    if choice == 1:
      con.first_name = input("Enter first name: ").strip()
    elif choice == 2:
      con.last_name = input("Enter last name: ").strip()
    elif choice == 3:
      con.phone = input("Enter phone: ")
    elif choice == 4:
      con.address = input("Enter address: ")
    elif choice == 5:
      con.city = input("Enter city: ")
    elif choice == 6:
      con.zip = input("Enter zip: ")
    elif choice == 7:
      break


def main():
  """Read file, repeatedly display main menu."""
  contacts = read_file()
  choice = 0
  while choice != 5:
    choice = get_menu_choice()

    if choice == 1:
      print(f"Number of contacts: {len(contacts)}")
      for item, c in enumerate(contacts, 1):
        print(f"{item}. {str(c)}")

    elif choice == 2:  ### The problem was with choice==3 where you were using the variable name as contact in the for loop, which was causing a conflict, I changed it to c it works now.
      print("Enter new contact: ")
      first_name = input("First name: ")
      last_name = input("Last name: ")
      phone = input("Phone #: ")
      address = input("Address: ")
      city = input("City: ")
      zip = input("Zip: ")

      new_contact = contact.Contact(first_name, last_name, phone, address,
                                    city, zip)
      contacts.append(new_contact)
      contacts.sort()

    elif choice == 3:
      print("Search: ")
      print("1. Search by last name")
      print("2. Search by zip")
      ln_or_zip = check_input.get_int_range(" ", 1, 2)

      if ln_or_zip == 1:
        last_name = input("Enter last name: ")
        found = []
        for c in contacts:
          if c.ln == last_name:
            found.append(c)
        if found:
          for c in found:
            print(str(c))
        else:
          print("No matches found.")

      elif ln_or_zip == 2:
        zip_code = input("Enter zip: ")
        found = []
        for c in contacts:
          if c.zip == zip_code:
            found.append(c)
        if found:
          for c in found:
            print(str(c))
        else:
          print("No matches found.")

    elif choice == 4:
      user_modify_fn = input("Enter first name: ")
      user_modify_ln = input("Enter last name: ")
      found_contact = None

      for con in contacts:
        if con.fn == user_modify_fn and con.ln == user_modify_ln:
          found_contact = con
          break
      if found_contact:
        print(found_contact)
        modify_contact(found_contact)
        contacts.sort()
      else:
        print("Contact not found.")

    elif choice == 5:
      write_file(contacts)
      print("Saving File...")
      print("Ending Program")
      break


if __name__ == "__main__":
  main()
