# Charles Hong (csh6cw)
# 09/05/17
# hw2_p1.py
__author__ = 'Charles Hong'
__emailID__ = 'csh6cw'


# Identifies the maximum and minimum values of a mixed list by order of ascending ASCII values
def maxmin(list):
    min = 'Z'
    max = -999999
    for x in list:
        if str(x).upper() > str(max):
            max = x
        if str(x).upper() < str(min):
            min = x
    max_min = (max, min)
    if max_min == {'0', 'Z'}:
        return None
    else:
        return max_min


# Returns a list of common items by comparing each element of one list with that of the other list
def commonitems(list1, list2):
    common = []
    for x in list1:
        for y in list2:
            if x == y and x not in common:
                common.append(x)
    return common


# Returns a set of elements unique in only one of two lists--no duplicates are present
def notcommon_items(list1, list2):
    notcommon = []
    for x in list1:
        if x not in notcommon and x not in list2:
            notcommon.append(x)
    for y in list2:
        if y not in notcommon and y not in list1:
            notcommon.append(y)
    return notcommon


# Creates a dictionary that stores counts of how often each item occurs
def count_list_items(list):
    count_dict = {}
    for entry in list:
        if entry not in count_dict.keys():
            count_dict[entry] = 1
        else:
            count_dict[entry] += 1
    return count_dict


if __name__ == "__main__":
    list1 = [1, 3, 3]
    list2 = [3, 1, -2]
    list3 = ['Q', 'Z', 'C', 'A']
    list5 = [3, -2]
    assert maxmin(list1) == (3, 1)
    assert maxmin(list2) == (3, -2)
    assert maxmin(list3) == ('Z', 'A')
    assert commonitems(list1, list2) == [1,3]
    list4 = notcommon_items(list1, list2)
    assert notcommon_items(list1, list2) == [-2]
    assert count_list_items(list4) == {-2: 1}