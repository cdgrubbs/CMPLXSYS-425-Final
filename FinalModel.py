class Song:
    def __init__(self, fitness, array, wav):
        self.fitness = fitness
        self.array = array
        self.wav = wav

    def set_fitness():
        # TODO:
        return
    
    def mutate():
        # TODO:
        return

    def __repr__(self):
        return "Item array: {0}, fitness: {1}".format(self.array, self.fitness)

def recombination(a, b):
    a_len = len(a)
    b_len = len(b)
    
    a_to_recomb = a_len / 10.0
    b_to_recomb = b_len / 10.0
    
    pool[a_to_recomb + b_to_recomb]
    
    a_chosen[a_to_recomb]
    b_chosen[b_to_recomb]
    
    while len(a_chosen) != a_to_recomb:
        index = random.randint(0, a_len)
        if (a_chosen.count(index) == 0):
            a_chosen.append(index)
            pool.append(a[index])

    while len(b_chosen) != b_to_recomb:
        index = random.randint(0, a_len)
        if (b_chosen.count(index) == 0):
            b_chosen.append(index)
            pool.append(b[index])

    for i in range(len(a_chosen)):
        index = random.randint(0, len(pool))
        a[a_chosen[i]] = pool[index]

    for i in range(len(b_chosen)):
        index = random.randint(0, len(pool))
        b[b_chosen[i]] = pool[index]
    return {a, b}

song_list = []
data_list = []

for item in song_list:
    data_list.append(Song(get_genre_class(item),item))

population = songs[]
for generation in range(num_generations):
    for song in population:
        song.set_fitness()
    # Create X many new songs by re arranging beats

    # Mutate new songs
    for song in population:

    # Keep it goin
Bash = "rm -rf /WorkingFolder/*.png"
import subprocess
process = subprocess.Popen(Bash.split, stdout=subprocess.PIPE)
output, error = process.communicate()
