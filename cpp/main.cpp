#include <iostream>
#include <fstream>
#include "airports.h"

using namespace std;

int main(int argc, char *argv[]) {

    if (argc < 3) {
        cerr << "Usage: ./country_sorter [input file] [output directory]";
        exit(EXIT_FAILURE);
    }

    Airports all_airports;

    all_airports.country("BOS");




    return 0;
}
