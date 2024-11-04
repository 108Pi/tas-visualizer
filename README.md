# tas-visualizer
### Extract position data
Play fm2 in Mesen. Start lua script on the first frame mario appears.  
Stop script when Mario changes rooms.  
Do this for each tas. Make sure you change the file name in the lua script.
### Generate frames
Add the path of each output file to the python script.  
**Make sure you have a picture of the level saved as map.png**.  
Set the endframe. Likely best to set it to the length of the longest tas.  
Make sure /output folder exists.  
Run python script. Requires pandas and pillow.  
Can take up to a minute because python is slow. 
### Combine frames
Place encode.bat in /output and run it. Requires ffmpeg.  
Had issues with this on windows. 
