import os
import os.path
import sys

def getAllFileInRootDir(rootdir, filter):
    allFiles = []
    retdirs = []
    for parent,dirnames,filenames in os.walk(rootdir):
        for dirname in  dirnames:                    
            #print("parent is:" + parent)
            #print("dirname is:" + dirname)
            retdirs.append(os.path.join(parent, dirname))
            
            pass
        for filename in filenames:                  
            #print "parent is:" + parent
            #print "filename is:" + filename
            #print "the full name of the file is:" + os.path.join(parent,filename) 
            ext = os.path.splitext(filename)[1][1:]
            #print(ext)
            if (ext == filter):
                allFiles.append(os.path.join(parent, filename))
    return allFiles, retdirs

if __name__ == "__main__":
    rootdir = sys.argv[1]
    fileter = sys.argv[2]
    #outdir = outdir
    #key = sys.argv[3]
    #sign = sys.argv[4]
    files, dirs = getAllFileInRootDir(rootdir, fileter)
    #print(dirs)
    
    #for file in files:
     #   os.system('xxtea.exe')