from helpers import *
from count import count_mode
from search import search_mode


while 1:
    intro()
    welcome()
    usr_options()
    selection = "Select a mode by inputting a number: "
    choice = input(selection)
    if choice == '1':
        count_mode()
    elif choice == '2':
        search_mode()
    elif choice == '3':
        tutorial()
    elif choice == '4':
        quit_pg()
    else:
        print("ERROR: Please enter a valid response.")
        continue

    input_prompt = "\nWould you like to exit inkCTR? [ Yes / No ]"
    resp = input(input_prompt).lower()
    if resp == 'yes':
        quit_pg()
    elif resp != 'no':
        print("\nERROR: Please enter a valid response.")
        quit_pg()
