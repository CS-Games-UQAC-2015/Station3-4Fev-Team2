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
    # Si on dépasse 40 en génération, on a failé
    if (generation > 40):
        return -1
    
    # Si on a un elfe, on a la bonne génération
    elif (p/q == 1):
        return generation

    # Sinon, on essaie de tendre vers 1
    else:
        return getElfGeneration(2*p, q, generation + 1)

def main():
    data = getFileData()
    
    for i in range(len(data)):
        case = data[i]
        p, q = case.split('/')
        
        # Démarrer la récursion
        gen = getElfGeneration(p, q, 1)
        
        if (gen == -1):
            gen = "impossible"
        
        print ("Case #" + i + ": " + gen)
    
    
if __name__ == "__main__":
    main()