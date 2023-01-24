# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    # --------------------------------------------------------------
    # Exercise 1: Convert two lists into a dictionary
    # Exercise 2: Merge two Python dictionaries into one
    # Exercise 3: Print the value of key ‘history’ from the below dict
    # Exercise 4: Initialize dictionary with default values
    # Exercise 5: Create a dictionary by extracting the keys from a given dictionary
    # Exercise 6: Delete a list of keys from a dictionary
    # Exercise 7: Check if a value exists in a dictionary
    # Exercise 8: Rename key of a dictionary
    # Exercise 9: Get the key of a minimum value from the following dictionary
    # Exercise 10: Change value of a key in a nested dictionary
    # Exercise 1: Convert two lists into a dictionary

    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    # Expected Output
    # {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    # empty dictionary
    res_dict = dict()

    for i in range(len(keys)):
        res_dict.update({keys[i]: values[i]})
    print(res_dict)

    # Exercise 2: Merge two Python dictionaries into one
    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

    dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
    dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}

    dict3 = {**dict1, **dict2}
    print(dict3)

    # Expected Output
    # {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Forty': 40, 'Fifty': 50}

    # Exercise 3:
    sampleDict = {
        "class": {
            "student": {
                "name": "Mike",
                "marks": {
                    "physics": 70,
                    "history": 80
                }
            }
        }
    }

    # understand how to locate the nested key
    # sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
    # sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
    # sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

    # solution
    print(sampleDict['class']['student']['marks']['history'])

    # Expected Output

    # Exercise 4: Initialize dictionary with default values
    employees = ['Kelly', 'Emma']
    defaults = {"designation": 'Developer', "salary": 8000}

    res = dict.fromkeys(employees, defaults)
    print(res)

    # Individual data
    print(res["Kelly"])

    # Expected Output

    # Exercise 5: Create a dictionary by extracting the keys from a given dictionary
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}

    # keys to extract
    keys = ["name", "salary"]

    # new dict
    res = dict()

    for k in keys:
        # add current key with its va;ue from sample_dict
        res.update({k: sample_dict[k]})
    print(res)

    # Expected Output

    # Exercise 6: Delete a list of keys from a dictionary
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }
    # Keys to remove
    keys = ["name", "salary"]

    sample_dict = {k: sample_dict[k] for k in sample_dict.keys() - keys}
    print(sample_dict)

    # Expected Output

    # Exercise 7: Check if a value exists in a dictionary
    sample_dict = {'a': 100, 'b': 200, 'c': 300}
    if 200 in sample_dict.values():
        print('200 present in a dict')

    # Expected Output

    # Exercise 8: Rename key of a dictionary
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"
    }

    sample_dict['location'] = sample_dict.pop('city')
    print(sample_dict)

    # Expected Output

    # Exercise 9: Get the key of a minimum value from the following dictionary
    sample_dict = {
        'Physics': 82,
        'Math': 65,
        'history': 75
    }
    print(min(sample_dict, key=sample_dict.get))

    # Expected Output

    # Exercise 10: Change value of a key in a nested dictionary
    sample_dict = {
        'emp1': {'name': 'Jon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 6500}
    }

    sample_dict['emp3']['salary'] = 8500
    print(sample_dict)

