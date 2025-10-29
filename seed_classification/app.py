# import math module for mathematical operations
import math

# input data
trainingSet = [ (3, 7, 2, 'red'), (2, 6, 3, 'red'), (4, 8, 2, 'red'), (5, 9, 3, 'red'), (3, 5, 2, 'red'), (6, 4, 5, 'yellow'), (7,
3, 6, 'yellow'), (8, 2, 5, 'yellow'), (6, 6, 4, 'yellow'), (7, 5, 5, 'yellow'), (9, 3, 7, 'blue'), (10, 4, 6,
'blue'), (8, 5, 8, 'blue'), (9, 6, 7, 'blue'), (10, 5, 7, 'blue')]
test_sample1 = (3,7,2, 'unknown')
test_sample2 = (7,3,7, 'unknown')
k = 7

# function for finding euclidean distance, takes two inputs between which will find the distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)


# the main function to do all the logic for predicting the colour
def classifyFlower(trainingSet, testSample, k):
    distances = []

    # find euclidean distance and store them in distances list
    for seed in trainingSet:
        dist = euclidean_distance(testSample, seed)
        distances.append((dist, seed))

    # sort distances manually through bubble sort
    n = len(distances)
    for i in range(n):
        for j in range(0, n - i - 1):
            if distances[j][0] > distances[j + 1][0]:
                distances[j], distances[j + 1] = distances[j + 1], distances[j]

    # finding the 'K' nearest neighbors
    closestK = [seed for _, seed in distances[:k]]

    # to find how many times a specific colour appears and what are the distances of that colour
    colour_counts = {}
    colour_distances = {}

    for i in range(k):
        _, _, _, colour = closestK[i]
        dist = distances[i][0]
        colour_counts[colour] = colour_counts.get(colour, 0) + 1
        colour_distances.setdefault(colour, []).append(dist)

    # find colours with maximym count
    max_count = max(colour_counts.values())
    tied_colours = [c for c, count in colour_counts.items() if count == max_count]

    # Tie-breaking by smallest average distance
    if len(tied_colours) > 1:
        avg_dist = {c: sum(colour_distances[c]) / len(colour_distances[c]) for c in tied_colours}
        min_avg = min(avg_dist.values())
        tied_colours = [c for c, avg in avg_dist.items() if avg == min_avg]

    # Final result (if still tied, return first)
    predicted_colour = tied_colours[0]
    return predicted_colour

# write a function to classify based on user entered data
def customClassification():
    while True:
        try:
            length = float(input("\nEnter seed length: "))
            width = float(input("Enter seed width: "))
            thickness = float(input("Enter seed thickness: "))
            k = int(input(f"Enter k (1 to {len(trainingSet)}): "))

            # check if k is greater than 0 and less then the trainingSet
            if k <= 0 or k > len(trainingSet):
                print(f"Error: k must be between 1 and {len(trainingSet)}.")
                continue

            user_sample = (length, width, thickness, 'unknown')
            prediction = classifyFlower(trainingSet, user_sample, k)
            print(f"Predicted flower colour: {prediction}")
            break

        except ValueError:
            print("Invalid input! Please enter numeric values for measurements and integer for k.")

pc1 = classifyFlower(trainingSet, test_sample1, k)

pc2 = classifyFlower(trainingSet, test_sample2, k)


print(pc1)
print(pc2)
customClassification()
print('Student ID - 100536294')


# reflection
# I solved this problem by step by step. first of all i define a separate function for calculating the euclidean distance between two points. I choose to define a separate function for finding the distances as i could solved it right in the classifyFlower function but writing a separate function for this is make my code more cleaner and moduler. It looks difficult at the first to do sorting manually but i understand the problem and make it happen.