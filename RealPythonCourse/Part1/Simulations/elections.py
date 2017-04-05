from random import *


def elections():
    candidate_ar1_wins = 0
    candidate_br1_wins = 0
    candidate_ar2_wins = 0
    candidate_br2_wins = 0
    candidate_ar3_wins = 0
    candidate_br3_wins = 0

    for i in range(1, 10000):
        region_1 = randint(1, 100)
        if region_1 in range (1, 87):
            candidate_ar1_wins += 1
        else:
            candidate_br1_wins += 1
        if candidate_ar1_wins > candidate_br1_wins:
            winner_r1 = "Candidate A"
        else:
            winner_r1 = "Candidate B"
#    print("The winner is {}. Results A/B: {}/{}".format(winner_r1, candidate_ar1_wins, candidate_br1_wins))

    for j in range(1, 10000):
        region_2 = randint(1, 100)
        if region_2 in range(1, 65):
            candidate_ar2_wins += 1
        else:
            candidate_br2_wins += 1
        if candidate_ar2_wins > candidate_br2_wins:
            winner_r2 = "Candidate A"
        else:
            winner_r2 = "Candidate B"
   # print("The winner is {}. Results A/B: {}/{}".format(winner_r2, candidate_ar2_wins, candidate_br2_wins))

    for x in range(1, 10000):
        region_3 = randint(1, 100)
        if region_3 in range(1, 17):
            candidate_ar3_wins += 1
        else:
            candidate_br3_wins += 1
        if candidate_ar3_wins > candidate_br3_wins:
            winner_r3 = "Candidate A"
        else:
            winner_r3 = "Candidate B"
   # print("The winner is {}. Results A/B: {}/{}".format(winner_r3, candidate_ar3_wins, candidate_br3_wins))


    winning_results = []
    winning_results.append(winner_r1)
    winning_results.append(winner_r2)
    winning_results.append(winner_r3)


    count = 0
    for k in winning_results:
        if k == "Candidate A":
            count += 1
    if count < 2:
        winner = "Candidate B"
        #print("Candidate B WINS !!!")
    else:
        winner = "Candidate A"
        #print("Candidate A WINS !!!")

    return winner

# winner_count_a = 0
# winner_count_b = 0
# if winner == "Candidate A":
#     winner_count_a +=1
# else:
#     winner_count_b +=1
# print("Total wins A/B: {}/{}".format(winner_count_a, winner_count_b))
A_COUNT = 0
B_COUNT = 0
for a in range(0, 100):
    result = elections()
    print(result)
    if result == "Candidate A":
        A_COUNT += 1
    else:
        B_COUNT += 1
print ("Results A/B: {}/{}".format(A_COUNT, B_COUNT))