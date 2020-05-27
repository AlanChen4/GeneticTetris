package.path = package.path .. ";../?.lua"
require 'lua.board_helper'

package.path = package.path .. ";../?.lua"
require 'lua.tetris_helper'


function test()
    press_start()
    while true do
        get_field()
        tetris_sleep()
    end
end

test()
