# Tic Tac Toe Solver
<img src="https://github.com/user-attachments/assets/3685a7cf-fcc0-4e46-a848-809acbd23b10" width="100%" alt="Tic Tac Toe"> <br><br>
"Tic Tac Toe" is considered to be the most classic game of all time, and this game sample space is not that much unlike chess(chess sample space is more than a total number of planet in this whole universe), this mean with household computer could easily generate all "Tic Tac Toe" sample space. by generating all sample space it could decide which is the next best move.
This repository is trying create "Tic Tac Toe" solver by to generate all the sample space, and also help player decide which is the best next move.


## Algorithm Behind
In this solver we use data structure that behave like a "Linked List" but having 9 branch.


## What do we learn from solver?
### Start at Edge (2,4,6,8)
[0, 1, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] <br>
[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 1] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] <br>
[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 1, 0] <br><br>
These starting cell are the worst choice for first player. <br> 
First Player Win Rate: 48.094% <br>
Second Player Win Rate: 34.387% <br>
Draw Rate: 17.518% <br>

### Start at Corner (1,3,7,9)
[1, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 1] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] <br>
[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] <br>
[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1, 0, 0] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0, 0, 1] <br><br>
These starting cell are second best choice for first player. <br>
First Player Wins Rate: 52.834% <br>
Second Player Wins Rate: 28.472% <br>
Draws Rate: 18.693% <br>

### Start at Middle (5)
[0, 0, 0] <br>
[0, 1, 0] <br>
[0, 0, 0] <br><br>
This starting cell is the best choice for first player. <br>
First Player Wins Rate: 60.482% <br>
Second Player Wins Rate: 21.706% <br>
Draws: 17.810% <br>

