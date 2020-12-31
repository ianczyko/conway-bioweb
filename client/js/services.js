/// @file services.js
/// @brief AngularJS services, AJAX communication with the server

angular.module('myAppServices', [])
    .service('srvInfo', //current information from zsm server
            function($http) {
                this.baseURL = client_server_prefix + '/ajax/'; //the prefix defined in version.js
                // $http.get(this.baseURL + 'conwaypy/acquire_csrf/').success(function(data){
                //     // self.csrf = data
                //     console.log($cookies.get('csrftoken'));
                //     $http.defaults.headers.post['X-CSRFToken'] = $cookies.get('csrftoken');
                // });
                this.evolve = function(grid, callback) {
                    var req = {
                        method: 'POST',
                        url: client_server_prefix + '/evolve/',
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        },
                        data: { 'grid': grid }
                    }
                    $http(req).then(callback);
                };
            });