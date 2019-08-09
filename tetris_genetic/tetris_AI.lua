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


-- uses tetris score as fitness function
function get_fitness()
  -- get_score is not to be confused with the score used to make decisions
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


-- record weights to game_state/lua_weights.txt
function record_weights(height, line, hole, bump)
  local weights_file = io.open('py_helpers/game_state/lua_weights.txt', 'w')
  local weight_info = height .. " " .. lines .. " " .. hole .. " "  .. bump

  io.output(weights_file)
  io.write(weight_info)
  io.close(weights_file)
end

-- get decision based on weights
function get_decision(height_w, lines_w, holes_w, bump_w)

  -- weights used
  height_weight = height_w
  lines_weight = lines_w
  holes_weight = holes_w
  bump_weight = bump_w

  record_weights(height_weight, lines_weight, holes_weight, bump_weight)

  -- heuristic information
  TOTAL_HEIGHT = game_status['height']
  LINES_CLEARED = game_status['lines_cleared']
  TOTAL_HOLES = game_status['holes']
  TOTAL_BUMPS = game_status['bumps']

  -- weights multiplied by conditional variables
  THe = height_weight * TOTAL_HEIGHT
  LCl = lines_weight * LINES_CLEARED
  THo = holes_weight * TOTAL_HOLES
  TBu = bump_weight * TOTAL_BUMPS

  -- decision function
  SCORE = THe + LCl + THo + TBu
end


function main()
  press_start()
  tetris_sleep()
  while true do
    update_info()
    -- get_decision()
    emu.frameadvance()
  end
end

main()
