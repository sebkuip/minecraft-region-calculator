# A simple calculator to see the region/chunks/blocks depending on coordinates
# You just enter your data in the format `T.X.Z`, with T being Type (B/C/R for Block, Chunk or Region respectively) and X and Z being the coordinates of the thing you want to calculate
# When given a block type, the format also allows for entering a Y coordinate following the format `B.X.Y.Z`
# The . may also be replaced by a , or a space.
# When given a block it will give you the chunk and region coordinates this block is in
# When given a chunk it shows what blocks it contains, and what region it is in
# When given a region it shows the coordinates of the blocks it contains and the coordinates of the chunks it contains
# Feel free to use this code anywhere. It's open source. If you want, please do link the github link.
# Enjoy

import re

print("Please enter the coordinates you want to calculate following the format `T.X.Z` or `B.X.Y.Z`. For more details, consult the readme")

while True:
    uinput = input("Input: ").strip().lower()

    if not re.search(r"(^[bcr][.,\s]-?\d+[.,\s]-?\d+$)|(^b[.,\s]-?\d+[.,\s]-?\d+[.,\s]-?\d+$)", uinput):
        print("This isn't a valid input. Please follow the format `T.X.Z` or `B.X.Y.Z` for input. For more details, consult the readme")
        continue

    break

uinput = re.split(r"[.,\s]+", uinput)

if len(uinput) > 3:
    uinput.pop(2)

utype = uinput[0]
ux = int(uinput[1])
uz = int(uinput[2])

print(f"type: {utype} x: {ux} y: {uz}")

if utype == "b":
    print(f"block {ux},{uz} is inside chunk {ux//16},{uz//16} and within region {ux//512},{uz//512}")

elif utype == "c":
    print(f"chunk {ux},{uz} contains blocks {ux*16},{uz*16} to {(ux+1)*16-1},{(uz+1)*16-1} and is within region {ux//32},{uz//32}")

elif utype == "r":
    print(f"region {ux},{uz} contains blocks {ux*512},{uz*512} to {(ux+1)*512-1},{(uz+1)*512-1} and contains chunks {ux*32},{uz*32} to {(ux+1)*32-1},{(uz+1)*32-1}")

input("Press enter to close the program")