# Assignment 4 - Part A
# This program collects positive test scores until the user enters -1.
# Then it displays the list of scores and calculates the average.

test_scores = []   # List to store positive numbers

score_str = ""     # Raw input as string

# Input loop
while score_str != "-1":
    score_str = input("Enter test score (positive float, -1 to stop): ")

    # --- ERROR HANDLING LINE ---
    # Check if score_str is a valid float:
    if score_str.replace(".", "", 1).isdigit() == False and score_str != "-1":
        print("Invalid input. Please enter a number.")
        continue
    # ----------------------------------------------------

    score = float(score_str)

    # Only store positive numbers
    if score > 0:
        test_scores.append(score)

# Display results
print("Test scores entered:")
for value in test_scores:
    print(value)

# Calculate average
if len(test_scores) > 0:
    total = 0
    for value in test_scores:
        total = total + value
    average = total / len(test_scores)
    print("The average is:", average)
else:
    print("No scores entered. Average cannot be calculated.")
