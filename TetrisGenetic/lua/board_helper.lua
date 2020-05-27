-- reads information on the tetris board

board_start = 0x0400
board_end = 0x04C7
row_count = 20
col_count = 10


function init_board()
    return {
        field = {{}},
        col_height = {},
        aggregate_height = 0,
        complete_lines = 0,
        holes = 0,
        bumpiness = 0
    }
end

-- TODO: finish this function
function get_field()
    local field = {{}}
    local current_field_addr = board_start

    for row = 1, row_count do
        field[row] = {}
        for col = 1, col_count do
            local spot = memory.readbyte(current_field_addr)
            -- 239 means empty cell
            field[row][col] = (cell == 239) and 0 or 1
            current_field_addr = current_field_addr + 1
        end
    end
    current_field_addr = board_start
end


function get_holes(board)
end


function get col_height(board)
end


function get_aggregate_height(col_heights)
end


function get_bumpiness(col_heights)
end


function get_complete_lines(board)
end


function get_hueristics(playfield)
end


function get_reward(playfield, a, b, c, d)
    -- get reward based get_hueristics
end

