import string

def is_palindrome(text):
    # Remove spaces and punctuation, and lowercase everything
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]

sentence = input("Enter a sentence: ")
if is_palindrome(sentence):
    print("The sentence is a Palindrome!")
else:
    print("The sentence is not a palindrome.")
