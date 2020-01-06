from Agent import Agent;
from Agent import RandomAgentBuilder;

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
        self.selection();
        self.crossOver();
        self.mutation();
        return;

    #weighted random selection alghorithm depending on the score of the agents
    def selection(self):
        #print(self.currentGeneration[0].localeSequence)
        print(self.currentGeneration[0].calculateScore(self.rawData));
        return;

    def crossOver(self):
        return;

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
