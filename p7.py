# p7 wapp to gen the follow:
#  *
#  *	*
#  *	*	*
#  *	*	*	*
# where number of lines to be gen, is given by user

num = int(input(" enter a number of lines"))
if num < 0:
	print("invalid input")
else:
	for i in range(1, num+1):
		print(i * " *\t ") # for more space type " *\t"