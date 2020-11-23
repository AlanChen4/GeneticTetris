package.path = package.path .. ";../?.lua"
require('lua.tetris_helper')

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
        print(individual)
    end
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
    return fitness
end


-- creates deep copy of table, or other data type
function deepcopy(data)
    local data_type = type(data)
    local copy
    if data_type == 'table' then
        copy = {}

        -- "pairs" function (used to iterate through Lua table)
        for key, value in next, data, nil do
            copy[deepcopy(key)] = deepcopy(data)
        end
    else
        copy = data
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