def findmax(numbers):
    maxim=numbers[0]
    for number in numbers:
        if number>maxim:
            maxim=number
    return maxim 