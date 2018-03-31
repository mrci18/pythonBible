from random import choice

questions = ["Why is the ocean blue? ", "How are babies made? ", "How long have you been programming? "]

question = choice(questions)

answer = input(question).strip().lower()

while answer != "just because":
    answer = input("Why? ").strip().lower()

print("Oh ok")