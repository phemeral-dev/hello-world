import random

from fastapi import FastAPI

app = FastAPI()

my_magic_8_ball_answers = [
    "I ain't readin all that. I'm happy for you though. Or sorry that happened.",
    "Ask AI",
    "Sir, this is a Wendy's.",
    "I'm just here so I won't get fined.",
    "kk",
]
regular_magic_8_ball_answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs point to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful",
]


@app.get("/")
def index():
    return "hello, world"


@app.get("/magic-eight-ball")
def magic_8_ball(question: str):
    return regular_magic_8_ball_answers[
        random.randint(0, len(regular_magic_8_ball_answers) - 1)
    ]


@app.get("/my-magic-eight-ball")
def my_magic_8_ball(question: str):
    return my_magic_8_ball_answers[random.randint(0, len(my_magic_8_ball_answers) - 1)]
