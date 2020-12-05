# GeneticTetris
A genetic algorithm that learns how to beat the 1989 version of Tetris. 

![demo](GeneticTetris/img/demo.gif)
Recording is the result of multiple generations of gameplay, eventually yielding chromosome {-0.50, 0.79, -0.37, -0.18} (See implementation section for more detail)

## Background for Genetic Algorithms

![ga diagram](GeneticTetris/img/ga.png)

For more information about genetic algorithms, check out [this](http://mat.uab.cat/~alseda/MasterOpt/Beasley93GA1.pdf) paper.

## Implementation for Tetris

### Chromosomes
Chromosomes were represented by four weights: aggregate height, completed lines, number of holes, and overall bumpiness. For instance, a chromosome represented by {-0.50, 0.79, -0.37, -0.18} would indicate an aggregate height weight of -0.5, completed lines weight of 0.79, holes weight of -0.37, and bumpiness weight of -0.18.

Aggregate height was calculated by summing the heights of each column. The number of completed lines is found by recording how many lines would be cleared if a piece was dropped in a specific location. Number of holes is the number of empty wells covered by a piece. Bumpiness was determined by finding absolute value differences in height between the columns. 

### Reward Function
```
Reward = (a * aggregate height) + (b * completed lines) + (c * number of holes) + (d * overall bumpiness)
```
Variables a, b, c, and d are the weights that each generation is manipulating in attempt to optimize the overall fitness.

The reward was found for every possible location and permutation that a piece could be placed. Essentially, each individual in the population would try to find the best possible move according to the weights in their chromosome. 

### Fitness
Fitness was represented by the score of the game once the game was lost, or when the move limit was reached. 

## Installation

[FCEUX](http://fceux.com/web/home.html) is an emulator that supports Nintendo Entertainment  System (NES) along with other consoles. FCEUX is used as an environment to run the Lua code and is necessary in order to run the genetic algorithm. 

FCEUX downloads can be found [here](http://fceux.com/web/download.html). FCEUX will also have to be added to the path so it can be called from the command line.


## Usage

To run the genetic algorithm, run the main.py file within the GeneticTetris folder.
```bash
python main.py 
```
Running main.py will then run main.lua within the FCEUX emulator.


## License
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
