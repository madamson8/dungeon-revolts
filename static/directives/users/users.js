function usersController(mainService){

  var vm = this;

  vm.gameboard = "";
  vm.activeCharacter = undefined;

  vm.pickCharacter = function (character) {
    vm.activeCharacter = character;
    // Load the board for the character
    console.log(vm.activeCharacter);
    mainService.getBoard(vm.activeCharacter).then(function(resp){
      vm.gameboard = resp;
    });
  }

  mainService.getCharacters().then(function(resp){
    vm.characters = resp;
  })

  vm.move = function(character,command){
    //make the request first
    mainService.moveCharacter(vm.activeCharacter,command).then(function(){
      //only display the gameboard if we get a response from the character
      mainService.getBoard(vm.activeCharacter).then(function(resp){
        //only set the gameboard if we get a response from the gameboard
        vm.gameboard = resp;
      });
    });
  }

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
