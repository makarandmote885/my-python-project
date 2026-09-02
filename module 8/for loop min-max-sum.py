scores = [2, 45, 65, 35, 37, 86, 32]

total = 0
for score in scores:
    total = total + score
print(total) 

total= sum(scores)        # sum function 
print(total)

# highest score 
high = scores[0]
for score in scores:
    if high < score:
        high=score
print(high)      

high=max(scores)           # max function
print(high)

low = scores[0]            # min function
low = min(scores)
print(low)
