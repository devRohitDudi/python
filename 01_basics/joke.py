print("Hello, world!")

def printJokes(joke):
    print(joke)

joke = [None]*6

joke[0] = "Hello"
joke[1] = "Doraemon."
joke[2] = "How "
joke[3] = "are "
joke[4] = "you"
joke[5] = "doing?"

for j in joke:
    printJokes(j)

newJoke = "new joke!"