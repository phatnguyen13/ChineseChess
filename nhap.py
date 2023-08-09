ranksToRows = {0:'10',1:'9', 2:'8', 3:'7', 4:'6', 5:'5', 6:'4', 7:'3', 8:'2', 9:'1'}
ranksToCols = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i'}
print(ranksToRows)
print(ranksToCols)
x=1
y=5
stayaway = [(x,y),(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
candidate = [(x,y) for x in range(10) if (x,y) not in stayaway ] + [(x,y) for y in range(9) if (x,y) not in stayaway ]

print(candidate)