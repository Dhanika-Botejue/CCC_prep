scores = []
participants = int(input())

for i in range(participants):
    participant_score = int(input())
    scores.append(participant_score)

scores.sort()
highest = scores[participants-1]
second_highest = 0
third_highest = 0

for i in range(participants):
    if scores[i] < highest and scores[i] > second_highest:
        second_highest = scores[i]

for i in range(participants):
    if scores[i] < second_highest and scores[i] > third_highest:
        third_highest = scores[i]

print(third_highest, scores.count(third_highest))
