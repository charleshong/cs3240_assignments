# Charles Hong (csh6cw)
# 08/29/17
# hw1.py
__author__ = 'Charles Hong'
__emailID__ = 'csh6cw'
import math


class Location(object):
    # Constructor
    def __init__(self, category, x, y):
        self.category = category
        self.x = float(x)
        self.y = float(y)
        self.distance = 0

    # Setter for distance
    def setDistance(self, dest_x, dest_y):
        self.distance = math.sqrt(pow(abs(float(dest_x) - self.x), 2) + pow(abs(float(dest_y) - self.y), 2))

if __name__ == "__main__":
    # Asks for inputs
    k_value = int(input("Enter k: "))
    M_value = int(input("Enter the number of entries to be read (M): "))
    file_name = input("Enter the file name: ")

    # Avoids the case where k > M so that the code
    if k_value > M_value:
        k_value = M_value

    # Reads in points that are already classified
    classified = []
    data_file = open(file_name, 'r')
    for line in range(0, M_value):
        try:
            entry = data_file.readline().split()
            obj = Location(entry[0], entry[1], entry[2])
            classified.append(obj)
        except IndexError:
            print("Not enough data points in the given file! Try a different file or a different M-value.")
            exit(-1)
    data_file.close()

    # Reads in new unclassified points
    unclassified = ' '
    while unclassified != '1 1' and unclassified != '1.0 1.0':
        unclassified = input('Enter unclassified values without parentheses or commas(x y): ')
        if unclassified == '1 1' or unclassified == '1.0 1.0':
            break
        unclassified = unclassified.split()
        try:
            if unclassified[0] is None or unclassified[1] is None:
                raise IndexError
            u_x = unclassified[0]
            u_y = unclassified[1]
            # Print the set of k data items that are closest to each unclassified data-item in non-decreasing order
            for objects in classified:
                objects.setDistance(float(u_x), float(u_y))
            cat1_count = 0
            cat2_count = 0
            cat1_sum = 0
            cat2_sum = 0
            classified.sort(key=lambda x:x.distance)
            category1 = classified[0].category
            category2 = ''
            for i in range(0, k_value):
                category = classified[i].category
                if category1 == category:
                    cat1_count += 1
                    cat1_sum += classified[i].distance
                else:
                    category2 = category
                    cat2_count += 1
                    cat2_sum += classified[i].distance
                print(category + ' ' + str(classified[i].x) + ' ' + str(classified[i].y) + ' ' + str("%.1f" % classified[i].distance))

            # Print which category this data-item would be assigned to
            if cat1_count < cat2_count:
                print("Data item assigned to: " + str(category1))
            else:
                print("Data item assigned to: " + str(category2))

            # Print the average distance of the k-nearest-neighbors to the data-item for each of the two categories
            cat1_avg = cat1_sum / cat1_count
            print("Average distance to cat1 items: " + str("%.2f" % cat1_avg))
            if cat2_count == 0:
                print("There are no cat2 items within k of the unclassified point.")
            else:
                cat2_avg = cat2_sum / cat2_count
                print("Average distance to cat2 items: " + str("%.1f" % cat2_avg))
        except IndexError:
            print("Not enough arguments! Make sure you are formatting your answers properly.")
            unclassified = '1 1'
