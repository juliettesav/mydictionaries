code = {'A':'%','B':'@','C':'!','D':'$','E':'&','F':'*','G':'(','H':')','I':'-',
                      'J':'+','K':'+','L':'^','M':'-','N':';','O':'~','P':':','Q':'//','R':'[',
                      'S':'}','T':'`','U':'[','V':']','W':'{','X':'"','Y':'?','Z':'}','a':'9',
                      'b':'8','c':'7','d':'6','e':'5','f':'4','g':'3','h':'2','i':'1','j':'0',
                      'k':'a','b':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j',
                      't':'k','u':'l','v':'m','w':'n','x':'o','y':'p','z':'q'} #create the code

infile1 = open('/Users/juliettesav/Downloads/info_security.txt','r') #opens the text
content1 = infile1.read() #reads all the text
infile1.close()
encryption = open('encrypted.txt','w') #writes the txt file

for ch in content1: #creates the encrypted txt
    if ch in code:
        encryption.write(code[ch])
    else:
        encryption.write(ch)