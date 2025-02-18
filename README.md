# Tic Tac Toe Solver
<img src="https://assets.wfcdn.com/im/98684311/resize-h755-w755%5Ecompr-r85/1466/146676057/GSE+Games+%26+Sports+Expert+2+Player+Wood+Tic+Tac+Toe.jpg" width="100%" alt="Tic Tac Toe"> <br><br>
"Tic Tac Toe" is considered to be the most classic game of all time, and this game sample space is not that much unlike chess (chess sample space is more than a total number of planet in this whole universe), this mean with household computer could easily generate all "Tic Tac Toe" sample space. With all these generated sample space, player could decide which next moves is the best move. <br><br>



## Algorithm Behind
In this solver we use data structure that behave like a "Linked List" but having 9 branch.
<br><br>


## What do we learn?
### Sample Space Amount
At first i though that "Tic Tac Toe" n(S) = 9! = 362,880 <br> 
but some of the event stop without filling the entire board, this is the reason why this game sample space amount is lower than 9!. <br>
Result from generation n(S)=255,168

### Which side have more edge?
<img src="https://github.com/user-attachments/assets/e2e9c88e-9ad8-4233-a715-4260b5db468c" height="150px" alt="Cell1"> <br>
By default player who start first have more edge. <br>
1st Player Wins Rate : 51.41% <br>
2nd Player Wins Rate : 30.53% <br>
Draws : 18.06% <br>

### Start at Middle (5)
<img src="https://github.com/user-attachments/assets/c29e684f-e98d-473e-96db-c5a7b8e92bb8" height="150px" alt="Cell1"> <br>
This starting cell is the best choice for first player. <br>
1st Player Wins Rate : 60.48% <br>
2nd Player Wins Rate : 21.71% <br>
Draws : 17.81% <br>

### Start at Corner (1,3,7,9)
<img src="https://github.com/user-attachments/assets/2201acf9-7213-489e-8d52-ff4b77dc8e7a" height="95px" alt="Cell1">
<img src="https://github.com/user-attachments/assets/3037b963-86d2-449b-8bfa-d20a4e97ed7c" height="95px" alt="Cell3">
<img src="https://github.com/user-attachments/assets/68236beb-533e-4b72-bfe0-e8502bb982a7" height="95px" alt="Cell7">
<img src="https://github.com/user-attachments/assets/8c623a47-6786-4ddc-9367-862f2024247f" height="95px" alt="Cell9"> <br>
These starting cell are second best choice for first player. <br>
1st Player Wins Rate : 52.83% <br>
2nd Player Wins Rate : 28.47% <br>
Draws Rate : 18.69% <br>

### Start at Edge (2,4,6,8)
<img src="https://github.com/user-attachments/assets/50be2859-65fb-4d92-b2d8-a06258a91cee" height="95px" alt="Cell2">
<img src="https://github.com/user-attachments/assets/5aacab70-b3ab-48d7-8656-f16675c986d6" height="95px" alt="Cell4">
<img src="https://github.com/user-attachments/assets/17376be0-e70c-4a7f-915d-f4830095d170" height="95px" alt="Cell6">
<img src="https://github.com/user-attachments/assets/0627b095-96cb-44e6-b544-de2cf8d93af9" height="95px" alt="Cell8"> <br>
These starting cell are the worst choice for first player. <br> 
1st Player Win Rate : 48.09% <br>
2nd Player Win Rate : 34.39% <br>
Draw Rate : 17.52% <br>

### What to do when first player start at the middle?
If first player start at the middle, the best option for second player is to fill the corner cell(1,3,7,9). <br>
(best option) <br>
<img src="https://github.com/user-attachments/assets/63e1c053-227a-4598-bfc5-f5b27a47c5ad" width="95px" height="95px" alt="Cell51"> 
<img src="https://github.com/user-attachments/assets/d2bfebff-6b1c-4ece-bbe2-828e527417d6" width="95px" height="95px" alt="Cell53"> 
<img src="https://github.com/user-attachments/assets/01422a6f-da5e-4b44-845e-6e4588bca9b6" width="95px" height="95px" alt="Cell57"> 
<img src="https://github.com/user-attachments/assets/cc21fdbb-23a2-4632-8563-9a7ffc765392" width="95px" height="95px" alt="Cell59"> <br>
(worst option) <br>
<img src="https://github.com/user-attachments/assets/12ea6981-687b-40f6-8751-fc5d12dc9be8" width="95px" height="95px" alt="Cell52"> 
<img src="https://github.com/user-attachments/assets/515350d5-fc24-4fec-ab27-aaef21a170d8" width="95px" height="95px" alt="Cell54"> 
<img src="https://github.com/user-attachments/assets/76585f59-c7fa-45a6-90ac-f954b381de04" width="95px" height="95px" alt="Cell56"> 
<img src="https://github.com/user-attachments/assets/327b35c3-a152-40cb-9743-96b5730c3a0c" width="95px" height="95px" alt="Cell57"> <br>

### What will happen if both side perfectly execute best move?
Result is a draw. <br>
Cell filling order of perfectly execute : 5, 1, 2, 8, 7, 3, 4, 6, 9 <br><br>
<img src="https://github.com/user-attachments/assets/bd087f1d-f4f6-4fc1-99d1-b4de005ec81a" height="400px" alt="Cell1"> <br>


