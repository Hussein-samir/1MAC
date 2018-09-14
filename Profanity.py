import urllib
def read_text():
    quotes = open(r"C:\Users\alityan\Desktop\movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    return contents_of_file
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+str(text_to_check))
    output = connection.read()
    connection.close()
    return output
def output(test):
    if "true" in test:
        print "Curse word detected!!!!"
    elif "false" in test:
        print "You're good to go :)"
    else:
        print "couldnt scan the doc"
output(check_profanity(read_text()))