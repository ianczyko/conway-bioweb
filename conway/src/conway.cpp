/**
 * \file conway.cpp
 * \brief the C++ file with conway library.
 */
#include "conway.hpp"
#include <thread>
// #include <boost/thread/thread.hpp>

bool check_node(const Grid & grid, const int & row, const int & col){
    if(row < 0 || row >= static_cast<int>(grid.size())) return false;
    if(col < 0 || col >= static_cast<int>(grid[row].size())) return false;
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
CONWAY_DLL(Grid evolve(Grid grid, int threads) ) {
    const int rows = grid.size();
    const int cols = grid[0].size();
    Grid new_grid(rows, std::vector<bool>(cols, false));
	auto grid_processing = [&](int thread_no){ 
        // evenly distribute grid (vertically) per each thread to process in parrarel
        for(int i=(rows/threads)*thread_no; i<(rows/threads)*(thread_no+1); ++i){
            for(int j=0; j<cols; ++j){
                int alive_n = alive_neighbours(grid, i, j);
                if(alive_n == 3){
                    new_grid[i][j] = true; 
                }
                else if(grid[i][j] && alive_n == 2){
                    new_grid[i][j] = true; 
                }
            }
        }
    };
    std::vector<std::thread> thread_grp;
    for(int thread_no=0; thread_no<threads; thread_no++){
        thread_grp.emplace_back(grid_processing, thread_no);
    }
    for (auto& thread : thread_grp){
        thread.join();
    }
	return new_grid;
}

