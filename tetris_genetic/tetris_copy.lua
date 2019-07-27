BOARD = {}

--[[
Add placement for these pieces

I_mino - in_progress
L_mino - in_progress
J_mino - in_progress
O_mino - in_progress
S_mino - in_progress
Z_mino - in_progress
T_mino - in_progress

]]--

function init_board()
  local row = {'*', '*', '*', '*', '*', '*', '*', '*', '*', '*'}
  for i = 1, 22 do
    BOARD[i] = row
  end
end


function place_i(index, rotate)
  local i_piece = {{'I', 'I', 'I', 'I'}}

  if rotate % 2 == 1 then
    i_piece = {{'I'},
               {'I'},
               {'I'},
               {'I'}} 
  end

  for col in #i_piece do
    for row in #i_piece[col] do
      BOARD[22][index+col]
end




