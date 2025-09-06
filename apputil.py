
def palindrome (word):
    clean = word.replace(",","").replace(".","").replace(" ","").lower()
    if clean == clean[::-1]:
        return True
    else: 
        return False

palindrome(word)

def parenthesis_balance(string):
    count = 0
    for char in string:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False

parenthesis_balance(string)