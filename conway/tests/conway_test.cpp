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

BOOST_AUTO_TEST_SUITE( conway_test )

// BOOST_AUTO_TEST_CASE( Testttest )
// {
// 	BOOST_CHECK_EQUAL( ttest(), 12345 );
// }

BOOST_AUTO_TEST_SUITE_END()
