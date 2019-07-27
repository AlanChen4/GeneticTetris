--[[
This file contains the helper methods for the tetris AI
]]--

TOTAL_HEIGHT = 0
LINES_CLEARED = 0
TOTAL_HOLES = 0
TOTAL_BUMPS = 0


function get_screen()
  gui.savescreenshotas('game_state/status.png')
end


function get_height()
  local aggregate_height = 0
  return aggregate_height
end


function get_lines_cleared()
  local lines_cleared = 0
  return lines_cleared
end


function get_holes()
  local total_holes = 0
  return total_holes
end


function get_bumps()
  local total_bumps = 0
  return total_bumps
end


-- returns the score
function getScore()
  local score = memory.readbyte(0x0053)
  return score
end

