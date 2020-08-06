import os, time, math
# Vahin Sharma
def getFileAge(x):
    return math.floor(time.time()-os.stat(x).st_mtime) // (24 * 3600)
while True:
    path = input("Please enter the path (enter 'quit' to stop this program): ")
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
                            print("Access denied, either due to system permissions, or the file is read-only.")
                    else:
                        print("Ignored {}".format(i))
        else:
            print("The folder is empty!")

    elif path == "quit":
        quit()
    else:
        print("Invalid Path: {}".format(path))
