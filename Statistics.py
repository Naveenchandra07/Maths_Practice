#!/usr/bin/env python
# coding: utf-8

# In[3]:


def convert_to_number(inputVal):
    
    isNumber = True
    
    try:
        return float(inputVal)
    except ValueError:
        isNumber = False
    
    try:
        return complex(inputVal)
    except ValueError:
        isNumber = False
    
    try:
        return int(inputVal)
    except ValueError:
        isNumber = False
    
    if not isNumber:
        return 'Not a Number'


# In[5]:


def calculate_mean():
    #Calculation of Mean

    #Sample Valid and Invalid Input dataset

    #Valid Inputs: 
    #   2 8 9 11 15 3 6 8 1
    #   2 8 9 11 15 3 6.5 8 1
    #   2 8 9 11 15 3 64343.45454545 8 1
    #   2 8 9 11 15 33423432432432432423434344 6.5 8 1

    #Invalid Inputs:
    #   2 8 9 11 15 3 6 8 1 sdsd
    #   2 8 9 11 15s 3 6 8 1

    #Start of Program

    inputStr = input("Please provide input array of numbers : ")
    print("\nThis is the input array provided by you : " + inputStr + "\n")

    #Split input string into an array
    inputStrArr = inputStr.strip().split(" ")

    isOnlyNumber = True

    #Input array which stores numbers
    inputNumArr = []

    for eachStr in inputStrArr:
        eachNumber = convert_to_number(eachStr)
        if eachNumber == 'Not a Number':
            print("Please provide only numbers as input!")
            isOnlyNumber = False
            break
        else:
            inputNumArr.append(eachNumber)

    #Execute next steps only if we have valid input data set
    if isOnlyNumber and len(inputNumArr) > 0:

        #find the count of numbers in array
        countOfNumbers = len(inputNumArr)

        #variable which holds total sum of input numbers
        totalSum = 0

        #loop though array to find the sum of numbers
        for x in inputNumArr:
            totalSum += x

        #calculate mean using the total sum and count of numbers (totalSum/countOfNumbers)
        mean = totalSum/countOfNumbers

        print("Count of the input numbers = " + str(countOfNumbers))
        print("Total sum of input numbers = " + str(totalSum))
        print("Mean of the numbers given = " + str(mean))


# In[6]:


def calculate_median():
    #Calculation of Median
    #To calculate the middle most value in the series.

    #Inputs
    #1 2 3 4 5 6 7 8 9 10
    #1 2 3 4 5 6 7 8 9

    #Start of Program

    inputStr = input("Please provide input array of numbers : ")
    print("\nThis is the input array provided by you : " + inputStr + "\n")

    #Split input string into an array
    inputStrArr = inputStr.strip().split(" ")

    isOnlyNumber = True

    #Input array which stores numbers
    inputNumArr = []

    for eachStr in inputStrArr:
        eachNumber = convert_to_number(eachStr)
        if eachNumber == 'Not a Number':
            print("Please provide only numbers as input!")
            isOnlyNumber = False
            break
        else:
            inputNumArr.append(eachNumber)

    #Execute next steps only if we have valid input data set
    if isOnlyNumber and len(inputNumArr) > 0:
        countOfNumbers = len(inputNumArr)

        inputNumArr.sort()

        median = 0

        if(countOfNumbers % 2 == 0):
            median = (inputNumArr[int(countOfNumbers/2)] + inputNumArr[int(countOfNumbers/2) + 1])/2
        else:
            median = inputNumArr[int(countOfNumbers/2)]

        print("Count of the input numbers = " + str(countOfNumbers))
        print("Median of the numbers given = " + str(median))


# In[7]:


def calculate_mode():
    #Calculation of Mode
    #The number which appers most in the series

    #Sample inputs
    #1 2 2 2 3 5 4 3 5 6 5

    #Start of Program

    inputStr = input("Please provide input array of numbers : ")
    print("\nThis is the input array provided by you : " + inputStr + "\n")

    #Split input string into an array
    inputStrArr = inputStr.strip().split(" ")

    isOnlyNumber = True

    #Input array which stores numbers
    inputNumArr = []

    for eachStr in inputStrArr:
        eachNumber = convert_to_number(eachStr)
        if eachNumber == 'Not a Number':
            print("Please provide only numbers as input!")
            isOnlyNumber = False
            break
        else:
            inputNumArr.append(eachNumber)

    #Execute next steps only if we have valid input data set
    if isOnlyNumber and len(inputNumArr) > 0:
        countOfNumbers = len(inputNumArr)

        inputNumArr.sort()

        mode = 0

        map_num_occurance = {}

        for number in inputNumArr:
            if number in map_num_occurance:
                map_num_occurance[number] = map_num_occurance[number] + 1
            else:
                map_num_occurance[number] = 1

        list_most_occured_num = []
        list_most_occured_num.append(inputNumArr[0])
        highest_occurance = map_num_occurance[most_occured_num]

        for number in map_num_occurance:
            if(map_num_occurance[number] > highest_occurance):
                highest_occurance = map_num_occurance[number]
                list_most_occured_num[0] = number
            elif(number != inputNumArr[0] and map_num_occurance[number] == highest_occurance):
                list_most_occured_num.append(number)

        print("Count of the input numbers = " + str(countOfNumbers))
        print("Most occured time = " + str(highest_occurance))
        print("Mode of the numbers given = " + str(list_most_occured_num))


# In[ ]:




