import os, time, math
# Vahin Sharma
def getFileAge(x):
    return math.floor(time.time()-os.stat(x).st_mtime) // (24 * 3600)
while True:
    path = input("Enter the path (enter 'quit' to stop this application): ")
    if os.path.exists(path):
        if os.listdir(path) != []:
            for i in os.listdir(path):
                nPath = path+"/"+i
                if getFileAge(nPath) > 25:
                    askUsr = input("Do I need to delete this: {} (y/n) ".format(i)).lower()
                    if askUsr == "y":
                        try:
                            os.remove(nPath)
                        except:
                            print("Access has been denied, either due to system permissions, or the file is read-only.")
                    else:
                        pass
        else:
            print("The folder is empty!")

    elif path == "quit":
        quit()
    else:
        print("Invalid Path: {}".format(path))
