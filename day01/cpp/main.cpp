//
// Created by Micha on 01.12.2020.
//

#include <iostream>
#include <fstream>
#include <array>
#include <vector>


const int year = 2020;

long findTwo(int target, const std::array<bool, year+1> &array, const std::vector<int> &vector)
{
    for (int value : vector)
    {
        int difference = target - value;
        if (difference < 0)
            continue;
        if (array.at(difference))
            return value * difference;
    }
    return -1;
}

long findThree(int target, const std::array<bool, year+1> &array, const std::vector<int> &vector)
{
    for (int value : vector)
    {
        int difference = target - value;
        long result = findTwo(difference, array, vector);
        if (result != -1)
            return result * value;
    }
    return -1;
}

int main()
{
    std::ifstream file;
    file.open("input01.txt");

    std::array<bool, year+1> array {false};
    std::vector<int> vector;

    int index;
    while(file >> index)
    {
        array.at(index) = true;
        vector.emplace_back(index);
    }

    std::cout << "Part 1: " << findTwo(year, array, vector) << std::endl;
    std::cout << "Part 2: " << findThree(year, array, vector) << std::endl;
}