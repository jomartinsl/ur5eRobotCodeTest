
from rtde_control import RTDEControlInterface as RTDEControl
from rtde_receive import RTDEReceiveInterface as RTDEReceive
from Classes.robotiq_gripper_control import RobotiqGripper
#from Classes.inverse_kinematics import ur5e_inverse_kinematics
import time
import math


#Sett roboten i remote controll
rtde_c = RTDEControl("172.31.1.144")
rtde_r = RTDEReceive("172.31.1.144")
gripper = RobotiqGripper(rtde_c)
#Deklarerer hva inverse kinematics skal være




# Activate the gripper and initialize force and speed
#g1= gripper.activate()  # returns to previous position after activation

#print(g1)

gripper.set_force(50)  # from 0 to 100 %
gripper.set_speed(100)  # from 0 to 100 %

# Perform some gripper actions
# gripper.open()
# gripper.close()
# time.sleep(1)
# gripper.open()
# gripper.move(10)  # mm


gripper.move(100)

RobotStart = True 
OnlyPosition = True

getActual_q = rtde_r.getActualQ()
tcpPos = rtde_r.getTargetTCPPose()


startPos = [-1.70, -2.186, 1.976, -1.343, 4.739, -0.052]
speed = 0.5
acceleration = 0.3
plukkeOppBoks = [-1.7, -1.05, 1.4, -1.343, 4.739, -0.052]


print (math.degrees(-2.186/180))


StartRobotKnapp = input('Press "1" for å starte eller "2" for TCP-position: ')
if StartRobotKnapp=='1':
	RobotStart=True
else:
	RobotStart= False
	


if RobotStart:

	motionToStart= rtde_c.moveJ(startPos, speed, acceleration)
	print('Startposisjon')
	
	motionToStart = rtde_c.moveJ(plukkeOppBoks, speed, acceleration )
	gripper.move(25)
	print('tilbake til start posisjon' )
	
	f1=input()
	if f1=='1':
		a = 1
		altPos = [-1.60, -2.186, 1.976, -1.343, 4.739, -0.052]
		altPos2 = [-1.70, -2.186, 1.976, -1.343, 4.739, -0.052]
		while a<6:
			motionToStart= rtde_c.moveJ(altPos, speed, acceleration)
			motionToStart= rtde_c.moveJ(altPos2, speed, acceleration)
			a = a+1
		print('Done with pos forandring')

	
		motionToStart= rtde_c.moveJ(startPos, speed, acceleration)
		print('Done with startposition')
		motionToStart = rtde_c.moveJ(plukkeOppBoks, speed, acceleration )
		gripper.open()
		motionToStart= rtde_c.moveJ(startPos, speed, acceleration)
		


	else:
		print(getActual_q)
	

	
	




