#Problem:
#Write a program to find the longest word in a sentence.

#Human Thinking:
# First, take a sentence from the user.
# Split the sentence into words.
# Assume the first word is the longest.
# Compare each word with the current longest word.
# If a word is longer, update the longest word.
# Repeat until all words are checked.
# Finally, display the longest word.

#Pseudocode:
# Start
# Take a sentence.
# Split the sentence into words.
# Set longest_word as the first word.
# For each word:
#     If the word is longer than longest_word:
#         Update longest_word.
# Display longest_word.
# End

#Python Code:
sentence = "Success requires consistency, patience, and continuous learning every single day."
words = sentence.split()
longest_word = words[0]
for word in words:
    if(len(word)>len(longest_word)):
        longest_word = word
print(f"Longest Word:{longest_word}")    