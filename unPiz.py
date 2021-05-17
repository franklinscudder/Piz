
import sys, os

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        elif fullPath[-4:] == ".piz":
            allFiles.append(fullPath)
                
    return allFiles
    
def sortFiles(files):
    out = [None]*len(files)
    
    for file in files:
        n = int(file.split("\\")[-1].split("_")[0])
        out[n] = file
        
    return out
    
def main():
    target = sys.argv[1]
    
    with open(target + "/info.pizinfo", "r") as f:
        info = f.readlines()
        
    outname = info[0].split(":")[1][1:-2]
    
    #print(outname)
    files = getListOfFiles(target)
    #print(files)
    files = sortFiles(files)
    #print(files)
    
    data = ""
    
    for file in files:
        with open(file, "r") as f:
            data += f.read()
    
    #print(data)
    data = [int(i,16) for i in data.split("0x")[1:]]
    #print(data)
    rawData = bytes(data)
    #print(rawData)
    
    size = len(rawData)
    
    with open("unPizzed_" + outname, "wb") as fout:
        fout.write(rawData)
        
    print(f"Wrote {size} bytes to {'unPizzed_' + outname}")


if __name__ == "__main__":
    main()