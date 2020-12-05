# GeneticTetris
A genetic algorithm that learns how to beat the 1989 version of Tetris. 

## Background for Genetic Algorithms

![ga diagram](GeneticTetris/img/ga.png)

For more information about genetic algorithms, check out [this](http://mat.uab.cat/~alseda/MasterOpt/Beasley93GA1.pdf) paper.

## Implementation for Tetris

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
