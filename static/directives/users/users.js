function usersController(mainService){

  var vm = this;

  vm.gameboard = "";
  vm.activeCharacter = undefined;

  vm.pickCharacter = function (character) {
    vm.activeCharacter = character;
    // Load the board for the character
    mainService.getBoard(vm.activeCharacter).then(function(resp){
      vm.gameboard = resp;
    });
  }

  mainService.getCharacters().then(function(resp){
    vm.characters = resp;
  })

}

angular
  .module("dungeonRevolt")
  .directive("usersDirective", function() {
    return {
      templateUrl: "directives/users/users.tpl.html",
      restrict: "E",
      controller: usersController,
      controllerAs: "UsersCtrl",
    }
  })
