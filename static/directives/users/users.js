function usersController(mainService){

  var vm = this;

  vm.test = mainService.getTest();
  // this.characters = [ {name: "Eric"}, {name: "other person"} ]

  mainService.getCharacters().then(function(resp){
    console.log(resp)
    vm.characters = resp
  })
  // this.characters = mainService.getCharacters();

  // console.log(this.characters);

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
