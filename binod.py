import os

def isBinod(filename):
    with open(filename,"r") as f:
        fileContent = f.read()
    if "binod" in fileContent.lower():
        return True
    else:
        return False

if __name__ == "__main__":
    # listing the contents of this folder
    dir_contents = os.listdir()

    nBinod = 0

    # for each text file, run isBinod for them
    for file in dir_contents:
        if file.endswith('txt'):
            print(f"\nDetecting Binod in {file}")
            flag = isBinod(file)
            if(flag):
                print(f"Binod found in {file}")
                nBinod += 1
            else:
                print(f"Binod not found in {file}")

    print("\n********* Binod Detector Summary **********")
    print(f"{nBinod} files found with Binod hidden into them")

    a = input()