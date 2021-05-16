
import os, sys, string, random
from datetime import datetime

def convert(string):
    return "".join([hex(c) for c in string])
    
def randname():
    return "".join([random.choice(string.ascii_letters) for i in range(10)])

def populate(basePath, data, depth, width, fpl):
    global index
    thisLevelName = randname()
    os.mkdir(basePath + "/" + thisLevelName)
    
    print(data)
    
    for fn in range(fpl):
        if len(data) == 0:
            return True
            
        with open(basePath + "/" + thisLevelName + "/" + f"{index}_{randname()}"+".piz","w") as f:
            d = data.pop(0)
            print(d)
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
    parts = [data[i:i+n] for i in range(0, len(data), n)]
    
    os.mkdir(outname+"_piz")
    
    global index
    index = 0
    populate("./" + outname + "_piz", parts, depth, width, fpl)
    
    with open(outname+"_piz"+"/info.pizinfo", "w") as f:
        f.write(f"Piz Info for: {filename} \nPizzed at {datetime.now()}")
        
    
        
    
    
if __name__ == "__main__":
    main()
