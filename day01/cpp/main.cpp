//
// Created by Micha on 01.12.2020.
//

#include <iostream>
#include <fstream>
#include <array>
#include <list>


const int year = 2020;

long findTwo(int target, const std::array<bool, year+1> &array, const std::list<int> &list)
{
    for (int value : list)
    {
        int difference = target - value;
        if (array.at(difference))
            return value * difference;
    }
    return -1;
}

long findThree(int target, const std::array<bool, year+1> &array, const std::list<int> &list)
{
    for (int value : list)
    {
        int difference = target - value;
        long result = findTwo(difference, array, list);
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
    std::list<int> list;

    int index;
    while(file >> index)
    {
        array.at(index) = true;
        list.push_back(index);
    }

    std::cout << "Part 1: " << findTwo(year, array, list) << std::endl;
    std::cout << "Part 2: " << findThree(year, array, list) << std::endl;
}