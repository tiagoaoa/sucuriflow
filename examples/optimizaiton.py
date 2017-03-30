from pyDF import *

def op1(input1):
#	print "Op 1"
	return 9

def op2(intput):
#	print "Op 2"
	return 2

def op3(intput):
#	print "Op 3"
	return 1



def assist(args):
	print "Solution %s" %args
	
	if args[1] < args[0] or args[0] < 0:
		return args[1]
	else:
		return args[0]


graph = DFGraph()

ini = Feeder(-1)
ini2 = Feeder(-2)



heur1 = Node(op1, 1)
heur2 = Node(op2, 1)
heur3 = Node(op3, 1)


assist1 = Node(assist, 2)
assist1.pin(0)

for i in range(1,4):
	graph.add(eval("heur%d" %i ))
graph.add(ini)
graph.add(ini2)

graph.add(assist1)

heur1.add_edge(assist1, 1)
heur2.add_edge(assist1, 1)
heur3.add_edge(assist1, 1)

assist1.add_edge(heur1, 0)
assist1.add_edge(heur2, 0)
assist1.add_edge(heur3, 0)
assist1.add_edge(assist1, 0)
ini.add_edge(heur1, 0)
ini.add_edge(heur2, 0)
ini.add_edge(heur3, 0)
ini.add_edge(assist1, 0)

ini2.add_edge(assist1, 1)

print len(ini.inport)
sched = Scheduler(graph, 5, mpi_enabled = False)
sched.start()