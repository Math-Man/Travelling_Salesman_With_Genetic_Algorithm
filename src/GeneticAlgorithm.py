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
    POPULATION_SIZE = 100;
    MUTATION_RATE = 0.1;
    MUTATION_STRENGTH = 0.05;
    CROSSOVER_CHANCE = 0.5;
    ##PARAMETERS OVER##









    rawData = [];
    currentGeneration = [];
    newGeneration = [];

    generationIndex = 0;

    bestInGenerations = [];
    bestEver = None;


    #random population
    def buildInitialPopulation(self):
        agentBuilder = RandomAgentBuilder();
        for i in range(self.POPULATION_SIZE):
            self.currentGeneration[i] = agentBuilder.randomAgent(len(self.rawData)); #Use agent builder to build random agents
            self.currentGeneration[i].calculateScore(self.rawData);

        return;


    #builds nextGeneration
    def BuildNextGeneration(self):
        listOfPairs = self.selection();
        self.crossOver(listOfPairs);
        self.mutateGeneration();
        return;

    #weighted random selection alghorithm depending on the score of the agents
    def selection(self):
        #Calculate scores
        scores = self.weightedScoreCalculation();

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

    def weightedScoreCalculation(self):
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
        return scores;


    def crossOver(self, listOfPairs):

        #select genes for each pair and create a new agent
        for i in range(len(listOfPairs)):

            #build a new sequence from parent sequences
            parent1 = listOfPairs[i][0];
            parent2 = listOfPairs[i][1];
            DNALength = len(parent1.localeSequence);

            #print(parent1.localeSequence);
            #print(parent2.localeSequence);
            #create child agent
            child = Agent(DNALength);
            child.localeSequence = [-1]*len(parent1.localeSequence); #parent1.localeSequence;

            #apply corssover
            #pick values from each parent and copy their locations to the child
            fromfirstParent = [];
            fromSecondParent = [];
            for k in range(DNALength):
                if(random.random() <= self.CROSSOVER_CHANCE):
                    fromfirstParent.append(k);
                    #pick from the sequence of second parent
                    #item = parent2.localeSequence[k]
                    #child.localeSequence[k] = item;
                else:
                    fromSecondParent.append(k);
                    #item = parent1.localeSequence[k]
                    #child.localeSequence[k] = item;
                    #print("NO crossOver " + str(k));

                #start pulling from parents and add to child

            #print("parents")
            #print(fromfirstParent)
            #print(fromSecondParent)

            for j in range(0,DNALength):
                if j in fromfirstParent:
                    locIndex = parent1.localeSequence[j]; #where the location j is in the parent's sequence
                    #print("first: " + str(locIndex));
                    child.localeSequence[parent1.localeSequence.index(j)] = j;

                elif j in fromSecondParent:
                    locIndex = parent2.localeSequence[j]; #where the location j is in the parent's sequence
                    #print("second: " + str(locIndex));
                    child.localeSequence[parent1.localeSequence.index(j)] = j;

            #add new child to newGenerations list
            self.newGeneration[i] = child;
            #print(child.localeSequence);
        #print("Crossover complete");
        return self.newGeneration;

    def mutateGeneration(self):
        for i in range(0, len(self.newGeneration)):
            self.newGeneration[i] = self.mutate(self.newGeneration[i]);
            #print(self.newGeneration[i].localeSequence);
        #print("mutations complete");
        return;

    #swap ceiling(mutationstrength) number of items randomly
    def mutate(self, agent):
        sequenceLength = len(agent.localeSequence);
        numberOfMutations = math.ceil(sequenceLength * self.MUTATION_STRENGTH);
        #print(agent.localeSequence)
        if random.random() < self.MUTATION_RATE: #If mutation chance check passes
            for i in range(0, numberOfMutations):
                #select a random index
                randomIndex = random.randint(0,sequenceLength-1);
                randomSwapIndex = random.randint(0,sequenceLength-1);
                agent.localeSequence[randomIndex] ,  agent.localeSequence[randomSwapIndex] = agent.localeSequence[randomSwapIndex] ,  agent.localeSequence[randomIndex]
                #print(agent.localeSequence)
        agent.calculateScore(self.rawData);
        return agent;




    #sets bests and replaces current generation
    def replaceCurrentGeneration(self):


        #set scores
        self.bestInGenerations.append(self.getBestInCurrentGeneration());
        self.bestEver = self.getBestEver();

        #print("best now: SCORE:" + str(self.getBestInCurrentGeneration().score) + " TOTAL DISTANCE: " + str(self.getBestInCurrentGeneration().distanceTravelled));
        #print("best ever: " + str(self.getBestEver().score )  + " TOTAL DISTANCE: " + str(self.getBestEver().distanceTravelled));

        #replace

        self.currentGeneration = self.newGeneration.copy();
        self.newGeneration = [0]*self.POPULATION_SIZE;

        self.generationIndex = self.generationIndex + 1;

        return;



    def step(self):
        print("Processing Next Generation...");
        self.BuildNextGeneration();
        self.replaceCurrentGeneration();





    #functions to get best and avrg in both generations
    def getBestInCurrentGeneration(self):
        best = -1;
        bestAgent = None;
        for agent in self.currentGeneration:
            if agent.score > best:
                best = agent.score;
                bestAgent = agent;
        return bestAgent;

    def getBestInNewGeneration(self):
        best = -1;
        bestAgent = None;
        for agent in self.newGeneration:
            if agent.score > best:
                best = agent.score;
                bestAgent = agent;
        return bestAgent;

    def getBestEver(self):
        best = -1;
        bestAgent = None;
        for agent in self.bestInGenerations:
            if agent.score > best:
                best = agent.score;
                bestAgent = agent;
        return bestAgent;

    def getCurrentGenerationAverage(self):
        sum = 0;
        for agent in self.currentGeneration:
            sum = sum + agent.score;
        return sum/self.POPULATION_SIZE;

    def getNewGenerationAverage(self):
        sum = 0;
        for agent in self.newGeneration:
            sum = sum + agent.score;
        return sum/self.POPULATION_SIZE;

    #entry
    def __init__(self, data):

        self.currentGeneration = [0]*self.POPULATION_SIZE; #list with size POPULATION_SIZE
        self.newGeneration = [0]*self.POPULATION_SIZE; #list with size POPULATION_SIZE
        self.rawData = data;
