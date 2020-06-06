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
    aux = 0
    if text[0] == ' ':
        aux = 1
    for char in text:
        if char in breakpoint:
            new_text += char + "\n\n"
            aux = 1
        else:
            if aux == 0:
                new_text += char
            elif aux == 1 and char == ' ':
                continue
            else:
                new_text += char
                aux = 0
    print(new_text,end='')
