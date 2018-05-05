from heft.core import (wbar, cbar, ranku, schedule, Event, start_time,
        makespan, endtime, insert_recvs, insert_sends, insert_sendrecvs, recvs,
        sends)

"""
This is a simple script to use the HEFT function provided based on the example given in the original HEFT paper.
You have to define the DAG, compcost function and commcost funtion.

Each task/job is numbered 1 to 10
Each processor/agent is named 'a', 'b' and 'c'

Output expected:
Ranking:
[10, 8, 7, 9, 6, 5, 2, 4, 3, 1]
Schedule:
('a', [Event(job=2, start=27, end=40), Event(job=8, start=57, end=62)])
('b', [Event(job=4, start=18, end=26), Event(job=6, start=26, end=42), Event(job=9, start=56, end=68), Event(job=10, start=73, end=80)])
('c', [Event(job=1, start=0, end=9), Event(job=3, start=9, end=28), Event(job=5, start=28, end=38), Event(job=7, start=38, end=49)])
{1: 'c', 2: 'a', 3: 'c', 4: 'b', 5: 'c', 6: 'b', 7: 'c', 8: 'a', 9: 'b', 10: 'b'}
"""


dag={0: (7, 11),
     1: (11,),
     2: (8, 9),
     3: (8, 9, 11, 7, 10, 12, 13),
     4: (10, 12, 13),
     5: (8, 9, 11, 7, 10 ,12, 13),
     6: (8, 9, 11),
     7: (14,),
     8: (15,),
     9: (14,),
     10: (15, 17),
     11: (16,),
     12: (),
     13: (16,),
     14: (17, 18),
     15: (18, 19),
     16: (19,),
     17: (),
     18: (),
     19: ()}

q7 = {0: (7, 11),
     1: (11,),
     2: (8, 9),
     3: (8, 9, 11, 7, 10, 12, 13),
     4: (10, 12, 13),
     5: (8, 9, 11, 7, 10, 12, 13),
     6: (8, 9, 11),
     7: (),
     8: (),
     9: (),
     10: (),
     11: (),
     12: (),
     13: ()}

a3 = {0: (4, 8),
       1: (8,),
       2: (13, 17),
       3: (17,),
       4: (5, 6, 7),
       5: (),
       6: (),
       7: (),
       8: (9, 17),
       9: (10, 11, 12),
       10: (),
       11: (),
       12: (),
       13: (14, 15, 16),
       14: (),
       15: (),
       16: (),
       17: (18,),
       18: (19, 20, 21),
       19: (),
       20: (),
       21: ()}


def compcost(job, agent):
    if(job==0):
        return 1
    if(job==1):
        return 1
    if(job==2):
        return 1
    if(job==3):
        return 1
    return 1


def commcost(ni, nj, A, B):
    if(A==B):
        return 0
    else:
        return 0

orders, jobson = schedule(a3, 'abcd', compcost, commcost)

for eachP in sorted(orders):
    print(eachP,orders[eachP])
print(jobson)
