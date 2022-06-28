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
The hill climber first makes with the random algoritmme a solution. The quality of this solution gets calculated. Then it takes a random track from the solution and changes this with another random track and swaps this track with the track that got taken out of the solution. The quality of the new solution gets calulated, if the quality is higher than the quality from the first solution, the solution gets replaced with the new one. The algorithm does this a certain amount of times.

## Greedy
Instead of taking a random solution it creates a solution with the greedy algorithm. The track that is swapped is also created with the greedy algorithm.

# Simulated annealing
The simulated annealing algorithm is also based on the hill climber. But instead of taking always the option with the highest quality it sometimes also accept solution that have a lower quality. This could make sure it does not stay in a local optimum.





