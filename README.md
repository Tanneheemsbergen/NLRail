# NLRail

# Case
Public transport is a fast and convenient way to travel. However, due to the many routes a train can take, the rail route map gets complex. 

In this project, we tried to find the set of trajects for intercity trains, that connects the stations in North- and South Holland, as well as for the entire Netherlands, as efficient as possible.

We started by looking at North- and South Holland, which we will refer to as Holland continuing. For Holland, we got the 22 most important stations, and their 28 connections. With a time limit of 120 minutes, and a maximum of 7 trajects, we tried to create a set of routes.

After looking at Holland, we looked at the entire Netherlands, which will be referred to as Nationaal. For Nationaal, we got a time constraint of 180 minutes, and 20 as a maxumim of trajects.

Our goals for both Holland and Nationaal was to create a set of trajects (called a solution) that result in a high quality road map.


# Quality of a solution
To measure the quality of a solution, we received a score function. This score function can be found beneath. 
K = p * 10.000 (T*100 - min)
K = quality of route set
p = fraction of used connections (between 0 and 1)
T = amount of routes
min = total amount of minutes used in all routes
The idea is, to get the K-value as high as possible.


# Getting Started
The code is written in Python 3.8.10. In requirements.txt all the packages required for running the code can be found. To get these, run:
pip install requirements.txt


# Structure
In the csvfiles folder, the csv files can be found. There are 4 files, namely:
- ConnectiesHolland; here the 29 connections between stations in Holland can be found.
- ConnectiesNationaal; here the 89 connections between stations in Nationaal can be found.
- StationsHolland; contains the 22 important stations in Holland.
- StationsNationaal; contains the 61 important stations in Nationaal

The functions folder contains: 
- The algorithms folder, this contains all algorithms used. More information about these can be found in this folder.
- The classes folder, this contains the graph and the station classes.
- Lastly, the helpers folder, here the calculation, visualisation and check50 files can be found.

In the result-picture folder, all the pictures that are made while running this code. 


# Using
To run our code you have to give several instructions in the command line:
python3 main.py {space} {algorithm} {iterations}:
- The space can be Holland, or Nationaal,
- The algorithm can be 'r' (random), 'g' (greedy), 'df' (depth-first), 'hc' (hillclimber), 'hcg' (hillclimber greedy),
- Iterations can be anything, if it is one, a traject representation will be made, and if it is more than one, a histogram will be made. Both of these will be stored in the Result-picture folder.


# Authors
Charlotte Hoffmans, Tanne Heemsbergen, Debby Bouma


# Acknowledgements
Minor Programmeren at the Universiteit van Amsterdam.
