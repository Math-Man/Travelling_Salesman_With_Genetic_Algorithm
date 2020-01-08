from GeneticAlgorithm import GeneticAlgorithm;
import csv;
import os;
clear = lambda: os.system('cls')

def main():

    #menu
    clear();
    print("Change parameters under (GeneticAlgorithm.py) to custimize the algorithm");
    print("Select Dataset (Enter: 1, 2, 3)");
    inDataset = input();
    dataSet = csvReader("Data" + str(inDataset) + ".csv");
    geneticAlgMenuLoop(dataSet);
    #print(getDistanceFor(1, 10, data));






    #genAlg.BuildNextGeneration();

def geneticAlgMenuLoop(dataset):
    exit = 0;


    clear();
    print("Starting genetic algorithm, enter (exit) anytime to return to dataset selection.\n");
    genAlg = GeneticAlgorithm(dataset);
    genAlg.buildInitialPopulation();

    print("Best in initial population:");
    printCurrentBests(genAlg);


    clear();
    while exit == 0:

        print("Current Generation: " + str(genAlg.generationIndex));
        printCurrentBests(genAlg);
        printHelpMenu();
        InMenu = input();
        clear();
        if InMenu == 'step':
            #genAlg.step();
            genAlg.BuildNextGeneration();
            #printCurrentBests(genAlg);
            genAlg.replaceCurrentGeneration();

        elif InMenu == 'run':
            clear();
            print("Enter number of generations to process");
            InNum = int(input());
            for i in range(0,InNum):
                genAlg.BuildNextGeneration();
                #printCurrentBests(genAlg);
                genAlg.replaceCurrentGeneration();

        elif InMenu == 'bests':
            for i in range(0, len(genAlg.bestInGenerations)):
                print("Score: " + str( genAlg.bestInGenerations[i].score));
                print("Distance Travelled: " +  str(genAlg.bestInGenerations[i].distanceTravelled));
                print("Sequence: " +  str(genAlg.bestInGenerations[i].localeSequence));

        elif InMenu == 'best ever':
            print("Score: " + str( genAlg.bestEver.score));
            print("Distance Travelled: " +  str(genAlg.bestEver.distanceTravelled));
            print("Sequence: " +  str(genAlg.bestEver.localeSequence));


        elif InMenu == 'exit':
            exit = 1;


def printHelpMenu():
    print("\nType (step) to process a single generation");
    print("Type (run) and enter a number to process ~x amount of generations");
    print("Type (bests) to show sequences and information of the bests in all processed generations");
    print("Type (best ever) to show sequence and information of the best ever agent");
    print("Type (exit) anytime to return to dataset selection")

def printCurrentBests(genAlg):
    print("\nScore: " + str( genAlg.getBestInCurrentGeneration().score));
    print("Distance Travelled: " +  str(genAlg.getBestInCurrentGeneration().distanceTravelled));
    print("Sequence: " +  str(genAlg.getBestInCurrentGeneration().localeSequence));
    print("Current Generation Average Score:" + str(genAlg.getCurrentGenerationAverage()));
#reads data file (converted to .csv file)
#data file should be outside src folder within a data folder
def csvReader(fileName):
    datafile = open('data/' + fileName,'r'); #'Data1.csv'
    datareader= csv.reader(datafile, delimiter=';');
    data = [];
    for row in datareader:
        data.append(row);
    return data;


#Get distance from distance matrix, utility
def getDistanceFor(l1, l2, data):
    if (l1 > 0 and l2 > 0 and l1 < len(data[0]) and l2 < len(data)):
        return data[l1][l2];
    else:
        return -1;




if __name__ == "__main__":
    main();
