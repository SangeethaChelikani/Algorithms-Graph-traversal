import sys

# Read cmd-line args to fetch the file i/o
file_in, file_out = sys.argv[1], sys.argv[2]


# Read lines from the file
with open(file_in, 'r') as f:
    lines = f.readlines()


# Transform to adjacency matrix
rows, cols = 0, 0
grid = []
ctr = 0
# extracted first line for rows and columns values
x, y = lines[0].split()
rows, cols = int(x), int(y)
for line in lines[1:]:
    row = line.split()
    row[cols - 1] = row[cols - 1].rstrip()
    grid.append(row)

# create a visited matrix to flag the visits
visited = [[0 for i in range(cols)] for j in range(rows)]

# moving pointers returns path values


def movements(val):
    if val == "N":
        return (0, -1)
    elif val == "S":
        return (0, 1)
    elif val == "E":
        return (1, 0)
    elif val == "W":
        return (-1, 0)
    elif val == "NE":
        return (1, -1)
    elif val == "NW":
        return (-1, -1)
    elif val == "SE":
        return (1, 1)
    elif val == "SW":
        return (-1, 1)


# starts from left top corner
init_node = grid[0][0]
cur_x = 0
cur_y = 0


# list to store nodes
lst = []
for i in range(0, rows-1):
    # fetch the direction from init_node
    dir = init_node.split('-')[1]
    # fetch the color and proceed with move
    color = init_node.split('-')[0]
    cur_x += movements(dir)[1]
    cur_y += movements(dir)[0]
    # not visited and next position has alternate color
    if visited[cur_x][cur_y] == 0 and (grid[cur_x][cur_y]).split('-')[0] != color:
        # mark visited
        visited[cur_x][cur_y] = 1
        # add to  list
        lst.append([cur_x, cur_y, str(i+1) + dir])


# found variable to break the loop if found
found = False
while lst and not found:
    # fetch last element from the list
    element = lst.pop()
    cur_x = element[0]
    cur_y = element[1]
    # retrieving the node
    node = grid[cur_x][cur_y]
    for i in range(0, rows):
        # if the node is bullseye node, break the loop
        if node == 'O':
            found = True
            break
        # fetch the direction from init_node
        dir = node.split('-')[1]
        # fetch the color and proceed with move
        color = node.split('-')[0]
        cur_x += movements(dir)[1]
        cur_y += movements(dir)[0]
        # valid postions only
        if not (cur_x < 0 or cur_y < 0 or cur_x >= len(grid) or cur_y >= len(grid[0])):
            # if the position is not the same color and it is not visited yet
            if grid[cur_x][cur_y].split('-')[0] != color and visited[cur_x][cur_y] == 0:
                # mark it visited
                visited[cur_x][cur_y] = 1
                lst.append([cur_x, cur_y, element[2] + " " + str(i+1) + dir])
        else:
            break

# write result to output file
output = element[2].lstrip()  # remove leading spaces
out_file = open(file_out, "w")
out_file.write(output)
out_file.close()
