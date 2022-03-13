
#this is an exercise in finding intersection numbers between two lists.
#for example: input1= [2,3,4,5,6,7]
#input 2=[2,3,4]
#output will be [2,3,4]

def intersection(list_1, list_2):
    intersect = []

    if len(list_1) > len(list_2):
        for i in range(0, len(list_2) - 1):
            # for every element in list2
            # check if they are in list1
            if list_1.count(list_2[i]):
                # if it can be found, append to intersect[]
                intersect.append(list_2[i])
    else:
        for i in range(0, len(list_1) - 1):
            if list_2.count(list_1[i]):
                intersect.append(list_1[i])
    if intersect:
        return list(set(intersect))
    else:
        return "There is no intersection."


if __name__ == "__main__":
    print("Enter integers for the two lists and stop by entering any non-integer.")
    try:
        input1 = []

        while True:
            input1.append(int(input("Please enter elements for the first list: ")))
    except:
        # handling exception by ending while loop
        list1 = input1

    try:
        input2 = []

        while True:
            input2.append(int(input("Please enter element for the second list: ")))
    except:
        list2 = input2

    print(intersection(list1, list2))
