inp = input("input a genre: ")
class Song:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        
    def __repr__(self):
        return "Item value: {0}, weight: {1}".format(self.value, self.weight)

def get_genre_class(g):
    return 1



song_list = []
data_list = []

for item in song_list:
    data_list.append(Song(get_genre_class(item),item))





pop_fitness = [get_genre_class(g) for g in population]

#keep track of mean fitness over time
mean_fitnesses = [mean(pop_fitness)]


for generation in range(num_generations):
    pop_fitness = [get_genre_class(g) for g in population]
    population = random.choices(population, k=pop_size, weights=pop_fitness)
    population = [mutate_genotype(g, prob_mut = 0.15) for g in population]
    
    #record new mean population fitness and knapsack values
    mean_fitnesses.append(mean(pop_fitness))
    mean_values.append(mean([get_genotype_value(ind) for ind in population]))