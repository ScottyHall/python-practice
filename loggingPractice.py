# logging module practice
import logging
import math

# allows writing status messages to file or string

# Levels:
# debug		10
# info		20
# warning	30
# error		40
# critical	50

# logging module contains, all caps == constants, title items == classes, lowerCamelcase == methods

# basicConfig Method then create a logger with the 'getLogger' method

# configure the log message format
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

# create and configure a logger
logging.basicConfig(filename = "Lumberjack.log",
	level = logging.DEBUG,	# what messages to write
	format = LOG_FORMAT,	# format the output of each message
	filemode = 'w')			# write a new file each time
logger = logging.getLogger()

# create logger without a name. Known as the 'root logger'

#test the logger
#logger.info("Our first log message")

def quadratic_formula(a, b, c):
	"""Return the solutions to the equiation ax^2 + bx + c = 0."""
	logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

	# compute the discriminant
	logger.debug("# Compute the discriminant")
	disc = b**2 - 4*a*c

	# compute the two roots
	logger.debug("# Compute the two roots")
	root1 = (-b + math.sqrt(disc)) / (2*a)
	root2 = (-b - math.sqrt(disc)) / (2*a)

	# return the roots
	logger.debug("# Return the roots")
	return (root1, root2)

roots = quadratic_formula(1, 0, -4)
print(roots)




