package.path = package.path .. ";../?.lua"
require 'lua.board_helper'

package.path = package.path .. ";../?.lua"
require 'lua.tetris_helper'


function test()
    press_start()
    while true do
        field = get_field()
        print(get_holes_and_col_heights(field))
        tetris_sleep()
    end
end

test()
