<div id="header" align="center"> 
  <img height="200px" src="https://media.giphy.com/media/VfK8uwEgsWawGtsSKO/giphy.gif"/> 
</div>

# inkCTR

A tool for authors to analyze their writing and word choice.

## Description

inkCTR, or inkCounter, was designed to help authors identify the most overused words in their writing. After running the program, an author will be able to view their most used words. Authors can also choose to ignore certain words when scanning the PDF (eg. exclude the word "Chapter" from the results). Once the PDF has been analyzed, the author can search the results to see the word count of a specific word. 

The program analyzes a PDF indicated by the user, counts the number of times each word appears, and then writes the results to a new file. A list of unique words and their frequencies are exported to a .csv file for the user to view with any spreadsheet software.

### Features

* **Word Count Mode**
  * specify a PDF to analyze
  * count all instances of unique words (ignore punctuation and ignored words)
  * export results to .csv file

* **Search Mode**
  * specify a CSV file to search
  * indicate the word to search for
  * view number of times the target word was found in original PDF

* **Ignored words**
  * all instances of words marked as _IGNORED_ will not be stored in the results file

* **Tutorial**
  * read about the program and learn how to use it

### Inspiration

As a reader, it is easy to be distracted by the author's word choice or overuse of a phrase or cliché. I was inspired to create this program while reading a series by one of my favorite authors. Somewhere in her first series, I noticed her use of the word "swaggering". It stood out to me but didn't bother me too much until the end of the second series. When encountering this word in Chapter 1 of the third series, it was impossible to ignore. 

I wanted to know how many times she had used the word "swaggering" in all of her books, so I compiled her work into one PDF and created a program to tell me exactly how many times it was found (the exact number is mentioned in the "Preview" section below, if you were wondering). I then polished the program so authors could use it as a tool to identify their most frequently used words, and decide whether they were okay with this number or whether they wanted to replace some instances of the word with a new word.

## Getting Started

### Prerequisites 

The file `requirements.txt` provides a list of all required packages.

### Running the Program

Program files should be saved in the same directory. Execute the program from the terminal.

Example syntax (Windows 11, using Windows Powershell): ```py main.py```

_To force the program to exit, hit Ctrl+C or Cmd+C._

### Modifications

Users can modify the words the program is set to ignore when scanning a PDF. To do this, open the [count.py] file and edit the list of words found at the top of the file. The user may ignore as many or as few words as preferred. 

The program currently ignores the words:

> can't, don't, he'd, he'll, I'll, she'd, she'll, they'd, they'll, we'll, will, won't, you're, about, after, away, because, been, before, beneath, beside, besides, between, beyond, case, chapter, down, during, each, except, from, have, inside, instead, into, like, means, near, next, ours, page, pages, place, that, their, theirs, them, they, this, well, were, what, with, work, your

## Preview

To demonstrate the program, inkCTR was run with a PDF consisting of 14 different books with a total length of 6,834 pages.

### Word Count Mode

Using the PDF mentioned above, inkCTR's Word Count Mode produced results in 4 minutes and 24 seconds (_Note: retrieving results from a PDF with 130 pages was nearly instantaneous_).

![Word Count Mode](/screenshots/word_count_mode.jpg)

### Search Mode

The results contained 32,652 unique words and the number of times each word was found in the PDF. The word "swaggering" was found 41 times throughout all of her books. 

![Search Mode](/screenshots/search_mode.jpg)

The file can be opened with any spreadsheet software, like Microsoft Excel, to view all results. As shown below, the author can determine their most used word ("said"). If the user would like to exclude any of these words from future analysis during Word Count Mode, the user can modify the contents of the 'Ignored' list declared at the top of the `count.py` file.

![Results](/screenshots/results.jpg)

> Note: On some operating systems, you may encounter special characters when viewing the .csv file using Microsoft Excel. To remedy this, [try this solution](https://support.knowbe4.com/hc/en-us/articles/360041788374-Why-Aren-t-Special-Characters-Displaying-in-My-CSV-File-in-Microsoft-Excel-). In these cases, inkCTR will still run as expected.