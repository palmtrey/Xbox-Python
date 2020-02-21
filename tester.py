import pygame, time, os

pygame.init()
print(pygame.joystick.get_count())

controller = pygame.joystick.Joystick(0)
controller.init()

print(controller.get_numaxes())

while True:
	time.sleep(0.5)
	os.system("clear")
	print(controller.get_axis(0), "\n")
	print(controller.get_axis(1), "\n")
	print(controller.get_axis(2), "\n")
	print(controller.get_axis(3), "\n")
	print(controller.get_axis(4), "\n")
	print(controller.get_axis(5), "\n")
