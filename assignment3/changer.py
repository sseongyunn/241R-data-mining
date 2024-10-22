import sys

def changer(filename):
    fp = open(filename, "r")
    
    for line in fp:
        ddd
    
    outfp=open(filename+"_changed", "w")
    
    
    fp.close()
    outfp.close()



if __name__=="__main__":
    
    if len(sys.argv) != 2:
        print( "[Usage] %s in-file(pickle)" %sys.argv[0], file=sys.stderr)
        sys.exit()
        
    with open(sys.argv[1], "rb") as fp:
        text = open(fp)
        changer(text)