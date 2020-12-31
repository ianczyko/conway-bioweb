/**
 * \file conway.hpp
 * \brief the C++ conway library interface
 */
 
#ifndef CONWAY_HPP
#define CONWAY_HPP

#if defined(_MSC_VER) && (_MSC_VER >= 1400)
//msvc disable warnings for sheduler_ and history_ member
#pragma warning(disable:4251)
#endif


#ifdef CONWAY_EXPORTS
/** Workaround for Windows DLL library exports */
#define CONWAY_DLL(X) __declspec(dllexport)X
#else
/** Workaround for Unix Shared Library exports */
#define CONWAY_DLL(X) X
#endif

#include <vector>
using Grid = std::vector<std::vector<bool>>;

//! Evolve a grid by 1 generation.
CONWAY_DLL( Grid evolve(Grid); )


#endif //CONWAY_HPP
