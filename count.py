import csv

from collections import Counter
from pypdf import PdfReader
from helpers import validate

# Add additional custom words to ignore:
IGNORED = ["can't", "don't", "he'd", "he'll", "i'll", "she'd", "she'll", "they'd", "they'll", "we'll", "will", "won't",
           "you're", 'about', 'after', 'away', 'because', 'been', 'before', 'beneath', 'beside', 'besides', 'between',
           'beyond', 'case', 'chapter', 'down', 'during', 'each', 'except', 'from', 'have', 'inside', 'instead',
           'into', 'like', 'means', 'near', 'next', 'ours', 'page', 'pages', 'place', 'that', 'their', 'theirs',
           'them', 'they', 'this', 'well', 'were', 'what', 'with', 'work', 'your']


def count_mode():
    """
    Reads PDF indicated by user and counts each occurrence of a word throughout entire document. Filters out
    words from ignored list (IGNORED) and removes punctuation.
    Users may add additional words to IGNORED in line 6 as needed.
    Special characters to remove/ignore can be seen and adjusted in line 40. To keep special characters and
        punctuation, delete or comment out lines 49-42.
    :return: n/a
    """
    print("\n<<<< ENTERED WORD COUNT MODE >>>>")
    pdf_prompt = "Input the name of the PDF to scan: "  # get user input
    in_name = input(pdf_prompt)
    pdf_name = validate(in_name, "pdf")
    print("  >> ...searching for PDF...")
    if not pdf_name:  # confirm file or path exists
        print(f"ERROR: '{pdf_name}' not found!\nPlease ensure the PDF is in the current directory or provide"
              f" the full path name to the PDF file and try again.")
        return
    reader = PdfReader(pdf_name)
    print(f"  >>  found '{pdf_name}'")
    print("  >> ...processing data... please wait...")
    page_len = len(reader.pages)
    text = ""
    for count in range(page_len):  # read data
        page = reader.pages[count]
        page_text = page.extract_text()
        text += page_text
    # clean data
    for char in '-.,:;!?—~`()"\n':  # remove specified punctuation
        text = text.replace(char, ' ')
    text = text.lower()
    words = text.split()

    c = Counter(words).most_common()  # count by most common (> freq -> < freq)
    data = []
    for item in c:
        if item[0] in IGNORED or (len(item[0]) <= 3):
            continue
        data.append(item)  # append non-ignored words and words > 3 letters long

    csv_name = in_name + '_results.csv'  # store .csv filename to store results
    with open(csv_name, 'w', newline='', encoding="utf-8") as results:
        csv_write = csv.writer(results)
        csv_write.writerow(['WORD', 'FREQUENCY'])  # write header
        for item in data:
            csv_write.writerow(item)  # write to csv, note encoding
    print(f"Success! {len(data)} unique word counts have been exported to '{csv_name}'!")  # print stats to user
    print("<<<< EXITED WORD COUNT MODE >>>>")
