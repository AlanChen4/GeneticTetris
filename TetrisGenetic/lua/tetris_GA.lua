require('lua_helper')

-- generates initial population
function init_population(size, move_limit)
    population = {}
    for i = 1, size do
        -- TODO: generate genes and create chromosome
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
