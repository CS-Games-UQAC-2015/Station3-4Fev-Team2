import sys

# python main.py 0 va tester en utilisant A-small-practice.in
#                1                        A-large-practice.in

files = [
    "A-small-practice.in",
    "A-large-practice.in"
]

def getFileData():
    fileId = int(sys.argv[1])
    data = open(files[fileId]).read().splitlines()
    
    return data[1:]

def main():
    data = getFileData()
    
    print data
    
    
if __name__ == "__main__":
    main()