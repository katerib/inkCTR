import csv
import os

from helpers import validate


def find_word(csv_name):
    """
    Reads .csv (csv_name) and searches for existence of target word (needle) in CSV file. If word is found,
    prints number of times the word was found in the PDF. Alerts user if word is not present in CSV.
    :param csv_name: user-provided, name of CSV file to read
    :return: n/a
    """
    with open(csv_name, 'rt', encoding="utf-8") as file:                # open CSV, note encoding
        reader = csv.reader(file, delimiter=',')
        target_prompt = f"Input the word would you like to search for in '{csv_name}': "
        needle = input(target_prompt)                                   # read target word
        found = False
        for row in reader:                                              # search for target, skip header
            if row[1] == 'FREQUENCY':
                continue
            if row[0] == needle:
                print(f"The word '{needle}' appears {row[1]} times in '{csv_name}'.")   # print frequency
                found = True
    if not found:
        print(f"The word '{needle}' was not found in '{csv_name}'.")


def search_mode():
    """
    Switches into "Search Mode" and prompts user for file name to search. Alerts user if invalid filename or
    path to file. Remains in "Search Mode" until user indicates "no" when prompted to search for another word.
    :return: n/a
    """
    print("\n<<<< ENTERED WORD SEARCH MODE >>>>")
    search_prompt = "Input the name of the .csv file to search: "    # get CSV file name from user
    input_name = input(search_prompt)
    # validate input
    csv_name = validate(input_name, "csv")
    print("  >> ...searching for CSV...")
    if os.path.exists(csv_name) is False:                               # confirm existing name / path
        print(f"ERROR: '{csv_name}' not found!\nPlease ensure the file is in the current directory or provide"
              f" the full path name to the CSV file and try again.")
        return
    while 1:                                                            # perform search -> find_word()
        find_word(csv_name)
        print(f"\nSearch for another word in this file? (yes/no)")
        if input().lower() == 'no':
            print("<<<< EXITED WORD SEARCH MODE >>>>")
            return                                                      # return to main
