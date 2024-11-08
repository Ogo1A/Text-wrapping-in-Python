import textwrap

value="""This function wraps the input paragraph such that each line in the paragraph is at most width characters long.The wrap method is empty if the wrapped output has no contect.


"""
wrapper=textwrap.TextWrapper(width=60)
word_list=wrapper.wrap(text=value)
for element in word_list:
    print (element)