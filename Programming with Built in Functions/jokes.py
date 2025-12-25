import random

jokes_list = [
    ("What do dentists call their X-rays?", "Toothpics!"),
    ("Why was 6 afraid of 7?", "Because 7 ate 9!"),
    ("What kind of music do mummies listen to?", "Wrap music!"),
    ("What lights up a stadium?", "A match!")
]

joke_question, punchline = random.choice(jokes_list)

print(joke_question)
print(punchline)