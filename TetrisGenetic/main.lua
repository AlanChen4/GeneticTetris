package.path = package.path .. ";../?.lua"
require 'lua.ga'

package.path = package.path .. ";../?.lua"
require 'lua.game_helper'


function main()
    -- sleep after start is pressed to wait for everything to load
    press_start()
    tetris_sleep()

    emu.speedmode('maximum')

    local selection_rate = 0.5
    local mutation_rate = 0.02

    local generation_limit = 5 
    local generation_count = 1
    local move_limit = 250

    local population_size = 4
    local children_size = math.floor(population_size * .5)

    -- generate initial population
    local population = init_population(population_size, move_limit)

    -- move onto generation 1 and continue until limit
    while (generation_count <= generation_limit) do
        -- compute fitness of population and add as attribute
        population = get_population_fitness(population, move_limit, generation_count)

        -- select parents with better fitness as mating pool
        local parents = get_mating_pool(population, selection_rate)

        -- crossover
        local offspring_crossover = crossover(parents, children_size)

        -- mutation
        local offspring_mutation = mutation(offspring_crossover, mutation_rate)

        -- replace population with offspring
        population = create_new_population(parents, offspring_mutation)
        
        print('[New Generation]: ' .. generation_count)
        generation_count = generation_count + 1
    end

    -- print results of best genome in final population
    print('[COMPLETE] Final Generation')
    print(population)  
end

main()

