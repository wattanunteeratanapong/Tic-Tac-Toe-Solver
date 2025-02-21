# Tic Tac Toe Solver
<img src="https://github.com/user-attachments/assets/3fb09713-1b7b-4174-9b10-0a6ce1977f15" width="100%" alt="Tic Tac Toe"> <br><br>
"Tic Tac Toe" is considered to be the most classic game of all time, and this game sample space is not that much unlike chess (chess sample space is more than a total number of planet in this whole universe), this mean with household computer could easily generate all "Tic Tac Toe" sample space. With all these generated sample space, player could decide which next moves is the best move. <br><br>



## Algorithm Behind
<img src="https://github.com/user-attachments/assets/84c2573c-a402-46da-901e-9e8de75ed45b" width="100%" alt="Tic Tac Toe"> <br>
In this solver i implement by using data structure that behave like a "Linked List" but having 9 branch to store the generate event. 
Implementing like this will make it fast to search, because it didn't have to iterate through and easier to implement than list. 
but it might take a bit of a time to generate all sample space by recursive. <br><br>
I also backtrackinng count win amount, lose amount, draw amount, of that root node in every child node, this is similar to a minimax algorithm, but this is a better version of minimax, where depth of this version is till the end of the game.
<br><br>


## What do we learn?
### Sample Space Amount
At first i though that "Tic Tac Toe" total sample space would be 9!(362,880). <br>
But some of the event stop without filling the entire board. <br>
This is the reason why this game sample space amount is lower than 9!. <br>
( Result from generation n(S)=255,168 )
<br><br>

### Which side have more edge?
<img src="https://github.com/user-attachments/assets/e2e9c88e-9ad8-4233-a715-4260b5db468c" height="190px" alt="Cell1"> <br>
By default player who start first have more edge. <br>
1st Player Wins Rate : 51.41% <br>
2nd Player Wins Rate : 30.53% <br>
Draws Rate : 18.06% <br>
<br>

### Start at Middle (5)
<img src="https://github.com/user-attachments/assets/c29e684f-e98d-473e-96db-c5a7b8e92bb8" height="190px" alt="Cell1"> <br>
This starting cell is the best choice for first player. <br>
1st Player Wins Rate : 60.48% <br>
2nd Player Wins Rate : 21.71% <br>
Draws Rate : 17.81% <br>
<br>

### Start at Corner (1,3,7,9)
<img src="https://github.com/user-attachments/assets/2201acf9-7213-489e-8d52-ff4b77dc8e7a" height="190px" alt="Cell1"> <br>
These starting cell are second best choice for first player. <br>
1st Player Wins Rate : 52.83% <br>
2nd Player Wins Rate : 28.47% <br>
Draws Rate : 18.69% <br>
<br>

### Start at Edge (2,4,6,8)
<img src="https://github.com/user-attachments/assets/50be2859-65fb-4d92-b2d8-a06258a91cee" height="190px" alt="Cell2"> <br>
These starting cell are the worst choice for first player. <br> 
1st Player Win Rate : 48.09% <br>
2nd Player Win Rate : 34.39% <br>
Draw Rate : 17.52% <br>
<br>

### What to do when first player start at the middle?
If first player start at the middle, the best option for second player is to fill the corner cell(1,3,7,9). <br>
<img src="https://github.com/user-attachments/assets/63e1c053-227a-4598-bfc5-f5b27a47c5ad" width="190px" height="190px" alt="Cell51"> 
<img src="https://github.com/user-attachments/assets/12ea6981-687b-40f6-8751-fc5d12dc9be8" width="190px" height="190px" alt="Cell52"> <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(best option)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (worst option)<br>
<br>

### What will happen if both side perfectly execute best move?
Result is a draw. <br>
Cell filling order of perfectly execute : 5, 1, 2, 8, 7, 3, 4, 6, 9 <br><br>
<img src="https://github.com/user-attachments/assets/bd087f1d-f4f6-4fc1-99d1-b4de005ec81a" height="380px" alt="Cell1"> <br>
<br>


