MAKEFLAGS += -L

CXX      = clang++
CXXFLAGS = -g3 -Wall -Wextra -Wpedantic -Wshadow
LDFLAGS  = -g3 

country_sorter: main.o airports.o
	${CXX} ${CXXFLAGS} $@ $^

main.o: main.cpp airports.h
	${CXX} ${LDFLAGS} -c $<

airports.o: airports.cpp airports.h IATAports.h
	${CXX} ${LDFLAGS} -c $<