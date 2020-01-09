-- This file contains the helper methods needed to play tetris

require('lua_helper')

-- resets buttons
function reset_buttons()
  local buttons = {A=false, up=false, left=false, B=false, select=false, right=false, down=false, start=false}
  joypad.set(1, buttons)
  emu.frameadvance()
end

-- moves the piece right
function move_right()
  local buttons = joypad.get(1)
  buttons['right'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end

-- moves the piece left
function move_left()
  local buttons = joypad.get(1)
  buttons['left'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end

-- moves the piece down
function move_down()
  local buttons = joypad.get(1)
  buttons['down'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end

-- moves the piece up
function move_up()
  local buttons = joypad.get(1)
  buttons['up'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end

-- press enter button
function press_start()
  local buttons = joypad.get(1)
  buttons['start'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end

-- rotate piece
function rotate()
  local buttons = joypad.get(1)
  buttons['A'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end

-- simulates sleep by skipping five frames
function tetris_sleep()
  emu.frameadvance()
  emu.frameadvance()
  emu.frameadvance()
  emu.frameadvance()
  emu.frameadvance()
end


-- updates all information for the python counterparts
function update_info()
  gui.savescreenshotas('game_state/status.png')

  -- current status of the game
  local status_number = memory.readbyte(0x0048)
  local status_file = io.open('game_state/fceux_status.txt', 'w')
  
  io.output(status_file)
  io.write(status_number)
  io.close(status_file)

  -- current and next piece loaded
  local current_piece = memory.readbyte(0x0042)
  local next_piece = memory.readbyte(0x00BF)

  local piece_file = io.open('py_helpers/game_state/current_next_piece.txt', 'w')

  io.output(piece_file)
  io.write(current_piece .. ' ' .. next_piece)
  io.close(piece_file)
end

function check_AI()
  local py_status = lines_from('game_state/AI_decision.txt')[1]
  if (py_status == 'wait') then
    -- pass
  elseif (py_status == 'restart') then
    -- TODO: ADD RESTART FROM OTHER LEVELS
    press_start()
    press_start()
  elseif (py_status == 'down') then
    -- TODO: THIS DOESN'T WORK
  end 
end
