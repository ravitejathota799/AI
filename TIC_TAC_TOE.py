```Approach-2```


poss={
    '1':[('2','3'),('4','7'),('5','9')],
    '2':[('1','3'),('5','8')],
    '3':[('1','2'),('6','9'),('5','7')],
    '4':[('1','7'),('5','6')],
    '5':[('4','6'),('2','8'),('1','9'),('3','7')],
    '6':[('3','9'),('4','5')],
    '7':[('1','4'),('8','9'),('5','3')],
    '8':[('7','9'),('5','2')],
    '9':[('6','3'),('7','8'),('1','5')]
}
 
theBoard = {'7':'-','8':'-','9':'-',
            '4':'-','5':'-','6':'-',
            '1':'-','2':'-','3':'-'}
board_Keys = []
for key in theBoard:
    board_Keys.append(key)
    
def printBoard(board):
    print('-------------')
    print('| '+board['7']+' | '+board['8']+' | '+board['9']+' |')
    print('-------------')
    print('| '+board['4']+' | '+board['5']+' | '+board['6']+' |')
    print('-------------')
    print('| '+board['1']+' | '+board['2']+' | '+board['3']+' |')
    print('-------------')
printBoard(theBoard)
 
def win(board,turn):
    for i in (1,4,7):
        a,b,c=str(i),str(i+1),str(i+2)                          #row wise win.
        if board[a]==board[b]==board[c]==turn:return True
    for i in (1,2,3):
        a,b,c=str(i),str(i+3),str(i+6)                          #column wise win.
        if board[a]==board[b]==board[c]==turn:return True
    if board['1']==board['5']==board['9']==turn:return True     # 1,5,9 diagonal win.
    if board['3']==board['5']==board['7']==turn:return True     # 3,5,7 diagonal win.
    else:return False

    
def poswin(board, turn):
    for i in (1,4,7):
        a,b,c=str(i),str(i+1),str(i+2)
        if board[a]==board[b]==turn or board[b]==board[c]==turn or board[c]==board[a]==turn:        #row wise.
            if board[a]=='-':return a
            elif board[b]=='-':return b
            elif board[c]=='-':return c
    
    for i in (1,2,3):
        a,b,c=str(i),str(i+3),str(i+6)
        if board[a]==board[b]==turn or board[b]==board[c]==turn or board[c]==board[a]==turn:        #column wise.
            if board[a]=='-':return a
            elif board[b]=='-':return b
            elif board[c]=='-':return c
    
    a,b,c='1','5','9'
    if board[a]==board[b]==turn or board[b]==board[c]==turn or board[c]==board[a]==turn:            # 1,5,9 diagonal.
        if board[a]=='-':return a
        elif board[b]=='-':return b
        elif board[c]=='-':return c       
    
    a,b,c='3','5','7'
    if board[a]==board[b]==turn or board[b]==board[c]==turn or board[c]==board[a]==turn:            # 3,5,7 diagonal.
        if board[a]=='-':return a
        elif board[b]=='-':return b
        elif board[c]=='-':return c 
        
    return '0'
    
def game():
    count=0
    while True:
        if count==9:
            print("!! Game Over !!")
            print("It's a tie.")
            break
        move=input("It's your turn. place at ? ")
        if theBoard[move]=='-':
            theBoard[move]='X'
            count+=1
        else:
            print("The place is already filled.\nplace at ?")
            continue
        printBoard(theBoard)
        if count>4 and win(theBoard,'X'):
            print("!! Game Over !!")
            print("You have Won.")
            break
        print("A.I's turn.")
        if move!='5' and theBoard['5']=='-':theBoard['5']='O'
        else:
            pos = poswin(theBoard, 'O')
            if pos!='0':
                theBoard[pos]='O'
            else:
                pos=poswin(theBoard, 'X')
                if pos=='0':
                    for p in poss[move]:
                        if theBoard[p[0]] == '-':
                            theBoard[p[0]] = 'O'
                            break
                        elif theBoard[p[1]] == '-':
                            theBoard[p[1]] = 'O'
                            break
                else:theBoard[pos]='O'
            count+=1
        printBoard(theBoard)
        if count>4 and win(theBoard,'O'):
            print("!! Game Over !!")
            print("A.I won.")
            break
game()



```Approach-3 :--```

import itertools as it
poss={
    1:[(2,3),(4,7),(5,9)],
    2:[(1,3),(5,8)],
    3:[(1,2),(6,9),(5,7)],
    4:[(1,7),(5,6)],
    5:[(4,6),(2,8),(1,9),(3,7)],
    6:[(3,9),(4,5)],
    7:[(1,4),(8,9),(5,3)],
    8:[(7,9),(5,2)],
    9:[(6,3),(7,8),(1,5)]
}

