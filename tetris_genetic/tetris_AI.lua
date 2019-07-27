require 'tetris_controls'
-- require 'tetris_copy'
require 'tetris_genetic'

-- weights used
height_weight = 0
lines_weight = 0
holes_weight = 0
bump_weight = 0

-- weights multiplied by conditional variables
THe = height_weight * TOTAL_HEIGHT
LCl = lines_weight * LINES_CLEARED
THo = holes_weight * TOTAL_HOLES
TBu = bump_weight * TOTAL_BUMPS

-- score function
SCORE = THe + LCl + THo + TBu

function init_env()
  env = init_board()
end


-- creates random set of weights
function new_chromosome()
  local chromosome = {}
  for i = 1, 4 do 
    -- random weight between -1 and 1
    chromosome[i] = (math.random()*2)-1
  end
  return chromosome
end


-- uses tetris score as fitness function
function get_fitness()
  return get_score()
end

function new_population()
  local population = {}
  for i = 1, 16 do
    population[i] = new_chromosome()
  end
end


function selection()
  -- body
end


function crossover()
  -- body
end


function main()
  press_start()
  tetris_sleep()
  while true do
    get_screen()
    emu.frameadvance()
  end
end

main()
