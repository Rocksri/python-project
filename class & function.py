class PalindromeChecker:
    def __init__(self, word):
        self.word = word

    def check_palindrome(self):
        return self.word == self.word[::-1]

word = input("Enter a word: ")
palindrome = PalindromeChecker(word)

if palindrome.check_palindrome():
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