ms={7:8, 8:1, 9:6,
    4:3, 5:5, 6:7,
    1:4, 2:9, 3:2}

theBoard = {7:'-',8:'-',9:'-',
            4:'-',5:'-',6:'-',
            1:'-',2:'-',3:'-'}

board_Keys = []
for key in theBoard:
    board_Keys.append(key)

def printBoard(board):
    print('-------------')
    print('| '+board[7]+' | '+board[8]+' | '+board[9]+' |')
    print('-------------')
    print('| '+board[4]+' | '+board[5]+' | '+board[6]+' |')
    print('-------------')
    print('| '+board[1]+' | '+board[2]+' | '+board[3]+' |')
    print('-------------')
printBoard(theBoard)

def win(board,turn):
    for i in (1,4,7):
        a,b,c=i,i+1,i+2                          #row wise win.
        if board[a]==board[b]==board[c]==turn:return True
    for i in (1,2,3):
        a,b,c=i,i+3,i+6                             #column wise win.
        if board[a]==board[b]==board[c]==turn:return True
    if board[1]==board[5]==board[9]==turn:return True     # 1,5,9 diagonal win.
    if board[3]==board[5]==board[7]==turn:return True     # 3,5,7 diagonal win.
    else:return False

def poswin(board, temp):
    keys=list(ms.keys())
    vals=list(ms.values())
    for i in it.combinations(temp,2):
        pos=15-sum(i) 
        if pos<=9 and pos>=1:
            val=keys[vals.index(pos)]   
            if board[val]=='-':return val
    return 0

def game():
    count=0
    hu,ai=[],[]
    while True:
        if count==9:
            print("!! Game Over !!")
            print("It's a tie.")
            break
        move=int(input("It's your turn. place at ? "))
        if theBoard[move]=='-':
            theBoard[move]='X'
            hu.append(ms[move])
            count+=1
        else:
            print("The place is already filled.\nplace at ?")
            continue
        printBoard(theBoard)
        if count>4 and win(theBoard, 'X'):
            print("!! Game Over !!")
            print("You have Won.")
            break
        print("A.I's turn.")
        if move!=5 and theBoard[5]=='-':
            theBoard[5]='O'
            ai.append(ms[5])
        else:
            pos = poswin(theBoard, ai)
            if pos!=0:
                theBoard[pos]='O'
                ai.append(ms[pos])
            else:
                pos=poswin(theBoard, hu)
                if pos==0:
                    for p in poss[move]:
                        if theBoard[p[0]] == '-':
                            theBoard[p[0]] = 'O'
                            ai.append(ms[p[0]])
                            break
                        elif theBoard[p[1]] == '-':
                            theBoard[p[1]] = 'O'
                            ai.append(ms[p[1]])
                            break
                else:
                    theBoard[pos]='O'
                    ai.append(ms[pos])
            count+=1
        printBoard(theBoard)
        if count>4 and win(theBoard, 'O'):
            print("!! Game Over !!")
            print("A.I won.")
            break
game()




#Another Approach




theBoard={'7':2,'8':2,'9':2,'4':2,'5':2,'6':2,'1':2,'2':2,'3':2}
board_keys=[]
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(str(board['7'])+'|'+str(board['8'])+'|'+str(board['9']))
    print('-+-+-')
    print(str(board['4'])+'|'+str(board['5'])+'|'+str(board['6']))
    print('-+-+-') b
    print(str(board['1'])+'|'+str(board['2'])+'|'+str(board['3']))

def make():
    if theBoard['5']==2:
        return '5'
    elif theBoard['2']==2:
        return '2'
    elif theBoard['4']==2:
        return '4'
    elif theBoard['6']==2:
        return '6'
    elif theBoard['8']==2:
        return '8'

def switch_player(count):
    current_player='C' if count%2!=0 else 'H'
    return current_player


def go(move):
    theBoard[str(move)]=5

