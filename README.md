# Tic Tac Toe Solver
<img src="https://www.bernzomatic.com/getattachment/495f277e-5ace-487a-a82e-5decc0772c4f/DIY-Tic-Tac-Toe-Game-Board.aspx?maxsidesize=1200" width="100%" alt="Tic Tac Toe"> <br><br>
"Tic Tac Toe" is considered to be the most classic game of all time, and this game sample space is not that much unlike chess(chess sample space is more than a total number of planet in this whole universe), this mean with household computer could easily generate all "Tic Tac Toe" sample space. With all these generated sample space, player could decide which next move is the best move. <br><br>



## Algorithm Behind
In this solver we use data structure that behave like a "Linked List" but having 9 branch.
<br><br>


## What do we learn?
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

### Sample Space Amount
At first i though that "Tic Tac Toe" n(S) = 9! = 362,880 <br> 
but some of the event stop without filling the entire board, this is the reason why this game sample space amount is lower than 9!. <br>
Result from simulation n(S)=255,168

