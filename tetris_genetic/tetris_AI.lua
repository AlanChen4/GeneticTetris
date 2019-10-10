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


-- record weights to game_state/lua_weights.txt
function record_weights(height, line, hole, bump)
  local weights_file = io.open('py_helpers/game_state/lua_weights.txt', 'w')
  local weight_info = height .. " " .. lines .. " " .. hole .. " "  .. bump

  io.output(weights_file)
  io.write(weight_info)
  io.close(weights_file)
end

-- get decision based on weights
function get_decision()
  -- local decision_file = io.open('py_helpers/game_state/AI_decision.txt', 'w')


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
