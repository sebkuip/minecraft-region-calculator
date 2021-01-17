# A simple calculator to see the region/chunks/blocks depending on coördinates
# You just enter your data in the format `T.X.Y`, with T being Type (B/C/R for Block, Chunk or Region respectively) and X and Y being the coördinates of the thing you want to calculate
# When given a block it will give you the chunk and region coordinates this block is in
# When given a chunk it shows what blocks it contains, and what region it is in
# When given a region it shows the coördinates of the blocks it contains and the coördinates of the chunks it contains
# Feel free to use this code anywhere. It's open source. If you want, please do link the github link.
# Enjoy

import re

print("Please enter the coördinates you want to calculate following the format `T.X.Y`. For more details, consult the readme")

while True:
    uinput = input("Input: ").strip().lower()

    if not re.search(r"^[bcr]\.-?\d+\.-?\d+$", uinput):
        print("This isn't a valid input. Please follow the format `T.X.Y` for input. For more details, consult the readme")
        continue

    break

uinput = uinput.split(".")

utype = uinput[0]
ux = int(uinput[1])
uy = int(uinput[2])

print(f"type: {utype} x: {ux} y: {uy}")

if utype == "b":
    print(f"block {ux},{uy} is inside chunk {ux//16},{uy//16} and within region {ux//512},{uy//512}")

elif utype == "c":
    print(f"chunk {ux},{uy} contains blocks {ux*16},{uy*16} to {(ux+1)*16-1},{(uy+1)*16-1} and is within region {ux//32},{uy//32}")

elif utype == "r":
    print(f"region{ux},{uy} contains blocks {ux*512},{uy*512} to {(ux+1)*512-1},{(uy+1)*512-1} and contains chunks {ux*32},{uy*32} to {(ux+1)*32-1},{(uy+1)*32-1}")

# input("Press enter to close the program")