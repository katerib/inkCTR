from collections import Counter
from pypdf import PdfReader
from helpers import validate

IGNORED = ['chapter', 'about', 'well', 'away', 'because', 'before', 'beneath', 'beside', 'besides', 'between', 'beyond',
           'means', 'down', 'during', 'case', 'front', 'lieu', 'place', 'into', 'inside', 'instead', 'except', 'that',
           'theirs', 'ours', "you're", "i'll", "she'll", "he'll", "will", "they'll", 'near', 'next', 'like', 'this',
           'after', 'with', "don't", "won't", "can't", 'have', 'work', 'page', 'pages', 'each', "she'd"]


def count_mode():
    print("\n<<<< ENTERED WORD COUNT MODE >>>>")
    pdf_prompt = "Input the name of the PDF to scan: "
    in_name = input(pdf_prompt)
    pdf_name = validate(in_name, "pdf")
    print("  >> ...searching for PDF...")
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
    for char in '-.,:;!?—"\n':
        text = text.replace(char, ' ')
    text = text.lower()
    words = text.split()

    # validate data and append to new variable
    c = Counter(words).most_common()
    data = []
    for item in c:
        if item[0] in IGNORED or (len(item[0]) <= 3):
            continue
        data.append(item)

    # export to csv
    csv_name = in_name + '_results.csv'
    with open(csv_name, 'w', newline='', encoding="utf-8") as results:
        csv_write = csv.writer(results)
        csv_write.writerow(['WORD', 'FREQUENCY'])
        for item in data:
            csv_write.writerow(item)
    print(f"Success! {len(data)} unique word counts have been exported to '{csv_name}'!")
    print("<<<< EXITED WORD COUNT MODE >>>>")