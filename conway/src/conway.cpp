/**
 * \file conway.cpp
 * \brief the C++ file with conway library.
 */
#include "conway.hpp"

bool check_node(const Grid & grid, const int & row, const int & col){
    if(row < 0 || row >= grid.size()) return false;
    if(col < 0 || col >= grid[row].size()) return false;
    return grid[row][col];
}

int alive_neighbours(const Grid & grid, const int & row, const int & col){
    int sum = 0;
    for(int relative_row=-1; relative_row<=1; ++relative_row){
        for(int relative_col=-1; relative_col<=1; ++relative_col){
            if(relative_row==0 && relative_col==0) continue;
            if(check_node(grid, row+relative_row, col+relative_col)) sum++;
        }
    }
    return sum;
}

//implementation
CONWAY_DLL(Grid evolve(Grid grid) ) {
	const int rows = grid.size();
    const int cols = grid[0].size();
	Grid new_grid(rows, std::vector<bool>(cols, false));
	for(int i=0; i<rows; ++i){
        for(int j=0; j<cols; ++j){
            int alive_n = alive_neighbours(grid, i, j);
            if(alive_n == 3){
                new_grid[i][j] = true; 
            }
            if(grid[i][j] && alive_n == 2){
                new_grid[i][j] = true; 
            }
        }
    }
	return new_grid;
}

