import random
dice = [1, 2, 3, 4, 5, 6]
roll = 0
#stair_number = 0
#count = 0
def roll_dice():
    global count
    global roll
    stair_number = 0
    for x in range(100):
        roll = random.choice(dice)
        oops = random.randrange(1, 1001)
        if oops < 2:
            stair_number = 0
        elif roll < 3:
            if stair_number > 0:
                stair_number -= 1
        elif roll < 6:
            stair_number += 1
        else:
            roll = random.choice(dice)
            stair_number += roll
    #print(stair_number)
    if stair_number >= 60:
        return 1
    else:
        return 0
def thousand_times():
    count = 0
    for x in range(100000):
        count += roll_dice()
    return count / 1000
total = thousand_times()
print(f"{total}%")