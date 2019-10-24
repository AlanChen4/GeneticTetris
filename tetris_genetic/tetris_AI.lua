require 'tetris_controls'


-- creates environment
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


function new_population()
  local population = {}
  for i = 1, 16 do
    population[i] = new_chromosome()
  end
end


-- uses get_fitness as the evaluation for candidate solution
function get_fitness()
  return get_score()
end


function selection()
  -- body
end


function crossover()
  -- body
end


function mutation()
  -- body
end


function replacement()
  -- body
end


function get_decision()


end


function main()
  press_start()
  tetris_sleep()
  while true do
    update_info()
    get_decision()
    emu.frameadvance()
  end
end

main()
