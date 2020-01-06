import random;
import math;


class Agent:

    localeSequence = [];
    distanceTravelled = 0;
    score = 0;


    def __init__(self, sequenceLength):
        self.localeSequence = [0]*sequenceLength; # list with size of sequenceLength


    #fitness (score) as 1/(x)^2, x being sum of total distance traveled.
    def calculateScore(self, data):
        sum = 0;
        for i in range(1, len(self.localeSequence)):
            locFrom = self.localeSequence[i-1];
            locTo = self.localeSequence[i];
            sum = sum + int(self.getDistance(locFrom, locTo, data));

        #add return distance
        sum = sum + int(self.getDistance(self.localeSequence[len(self.localeSequence) - 1], self.localeSequence[0], data));

        #sum needs to be low for a higher fitness(score)
        # 1/sum^2 => higher sum => lower score
        print(sum);
        self.score = (1 / math.pow(sum,2));

        return self.score;



    #Get distance from distance matrix, utility (copy from main)
    def getDistance(self, l1, l2, data):
        l1 = l1-1;
        l2 = l2-1;
        if (l1 > 0 and l2 > 0 and l1 < len(data[0]) and l2 < len(data)):
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
