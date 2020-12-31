/**
 * \file conwaypy.cpp
 * \brief the Python interface for conway library.
 */

#if defined(_MSC_VER) && (_MSC_VER >= 1400)
//msvc disable warnings for Boost.Python
#pragma warning(disable:4100)
#pragma warning(disable:4127)
#pragma warning(disable:4244)
#pragma warning(disable:4267)
#pragma warning(disable:4512)
#endif

#include <vector>
#include <boost/python.hpp>
#include <boost/python/object.hpp>
#include <boost/python/stl_iterator.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

#include "conway.hpp"

namespace Py = boost::python;

/**
 * Converts Python's list (of lists) to C++'s Grid (vector<vector<bool>>)
 */
Grid to_cpp_grid(const Py::list & py_grid){
    const int rows = Py::len(py_grid);
    const int cols = Py::len(py_grid[0]);
    Grid grid(rows, std::vector<bool>(cols, false));
    for(int i=0; i<rows; ++i){
        for(int j=0; j<cols; ++j){
            grid[i][j] = py_grid[i][j];
        }
    }
    return grid;
}

/**
 * Converts C++'s Grid (vector<vector<bool>>) to Python's list (of lists)
 */
Py::list to_py_grid(const Grid & cpp_grid){
    const int rows = cpp_grid.size();
    const int cols = cpp_grid[0].size();
    Py::list py_list;
    for(int i=0; i<rows; ++i){
        Py::list row;
        for(int j=0; j<cols; ++j){
           row.append(cpp_grid[i][j]);
        }
        py_list.append(row);
    }
    return py_list;
}

/**
 * evolve() adapter. Adapts Python's list of lists to c++'s vector of vectors
 */
Py::list evolve_adapter(Py::list grid){
    auto cpp_grid = to_cpp_grid(grid);
    cpp_grid = evolve(cpp_grid);
    return to_py_grid(cpp_grid);
}

/**
 * Python wrapper using Boost.Python
 */
BOOST_PYTHON_MODULE( conway ) {
    //! exports evolve to Python
    Py::def( "evolve", evolve_adapter);
}
