#RoboPositionsChess

class Posisjoner:

    from rtde_control import RTDEControlInterface as RTDEControl
    from rtde_receive import RTDEReceiveInterface as RTDEReceive
    from Classes.robotiq_gripper_control import RobotiqGripper
    from Classes.tcp_verdi_mm_degree import TCPValues
    import time
    import math
    import copy
    from Classes.CalculatePositions import ChessPositionsCalculator
    import asyncio
    import asyncdgt
    import chess

    #Sett roboten i remote controll
    rtde_c = RTDEControl("172.31.1.144")
    rtde_r = RTDEReceive("172.31.1.144")
    gripper = RobotiqGripper(rtde_c)

    gripper.set_force(50)  # from 0 to 100 %
    gripper.set_speed(100)  # from 0 to 100 %
    speed = 0.5
    acceleration = 0.3
    gripper.move(100)


    list_pos = ['a','b','c','d','e','f','g','h']




    loop = asyncio.get_event_loop()
    dgt = asyncdgt.auto_connect(loop, ["/dev/ttyACM*"])

    print("Version:", loop.run_until_complete(dgt.get_version()))
    
    board = chess.Board()
    @dgt.on("board")
    def on_board(board):
        print("Position changed:")

        # idlePos = rtde_c.moveL(ChessPositionsCalculator.startPosition())
        # sjakkbrikke = ChessPositionsCalculator.getPosition('a1')
        # GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        # sjakkbrikke[2] = ChessPositionsCalculator.lower()
        # senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        # gripper.move(10)
        # sjakkbrikke[2] = ChessPosit#RoboPositionsChess

class Posisjoner:

    from rtde_control import RTDEControlInterface as RTDEControl
    from rtde_receive import RTDEReceiveInterface as RTDEReceive
    from Classes.robotiq_gripper_control import RobotiqGripper
    from Classes.tcp_verdi_mm_degree import TCPValues
    import time
    import math
    import copy
    from Classes.CalculatePositions import ChessPositionsCalculator
    import asyncio
    import asyncdgt

    #Sett roboten i remote controll
    rtde_c = RTDEControl("172.31.1.144")
    rtde_r = RTDEReceive("172.31.1.144")
    gripper = RobotiqGripper(rtde_c)

    gripper.set_force(50)  # from 0 to 100 %
    gripper.set_speed(100)  # from 0 to 100 %
    speed = 0.5
    acceleration = 0.3
    gripper.move(100)




    # loop = asyncio.get_event_loop()
    # dgt = asyncdgt.auto_connect(loop, ["/dev/ttyACM*"])

    # print("Version:", loop.run_until_complete(dgt.get_version()))


    # @dgt.on("board")
    # def on_board(board):
    #     print("Position changed:")
    #     print(board)

        

    # try:
    #     loop.run_forever()
    # except KeyboardInterrupt:
        
    #     pass
    # finally:
    #     dgt.close()
    #     loop.close()
        
    




    

    


    list_pos = ['a','b','c','d','e','f','g','h']


    startsjakkSpillet = True

    # PUP = #Pick uo point
    # DOP = #Drop off point
    # while startsjakkSpillet:

    # def MovePiece(startSquare, endSquare):

    #______________________________________________________
    #08.14, 30.06.2023 sist endret, programmet gjører fint:
    idlePos = rtde_c.moveL(ChessPositionsCalculator.startPosition())
    
    sjakkbrikke = ChessPositionsCalculator.getPosition('a1')
    GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    sjakkbrikke[2] = ChessPositionsCalculator.lower()
    senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    gripper.move(10)
    sjakkbrikke[2] = ChessPositionsCalculator.elevate()
    løftArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    sjakkbrikke = ChessPositionsCalculator.getPosition('a3')
    GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    sjakkbrikke[2] = ChessPositionsCalculator.lower()
    senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    gripper.move(50)
    #______________________________________________________


    

    # for i in range(8):
    #     for j in range(8):
    #         position = f"{list_pos[j]}{i+1}"
    #         sjakkbrikke= ChessPositionsCalculator.getPosition(position)

    #         GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
            
    #         sjakkbrikke[2] = ChessPositionsCalculator.lower()

    #         senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    #         gripper.move(10)
    #         sjakkbrikke[2] = ChessPositionsCalculator.elevate()
    #         løftArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    #         if list_pos[j]=='h':
    #             sjakkbrikke= ChessPositionsCalculator.getPosition(f"{'a'}{i+2}")
    #         else:
    #             position = f"{list_pos[j+1]}{i+1}"
    #             sjakkbrikke= ChessPositionsCalculator.getPosition(position)

    #         GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    #         sjakkbrikke[2] = ChessPositionsCalculator.lower()
    #         senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    #         gripper.move(50)






            # sjakkbrikke[2]=ChessPositionsCalculator.placePiece()
            # SetterNed= rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
            # gripper.move(50)
            # sjakkbrikke[2] = ChessPositionsCalculator.pickUp()
            # PlukkerOpp = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
            



            
        
    





















    









    a = 1
    
    








    





    







ionsCalculator.elevate()
        # løftArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        # sjakkbrikke = ChessPositionsCalculator.getPosition('a3')
        # GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        # sjakkbrikke[2] = ChessPositionsCalculator.lower()
        # senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
        # gripper.move(50)
        
        
        
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        
        pass
    finally:
        dgt.close()
        loop.close()
        
    




    

    


    


    

    # PUP = #Pick uo point
    # DOP = #Drop off point
    # while startsjakkSpillet:

    # def MovePiece(startSquare, endSquare):

    #______________________________________________________
    #08.14, 30.06.2023 sist endret, programmet gjører fint:
    # idlePos = rtde_c.moveL(ChessPositionsCalculator.startPosition())
    
    # sjakkbrikke = ChessPositionsCalculator.getPosition('a1')
    # GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    # sjakkbrikke[2] = ChessPositionsCalculator.lower()
    # senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    # gripper.move(10)
    # sjakkbrikke[2] = ChessPositionsCalculator.elevate()
    # løftArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    # sjakkbrikke = ChessPositionsCalculator.getPosition('a3')
    # GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    # sjakkbrikke[2] = ChessPositionsCalculator.lower()
    # senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    # gripper.move(50)
    #______________________________________________________


    

    # for i in range(8):
    #     for j in range(8):
    #         position = f"{list_pos[j]}{i+1}"
    #         sjakkbrikke= ChessPositionsCalculator.getPosition(position)

    #         GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
            
    #         sjakkbrikke[2] = ChessPositionsCalculator.lower()

    #         senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    #         gripper.move(10)
    #         sjakkbrikke[2] = ChessPositionsCalculator.elevate()
    #         løftArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    #         if list_pos[j]=='h':
    #             sjakkbrikke= ChessPositionsCalculator.getPosition(f"{'a'}{i+2}")
    #         else:
    #             position = f"{list_pos[j+1]}{i+1}"
    #             sjakkbrikke= ChessPositionsCalculator.getPosition(position)

    #         GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    #         sjakkbrikke[2] = ChessPositionsCalculator.lower()
    #         senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    #         gripper.move(50)






            # sjakkbrikke[2]=ChessPositionsCalculator.placePiece()
            # SetterNed= rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
            # gripper.move(50)
            # sjakkbrikke[2] = ChessPositionsCalculator.pickUp()
            # PlukkerOpp = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
            



            
        
    





















    









    a = 1
    
    








    





    








