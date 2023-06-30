

class ChessPositionsCalculator:

    

    def __init__(self, startPos, brikkePos):
        
        self.brikkePos = brikkePos
        self.getPosition = Position
    
    
    def startPosition():
        a = standardPosition = [-0.01748171324078468, 0.4066080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        return a
    
    

    
    def lower():
        chess_orgin = [-0.2124817132407847, 0.5016080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        gripperheight = chess_orgin[2]
        gripperheight-=0.10
        return gripperheight
    
    def elevate():
        return 0.19681733919878186

    
    
    def getPosition(brikkePos):
        chess_orgin = [-0.2124817132407847, 0.5016080009731705, 0.19681733919878186, 3.141500465469358, 3.7361539352121305e-05, 4.294447431824948e-06]
        length = 0.058
        chessboard_dict ={}
        list_pos = ['a','b','c','d','e','f','g','h']
        for i in range(8):
            for j in range(8):
                postion = f"{list_pos[j]}{i+1}"
                x = chess_orgin[0]+j*length
                y = chess_orgin[1]+i*length
                z = chess_orgin[2]
                Rx= chess_orgin[3]
                Ry= chess_orgin[4]
                Rz= chess_orgin[5]
                chessboard_dict[postion] = [x,y,z,Rx,Ry,Rz]
        pos_a1 = chessboard_dict.get(brikkePos)
        print(pos_a1)
        return pos_a1
        


    # def henterStartSquare():
