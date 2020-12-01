package.path = package.path .. ";../?.lua"
require('lua.board_helper')
require('lua.game_helper')
require('lua.piece_helper')

require('math')
require('table')

-- generates initial population
function init_population(size, move_limit)
    population = {}

    -- initialize and warm random
    math.randomseed(os.time())
    math.random();math.random();math.random();

    for i = 1, size do
        -- generate genes and create chromosome

        -- genes with negative multiplier indicate things that 
        -- should be minimized, such as number of holes
        local individual = {
            math.random() * -1, -- aggregate height
            math.random(), -- complete lines
            math.random() * -1 , -- holes
            math.random() * -1  -- bumpiness
        }
        table.insert(population, individual)
    end
    print('[Generated initial population] ' .. size .. ' Individuals')
    return population
end


function get_population_fitness(population, move_limit, generation)
    local temp_population = deepcopy(population)
    for i = 1, #temp_population do
        -- get fitness
        if (not temp_population[i].fitness) then
           temp_population[i].fitness = play_game(temp_population[i], move_limit)
           print('[Finished] Individual #' .. i .. ' Fitness: ' .. temp_population[i].fitness)
       end
   end
   return temp_population
end


function play_game(chromosome, move_limit)
    is_game_over = false 
    pre_state = savestate.create(2)
    savestate.save(pre_state)

    for i = 1, move_limit do
        local best_action_score = -1000000
        local best_action = {
            ['turns'] = 0,
            ['left'] = 0,
            ['right'] = 0
        }
        local og_state = savestate.create(1)
        savestate.save(og_state)

        local curr_piece = get_curr_piece()
        local turns = turns_needed(curr_piece)
        local right_moves, left_moves = moves_needed(curr_piece) 

        -- start over from beginning and move to next individual
        if is_game_over then
            fitness = get_score()
            savestate.load(pre_state)
            return fitness
        end

        -- left
        for move_count = left_moves, 1, -1 do
            for turn_count = 1, turns do
                -- move returns -1 when game is lost
                local move = do_action('left', turn_count, move_count)
                if move == -1 then
                    fitness = get_score()
                    savestate.load(pre_state)
                    return fitness
                end

                local board = init_board()
                board['field'] = get_field()
                local hueristics = get_hueristics(board)
                local score = get_reward(hueristics, 
                                chromosome[1],
                                chromosome[2],
                                chromosome[3],
                                chromosome[4]
                            )
                if score > best_action_score then
                    best_action_score = score
                    best_action = {
                        ['turns'] = move['turns'],
                        ['left'] = move['left'],
                        ['right'] = move['right']
                    }
                end
                savestate.load(og_state)
            end
        end

        -- middle
        for turn_count = 0, turns do
            -- move returns -1 when game is lost
            local move = do_action('middle', turn_count, 0)
            if move == -1 then
                fitness = get_score()
                savestate.load(pre_state)
                return fitness
            end

            local board = init_board()
            board['field'] = get_field()
            local hueristics = get_hueristics(board)
            local score = get_reward(hueristics, 
                            chromosome[1],
                            chromosome[2],
                            chromosome[3],
                            chromosome[4]
                        )
            if score > best_action_score then
                best_action_score = score
                best_action = {
                    ['turns'] = move['turns'],
                    ['left'] = move['left'],
                    ['right'] = move['right']
                }
            end
            savestate.load(og_state)
        end

        -- right
        for move_count = 1, right_moves do
            for turn_count = 1, turns do
                -- move returns -1 when game is lost
                local move = do_action('right', turn_count, move_count)
                if move == -1 then
                    fitness = get_score()
                    savestate.load(pre_state)
                    return fitness
                end

                local board = init_board()
                board['field'] = get_field()
                local hueristics = get_hueristics(board)
                local score = get_reward(hueristics, 
                                chromosome[1],
                                chromosome[2],
                                chromosome[3],
                                chromosome[4]
                            )
                if score > best_action_score then
                    best_action_score = score
                    best_action = {
                        ['turns'] = move['turns'],
                        ['left'] = move['left'],
                        ['right'] = move['right']
                    }
                end
                savestate.load(og_state)
            end
        end

        -- choose best action
        for i = 1, best_action['turns'] do
            rotate()
        end
        for i = 1, best_action['left'] do
            move_left()
        end
        for i = 1, best_action['right'] do
            move_right()
        end

        -- drop_down returns -1 when game is over
        if drop_down() == -1 then
            fitness = get_score()
            savestate.load(pre_state)
            return fitness
        end
    end

    -- return score of the game as fitness score once move limit is reached
    local fitness = get_score()
    savestate.load(pre_state)
    return fitness
end


-- assume game is over when spot in top row is filled
function game_over()
    local check = memory.readbyte(0x0400)
    if check ~= 239 then
        is_game_over = true
        return true
    end
    return false
end


function do_action(direction, turn_count, move_count)
    for t = 1, turn_count do
        rotate()
    end
    if direction ~= 'middle' then
        for m = 1, move_count do
            -- move sideways
            if direction == 'left' then
                move_left()
            else
                move_right()
            end
        end
    end

    -- drop down returns -1 when game is over
    if drop_down() == -1 then
        return -1
    end

    local left 
    local right

    if direction == 'left' then
        left = move_count
        right = 0
    else
        left = 0
        right = move_count
    end

    local action = {
        ['turns'] = turn_count,
        ['left'] = left,
        ['right'] = right
    }
    return action
end


function drop_down()
    local started = false
    local y_pos = memory.readbyte(0x0041)
    local piece_height = piece_heights[tonumber(memory.readbyte(0x0062))]
    while (y_pos ~= 0 or not started) do
        if y_pos > 1 then
            started = true
        end
        move_down()
        y_pos = memory.readbyte(0x0041) - piece_height
        if game_over() then
            return -1
        end
    end
end


function turns_needed(piece) 
    if piece == 'I' or piece == 'Z' or piece == 'S' then
        return 2
    end
    if piece == 'O' then
        return 1
    end
    return 4
end


function moves_needed(piece)
    if piece == 'Z' or piece == 'S' then
        return 3, 5 
    end
    if piece == 'O' then
        return 4, 4
    end
    return 4, 5
end


-- creates deep copy of data input
function deepcopy(orig)
    local orig_type = type(orig)
    local copy
    if orig_type == 'table' then
        copy = {}
        for orig_key, orig_value in next, orig, nil do
            copy[deepcopy(orig_key)] = deepcopy(orig_value)
        end
        setmetatable(copy, deepcopy(getmetatable(orig)))
    else -- number, string, boolean, etc
        copy = orig
    end
    return copy
end
