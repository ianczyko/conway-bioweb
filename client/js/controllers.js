/// @file controllers.js
/// @brief AngularJS controllers

angular.module('myAppControllers', [])
	.controller('settingsController', //client static settings
				['$scope',
				 '$translate',
				 function($scope, $translate) {
					 $scope.langs = ['en', 'pl'];
					 $scope.changeLanguage = function (lang) {
						 $translate.use(lang);
					 };
				 }])
	// .controller('versionController', //versions of system modules
	// 			['$scope',
	// 			 'srvInfo',
	// 			 function($scope, srvInfo) {
	// 				 srvInfo.getVersion(
	// 				 	 function(data) {
	// 				 		 $scope.server_ver = data;
	// 				 	 });
	// 				 $scope.client_ver = client_ver_major.toString() + '.' + client_ver_minor.toString() + '.' + client_ver_compilation.toString(); //from version.js file
	// 			 }])
	// .controller('commandController', //cpp commands
	// 			['$scope',
	// 			 'srvCommands',
	// 			 function($scope, srvCommands) {
	// 				 $scope.getCppCommandsNo = function() {
	// 					 srvCommands.getCppCommands(
	// 						 function(data) {
	// 							 $scope.cpp_commands_no = Object.keys(data).length;
	// 						 });
	// 				 };
	// 				 $scope.clickNewCommand = function() {
	// 					 srvCommands.startCommand(
	// 						 function(data) {
	// 							 $scope.getCppCommandsNo();
	// 						 })
	// 				 };
	// 				 $scope.getCppCommandsNo();
	// 			 }])
	// .controller('currentController', //current server params
	// 			['$scope',
	// 			 '$timeout',
	// 			 'srvInfo',
	// 			 'srvCommands',
	// 			 function($scope, $timeout, srvInfo, srvCommands) {
	// 				 var REFRESH_INTERVAL = 1000; //ms

	// 				 var call = function() { //function called periodically
	// 					 $scope.getCppCommands = function() {
	// 						 srvCommands.getCppCommands(
	// 							 function(data) {
	// 								 $scope.cpp_commands = data;
	// 							 });
	// 					 };

	// 					 srvInfo.getCurrent(
	// 				 		 function(data) {
	// 				 			 $scope.current = data;
	// 							 $scope.getCppCommands();
	// 							 $timeout(call, REFRESH_INTERVAL);
	// 				 		 });
	// 				 };
	// 				 $timeout(call, 0); //start calling the service
	// 			 }])
	.controller('conway',
				'srvInfo',
				function($scope, srvInfo) {
					$scope.resetGrid = function() {
						$scope.grid = Array($scope.rows).fill().map(() => Array($scope.columns).fill(false));
					};
					$scope.negateElement = function(column, row) {
						$scope.grid[row][column] = !$scope.grid[row][column];
					};
					$scope.evolvebtn = function(){
						srvInfo.evolve($scope.grid);
					}
					srvInfo.evolve(
						grid,
						function(data) {
							$scope.grid = data;
					});
					$scope.rows = 32;
					$scope.columns = 32;
					$scope.resetGrid();
				});
				