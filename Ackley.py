import random
import math
import matplotlib.pyplot as plt

def createPopulation(amount):
    population = []
    for i in range(0, amount):
        aux = []
        for e in range(0, 30):
            aux = aux + [random.uniform(-15.0, 15.0)]
        population = population + [aux]
    return population

def individualFitness(c1, c2, c3, subject):
    sum1 = 0
    sum2 = 0
    for i in range(0,len(subject)):
        sum1 = sum1 + (subject[i] * subject[i])
        sum2 = sum2 + (math.cos(c3 * subject[i]))
    y = sum1/30
    a = math.sqrt(y)
    b = sum2/30
    fitness = -c1 * math.exp(-c2 * a) - math.exp(b) + c1 + 1
    return fitness

def cutAndCrossfill(parent1, parent2, cut):
    child = parent1[:cut] + parent2[cut:]
    return child

def xRandom(x, population):
    chosen = []
    for i in range(0, x):
        chosen = chosen + [random.randint(0, (len(population) - 1))]
    return chosen

def xTournament(population, chosen, x):
    best = chosen[:x]
    for i in range(x, len(chosen)):
        for e in range(0, x):
            if individualFitness(20.0, 0.2, (2 * math.pi), population[chosen[i] - 1]) < individualFitness(20.0, 0.2, (2 * math.pi), population[best[e] - 1]):
                best[e] = chosen[i]
                break
    return best

def xWost(population, chosen, x):
    worst = chosen[:x]
    for i in range(x, len(chosen)):
        for e in range(0, x):
            if individualFitness(20.0, 0.2, (2 * math.pi), population[chosen[i]]) > individualFitness(20.0, 0.2, (2 * math.pi), population[worst[e]]):
                worst[e] = chosen[i]
                break
    return worst

def APFwithBestSubject(population):
    fitness = 0.0
    bestFitness = 9999999.9
    bestIndex = 0
    for i in range(0, len(population)):
        x = individualFitness(20.0, 0.2, (2 * math.pi), population[i])
        if x < bestFitness:
            bestFitness = x
            bestIndex = i
        fitness = fitness + x
    fitness = fitness / (len(population))
    return fitness,bestFitness,bestIndex

def mutation(subject, x):
    for i in range(0, x):
        aux = random.randint(0, 29)
        subject[aux] = (subject[aux]) + (random.uniform(-1.0, 1.0))
        if subject[aux] < -15:
            subject[aux] = -15
        elif subject[aux] > 15:
            subject[aux] = 15

def replace(population, new, old):
    for i in range(0, len(new)):
        population[old[i] - 1] = new[i]

def test(iterations):
    population = createPopulation(100)
    average = []
    best = []
    x = 0
    y = 0
    z = 0

    for i in range(0, iterations):
        avgF, bestF, bestI = APFwithBestSubject(population)
        x = avgF
        y = bestF
        z = bestI
        #average = average + [avgF]
        #best = best + [bestF]
        print ("Media: " + str(avgF) + ", Melhor Individuo: " + str(bestF) + ", " + str(population[bestI]))
        chosen = xRandom(10, population)
        parents = xTournament(population, chosen, 5)

        childs = []
        childs = childs + [cutAndCrossfill(population[parents[0] - 1], population[parents[3] - 1], random.randint(8, 12))]
        childs = childs + [cutAndCrossfill(population[parents[3] - 1], population[parents[0] - 1], random.randint(8, 12))]
        childs = childs + [cutAndCrossfill(population[parents[1] - 1], population[parents[2] - 1], random.randint(8, 12))]
        childs = childs + [cutAndCrossfill(population[parents[2] - 1], population[parents[1] - 1], random.randint(8, 12))]

        old = xWost(population, chosen, 4)

        replace(population, childs, old)
        mutation(population[parents[4] - 1], random.randint(3, 5))


    #print ("Media: " + str(x) + ", Melhor Individuo: " + str(y) + ", " + str(population[z]))
    #xAxis = range(0, len(average))
    #plt.plot(xAxis, average, color='blue')
    #plt.plot(xAxis, best, color='red')
    #plt.xlabel('Iteracoes')
    #plt.ylabel('Fitness')
    #plt.show()

test(100000)



#x = []
#for i in range(0, 30):
#    x = x + [0]

#z = individualFitness(20.0, 0.2, (2 * math.pi), x)
#print z