from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        
        visited = []
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]    
        dest = (destination[0],destination[1])
        
        def rollFrom(pos):
            #check all possible stop positions that current pos can roll to
            #and exclude those that are already in visited 
            #and then keep rolling from the rest
            #print("rolling from {}".format(pos))
            newStops = []
            for d in dirs:
                newX = pos[0]
                newY = pos[1]
                while(True): #rolling
                    possibleNewX = newX + d[0] 
                    possibleNewY = newY + d[1]                     
                    if (possibleNewX >= 0 and possibleNewX < len(maze) ) and (possibleNewY >= 0 and possibleNewY < len(maze[0])) and (maze[possibleNewX][possibleNewY] != 1):
                        newX = possibleNewX
                        newY = possibleNewY
                        continue
                    else:
                        break
                newStop = (newX, newY)
                if newStop == dest:
                    return True
                newStops.append(newStop)
                
            visited.append(pos)
                
            for newStop in newStops:            
                if newStop not in visited:
                    if rollFrom(newStop):
                        return True                
            return False
            
        startPos = (start[0], start[1])        
        return rollFrom(startPos)

if __name__ =="__main__":
    s = Solution()
    #example1
    maze1 =[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start1= [0,4]
    des1 =[4,4]
    print(s.hasPath(maze1,start1,des1))


   #example2
    maze2 =[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]
    start2= [0,4]
    des2 =[3,2]
    print(s.hasPath(maze2,start2,des2))
    

    #example3
    maze3 =[[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]
    start3= [4,3]
    des3 =[0,1]


    print(s.hasPath(maze3,start3,des3))

