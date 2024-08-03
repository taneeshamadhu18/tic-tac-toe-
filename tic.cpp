#include<iostream>
using namespace std;

const int size = 3;
char board[size][size];

void initializeboard() {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            board[i][j] = ' ';
        }
    }
}

void displayboard()
{
    for(int i =0;i<size;i++)
    {
        for(int j=0;j<size;j++)
        {  
            cout<<board[i][j]<<" ";
        }
        cout<<endl;
    }
}


bool move(int row, int col, char player) {
    if (row>=0&&row<size&&col>=0&&col<size&&board[row][col]==' ') {
        board[row][col]=player;
        return true;
    }
    return false;
}

bool win(char player) {
    for (int i = 0; i < size; i++) {
        if ((board[i][0]==player&&board[i][1]==player&&board[i][2]==player) ||(board[0][i]==player&&board[1][i]==player&&board[2][i]==player)) {
            return true;
        }
    }
    if ((board[0][0]==player&&board[1][1]==player&&board[2][2]==player) ||(board[0][2]==player&&board[1][1]==player&&board[2][0]==player)) {
        return true;
    }
    return false;
}

bool draw() {
    for (int i =0; i< size;i++) {
    for (int j =0; j< size;j++) {
     if (board[i][j]==' ') {
         return false;
        }
        }
    }
    return true;
}

int main() {
    char cplayer;
    int row, col;
    initializeboard();
    displayboard();
    
    cout<<"Enter the player name ie either X or O: ";
    cin>>cplayer;
    
    if (cplayer!='X'&&cplayer!='O') {
        cout<<"Invalid player name"<<endl;
        return 1; 
    }
    
    while (true) {
        cout<<"Enter the row and col (between 0 and 2): ";
        cin>>row>>col;
        
        if (row>=size||row<0||col>=size||col<0) {
            cout << "Array out of bounds, enter a valid value" << endl;
            continue; 
        }
        
        if (move(row, col, cplayer)) {
            displayboard();
            
            if (win(cplayer)) {
                cout<<"Player " << cplayer << " wins!" << endl;
                break;
            } else if (draw()) {
                cout<<"The game is a draw" << endl;
                break;
            } else {
                cplayer=(cplayer == 'X') ? 'O' : 'X';
            }
        } else {
            cout<<"Invalid move" << endl;
        }
    }
    
    return 0;
}
