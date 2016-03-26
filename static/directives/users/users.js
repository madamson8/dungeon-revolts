function usersController(mainService,$scope){

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

    if(vm.activeCharacter != undefined){
      mainService.moveCharacter(vm.activeCharacter,command).then(function(){
        //only display the gameboard if we get a response from the character
        mainService.getBoard(vm.activeCharacter).then(function(resp){
          //only set the gameboard if we get a response from the gameboard
          vm.gameboard = resp;
        });
      });
    }else {
      console.log("Silly goose, you haven't chosen a character");
    }

  }

  vm.keydown = function($event){
    //populate this with the if statements to controll the character

    //Up Arrow = 38
    //Down Arrow = 40
    //Left Arrow = 37
    //Right Arrow = 49

    if($event == 38){
      vm.move(vm.activeCharacter, 'move north');
    }
    if($event == 40){
      vm.move(vm.activeCharacter, 'move south');
    }
    if($event == 37){
      vm.move(vm.activeCharacter, 'move west');
    }
    if($event == 39){
      vm.move(vm.activeCharacter, 'move east');
    }

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
