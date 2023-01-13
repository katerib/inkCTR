def usr_options():
    """
    Prints options to user.
    :return: n/a
    """
    print(
        '''
    What would you like to do?
      [1] WordCounter for PDFs
      [2] Search results for a word
      [3] Tutorial
      [4] Exit
      ''')


def intro():
    """
    Prints program intro to user.
    :return: n/a
    """
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


def tutorial():
    pass
