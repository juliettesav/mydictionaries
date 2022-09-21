def main():
    import re
    infile = open('/Users/juliettesav/Downloads/Adv Python/sometext.txt', 'r') #opens the text
    myDict = {} #creates empty dictionary 
    content = infile.read() #reads all the text
    content_list = re.findall(r'\b[a-z]{1,15}\b', content)

    for word in content_list:
        count = myDict.get(word,0) #finds each word
        myDict[word] = count + 1 #adds 1 each time word is found 

    myDict_list = myDict.keys() 

    for words in myDict_list:
        print(words, myDict[words]) #prints the frequency of each word 

main()