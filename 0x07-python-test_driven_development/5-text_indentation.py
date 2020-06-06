#!/usr/bin/python3
""" Module that prints a text with 2 new lines after each
of these characters: ., ? and : """


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each
    of these characters: ., ? and : """
    if type(text) is not str:
        raise TypeError('text must be a string')
    new_text = ""
    breakpoint = ['.', '?', ':']
    aux = 1
    for char in text:
        if aux == 0:
            if char == ' ':
                char = ''
                aux = 1
        if char in breakpoint:
            new_text += char + "\n\n"
            aux = 0
        else:
            new_text += char
    print(new_text)
