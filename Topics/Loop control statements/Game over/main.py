scores = input().split()
# put your python code here
let_i = [i for i in range(len(scores)) if scores[i] == 'I']

if len(let_i) < 3:
    print('You won')
    print(scores.count('C'))
else:
    lost_scores = scores[:let_i[2]]
    print('Game over')
    print(lost_scores.count('C'))
