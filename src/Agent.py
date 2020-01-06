import random;

class Agent:

    localeSequence = [];
    distanceTravelled = 0;
    score = 0;


    def __init__(self, sequenceLength):
        self.localeSequence = [0]*sequenceLength; # list with size of sequenceLength




    def calculateScore(self):
        print("");


class RandomAgentBuilder:

    def randomAgent(self, sequenceLength):
        a  = Agent(sequenceLength);
        for i in range(0, sequenceLength):
            a.localeSequence[i] = i;
        random.shuffle( a.localeSequence );
        print(a.localeSequence);
        return self
