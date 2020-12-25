//
// Created by Micha on 25.12.2020.
// test

#include <map>
#include <iostream>
#include <fstream>
#include <array>
#include <list>

struct Coord
{
    int x, y;
    Coord(int x, int y) : x(x), y(y) {}
    friend bool operator==(const Coord& coord1, const Coord& coord2)
    {
        return coord1.x == coord2.x and coord1.y == coord2.y;
    }
    friend bool operator<(const Coord& coord1, const Coord& coord2)
    {
        if (coord1.x != coord2.x)
        {
            return coord1.x < coord2.x;
        }
        else
        {
            return coord1.y < coord2.y;
        }
    }

};

struct hash_coord
    {
        size_t operator()(const Coord & coord) const
        {
            return std::hash<int>()(coord.x) ^ std::hash<int>()(coord.y);
        }
    };

typedef std::map<Coord, std::array<bool, 2>> ordered_tiles;
//typedef std::map<Coord, std::array<bool, 2>, hash_coord, std::equal_to<>> ordered_tiles;

unsigned int countSubstring(std::string str, std::string sub)
{
    size_t pos = 0;
    unsigned int count = 0;
    while (((pos = str.find(sub, pos)) != str.npos))
    {
        ++count;
        ++pos;
    }
    return count;
}

Coord convertDirToXY(std::string dir)
{
    unsigned int nw = countSubstring(dir, "nw");
    unsigned int ne = countSubstring(dir, "ne");
    unsigned int sw = countSubstring(dir, "sw");
    unsigned int se = countSubstring(dir, "se");
    unsigned int w = countSubstring(dir, "w") - nw - sw;
    unsigned int e = countSubstring(dir, "e") - ne - se;
    unsigned int z = nw - se;
    unsigned int x = e - w - z;
    unsigned int y = ne - sw + z;
    return Coord(x, y);
}

int countNeighbours(const Coord& tile, ordered_tiles& tiles, const bool& current)
{
    // Nachbarn berechnen
    std::array<Coord, 6> coords =
    {
    Coord(tile.x+1, tile.y),        // e
    Coord(tile.x-1, tile.y),        // se
    Coord(tile.x, tile.y+1),        // sw
    Coord(tile.x+1, tile.y-1),   // w
    Coord(tile.x, tile.y-1),        // nw
    Coord(tile.x-1, tile.y+1)    // ne
    };

    int count = 0;
    for (const Coord& coord: coords)
    {
        // Überprüfe, ob Nachbar bereits existiert
        if (tiles.find(coord) != tiles.end())
        {
//            std::cout << "if" << std::endl;
            count+= tiles[coord][current];
        }
        // Wenn nicht wird der Nachbar weiß erstellt
        else //if (create)
        {
//            std::cout << "else" << std::endl;
            tiles[coord] = {false, false};
        }
    }
    return count;
}

int main()
{
    ordered_tiles tiles;
    bool current = false;


    // Part 1
    std::ifstream myfile("input.txt");
    for( std::string line; getline( myfile, line ); )
    {
        Coord tile = convertDirToXY(line);
        // Falls die Tile bereits existiert wird die Farbe geflippt
        if (tiles.find(tile) != tiles.end())
        {
            tiles[tile][current] = !tiles[tile][current];
        }
        // Ansonsten wird die Tile mit Farbe schwarz erstellt
        else
        {
            tiles[tile] = {true, true};
        }
    }

    int count = 0;
    for (auto key_value : tiles)
    {
        count += key_value.second[current];
    }
    std::cout << "Part 1: " << count << std::endl;

    // Part 2
    // Einmal die Nachbarn aller Tiles erstellen
    std::list<Coord> list;
    for(auto key_value : tiles)
    {
        list.emplace_back(key_value.first);
    }

    for (Coord tile : list)
    {
        countNeighbours(tile, tiles, current);
    }
    for (int i=0; i<100; i++)
    {
        // Items aus der Map kopieren
        std::list<Coord> list;
        for(auto key_value : tiles)
        {
            list.emplace_back(key_value.first);
        }

        for (auto key : list)
        {
            bool color = tiles[key][current];
            int counter = countNeighbours(key, tiles, current);
            if (color and (counter == 0 or counter > 2))
            {
                tiles[key][not current] = false;
            }
            else if ((not color) and counter == 2)
            {
                tiles[key][not current] = true;
            }
            else
            {
                tiles[key][not current] = color;
            }
        }
        current = not current;
    }

    count = 0;
    for (auto key_value : tiles)
    {
        count += key_value.second[current];
    }
    std::cout << "Part 2: " << count << std::endl;
}