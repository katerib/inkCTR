import csv
import os

from helpers import validate


def find_word(csv_name):
    with open(csv_name, 'rt', encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=',')
        # read target word
        target_prompt = f"Input the word would you like to search for in '{csv_name}': "
        needle = input(target_prompt)
        # search for target
        found = False
        for row in reader:
            if row[1] == 'FREQUENCY':                   # skip header row
                continue
            if row[0] == needle:
                print(f"the word '{needle}' appears {row[1]} times in '{csv_name}'.")
                found = True
    if not found:
        print(f"The word '{needle}' was not found in '{csv_name}'.")


def search_mode():
    print("\n<<<< ENTERED WORD SEARCH MODE >>>>")
    search_prompt = "Input the name of the .csv file to search in: "
    input_name = input(search_prompt)
    # validate input
    csv_name = validate(input_name, "csv")
    print("  >> ...searching for CSV...")
    if os.path.exists(csv_name) is False:
        print(f"ERROR: '{csv_name}' not found!\nPlease ensure the file is in the current directory or provide"
              f" the full path name to the CSV file and try again.")
        return
    # search for word
    while 1:
        find_word(csv_name)

        print(f"\nSearch for another word in this file? (yes/no)")
        if input().lower() == 'no':
            print("<<<< EXITED WORD SEARCH MODE >>>>")
            return
