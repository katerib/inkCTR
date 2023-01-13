def usr_options():
    print(
        '''
    What would you like to do?
      [1] WordCounter for PDFs
      [2] Search results for a word
      [3] Tutorial
      [4] Exit
      ''')


def intro():
    print(
        '''
        __________________   __________________
    .-/|                  \ /                  |\-.
    ||||                   |                   ||||
    ||||                   |                   ||||
    ||||                   |                   ||||
    ||||                   |                   ||||
    ||||      Welcome      |                   ||||
    ||||        to         |       by KB       ||||
    ||||     PDFParser     |                   ||||
    ||||                   |                   ||||
    ||||                   |                   ||||
    ||||                   |                   ||||
    ||||                   |                   ||||
    ||||__________________ | __________________||||
    ||/===================\|/===================\||
    `--------------------~___~-------------------''
    '''
    )


def validate(name, filetype):
    if filetype == "pdf":
        if name[-4:] != ".pdf":  # format if necessary
            name += ".pdf"
        return name
    elif filetype == "csv":
        if name[-4:] != ".csv":  # format if necessary
            name += ".csv"
        return name


def tutorial():
    pass
