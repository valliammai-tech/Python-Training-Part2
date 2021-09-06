#Write python code to find the count of occurrence of vowels.

def count_vowels(x):
    vowels='aeiou'
    finalstr = {}.fromkeys(vowels.lower(), 0)
    for i in x:
        if i in vowels:
            finalstr[i.lower()]=finalstr[i]+1
    print(finalstr)
    return finalstr

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    count_vowels('hellooo')
