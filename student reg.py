"""
Name: Yash Nagar,
Enrollment no. : 0157AL231230,
Branch: CSE-AIML
LNCTS

"""

users = {
    "yash": {
        "password": "yash123",
        "contact": "9827383104",
        "branch": "CSE-AIML",
        "section": "C",
        "course": "B.Tech"
    },
    "ram": {
        "password": "ram123",
        "contact": "9837785124",
        "branch": "CSE",
        "section": "B",
        "course": "B.Tech"
    }
}


logged = False
current_user = None


def register():
    global users, logged, current_user
    print("\nRegistration......")
    username = input("Enter username: ")

    if username in users:
        print("Already registered, please login.")
        return

    password = input("Enter password: ")
    contact = input("Enter contact number: ")
    branch = input("Enter branch: ")
    section = input("Enter section: ")
    course = input("Enter course: ")

    users[username] = {
        "password": password,
        "contact": contact,
        "branch": branch,
        "section": section,
        "course": course
    }

    logged = True
    current_user = username
    print("Successfully registered and logged in!")
    show_profile()


def login():
    global users, logged, current_user
    print("\nLogin......")
    username = input("Enter username: ")

    if username not in users:
        print("Not registered. Please register first.")
        return

    password = input("Enter password: ")

    if users[username]["password"] == password:
        logged = True
        current_user = username
        print("Login successful!")
        show_profile()
    else:
        print("Wrong password.")


def show_profile():
    global logged, current_user, users
    print("\nShow Profile......")
    if logged and current_user:
        profile = users[current_user]
        print(f"Username: {current_user}")
        print(f"Password: {profile['password']}")
        print(f"Contact No.: {profile['contact']}")
        print(f"Branch: {profile['branch']}")
        print(f"Section: {profile['section']}")
        print(f"Course: {profile['course']}")
    else:
        print("Please login first.")


def update_profile():
    global logged, current_user, users
    print("\nUpdate Profile......")
    if not logged or not current_user:
        print("Please login first.")
        return

    choice = input("""Choose an option:
    1 - Edit username
    2 - Edit password
    3 - Edit contact number
    4 - Edit branch
    5 - Edit section
    6 - Edit course
    Enter choice: """)

    profile = users[current_user]

    if choice == "1":
        new_username = input("Enter new username: ")
        if new_username in users:
            print("Username already taken.")
        else:
            users[new_username] = users.pop(current_user)
            current_user = new_username
            print("Username updated successfully!")

    elif choice == "2":
        new_password = input("Enter new password: ")
        profile["password"] = new_password
        print("Password updated successfully!")

    elif choice == "3":
        new_contact = input("Enter new contact number: ")
        profile["contact"] = new_contact
        print("Contact number updated successfully!")

    elif choice == "4":
        new_branch = input("Enter new branch: ")
        profile["branch"] = new_branch
        print("Branch updated successfully!")

    elif choice == "5":
        new_section = input("Enter new section: ")
        profile["section"] = new_section
        print("Section updated successfully!")

    elif choice == "6":
        new_course = input("Enter new course: ")
        profile["course"] = new_course
        print("Course updated successfully!")

    else:
        print("Invalid option.")


def logout():
    global logged, current_user
    if logged:
        print(f"{current_user}, you are logged out.")
        logged = False
        current_user = None
    else:
        print("No user is currently logged in.")


def terminate():
    print("Thank You. Goodbye!")
    exit()


def main():
    while True:
        print("\nWelcome to the Site.....")
        response = input("""Choose an option:
    1 - Register
    2 - Login
    3 - Show Profile
    4 - Update Profile
    5 - Logout
    6 - Main Menu
    7 - Terminate
    Select option (1/2/3/4/5/6/7): """)

        if response == "1":
            register()
        elif response == "2":
            login()
        elif response == "3":
            show_profile()
        elif response == "4":
            update_profile()
        elif response == "5":
            logout()
        elif response == "6":
            continue  
        elif response == "7":
            terminate()
        else:
            print("❌ Invalid choice, please try again.")


main()
