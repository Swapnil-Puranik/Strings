#Task 1 - String Slicing and Indexing
text = "Python is amazing!"
print("First word:", text[:6])                    # First 6 characters
print("Amazing part:", text[10:17])               # 'amazing'
print("Reversed string:", text[::-1])             # Full string reversed

print("-"*40)

#Task 2 - String Methods
message = " hello, python world! "
print("Original string:", message)
print("After strip():", message.strip())
print("After capitalize():", message.strip().capitalize())
print("After replace():", message.replace("world", "universe"))
print("After upper():", message.upper())

print("-"*40)

#Task 3 - Check for Palindromes
word = input("Enter a word: ").strip()
if word.lower() == word[::-1].lower():
    print("Yes, ",word, "is a palindrome!")
else:
    print("Nope, ",word," is not a palindrome.")
