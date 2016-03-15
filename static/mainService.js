angular.module("dungeonRevolt")
  .service("mainService", function($http){

    this.getCharacters = function(){
      $http({
        method: "GET",
        url: "0.0.0.0:9000/api/characters/"
      }).then(function(response){
        return response.data;
      })
    }

    this.getTest = function(){
      return "Test from service is working."
    }
  })
