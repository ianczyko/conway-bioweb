/**
 * \file conway.cpp
 * \brief the C++ file with conway library.
 */
#include "conway.hpp"

//implementation
CONWAY_DLL(Grid evolve(Grid grid) ) {
	const int rows = grid.size();
    const int cols = grid[0].size();
	Grid new_grid(rows, std::vector<bool>(cols, false));
	for(int i=0; i<rows; ++i){
        for(int j=0; j<cols; ++j){
            new_grid[i][j] = !grid[i][j];
        }
    }
	return new_grid;
}

