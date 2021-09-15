import array
def knapsack(weights, capacity):
    weight_set = set([0])
    for weight in weights:
        temp = set()
        for curr_sum in weight_set:
            if weight + curr_sum == capacity:
                return capacity
            elif weight + curr_sum < capacity:
                temp.add(weight + curr_sum)
        weight_set.update(temp)
    return max(weight_set)
if __name__ == '__main__':
    print("Enter n")
    n = input()
    i = 0
    weights = array.array('i', (0 for i in range(0,int(n))))
    capacity = 0
    while i < int(n):
        print("Enter weight of w" + str(i) + " bag")```
        weights[i] = int(input())
        i += 1
    print("Enter size of your knapsack:")
    capacity = int(input())
    print(knapsack(weights, capacity))