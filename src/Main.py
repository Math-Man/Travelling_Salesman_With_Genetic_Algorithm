from GeneticAlgorithm import GeneticAlgorithm;
import csv;


def main():
    data = csvReader("Data1.csv");
    #print(getDistanceFor(1, 10, data));
    genAlg = GeneticAlgorithm(data);
    genAlg.BuildNextGeneration();

#menu loop function
def menu():
    print("Select Dataset... etc");


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
