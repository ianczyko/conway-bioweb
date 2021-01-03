/// @file test02_services.js
/// @brief client unit tests, check the service calling

var injector = angular.injector(['ng', 'myApp']);
var srv = injector.get('srvInfo')
var srv2 = injector.get('srvCommands')
srv.baseURL = "http://127.0.0.1:50008/"; //port for srv.py mock service
srv2.baseURL = "http://127.0.0.1:50008/"; //port for srv.py mock service

module( "test02_services", {
    setup: function() {
	    this.$scope = injector.get('$rootScope').$new();
    },
    teardown: function() { }
});

function functionResponseCheck(r) {
    //ok( 1 == "1", "function response check");
	ok( typeof(r) != undefined && r.ala == "ala", "srv.py non-empty response testing" );
}

asyncTest( "service getCppNumber", function() {
    expect( 1 );
	var srv = injector.get('srvInfo');
	srv.evolve([[true]], 1, functionResponseCheck);
    setTimeout(
		function() {
			start();
		},
		100);
});




