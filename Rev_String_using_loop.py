#Reverse string using while loop

def revString(s):
    i=len(s)-1
    output=''
    while i>=0:
        output=output+s[i]
        i=i-1
    return output

s=input("Enter the string:\n")
ans=revString(s)
print(ans)