def posswin():
        if theBoard['7']*theBoard['8']*theBoard['9']==18 or theBoard['7']*theBoard['8']*theBoard['9']==50:
            if theBoard['7']==2:
                return 7
            elif theBoard['8']==2:
                return 8
            else:
                return 9
        elif theBoard['4']*theBoard['5']*theBoard['6']==18 or theBoard['4']*theBoard['5']*theBoard['6']==50:
            if theBoard['4']==2:
                return 4
            elif theBoard['5']==2:
                return 5
            else:
                return 6
        elif theBoard['1']*theBoard['2']*theBoard['3']==18 or theBoard['1']*theBoard['2']*theBoard['3']==50:
            if theBoard['1']==2:
                return 1
            elif theBoard['2']==2:
                return 2
            else:
                return 3
        elif theBoard['1']*theBoard['4']*theBoard['7']==18 or theBoard['1']*theBoard['4']*theBoard['7']==50:
            if theBoard['1']==2:
                return 1
            elif theBoard['4']==2:
                return 4
            else:
                return 7
        elif theBoard['2']*theBoard['5']*theBoard['8']==18 or theBoard['2']*theBoard['5']*theBoard['8']==50:
            if theBoard['2']==2:
                return 2
            elif theBoard['5']==2:
                return 5
            else:
                return 8
        elif theBoard['3']*theBoard['6']*theBoard['9']==18 or theBoard['3']*theBoard['6']*theBoard['9']==50:
            if theBoard['3']==2:
                return 3
            elif theBoard['6']==2:
                return 6
            else:
                return 9
        elif theBoard['1']*theBoard['5']*theBoard['9']==18 or theBoard['1']*theBoard['5']*theBoard['9']==50:
            if theBoard['1']==2:
                return 1
            elif theBoard['5']==2:
                return 5
            else:
                return 9
        elif theBoard['3']*theBoard['5']*theBoard['7']==18 or theBoard['3']*theBoard['5']*theBoard['7']==50:
            if theBoard['3']==2:
                return 3
            elif theBoard['5']==2:
                return 5
            else:
                return 7
        else:
            return 0
       
       
def checkwin(current_player):
    if current_player=='C':
        turn="player"
    else:
        turn="computer"
   
    if theBoard['7']==theBoard['8']==theBoard['9']!=2:
        printBoard(theBoard)
        print("Game Over!!!.")
        print(" *** "+turn+" won. *** ")
        return 1
    elif theBoard['4']==theBoard['5']==theBoard['6']!=2:
        printBoard(theBoard)
        print("Game Over!!!.")
        print(" *** "+turn+" won. *** ")
        return 1
    elif theBoard['1']==theBoard['2']==theBoard['3']!=2:
        printBoard(theBoard)
        print("Game Over!!!.\n")
        print(" *** "+turn+" won. *** ")
        return 1
    elif theBoard['1']==theBoard['4']==theBoard['7']!=2:
        printBoard(theBoard)
        print("Game Over!!!.\n")
        print(" *** "+turn+" won. *** ")
        return 1
    elif theBoard['2']==theBoard['5']==theBoard['8']!=2:
        printBoard(theBoard)
        print("Game Over!!!.\n")
        print(" *** "+turn+" won. *** ")
        return 1
    elif theBoard['3']==theBoard['6']==theBoard['9']!=2:
        printBoard(theBoard)
        print("Game Over!!!.\n")
        print(" *** "+turn+" won. *** ")
        return 1
    elif theBoard['7']==theBoard['5']==theBoard['3']!=2:
        printBoard(theBoard)
        print("Game Over!!!.\n")
        print(" *** "+turn+" won. *** ")
        return 1
    elif theBoard['1']==theBoard['5']==theBoard['9']!=2:
        printBoard(theBoard)
        print("Game Over!!!.\n")
        print(" *** "+turn+" won. *** ")
        return 1
    return 0
           
       
       
def game():
    count=0
    current_player="H"
    for i in range(9):
        printBoard(theBoard)
        if current_player=="H":
            print("It's your turn.Move to which place?")
            move=input()
            if theBoard[move]==2:
                theBoard[move]=3
                count+=1
            else:
                print("That place is already filled.\nMove to which place?")
                move=input()
                while theBoard[move]!=2:
                    print("That place is already filled.\nMove to which place?")
                    move=input()
                theBoard[move]=3
                count+=1
            current_player=switch_player(count)
        else:
            poss=posswin()
            if poss==0:
                x=make()
                go(x)
            else:
                go(poss)
            print("\nComputer's move\n")
            count+=1
            current_player=switch_player(count)
       
        if count>=5:
            flag=checkwin(current_player)
            if flag:
                break
        if count==9:
            printBoard(theBoard)
            print("Game Over.\n")
            print("it's a tie!!!")
    restart=input("Do you want to play again?(y/n)")
    if restart=="y" or restart=="Y":
        for key in board_keys:
            theBoard[key]=2
        game()
     

if __name__=="__main__":
    game()
