def GeneticAlgorithm:

 #Agents are individuals that makes up populations.

 #Agents have their DNA as 'localeSequence', fitness as ln(x) * (100) floored to significance of 2
 #This allows for an exponentially increasing score for lower distance travelled.

 #DNA is made up of two main parts:
 #starting locale: important to seperate as agents have to return to this locale at the end
 #localesequence: sequence of travel

 #initial selection is random sequence of locale with no bias and a random starting locale

 #selectin is done using weighted random selection depending on the agent's score

 #crossover is done without bias, randomly switching targeted locale for at an index
 #crossover happens for each index of the localesequence 50% chance for either parent's item to be selected
 #crossover chance depends on the global variable of this class 'CROSSOVER_CHANCE'


    POPULATION_SIZE = 25;
    MAX_GENERATION = 9999;
    MUTATION_RATE = 0.1;
    MUTATION_STRENGTH = 1;

    currentGeneration = [];
    newGeneration = [];
    rawData = [];

    def __init__(self, data):
        rawData = data;


    def buildInitialPopulation:


    def BuildNewGeneration:

    def selection:

    def crossOver:

    def mutation:
