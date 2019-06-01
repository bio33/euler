import math
def get_ways(rows,seed,color):
    print("ways for "+color+"\n")
    temp_count = 0
    for color_tiles in range(seed,rows+1,seed):
        black_tiles = rows - color_tiles
        color_tiles_count = color_tiles//seed
        ways = math.factorial(black_tiles + color_tiles_count)//(math.factorial(color_tiles_count)*math.factorial(black_tiles))
        print("{0} {1} {2}".format(color_tiles, color, ways))
        temp_count += ways
    return temp_count


# take input n
rows = int(input())

red = get_ways(rows,2,"red")
green = get_ways(rows,3,"green")
blue = get_ways(rows,4,"blue")

print("total ways : " + str(red+green+blue))