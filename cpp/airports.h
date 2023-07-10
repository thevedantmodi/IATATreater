/* airports.h

Vedant Modi
07/03/2023

Class definition for all IATA airports
 */

#include <string>
#include <map>
#include <utility>

#ifndef __AIRPORTS__H
#define __AIRPORTS__H

class Airports {
    public:
        Airports();
        ~Airports();
        std::string country(std::string code);

    private:
        std::map<std::string,std::string> ports;
};


#endif