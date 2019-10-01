word = input("Enter word: ")

for i in range(1, len(word) + 1):
    print(word[i-1], word[-i])
    if word[i-1] != word[-i]:
        print("Not a Palindrome!")
        break
else:
    print("Palindrome!")