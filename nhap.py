ranksToRows = {0:'10',1:'9', 2:'8', 3:'7', 4:'6', 5:'5', 6:'4', 7:'3', 8:'2', 9:'1'}
ranksToCols = {0:'a',1:'b',2:'c',3:'d',4:'e',5:'f',6:'g',7:'h',8:'i'}
print(ranksToRows)
print(ranksToCols)
for i in range(10):
    if i%2 == 0:
        print(i)
    if i ==7: break
else:
    print('b')