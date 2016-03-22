function usersController(mainService){

  var vm = this;

  vm.gameboard = "000ii00\n0mm0000\n0012300";
  vm.test = mainService.getTest();

  mainService.getCharacters().then(function(resp){
    vm.characters = resp
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
