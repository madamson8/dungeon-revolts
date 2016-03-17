function usersController(mainService){

  var vm = this;

  vm.gameboard = "xhfdghfjhfhj";
  vm.test = mainService.getTest();

  mainService.getCharacters().then(function(resp){
    console.log(resp)
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
