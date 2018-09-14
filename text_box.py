def bar(n):
    return n*'-'

def textBox(text):
    print '+' + bar (len(text)) + '+'
    print '|' + text + '|'
    print '+' + bar (len(text)) + '+'

textBox ("my name is hussein")