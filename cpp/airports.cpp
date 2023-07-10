#include "airports.h"
#include "IATAports.h"

using namespace std;

Airports::Airports() {
    string text = "";
    int count = 0;
    while (IATAports >> text) {
        string code, country = "";
        if (count % 2 == 0) { //code, only even words will be an airport
            code = text;
        } else { //country
            country = text;
        }
        
        ports.emplace(code, country);
        count++;
    }

}

string Airports::country(string code) {
    return ports.at(code);
}