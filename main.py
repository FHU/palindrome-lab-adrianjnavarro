#REMOVE PASS AND FIX THIS FUNCTION
def palindrome(word):
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word [::-1]

if __name__ == '__main__':
    user_input = input()
    result = palindrome(user_input)


    if result:
        print("True")
    else:
        print("False") 


#YOUR CODE GOES HERE
