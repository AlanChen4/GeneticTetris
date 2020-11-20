package.path = package.path .. ";../?.lua"
require 'lua.ga'

package.path = package.path .. ";../?.lua"
require 'lua.tetris_helper'


function main()
    -- sleep after start is pressed to wait for everything to load
    press_start()
    tetris_sleep()


    local selection_rate = 0.5
    local mutation_rate = 0.02

    local generation_limit = 0 
    local generation = 0
    local move_limit = 250

    local population_size = 50
    local children_size = math.floor(population_size * .5)

    -- TODO: generate initial population
    local population = init_population(population_size, move_limit)

    -- TODO: compute fitness of initial population
 
    -- TODO: move onto generation 1 and continue until limit
    while (generation <= generation_limit) do
        local children = {}
        for i = 1, children_size do
            -- TODO: select genomes and sort by fitness
            -- TODO: crossover and add child to children
        end
        
        -- TODO: replace least fit with new children
        for i = 1, children_size do
        end

        -- TODO: sort population by fitness
        
        print('generation: ' .. generation)
        print(population[#population])  
        generation = generation + 1
    end

    -- print results of best genome in final population
    print('FITTEST GENOME:')
    print(population[#population])  
end

main()

