/// @file test01_basic.js
/// @brief client unit tests, check the qunit testing library

module( "test01_basic", {
  setup: function() { },
  teardown: function() { }
});

test( "trivial test for qunit", function() {
    ok( 1 == "1", "Passed!" );
});

test( "please remember to copy body tag from src/index.html into tests/qu-test.html every time index.html is changed!", function() {
    ok( 1 == "1", "Passed!" );
});
