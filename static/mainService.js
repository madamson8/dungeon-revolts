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

    this.getBoard = function(character) {
      return $http({
        method: "GET",
        url: "/api/characters/" + character.id + "/show/"
      }).then(function(response){
        return response.data
      })
    }
  })
