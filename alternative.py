input_sentence = input("Please type your sentence: ")
print(input_sentence)
new_sentence = ""

for i in range(len(input_sentence)):
    if i % 2 == 1:
        new_sentence += input_sentence[i].lower()
    else:
        new_sentence += input_sentence[i].upper()

print(new_sentence)

user_sentence = input("Please type your sentence: ").split()
alternative_sentence = ""

for i in user_sentence:
    if i % 2 == 1:
        alternative_sentence = " ".join(user_sentence).upper()
    else:
        alternative_sentence = " ".join(user_sentence).lower()

print(alternative_sentence)