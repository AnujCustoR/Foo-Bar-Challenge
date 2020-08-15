'''
Bringing a Gun to a Guard Fight
===============================

Uh-oh - you've been cornered by one of Commander Lambdas elite guards! Fortunately, you grabbed a beam weapon from an abandoned guard post while you were running through the station, so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the elite guard: its beams reflect off walls, meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either you or the guard, it will stop immediately (albeit painfully). 

Write a function solution(dimensions, your_position, guard_position, distance) that gives an array of 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers of the guard's x and y coordinates in the room, and returns an integer of the number of distinct directions that you can fire to hit the elite guard, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite guard are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with dimensions [3, 2], your_position [1, 1], guard_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite guard (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite guard with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite guard with a total shot distance of sqrt(5).

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases --
Input:
Solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
Solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9

-- Python cases --
Input:
solution.solution([3,2], [1,1], [2,1], 4)
Output:
    7

Input:
solution.solution([300,275], [150,150], [185,100], 500)
Output:
    9
'''

import math

def mirror_atlas(node, dimensions, distance):
    node_mirrored = []
    for i in range(len(node)):
        points = []
        for j in range(-(distance//dimensions[i])-1, (distance//dimensions[i]+2)):
            points.append(get_mirror(j, node[i], dimensions[i]))
        node_mirrored.append(points)
    return node_mirrored


def get_mirror(mirror, coordinates, dimensions):
    res = coordinates
    mirror_rotation = [2*coordinates, 2*(dimensions-coordinates)]
    if(mirror < 0):
        for i in range(mirror, 0):
            res -= mirror_rotation[(i+1) % 2]
    else:
        for i in range(mirror, 0, -1):
            res += mirror_rotation[i % 2]
    return res


def solution(dimensions, your_position, guard_position, distance):
    mirrored = [mirror_atlas(your_position, dimensions,
                             distance), mirror_atlas(guard_position, dimensions, distance)]
    res = set()
    angles_dist = {}
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam = math.atan2((your_position[1]-k), (your_position[0]-j))
                l = math.sqrt((your_position[0]-j)**2 + (your_position[1]-k)**2)
                if [j, k] != your_position and distance >= l:
                    if((beam in angles_dist and angles_dist[beam] > l) or beam not in angles_dist):
                        if i == 0:
                            angles_dist[beam] = l
                        else:
                            angles_dist[beam] = l
                            res.add(beam)
    return len(res)



'''
Solution Explaination:
https://github.com/bezzad/foobar.withgoogle/blob/master/4.3%20Bringing%20a%20Gun%20to%20a%20Guard%20Fight/solution.py
'''