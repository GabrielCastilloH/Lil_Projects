"""
WHAT THIS PROGRAM DOES:
- Makes a new line after every capitalized word (not including the word I)
- Indents the second and third lines ONCE
- Indents the fourth line TWICE
- Then begins from the beginning, the first line does not get indented.
"""

# String that the program will reformat
sample_string = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a " \
                "diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are "

# Make a list of the words in the string, and makes another list that will include words with formatting.
words = sample_string.split(" ")
list_w_formatting = []
tabs = 0

# For every word in the new list made from the sample string, we make a line for each capitalized word.
# Makes 1 tab for 2nd and 3rd lines, makes 2 tabs for 4th line. No tab for first line. Repeats over and over again.

for word in words:
    if word.title() == word and word != "I":
        list_w_formatting.append("\n")
        tabs += 1
        if 1 < tabs < 4:
            list_w_formatting.append("\t")
        elif tabs == 4:
            list_w_formatting.append("\t\t")
            tabs = 0

        list_w_formatting.append(word)
    else:
        list_w_formatting.append(word)

# Joins the final formatted list (which includes tabs and new lines) and then prints it out.
print(" ".join(list_w_formatting))
