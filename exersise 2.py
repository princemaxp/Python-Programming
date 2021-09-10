#The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter, including one-letter words. Store the result in the variable same_letter_count.
sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
sentence_split = sentence.split(" ")
same_letter_count = 0
for word in sentence_split:
    if word[0] == word[-1]:
        same_letter_count += 1
print(same_letter_count)
