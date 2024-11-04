from PIL import Image, ImageOps
import pandas as pd  

pds = [pd.read_csv("1.txt")]
pds.append(pd.read_csv("2.txt"))

startframe = 0
endframe = 1000
for i in range(startframe,endframe):
    img1 = Image.open("map.png","r").convert("RGB")
    for player in pds:
        try:
            img2 = Image.open(str(player.iloc[i][3])+".png","r") 
            if (player.iloc[i][4] != 1):
                img2 = ImageOps.mirror(img2)
            img1.paste(img2, ((player.iloc[i][0]+player.iloc[i][1]*256),player.iloc[i][2]+17), mask = img2) 
        except:
            continue
    img1.save("output/" + str(i).zfill(4) + ".png")
