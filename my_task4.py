import array
def knapsack(weights,capacity):
    weight = [0] * (capacity + 1)  # weight of all bars
    weight[0] = 1  # we start from zero weight, which can be collected 0 bars
    bar = [0] * (capacity + 1)  # weight of one bar
    for i in range(len(weights)):
        for k in range(capacity, weights[i] - 1, -1):
            if weight[k - weights[i]] == 1:
                weight[k] = 1
                bar[k] = weights[i]
    i = capacity
    while weight[i] == 0:
        i -= 1
    print(i)
# i - max weigth of weights in backpack
if __name__ == '__main__':
    #Initialising all variables
    print("Enter n")
    n = input()
    i = 0
    weights = array.array('i', (0 for i in range(0,int(n))))
    capacity = 0
    while i < int(n):
        print("Enter weight of w" + str(i) + " bag")
        weights[i] = int(input())
        i += 1
    print("Enter size of your knapsack:")
    capacity = int(input())
    knapsack(weights, capacity)
