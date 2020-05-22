package.path = package.path .. ";../?.lua"
require 'lua.general_helper'

package.path = package.path .. ";../?.lua"
require 'lua.tetris_controls'

package.path = package.path .. ";../?.lua"
require 'lua.tetris_env'

function main()
    -- starts level
    press_start()

    -- generate initial population
    -- compute fitness
 
    -- repeat selection, crossover, mutation, & compute fitness
    -- stop once population converges
end

main()

