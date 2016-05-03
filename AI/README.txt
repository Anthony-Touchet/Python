Locate the Repo:
	The Project holding AStar is in a repository containing other work. This happened because of poor early choices. The following link will take you straight to the project will all the appropriate files: https://github.com/atouchetAIE/Python/tree/master/AI . For a more step by step guide, here are the following steps: 
	1.Go to www.github.com
	2.Search for atouchetAIE
	3.Go to the repositories and click on the “Python” repository.
	4.Then, Click the folder for “AI”
	5.All the code is there. The run.bat file can be used as an executable
	6.node.py is the classes and astar.py can be considered the main program that runs it.

The A* Algorithm:
	The A* algorithm is used to find a path that has an efficient cost to get to it. This algorithm will not find the least costly path, but it will also not take unnecessary turns or detours. Let me break it into parts.
	
	Parts: The algorithm will need the following items:
		1.A search space, in this case the program will have nested lists with nodes in them.
		2.A list for closed nodes that the program have already visited.
		3.A list for open nodes that the program can go to.
		4.A starting node and an ending node.
		5.Lastly the program will need a current kind of node that will be changing throughout this algorithm. 
	
	Nodes: Each node will have three costs: one that will calculate the cost to the goal (H), one that will calculate how much it costs to go to its parent(G), and one that will be the sum of the previous two costs(F). Simply put: F = G + H. Lastly, the node will have to have a variable that states if it is walkable or not.

	Functions: Next, the program will need the following Functions for the ALgorithm itself.
		Finding Adjacent Nodes - This function will have to find any node that is adjacent to another node. This is to identify what nodes are around the node the program is searching around and seeing what nodes the program can walk to. Will also check if the node is even walkable.

		Calculating the H value - In this implementation, the H value is more like a guess. Yet we can still do math to figure out how close we are to the goal. This Number will help filter what node is chosen so the whole grid is not checked. This function will also have to update that node’s F once done.

		Calculating the G value - This function will be more rooted in logic. This function should be similar to the previous function for calculating H. The only difference is how the cost is calculated. In this implementation, diagonal nodes will have a cost of 14 while all others will have a cost of 10. This function will also have to update that node’s F once done.

		Finding the Lowest F cost - This function is more of a sorting problem. In this implementation, I made my own kind of searching algorithm. I just keeps the first lowest cost it can find until it finds one that has a lower cost. In this case, those costs will be the F costs of nodes in a list.

		Starting the Program - The way this code is structured requires jump starting the algorithm before other math is done. What this function will do is set the current node to the starting node and put that node on the open list. Then, the program will find all adjacent nodes, put them on the open list, and calculate the nodes’ G scores and H scores which will in turn update the F scores for those nodes. Once done, the program will take the current node off the open list and put it on the closed list.

	A* Algorithm:
		The program will first run the start function, setting up the rest of the algorithm. The following are the steps that are in a while loop stating that if there are no nodes in the open list, stop.

		1.Use the Find Lowest F Function and use the open list as you list to search through.
		2.Set that lowest F node you find to the current node
		3.Remove the current node from the open list and put it on the closed list.
		4.Find the surrounding nodes of the current node and set it equal to a list.
		5.(This step can be done in a variety of places but I believe this is where it is most useful) Check to see if the current node is the goal or if the goal is on the open list, if true, return true.
		6.Next, the program will loop through all of the adjacent nodes and do calculations on them:
		7.In the loop, the program will ask if it is in the closed list, if so skip this node, else continue.
		8.If the node is not in the open list, the program will set the node’s parent to the current node, Calculate the G cost and the H cost, and add that node to the open list.
		9.Else, if the node is already on the open list, the program will do some math. The program will calculate the G score to get from the current node to that node, add the current Node’s G, and set that number to a variable. The program will then ask, is this number less than the G cost of this node. If true, the program will set that Node’s parent to the current node and calculate the G and the H scores.
		10.This last step is for if the goal has not been found and the while loop for the algorithm breaks. If the while loop breaks or finishes and true is not returned, return false.

	Drawing the Results:
		In this Project, the file astar.py is mainly responsible for drawing the results to the screen and closing the progrm. This file will mark all closed nodes as dark blue, open nodes as green, impassable nodes as red, the start as light blue, and the goal as purple. The Screen will also draw a line to the parent of the node if the node has a parent. Lastly, if the project fails to find a path, a Grey line will be drawn from the top left corner to the bottom right corner. Else, a grey line will trace the path of parents from the goal back to the start.
