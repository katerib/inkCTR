from helpers import intro, usr_options, tutorial
from count import count_mode
from search import search_mode


while 1:
    intro()
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
        exit()
    else:
        print("Please enter a valid response")
        continue

    print(f"\nWould you like to exit PDF Parser? (yes/no)")
    if input().lower() == 'yes':
        print('''
        <<<< EXITING PDF PARSER >>>>\n
        ''')
        exit()
