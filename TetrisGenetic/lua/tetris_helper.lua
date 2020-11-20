-- This file contains the helper methods needed to play tetris


function reset_buttons()
  local buttons = {A=false, up=false, left=false, B=false, select=false, right=false, down=false, start=false}
  joypad.set(1, buttons)
  emu.frameadvance()
end


function move_right()
  local buttons = joypad.get(1)
  buttons['right'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end


function move_left()
  local buttons = joypad.get(1)
  buttons['left'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end


function move_down()
  local buttons = joypad.get(1)
  buttons['down'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end


function move_up()
  local buttons = joypad.get(1)
  buttons['up'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end


function press_start()
  local buttons = joypad.get(1)
  buttons['start'] = true
  joypad.set(1, buttons)
  emu.frameadvance()
  reset_buttons()
end


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
