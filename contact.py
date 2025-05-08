contacts={}

def add_contacts():
    name=input("Enter the Contact name :")
    phone=input("Enter the  phone number :")
    email=input("Enter the email id :")
    contacts[name]={"Phone":phone,"Email":email}
    print(f"contact  for [name] added sucessfully.")

def view_contacts():
    if not contacts:
        print("No contacts detial to show")
    else:
        for name , info in contacts .items():
            print(f"\nNmae:{name}")
            print(f"Phone:{info['phone']}")
            print(f"Email :{info["Email"]}")


def search_contacts():
    name=input("Enter the name to sreach contact detail :")
    if name in contacts:
         print(f"\nName: {name}")
         print(f"Phone: {contacts[name]['Phone']}")
         print(f"Email: {contacts[name]['Email']}")
    else:
        print("Contact not found.")


def delete_contacts():
    name=input("Enter the name to delete :")
    if name in contacts:
        del contacts[name]
        print(f"contact for {name} is deleted.")
    else:
        print("the contact detail is not found.")

def main():
    while True:
        print("\n------Contact Book-----")
        print("1.Add contact ")
        print("2.view COntacts")
        print("3.search contacts")
        print("4.delete contacts")
        print("5.Exit")

        choice=input("choose an option(1-5)")
        if choice =="5":
            print("Exiting the Contact Book.Good Bye")
            break
        
        try:
            if choice=="1":
                add_contacts()
            if choice=="2":
                view_contacts()
            if choice=="3":
                search_contacts()
            if choice=="4":
                delete_contacts()
            else:
                print("Inclide choice ! pls select a number between 1-5 ")
        except ValueError as ve:
             print(f" Error: {ve}")
        except Exception as e:
            print(f" Unexpected error: {e}")


main()


            

            
        




                      

