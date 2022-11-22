def readfile():
    f = open("datafile.txt")
    contents = f.read()
    f.close()
    print(contents)

def makefile():
    f = open("createdfile.txt", "w")
    f.write("This is some data that our Python script created.\n")
    f.close()

# if __name__ == "__main__":
    