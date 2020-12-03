piece_addr = 0x0062

-- Memory address values of pieces:
  -- 00 - T Up
  -- 01 - T Right
  -- 02 - T Down
  -- 03 - T Left
  -- 04 - J Left
  -- 05 - J Up
  -- 06 - J Right
  -- 07 - J Down
  -- 08 - Z
  -- 09 - Z Rotated
  -- 10 - O
  -- 11 - S
  -- 12 - S Rotated
  -- 13 - L Right
  -- 14 - L Down
  -- 15 - L Left
  -- 16 - L Up
  -- 17 - I
  -- 18 - I Rotated

piece_index = {
    [0] = 'T',   
    [1] = 'T',   
    [2] = 'T',   
    [3] = 'T',   
    [4] = 'J',   
    [5] = 'J',   
    [6] = 'J',   
    [7] = 'J',   
    [8] = 'Z',   
    [9] = 'Z',   
    [10] = 'O',  
    [11] = 'S',  
    [12] = 'S',  
    [13] = 'L',  
    [14] = 'L',  
    [15] = 'L',  
    [16] = 'L',  
    [17] = 'I',  
    [18] = 'I'  
}


function get_curr_piece()
    local piece = piece_index[tonumber(memory.readbyte(piece_addr))]
    return piece
end
