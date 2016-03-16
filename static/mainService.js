angular.module("dungeonRevolt")
  .service("mainService", function($http){

    this.getCharacters = function(){
      return $http({
        method: "GET",
        url: "/api/characters/"
      }).then(function(response){
        return response.data
      })
    }

    this.getTest = function(){
      return "Test from service is working."
    }
  })
