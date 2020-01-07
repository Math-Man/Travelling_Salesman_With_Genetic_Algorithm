from Agent import Agent;
from Agent import RandomAgentBuilder;
import math;
import random;

class GeneticAlgorithm:

 #Agents are individuals that makes up populations.

 #Agents have their DNA as 'localeSequence', fitness (score) as 1/(x)^2 , x being sum of total distance traveled.
 #This allows for an exponentially increasing score for lower distance travelled.

 #DNA is made up of two main parts:
 #starting locale: important to seperate as agents have to return to this locale at the end
 #localesequence: sequence of travel

 #initial selection is random sequence of locale with no bias and a random starting locale

 #selection is done using weighted random selection depending on the agent's score

 #crossover is done without bias, randomly switching targeted locale for at an index
 #crossover happens for each index of the localesequence 50% chance for either parent's item to be selected
 #crossover chance depends on the global variable of this class 'CROSSOVER_CHANCE'

#mutation has a chance of occuring "MUTATION_RATE"
#mutation strength effects the percantage of the DNA that is going to be mutated
#0.1 mutation strength will result in 10% of the DNA getting shuffled randomly without bias
#mutation strength will always round up, example: 0.00000000001% will result in a single mutation for an agent

#new generation is built by the consecutive events of selection->crossover->mutation for each agent

    ##PARAMETERS##
    MAX_GENERATION = 9999;
    POPULATION_SIZE = 25;
    MUTATION_RATE = 0.05;
    MUTATION_STRENGTH = 0.05;
    CROSSOVER_CHANCE = 0.5;
    ##PARAMETERS##

    rawData = [];
    currentGeneration = [];
    newGeneration = [];


    #random population
    def buildInitialPopulation(self):
        agentBuilder = RandomAgentBuilder();
        for i in range(self.POPULATION_SIZE):
            self.currentGeneration[i] = agentBuilder.randomAgent(len(self.rawData)); #Use agent builder to build random agents
        return;


    #builds nextGeneration
    def BuildNextGeneration(self):
        listOfPairs = self.selection();
        self.crossOver(listOfPairs);
        self.mutation();
        return;

    #weighted random selection alghorithm depending on the score of the agents
    def selection(self):
        #Calculate scores
        scoreSum = 0;
        scores = [0]*self.POPULATION_SIZE;
        for i in range(0,self.POPULATION_SIZE):
            scores[i] = self.currentGeneration[i].calculateScore(self.rawData);
            scoreSum = scoreSum + scores[i];
        #translate values to range between: (0,POPULATION_SIZE/100)
        currentMax = max(scores);
        currentMin = min(scores);

        summ = 0;
        for i in range(0,self.POPULATION_SIZE):
            scores[i] = (scores[i]/scoreSum) * 100;
            summ = summ + scores[i];
        #add division fault to first score to make the selection algorithm work properly (usually has very low significance has no effect on algorithm)
        scores[0] = scores[0] + (100 - summ);

        #apply weighted random selection, create a list of pairs and return it
        listOfPairs = [0]*self.POPULATION_SIZE;

        for i in range(0,self.POPULATION_SIZE):
            tempScores = scores.copy();
            parent1SelectionIndex = self.weightedRandomSelect(tempScores);
            parent1 = self.currentGeneration[parent1SelectionIndex];

            #remove selected index from tempScores so its not selected twice
            tempScores.pop(parent1SelectionIndex);
            parent2 = self.currentGeneration[self.weightedRandomSelect(tempScores)];

            listOfPairs[i] = (parent1, parent2);

        return listOfPairs;

    #returns index of selected element for values that total upto 100
    def weightedRandomSelect(self,list):

        target  = random.random()*100;
        total = 0;
        currentItem = 0.0;
        for i in range(0,len(list)):
            currentItem = list[i];
            if target > total and target <= (total + currentItem):
                return i;
            total = total + currentItem;
        return -1;




    def crossOver(self, listOfPairs):

        #select genes for each pair and create a new agent
        for i in range(len(listOfPairs)):

            #build a new sequence from parent sequences
            parent1 = listOfPairs[i][0];
            parent2 = listOfPairs[i][1];
            DNALength = len(parent1.localeSequence);

            print(parent1.localeSequence);
            print(parent2.localeSequence);
            #create child agent
            child = Agent(DNALength);
            child.localeSequence = parent1.localeSequence;

            #apply corssover
            for k in range(DNALength):
                if(random.random() >= self.CROSSOVER_CHANCE):
                    #pick from the sequence of second parent
                    #print("crossOver "+ str(k));
                    child.localeSequence[k] = parent2.localeSequence[k];
                #print("NO crossOver " + str(k));

            #add new child to newGenerations list
            self.newGeneration[i] = child;
            print(child.localeSequence);
        return self.newGeneration;


    def mutation(self):
        return;


    def replaceCurrentGeneration(self):
        self.currentGeneration = self.newGeneration;
        self.newGeneration = [0]*self.POPULATION_SIZE;
        return;

    #entry
    def __init__(self, data):

        self.currentGeneration = [0]*self.POPULATION_SIZE; #list with size POPULATION_SIZE
        self.newGeneration = [0]*self.POPULATION_SIZE; #list with size POPULATION_SIZE
        self.rawData = data;

        self.buildInitialPopulation();
