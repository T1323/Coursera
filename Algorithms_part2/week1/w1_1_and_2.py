"""
1 :
In this programming problem and the next you'll code up the greedy algorithms from lecture for minimizing the weighted sum of completion times..
Download the text file below.
jobs.txt
This file describes a set of jobs with positive and integral weights and lengths. It has the format
[number_of_jobs]
[job_1_weight] [job_1_length]
[job_2_weight] [job_2_length]
...
For example, the third line of the file is "74 59", indicating that the second job has weight 74 and length 59.
You should NOT assume that edge weights or lengths are distinct.
Your task in this problem is to run the greedy algorithm that schedules jobs in decreasing order of the difference (weight - length). Recall from lecture that this algorithm is not always optimal. IMPORTANT: if two jobs have equal difference (weight - length), you should schedule the job with higher weight first. Beware: if you break ties in a different way, you are likely to get the wrong answer. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
ADVICE: If you get the wrong answer, try out some small test cases to debug your algorithm (and post your test cases to the discussion forum).

2:
Your task now is to run the greedy algorithm that schedules jobs (optimally) in decreasing order of the ratio (weight/length). In this algorithm, it does not matter how you break ties. You should report the sum of weighted completion times of the resulting schedule --- a positive integer --- in the box below.
"""

import heapq
import time

start = time.time()

j1heap=[]
j2heap = []

fin = open('jobs.txt', 'rt')
itemTotal = int(fin.readline())

while True:
    line = fin.readline()
    if not line:
        break
    job = [int(i) for i in line.split(' ')]
    item = [-(job[0] - job[1]), -job[0], -job[1]]
    item2 = [-(job[0] / job[1]), -job[0], -job[1]]
    heapq.heappush(j1heap, item)
    heapq.heappush(j2heap, item2)
fin.close()

lengthTotal = 0
wlTotal= 0
lengthTotal2= 0
wlTotal2 = 0

for i in range(itemTotal):
    tmp, nWeight, nLength = heapq.heappop(j1heap)
    lengthTotal += -nLength
    wlTotal += -nWeight * lengthTotal

    tmp, nWeight2, nLength2 = heapq.heappop(j2heap)
    lengthTotal2 += -nLength2
    wlTotal2 += -nWeight2 * lengthTotal2

end = time.time()
print(wlTotal,wlTotal2, end - start)
