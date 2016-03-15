function usersController(mainService){
  this.test = mainService.getTest();

  this.characters = mainService.getCharacters();

  console.log(this.characters);

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
