# loop inside loop 
for i in range(3):
    
    for j in range(3):
        print(f"i={i},j={j}")
        if i==2 and j==2:
            break
    if i==2 and j==2:
        break    
        
        

# firstly it goes to 1st loop it has to run 3 times
# 2nd loop runs 3 times then print
# now 1st loop then 2nd loop execute then it goes to 2nd loop only because it runs 3 times
# means 1 time outer loop amd 3 time inner loop           