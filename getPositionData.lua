function getPos()
    file = io.open(filename, "a")
    io.output(file)
    Player_X_Position = emu.read(0x86,256)
    Player_PageLoc = emu.read(0x6d,256)
    Player_Y_Position = emu.read(0xce,256)
    PlayerGfxOffset = emu.read(0x6d5,256)
    PlayerFacingDir = emu.read(0x33, 256)
    io.write(Player_X_Position .. "," .. Player_PageLoc .. "," .. Player_Y_Position .. "," .. PlayerGfxOffset .. "," .. PlayerFacingDir .. "\n")
    io.close(file)
end

filename = "1.txt"
os.remove(filename)
emu.addEventCallback(getPos, 4)