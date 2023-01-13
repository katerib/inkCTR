# ASCII art

def usr_options():
    """
    Prints options to user.
    :return: n/a
    """
    print(
    '''
Where would you like to start?
  [1] Get Started: scan a PDF
  [2] View Results: search for a word
  [3] Tutorial
  [4] Exit
  ''')


def intro():
    """
    Prints program intro to user.
    :return: n/a
    """
    print('''
      _       _     ____ _____ 
     (_)_ __ | | __/ ___|_   _|
     | | '_ \| |/ / |     | |  
     | | | | |   <| |___  | |  
     |_|_| |_|_|\_\x5c\x5c____| |_|  
    ''')


def validate(name, filetype):
    """
    Manually adds file extension if file name provided by user does not already include extension.
    :param name: file name provided by user
    :param filetype: expected file extension
    :return: returns name + file extension (either .pdf or .csv, as indicated by filetype)
    """
    if filetype == "pdf":
        if name[-4:] != ".pdf":  # format if necessary
            name += ".pdf"
        return name
    elif filetype == "csv":
        if name[-4:] != ".csv":  # format if necessary
            name += ".csv"
        return name


def welcome():
    print("Welcome to inkCT, a tool to help authors identify overused words in their work.")


def tutorial():
    print("<< ENTERED TUTORIAL MODE >>")
    print('''
inkCT is a program designed for authors to analyze their writing. To get started, 
provide a PDF version of the document you want to scan and inkCT will do the rest! 

-- How to Use inkCT --
  [Mode 1] Word Count Mode
      From the main menu, type '1' to enter Word Count Mode. When prompted, type 
    the name of your PDF file.*
      Now inkCT will start counting the number of times each word is found in your 
    document. inkCT will only count words that are four letters or longer. Words
    specified in the "Ignored" section of code will also not be counted.
        If you would like to change the ignored words, open the [count.py] file 
        and modify the list of words at the top of the page. You can ignore as 
        many or as few words as you'd like. 
      After scanning, your results will be saved as a .csv file in the folder 
    containing inkCT's program files. You can open this file with any spreadsheet
    software (eg. Excel) or use it with inkCT's Search Mode.
    
  [Mode 2] Search Mode
      Now that you've found your results, you can use the .csv file to find the 
    number of times a specific word was mentioned. From the main menu, type
    '2' to enter Search Mode. When prompted, type the name of the .csv file 
    created during [Mode 1] Word Count Mode.*
      Now type the word you would like to see the count for. If the word exists
    in the results page, you'll be shown how many times that word was found
    in the PDF you provided.
    
* Notes about files:
    - Don't worry about including file extensions. If you leave them out, inkCT 
      will manually add them to the file name for you.
    - Your file should be in the same folder that contains the inkCT program 
      files. If your file is saved at another location, please provide the
      explicit path to your file instead of the file name.
          
  You can exit the program at any time by typing '4' in the main menu, or 
  clicking Ctrl+C.
  
  {{ More features to come! }}
    ''')


def quit_pg():
    print("\n  Thanks for using inkCT! \n")
    exit()
