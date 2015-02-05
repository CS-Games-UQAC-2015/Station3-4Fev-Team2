import sys

# python main.py 0 va tester en utilisant A-small-practice.in
#                1                        A-large-practice.in

files = [
    "A-small-practice.in",
    "A-large-practice.in"
]

# Lit le fichier et retourne le tableau des cas
def getFileData():
    fileId = int(sys.argv[1])
    data = open(files[fileId]).read().splitlines()
    
    return data[1:]

# Fonction récursive, prend en parametre p, q et le numéro de génération
def getElfGeneration(p, q, generation):
    print(str(p)+"/"+str(q) + " "+str(generation))
    # Si on dépasse 40 en génération, on a failé
    if (generation > 40):
        return -1
    
    # Si on a un elfe, on a la bonne génération
    elif (int(p)/int(q) == 1):
        return generation

    # Sinon, on essaie de tendre vers 1
    else:
        return getElfGeneration(str(2*int(p)), q, generation + 1)



def main():
    #data = getFileData()
    data = open(files[0]).read().splitlines()
    amountTest = data[0]
    print(str(len(data)))
    for i in range(1,len(data)):
        case = data[i]
        p, q = case.split('/')
        print("why me?")
        # Démarrer la récursion
        gen = getElfGeneration(p, q, 1)

        if (gen == -1):
            gen = "impossible"

        print ("Case #" + str(i) + ": " + str(gen))
    
    
if __name__ == "__main__":
    main()