import csv

from pypdf import PdfReader
from collections import Counter

IGNORED = ['chapter','about','well','away','because','before','beneath','beside','besides','between','beyond',\
           'means','down','during','case','front','lieu','place','into','inside','instead','except',\
           'theirs','ours',"you're","i'll","she'll","he'll","will","they'll",'near','next','like','this','that',\
           'after','with',"don't","won't","can't",'have','work','page','pages','each', "she'd"]


def validate_name(name, filetype):
    if filetype == "pdf":
        if name[-4:] != ".pdf":  # format if necessary
            name += ".pdf"
        return name
    elif filetype == "csv":
        if name[-4:] != ".csv":  # format if necessary
            name += ".csv"
        return name


def pdf_scan():
    print("\n<<<< ENTERED WORD COUNT MODE >>>>")
    pdf_prompt = "Input the name of the PDF to scan: "
    in_name = input(pdf_prompt)
    pdf_name = validate_name(in_name, "pdf")
    print("  >> ...searching...")
    if not pdf_name:
        print(f"ERROR: '{pdf_name}' not found!\nPlease ensure the PDF is in the current directory or provide"
              f" the full path name to the PDF file and try again.")
        return
    reader = PdfReader(pdf_name)
    print(f"  >>  found '{pdf_name}'")
    print("  >> ...processing data... please wait...")
    page_len = len(reader.pages)
    text = ""
    for count in range(page_len):
        page = reader.pages[count]
        page_text = page.extract_text()
        text += page_text
    # clean data
    for char in '-.,:;!?—\n':
        text = text.replace(char, ' ')
    text = text.lower()
    words = text.split()

    # validate data and append to new variable
    c = Counter(words).most_common()
    data = []
    for item in c:
        if item[0] in IGNORED or (len(item[0]) <=3):
            continue
        data.append(item)

    # export to csv
    csv_name = in_name + '_results.csv'
    with open(csv_name, 'w', newline='') as results:
        csv_write = csv.writer(results)
        csv_write.writerow(['WORD','FREQUENCY'])
        for item in data:
            csv_write.writerow(item)
    print(f"Success! {len(data)} word counts have been exported to '{csv_name}'!")
    print("<EXITED WORD COUNT MODE>")


def user_options():
    print("\nWhat would you like to do?")
    print("      [1] WordCounter for PDFs")
    print("      [2] Search results for a word")
    print("      [3] Exit")


while 1:
    print("Welcome to PDF Parser")
    user_options()
    choice_prompt = "Select a mode by inputting a number: "
    choice = input(choice_prompt)
    if choice == '1':
        pdf_scan()
    elif choice == '2':
        word_search()
    elif choice == '3':
        exit()
    else:
        print("Please enter a valid response")
        continue

    print(f"\nContinue? (yes/no)")
    if input().lower() == 'no':
        exit()
