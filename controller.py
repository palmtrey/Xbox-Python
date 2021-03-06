import pygame
pygame.init()
joysticks = []
clock = pygame.time.Clock()
keepPlaying = True

# for all the connected joysticks
for i in range(0, pygame.joystick.get_count()):
	# create a Joystick object in our list
	joysticks.append(pygame.joystick.Joystick(i))
	# initialize them all (-1 means loop foerever)
	joysticks[-1].init()
	# print a statement telling what the name of the controller is
	print("Detected joystick ", joysticks[-1].get_name(),"'")
	
while keepPlaying:
	clock.tick(60)
	for event in pygame.event.get():
		#The zero button is the 'a' button, 1 the 'b' button, 3 the 'y' button, 2 the 'x' button
		if event.button == 0:
			print("A")
		if event.button == 1:
			print("B")
		if event.button == 2:
			print("X")
		if event.button == 3:
			print("Y")				
