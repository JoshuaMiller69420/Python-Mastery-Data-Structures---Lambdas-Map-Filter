#1. Create an empty stack to store the visited websites.

#2. Implement a function to add a website to the stack. 
# This function should take the website URL as input and push it onto the stack.

#3. Implement a function to display the current website. 
# This function should retrieve the top website from the stack and display it.

#4. Implement a function to handle the "back" button click. 
# This function should pop the top website from the stack and display it. If the stack is empty, display a message indicating that there are no previous websites.

#5. Implement a function to handle the "forward" button click. 
# This function should push the current website back onto the stack. If the stack is empty, do nothing.
import sys

visited_websites = []

def add_website(visited_websites):
    websites_to_visit = ("google.com", "reddit.com", "youtube.com")
    user_in = input("Enter a website you would like to visit. Ex: google.com, reddit.com, youtube.com -> ").lower()
    website_returned = None
    for website in websites_to_visit:
        if user_in == website:
            visited_websites.append(website)
            visited_websites = website
            print(f"Added {user_in} to the stack.")
            return play_game()
    if website_returned is None:
        print(f"Website {user_in} does not exsist, try again")
    display_current_website()
    


def display_current_website():
    if visited_websites:
        print(f"Current website: {visited_websites[-1]}")
    else:
        print("No previous websites.")


def handle_back_button():
    if visited_websites:
        visited_websites.pop()
        print(f"Popped {visited_websites[-1]} from the stack.")
        display_current_website()
    else:
        print("No previous websites to go back to.")


def handle_forward_button():
    if len(visited_websites) > 1:
        visited_websites.append(visited_websites[-1])
        visited_websites.pop()
        print(f"Pushed {visited_websites[-1]} back onto the stack.")
        display_current_website()
    else:
        print("No websites to go forward to.")


def play_game():
    while True:
        print("\nWelcome to the Web Browser!")
        print("1. Visit a website")
        print("2. Display current website")
        print("3. Go back")
        print("4. Go forward")
        print("5. Exit")
        user_choice = input("Enter your choice (1-5): ")
        
        if user_choice == "1":
            add_website(visited_websites)
        elif user_choice == "2":
            display_current_website()
        elif user_choice == "3":
            handle_back_button()
        elif user_choice == "4":
            handle_forward_button()
        elif user_choice == "5":
            print(visited_websites)
            sys.exit("Goodbye!")


if __name__ == '__main__':
    play_game()





