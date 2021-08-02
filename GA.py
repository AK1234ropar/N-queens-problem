import random
import copy
import math
import numpy as np

"""reference help taken from:https://github.com/waqqasiq/n-queen-problem-using-genetic-algorithm and
"""

result=[]

    

def fitness(individual):#number of  attacking queen pairs
    collisions1= abs(len(individual))
    collisions1-=len(np.unique(individual))
    collisions2 = 0

    n = len(individual)
    ld = [0] * 2*n
    rd = [0] * 2*n
    for i in range(n):
        ld[i + individual[i] - 1] += 1
        rd[n - i + individual[i] - 2] += 1

    
    for i in range(2*n-1):
        c = 0
        if ld[i] > 1:
            c += ld[i]-1
        if rd[i] > 1:
            c += rd[i]-1
        collisions2 += c / (n-abs(i-n+1))
    
    return int((collisions1 + collisions2))


def crossover(individual1, individual2):
    n = len(individual1)
    c = random.randint(0, n - 1)
    return individual1[0:c] + individual2[c:n]


def crossover(individual1, individual2):
    n=len(individual1)
    c = random.randint(0,n-1)
    x1=individual1[0:c]
    y1=individual1[c:n]
    x2=individual1[0:c]
    y2=individual1[c:n]
    offspring1=x1+y2
    offspring2=x2+y1
    return (offspring1,offspring2)





def mutation(individual):
    n = len(individual)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def generate_individual(n):
    result = list(range(1, n + 1))
    np.random.shuffle(result)
    return result

class Genetic(object):

    def __init__(self, n ,pop_size,mutation_prob,crossover_prob):
        #initializing a random individuals with size of initial population entered by user
        self.queens = []
        for i in range(pop_size):
            self.queens.append(generate_individual(n))

    #generating individuals for a single iteration of algorithm
    def generate_population(self, random_selections=5):
        candid_parents = []
        candid_fitness = []
        my_dict={}
        #getting individuals from queens randomly for an iteration
        for i in range(random_selections):
            candid_parents.append(self.queens[random.randint(0, len(self.queens) - 1)])
            candid_fitness.append(fitness(candid_parents[i]))
            lst=candid_parents[i]
            fitval=candid_fitness[i]
            my_dict.update({fitval:lst})
        sorted_fitness = copy.deepcopy(candid_fitness)
        #sort the fitnesses of individuals
        sorted_fitness.sort()
        #getting 2 first individuals(min attackings)
        individual1=my_dict[sorted_fitness[0]]
        individual2=my_dict[sorted_fitness[1]]
        #crossover the two parents
        if crossover_prob <=  random.random(0.0, 1.0):
          child1,child2=crossover(individual1,individual2)
        else:
           child1,child2 =individual1,individual2
     
        # mutation
        if mutation_prob <=  random.random(0.0, 1.0):
            child1 = mutation(child1)
        else:
            child1 = child1
            
        if mutation_prob <=  random.random(0.0, 1.0):
            child2 = mutation(child2)
        else:
            child2 = child2
        fitness_child1=fitness(child1)
        fitness_child2=fitness(child2)
        #in code below check if each child is better than each one of queens individuals, set that individual the new child
        for i in self.queens:
             flag=1
             if (fitness(i)<=fitness_child1):
                flag=0
                break
        if(flag==1):       
          self.queens.append(child1)
          
        for i in self.queens:
             flag=1
             if (fitness(i)<=fitness_child2):
                flag=0
                break
        if(flag==1):       
          self.queens.append(child2)  
          
        

    def finished(self):
          lst=[0,[]]
          for i in self.queens:
            if(fitness(i)==0):
              lst[0]=1
              lst[1]=i
             
          return lst
            
              
            #we check if for each queen there is no attacking(cause this algorithm should work for n queen,
            # it was easier to use attacking pairs for fitness instead of non-attacking)
            
    
    def start(self, random_selections=5):
        #generate new population and start algorithm until number of attacking pairs is zero
        while not self.finished()[0]:
            self.generate_population(random_selections)
        final_state = self.finished()
        print(('Solution : ' + str(final_state[1])))
        print("Fitness of solution i.e. is Number of Conflicts are equal to= "+str(fitness(final_state[1])))
        


nq=[8,16,20,24,28]
ps=[1000,2000,3000,4000,5000]
cp=[0.80,0.81,0.82,0.83,0.84]
mp=[0.01,0.02,0.03,0.04,0.045]

@profile
def program():
 for i in range(0,5):
  
  algorithm = Genetic(n=nq[i],pop_size=ps[i],mutation_prob=mp[i],crossover_prob=cp[i])
  algorithm.start()
  
if __name__ == "__main__":
    program()
    
