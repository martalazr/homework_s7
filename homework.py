import requests

r = requests.get("https://raw.githubusercontent.com/itb-ie/contest/master/text.txt")
t = r.text

vowels = "aeiou"
letters = " abcdefghijklmnopqrstuvwxyz"

tmp = [] # in this list we add the number of vowels of each line
n = 0 # n allows to count the number of vowels
for l in t:
    if (l in vowels):
        n += 1
    if (l == '\n'): # '\n' indicates the end of a line, to know when to restart n
        tmp.append(n)
        n = 0

sol = ""
for i in range(len(tmp)): # loop to identify the number of vowels and add it to the solution
    sol += letters[tmp[i]]

print(tmp)
print("The secret message is: " + sol)