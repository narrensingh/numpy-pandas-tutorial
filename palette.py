import numpy as np
## the thing is i can use an array of indexes to access the objects from another array
palette = np.array([[0, 0, 0],         # black
                    [255, 0, 0],       # red
                    [0, 255, 0],       # green
                    [0, 0, 255],       # blue
                    [255, 255, 255]])  # white

images = np.array([[[[0,1,2],[2,3,4],[4,3,2]],[[3,4,2],[2,3,4],[0,3,2]],[[3,4,2],[4,3,2],[2,3,4]]],[[[0,1,2],[2,3,4],[4,3,2]],[[3,4,2],[2,3,4],[0,3,2]],[[3,4,2],[4,3,2],[2,3,4]]],[[[0,1,2],[2,3,4],[4,3,2]],[[3,4,2],[2,3,4],[0,3,2]],[[3,4,2],[4,3,2],[2,3,4]]]]) #simple random image collection of colors from the palette

## bareborn image 

# # # ---> []
# # # ---> []
# # # ---> []
# each # --> rgb code
print(images.ndim)
print(palette[images].ndim)
# we can excape the for loop thing from this array of indixes we can use
a = np.arange(12)
a.resize((3,4))
print(a)
j = np.array([[0,1],[2,2]])
i = np.array([[2,2],[1,1]])
print(a[i,j])
print(a[i,2])
print(a.ravel())