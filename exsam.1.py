import random
import turtle
question_list = [
    {'question': 'Which animal is the fastest on land?',
        'answer': 'cheetah'
    },
    {'question': 'Which animal has the longest pregnancy period?',
     'answer':'elephant'},
    {'question': 'Which animal is the largest mammal in the world?',
     'answer': 'blue whale'},
    {'question': 'Which animal can change the color of its skin?',
     'answer': 'chameleon'},
    {'question': 'Which animal is a symbol of New Zealand?',
     'answer': 'kiwi'}
]

color_ok = ['Green','Blue','Purple']
color_bad = ['Red','Orange','Yellow']

result = 0
t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
for question in question_list:
    print(question['question'])
    user_answer = input()
    if user_answer.lower() == question['answer']:
        print("The answer is correct")


        t.color(random.choice(color_ok))
        t.left(45)
        t.forward(200)
        t.left(180)
        t.forward(200)
        t.right(90)
        t.forward(200)
        t.home()
        t.clear()
        #turtle.bye()

        result += 1
    else:
        print("The answer is incorrect")


        t.color(random.choice(color_bad))
        t.left(45)
        t.forward(200)
        t.left(180)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(180)
        t.forward(200)
        t.home()
        t.clear()



print("Congratulations, you have typed ", result, " correct answers")

