cong={
     7:5,
     18:22,
     32:8,
     71:5,
     66:6
 }#keys are ages of voters and values are vote
bjp={
     7:15,
     18:20,
     32:4,
     71:9,
     66:2
 }
'''countc,countb=0,0
for k,v in cong.items():
    if k>=18:
        countc+=v#41

for k,v in bjp.items():
    if k>=18:
        countb+=v#35
if countb>countc:
    print("bjp won by",countb-countc,"votes")
else:
    print("cong won by",countc-countb,"votes")'''


#executes before else condition
'''countc,countb=0,0
for k,v in cong.items():
    if k>=18:
        countc+=v#41

for k,v in bjp.items():
    if k>=18:
        countb+=v#35
if countc>countb:
    print("cong won by",countc-countb,"votes")
else:
    print("bjp won by",countb-countc,"votes")'''



cong_sum=0
bjp_sum=0
for age,votes in cong.items():
    if age>=18:
        cong_sum+=votes
for age,votes in bjp.items():
    if age>=18:
        bjp_sum+=votes
diff=abs(cong_sum-bjp_sum)
if cong_sum>bjp_sum:
    print("cong win: ",diff)
else:
    print("bjp win:",diff)
