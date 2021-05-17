
import os, sys, string, random, textwrap
from datetime import datetime

def convert(string):
    return "".join([hex(c) for c in string])
    
def randname():
    return "".join([random.choice(string.ascii_letters) for i in range(10)])

def populate(basePath, data, depth, width, fpl):
    global index
    thisLevelName = randname()
    os.mkdir(basePath + "/" + thisLevelName)
    
    for fn in range(fpl):
        if len(data) == 0:
            return True
            
        with open(basePath + "/" + thisLevelName + "/" + f"{index}_{randname()}"+".piz","w") as f:
            d = data.pop(0)
            f.write(d)
            index += 1
            
    if depth != 1:
        for w in range(width):
            if populate(basePath + "/" + thisLevelName, data, depth - 1, width, fpl):
                return True
    
    return False

def main():
    import shutil
    shutil.rmtree("dummy_piz")
    
    filename = sys.argv[1]
    
    outname = sys.argv[2]

    try:
        depth = int(sys.argv[3])
    except:
        depth = 3
    
    try:
        width = int(sys.argv[4])
    except:
        width = 3
        
    try:
        fpl = int(sys.argv[5])
    except:
        fpl = 3
    
    with open(filename, "rb") as file:
        data = convert(file.read())
    
    n = (depth * width * fpl) + 1
    parts = textwrap.wrap(data, n)
    
    os.mkdir(outname+"_piz")
    
    global index
    index = 0
    dataSize = len(data.replace("0x",""))*0.5
    outDataSize = len(data)
    populate("./" + outname + "_piz", parts, depth, width, fpl)
    
    with open(outname+"_piz"+"/info.pizinfo", "w") as f:
        f.write(f"Piz Info for: {filename} \nPizzed at {datetime.now()}\nInitial size: {dataSize}B \nOutput size: {outDataSize}B")
        
    print(f"Expanded {int(dataSize)} bytes to {int(outDataSize)} bytes in {outname}_piz")
        
    
    
if __name__ == "__main__":
    main()
