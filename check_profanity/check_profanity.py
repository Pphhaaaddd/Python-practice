import urllib

#Read text from file
def read_text():
    texts = open("/home/phad/version-control/python-practice/check_profanity/texts.txt")
    contents_of_file = texts.read()
    #print(contents_of_file)
    texts.close()
    check_for_profanity(contents_of_file)
###########################

#check for curse words
def check_for_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    if "false" in output:
        print "No profane words."
    elif "true" in output:
        print "Profanity alert!"
    else:
        print "Error in reading"
    connection.close()
###########################

read_text()
