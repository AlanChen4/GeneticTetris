-- This file contains the helper methods needed to play tetris


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

  local status_number = memory.readbyte(0x0048)
  local output_file = io.open('game_state/fceux_status.txt', 'w')
  
  io.output(output_file)
  io.write(status_number)
  io.close(output_file)
end


