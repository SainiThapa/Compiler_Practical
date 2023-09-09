stringC=input("Enter a line of code: ")
if(stringC[0]=='/'):
    if(stringC[1]=='/'):
        print("This is a comment")
    elif(stringC[1]=='*'):
        stringR=stringC[::-1]
        if(stringR[0]=='/' and stringR[1]=='*'):
            print("This is a comment")
        else:
            print("This is not a comment")
    else:
        print("This is not a comment")
else:
    print("This is not a comment")
