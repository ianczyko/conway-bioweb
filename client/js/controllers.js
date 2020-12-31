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
	.controller('conway',
				['$scope',
				'srvInfo',
				function($scope, srvInfo) {
					$scope.resetGrid = function() {
						$scope.grid = Array($scope.rows).fill().map(() => Array($scope.columns).fill(false));
					};
					$scope.negateElement = function(column, row) {
						$scope.grid[row][column] = !$scope.grid[row][column];
					};
					$scope.evolvebtn = function(){
						srvInfo.evolve(
							$scope.grid,
							function(data) {
								$scope.grid = data.data.grid;
						});
					}
					$scope.rows = 32;
					$scope.columns = 32;
					$scope.resetGrid();
				}])
	
				