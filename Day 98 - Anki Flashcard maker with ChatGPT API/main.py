

if __name__ == '__main__':
    print('hello world')



# Concept
    # step a - electronjs Gui for variable input
        # Open pdf file path
        # main_topic - revelant information about/anki deck title
        # focus_input - write with own words what should generator focus on
        # only_source - TRUE == "only if present in the source text" or FALSE == "not only present in the source text but within scope of main_topic and focus_keywords"
        # cloze_number - cloze number in each front statement
        # word_count - word count

        # Pages range - Select range of desired page range
        # Save file path

    # steb b - Read pdf with fitz and format
        # Read pdf file
        # Analyze text to see if there is a way to keep together the revelant text (end of the page/paragraph mark)
        # Remove repetitive sentences that may come from footers etc
        # Part revelant text

    # step c - Generate the contents of flashcards

    # step d - Save into .csv file for review
