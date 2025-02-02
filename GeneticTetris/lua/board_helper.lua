BOARD_START = 0x0400
BOARD_END = 0x04C7
ROW_COUNT = 20
COL_COUNT = 10


function init_board()
    return {
        ['field'] = {{}},
        ['col_height'] = {},
        ['aggregate_height'] = 0,
        ['complete_lines'] = 0,
        ['holes'] = 0,
        ['bumpiness'] = 0
    }
end


function get_field()
    local field = {{}}
    local current_field_addr = BOARD_START

    for row = 1, ROW_COUNT do
        field[row] = {}
        for col = 1, COL_COUNT do
            local cell = memory.readbyte(current_field_addr)
            -- 239 means empty cell
            field[row][col] = (cell == 239) and 0 or 1
            current_field_addr = current_field_addr + 1
        end
    end
    current_field_addr = BOARD_START
    return field
end


function fields_equal(one, two)
    -- returns true if field one is equal to field two
    for i = 1, ROW_COUNT do
        for j = 1, COL_COUNT do
            if (one[i][j] ~= two[i][j]) then
                return false
            end
        end
    end
    return true
end


function get_holes_and_col_heights(field)
    local holes = 0
    local col_heights = {}

    -- initialize the col_heights array
    for i = 1, COL_COUNT do 
        col_heights[i] = 0
    end

    -- go through each cell, checking for hole/height
    for row = 1, ROW_COUNT do
        for col = 1, COL_COUNT do
            local cell = field[row][col]

            -- empty cell: check for hole
            if (cell == 0) then
                if (row > 1) and (col_heights[col] > 0) then
                    holes = holes + 1
                end

            -- not empty: get col height 
            else
                if (col_heights[col] == 0 and row > 1) then
                    col_heights[col] = 21 - row
                end
            end
        end
    end
    
    return {holes, col_heights}
end


function get_aggregate_height(col_heights)
    local aggregate_height = 0
    for i = 1, COL_COUNT do
        aggregate_height = aggregate_height + col_heights[i]
    end
    return aggregate_height
end


function get_bumpiness(col_heights)
    local bump = 0
    for i = 1, COL_COUNT - 1 do
        bump = bump + math.abs(col_heights[i] - col_heights[i+1])
    end
    return bump
end


function get_complete_lines(field)
    local comp_lines = 0
    for row = 1, ROW_COUNT do
        for col = 1, COL_COUNT do
            local cell = field[row][col]
            if (cell == 0) then
                break
            end
            if (cell == 1 and col == num_cols) then
                comp_lines = comp_lines + 1
            end
        end
    end
    return comp_lines
end


function get_hueristics(board)
    board.holes, board.col_heights = unpack(get_holes_and_col_heights(board.field))
    board.complete_lines = get_complete_lines(board.field)
    board.aggregate_height = get_aggregate_height(board.col_heights)
    board.bumpiness = get_bumpiness(board.col_heights)

    return board
end


function get_reward(board, a, b, c, d)
    -- get reward based get_hueristics
    return (a * board.aggregate_height) +
           (b * board.complete_lines) +
           (c * board.holes) +
           (d * board.bumpiness)
end


-- debugging functions below --

function print_field(field)
    print('printing field')
    for row = 1, ROW_COUNT do
        print(field[row])
    end
end


function print_heuristics(playfield)
  print("\nCol Heights")
  print(playfield.col_heights)

  print("\nHoles")
  print(playfield.holes)

  print("\nAggregate Height")
  print(playfield.aggregate_height)

  print("\nBumpiness")
  print(playfield.bumpiness)

  print("\nComplete Lines")
  print(playfield.complete_lines)
end
