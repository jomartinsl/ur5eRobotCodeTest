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
    

    # PUP = #Pick uo point
    # DOP = #Drop off point
    # while startsjakkSpillet:

    # def MovePiece(startSquare, endSquare):

    #______________________________________________________
    #08.14, 30.06.2023 sist endret, programmet gjører fint:
    idlePos = rtde_c.moveL(ChessPositionsCalculator.startPosition())
    
    sjakkbrikke = ChessPositionsCalculator.getPosition('a5')
    GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    sjakkbrikke[2] = ChessPositionsCalculator.lower()
    senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    gripper.move(10)
    sjakkbrikke[2] = ChessPositionsCalculator.elevate()
    løftArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    sjakkbrikke = ChessPositionsCalculator.getPosition('b1')
    GårTilPosisjon = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    løftArmIgjen = copy.deepcopy(sjakkbrikke) #Deepcopy
    sjakkbrikke[2] = ChessPositionsCalculator.lower()
    senkArm = rtde_c.moveL(sjakkbrikke,0.25,1.2,False)
    gripper.move(50)
    GårTilPosisjon = rtde_c.moveL(løftArmIgjen,0.25,1.2,False)
    idlePos = rtde_c.moveL(ChessPositionsCalculator.startPosition())
    
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
    
    








    





    








