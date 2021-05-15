
import os, sys, string, random

def convert(string):
    return "".join([hex(c) for c in string])
    
def randname():
    return "".join([random.choice(string.ascii_letters) for i in range(10)])

def populate(basePath, data, depth, width, fpl, index):
    
    thisLevelName = randname()
    os.mkdir(basePath + "/" + thisLevelName)
    
    for fn in range(fpl):
        if len(data) == 0:
            return True
            
        with open(basePath + "/" + thisLevelName + "/" + f"{index}_{randname()}"+".piz","w") as f:
            f.write(data.pop())
            index += 1
            
    if depth != 1:
        for w in range(width):
            populate(basePath + "/" + thisLevelName, data, depth - 1, width, fpl, index)


def main():
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
    print(parts)
    
    os.mkdir(outname+"_piz")
    
    index = 0
    populate("./" + outname + "_piz", parts, depth, width, fpl, index)
        
        
        
    
    
if __name__ == "__main__":
    main()
