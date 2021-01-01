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
				'$interval',
				function($scope, srvInfo, $interval) {
					$scope.resetGrid = function() {
						$scope.generation = 0;
						$scope.grid = Array($scope.rows).fill().map(() => Array($scope.columns).fill(false));
					};
					$scope.initialArrangement = function() {
						$scope.resetGrid();
						var mid_row = Math.floor($scope.rows / 2);
						var mid_col = Math.floor($scope.columns / 2);
						$scope.grid[mid_row-1][mid_col] = true;
						$scope.grid[mid_row][mid_col] = true;
						$scope.grid[mid_row+1][mid_col] = true;
						$scope.grid[mid_row][mid_col-1] = true;
						$scope.grid[mid_row-1][mid_col] = true;
						$scope.grid[mid_row-1][mid_col+1] = true;
					};
					$scope.negateElement = function(column, row) {
						$scope.grid[row][column] = !$scope.grid[row][column];
					};
					$scope.evolve = function(){
						$scope.generation++;
						srvInfo.evolve(
							$scope.grid,
							function(data) {
								$scope.grid = data.data.grid;
						});
					}
					$scope.generation = 0;
					var stop;
					$scope.simulationIsOn = false;
					$scope.startSimulation = function(){
						if ( angular.isDefined(stop) ) return;
						$scope.simulationIsOn = true;
						stop = $interval(function() {
							$scope.evolve()
						}, 200);
					}
					$scope.stopSimulation = function(){
						if (angular.isDefined(stop)) {
							$scope.simulationIsOn = false;
							$interval.cancel(stop);
							stop = undefined;
						}
					}
					$scope.$on('$destroy', function() {
						// Make sure that the interval is destroyed too
						$scope.stopSimulation();
					});
					$scope.rows = 32;
					$scope.columns = 32;
					$scope.initialArrangement();
				}])
	
				