winners = ["FirstWinner", "SecondPlace", "ThirdPlace"]

# enumerate() gives both the index (position) and the value from the list
for index, winner in enumerate(winners):
    # index starts from 0, so we add 1 to make it human-friendly
    print("{}. {}".format(index + 1, winner))
