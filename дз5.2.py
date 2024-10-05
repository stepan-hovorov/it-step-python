question_1 = "I have 4 legs and a tail. I am very smart.I like to play with you. When I see a cat, I say Woof, woof I am…."
question_2 = "I am a pet. I am soft and furry. I like to sleep and drink milk. I do not like mice and dogs. I say Meow, meow. I am…."
question_3 = "I am a big farm animal. I can be black, white or brown. I like to eat green grass. I give milk. I can say Moo, moo. I am…."
question_4 = "I have four legs and a tail. I have no teeth. I can swim  and dive underwater. I carry my house around with me. I am a…"
question_5 = "I live in the woods. I'm very big and furry. I have a big nose, a little tail and four legs. I like to eat fish and berries. I am a…"
answer_1 = "dog"
answer_2 = "cat"
answer_3 = "cow"
answer_4 = "turtle"
answer_5 = "bear"
result = 0
print(question_1)
user_answer = input()
if user_answer.lower() == answer_1:
    result += 1
print("The answer is correct")
print(question_2)
user_answer = input()
if user_answer.lower() == answer_2:
    result += 1
print("The answer is correct")
print(question_3)
user_answer = input()
if user_answer.lower() == answer_3:
    result += 1
print("The answer is correct")
print(question_4)
user_answer = input()
if user_answer.lower() == answer_4:
    import turtle

    t = turtle.Turtle()
    t.shape("turtle")
    t.speed(1)
    t.color("Green")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
print("The answer is correct")
print(question_5)
user_answer = input()
if user_answer.lower() == answer_5:
    result += 1
print("The answer is correct")
print("Congratulations, you have typed ", result, " correct answers")
