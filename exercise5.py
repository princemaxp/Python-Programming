#Write code that counts the number of words in sentence that contain either an “a” or an “e”. Store the result in the variable num_a_or_e.

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
sentence_split = sentence.split(" ")
num_a_or_e = 0
for word in sentence_split:
    if 'a' in word or 'e' in word:
        num_a_or_e += 1
print(num_a_or_e)
