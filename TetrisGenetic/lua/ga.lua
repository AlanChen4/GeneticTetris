package.path = package.path .. ";../?.lua"
require('lua.game_helper')
require('lua.piece_helper')

require('math')
require('table')

-- generates initial population
function init_population(size, move_limit)
    population = {}
    for i = 1, size do
        -- TODO: generate genes and create chromosome
        local individual = {
            math.random()*randomNegative(),
            math.random()*randomNegative(),
            math.random()*randomNegative(),
            math.random()*randomNegative()
        }
        table.insert(population, individual)
    end
    print('Generated initial population')
    return population
end


function get_population_fitness(population, move_limit, generation)
    local temp_population = deepcopy(population)
    for i = 1, #temp_population do
        -- get fitness
        if (not temp_population[i].fitness) then
           temp_population[i].fitness = play_game(temp_population[i], move_limit)
       end
   end
   return temp_population
end


function play_game(chromosome, move_limit)
    for i = 1, move_limit do

    end
    return get_score()
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


-- returns 50/50 chance of negative multiplier
function randomNegative()
    local num = math.random()
    if num > 0.5 then
        return 1
    end
    return -1
end