/**
   conway library tests
   defines 'main' for cpp unit test
**/

#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MAIN

#include <boost/test/unit_test.hpp>

#include "../src/conway.hpp"

using namespace boost;
using boost::unit_test::test_suite;

BOOST_TEST_DONT_PRINT_LOG_VALUE(Grid)

BOOST_AUTO_TEST_SUITE( conway_test )

BOOST_AUTO_TEST_CASE( AllDead )
{
   int rows = 3;
   int cols = 3;
   Grid initial(rows, std::vector<bool>(cols, false));
	BOOST_CHECK_EQUAL( evolve(initial, 1), initial );
}
BOOST_AUTO_TEST_CASE( LonelinessDeath )
{
   int rows = 3;
   int cols = 3;
   Grid initial(rows, std::vector<bool>(cols, false));
   Grid expected(rows, std::vector<bool>(cols, false));
	initial[1][1] = true;
   auto evolved = evolve(initial, 1);
   BOOST_CHECK_EQUAL( evolved, expected );
}
BOOST_AUTO_TEST_CASE( OverpopulationDeath )
{
   int rows = 3;
   int cols = 3;
   Grid initial(rows, std::vector<bool>(cols, true));
	initial[0][0] = false;
	initial[0][2] = false;
	initial[2][2] = false;
	initial[2][0] = false;
   auto evolved = evolve(initial, 1);
   Grid expected(rows, std::vector<bool>(cols, true));
   expected[1][1] = false;
   BOOST_CHECK_EQUAL( evolved, expected );
}
BOOST_AUTO_TEST_CASE( Birth )
{
   // using a Blinker (Period 2 oscillator)
   int rows = 3;
   int cols = 3;
   Grid initial(rows, std::vector<bool>(cols, false));
	initial[0][1] = true;
	initial[1][1] = true;
	initial[2][1] = true;
   auto evolved = evolve(initial, 1);
   Grid expected(rows, std::vector<bool>(cols, false));
   expected[1][0] = true;
   expected[1][1] = true;
   expected[1][2] = true;
   BOOST_CHECK_EQUAL( evolved, expected );
}

BOOST_AUTO_TEST_SUITE_END()
