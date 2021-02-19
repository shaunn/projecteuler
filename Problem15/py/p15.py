# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
#
# How many such routes are there through a 20×20 grid?
#
# ----
#
# Strategy
#
# - Starting from an origin point (x,y) represented by (0,0)
# - Identify the endpoint (x+end,y+end) represented in the example as (1,1)
# - (1,1) represents the end of a 2x2 grid assuming (0,0) is the origin
# - Iterate through a combination of choices to either go right or down through each iteration
# - ? Start with the most expensive path from (0,0) to (x+end,y+end)? and work backwards?


def main():
    print("init")



if __name__ == "__main__":
    main()
