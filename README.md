# Worm Physics
This is worm/snake physics class for game devs working in Pygame. Pretty easy to use. Use for your Pygame game if you want to.

# How to use the class
## Inputs
The _Worm_ Class takes in 3 inputs:
* Starting Position (_start_pos_)
* Number of Nodes (_nodes_)
* Length of each segment (_length_)

### start_pos
The starting position of the worm. It's laid out in a straight line with the head node being at the starting position and the rest of the nodes being to the left of it.

### nodes
The number of nodes your worm has.

### length
The length of each segment of the worm.

## Functions
The _Worm_ Class has 2 functions:
* Drawing Function (_draw_)
* Update Node Position Function (_update_)

### draw(node_color, segment_color)
The drawing function of the worm. The _node_color_ and _segment_color_ parameters are the colors of the nodes and segments respectively.

### update(speed)
The update function of the worm which updates the position of the nodes when the head node moves. In this case, the _speed_ parameter is the speed in which the head node is moving at. Recommended to call this function at the end of your game loop.
