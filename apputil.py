word = "Sit on a potato pan, Otis."

def palindrome (word):
    clean = word.replace(",","").replace(".","").replace(" ","").lower()
    if clean == clean[::-1]:
        return True
    else: 
        return False

palindrome(word)

sequence = ")((())"

def parentheses(sequence):
    count = 0
    for char in sequence:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False

parentheses(sequence)