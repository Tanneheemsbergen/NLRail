We will discuss our algorithms here:

For all our algorithms the following track stops are applied:
- If there are no stations accessible from the current station, that track stops.
- If moving to a next station would mean that the total time, the move is not made, and the track stops.

# Random
Our first algorithm, and the algorithm we used as our baseline is random. Random picks a random station as a begin station. From this beginning station, the algorithm looks at the possible stations that can be 'accessed' through the starting station. From the options, the algorithm chooses a random station to be the next station. This only happens if the track stops did not happen. In a track, a connection will never be ridden more than once. 
This is done seven times, and when that is done, the K-value will be calculated.

# Greedy
Our greedy algorithm is slighty different than our random algorithm. Instead of picking the next station randomly, it picks the station that is the closest (has the smallest distance). In this algorithm, each solution has 7 different tracks. In our random algorithm, each track was unique, but in greedy, every solution is unique. 
Because of the formula, a higher percentage of travelled connections and a lower total amount of minutes leads to a higher K-value. By our greedy algorithm choosing the shortest route, and thus the lowest minutes, we thought we could optimize the p, while minimizing the Min.

# Hillclimber
## Random

## Greedy


# First-option



# AI

