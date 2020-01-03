from Locale import Locale;
import csv;

def main():
    print("Hello World!")
    a1 = Locale(0,0);
    a2 = Locale(3,4);
    print(a1.calcDistanceFromLocale(a2));
    data = csvReader();
    print(data);

def menu():
    print("Select Dataset... etc");

def csvReader():
    datafile = open('data/Data1.csv','r');
    datareader= csv.reader(datafile, delimiter=';');
    data = [];
    for row in datareader:
        data.append(row);
    return data;


if __name__ == "__main__":
    main();
