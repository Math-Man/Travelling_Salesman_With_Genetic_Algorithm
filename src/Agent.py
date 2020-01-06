import random;


class Agent:

    localeSequence = [];
    distanceTravelled = 0;
    score = 0;


    def __init__(self, sequenceLength):
        self.localeSequence = [0]*sequenceLength; # list with size of sequenceLength




    def calculateScore(self):
        print("");


    #Get distance from distance matrix, utility (copy from main)
    def getDistance(l1, l2, data):
        if (l1 > 0 and l2 > 0 and l1 < len(data[0]) and l2 < len    (data)):
            return data[l1][l2];
        else:
            return -1;



class RandomAgentBuilder:

    def randomAgent(self, sequenceLength):
        a  = Agent(sequenceLength);
        for i in range(0, sequenceLength):
            a.localeSequence[i] = i;
        random.shuffle( a.localeSequence );
        #print(a.localeSequence);
        return a;
