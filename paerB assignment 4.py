# Assignment 4 - Part B
# This program collects words until the user enters "quit".

words = []   # List to store words

word = ""

# Input loop
while word != "quit":
    word = input("Enter a word (type 'quit' to stop): ")

    # --- ERROR HANDLING LINE ---
    if word == "":
        print("Invalid input. Please type a word.")
        continue
    # ----------------------------

    if word != "quit":
        words.append(word)

# Display list
print("Words entered:")
for w in words:
    print(w)

# Level 4 requirement
check = input("Do you want to check if a name exists in the list? (yes/no): ")

if check == "yes":
    target = input("Enter the name to check: ")

    found = False
    for w in words:   # Manual search
        if w == target:
            found = True

    if found:
        print(target, "is in the list!")
    else:
        print(target, "is NOT in the list.")
