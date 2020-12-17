Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

Turns out this problem couldn't be simpler (well, it could if you're unfamiliar with the combinations operator in mathematics).

To get to the opposite corner of an nxn grid, you have to go down n times and right n times, so you move a total of 2n times, half of which are right, so simply work out how many different ways you can arrange that with C(2n,n).
