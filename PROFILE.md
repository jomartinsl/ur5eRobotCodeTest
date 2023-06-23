#Here is my code for the ur5e robot. It's pretty simple for now, but will become more complicated.
#I need to import the robotiqGripper lib too, but haven't figured that part out yet.

from rtde_control import RTDEControlInterface as RTDEControl
from rtde_receive import RTDEReceiveInterface as RTDEReceive

rtde_c = RTDEControl("172.31.1.144")
rtde_r = RTDEReceive("172.31.1.144")




RobotStart = True 
OnlyPosition = True

getActual_q = rtde_r.getActualQ()
tcpPos = rtde_r.getTargetTCPPose()


startPos = [-1.70, -2.186, 1.976, -1.343, 4.739, -0.052]
speed = 0.5
acceleration = 0.3
rotereRundt = [-1.7, -1.05, 1.4, -1.343, 4.739, -0.052]



if RobotStart:
	
	motionToStart= rtde_c.moveJ(startPos, speed, acceleration)
	print('Done with startposition')

	motionToStart= rtde_c.moveJ(rotereRundt, speed, acceleration)
	print('tilbake til start posisjon')
	
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

else:
	
	print(getActual_q)
	

	
	




