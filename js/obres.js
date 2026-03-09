$(function () {
  var isCollapsed = false;

  
  var total = $("dl dd").length ;

  $("#infoRessenyes").text("Total de ressenyes: " + total);

  $("#toggleRessenyes").on("click", function () {
    if (!isCollapsed) {
      $("dl dd").addClass("is-hidden");
      $(this).text("Mostra ressenyes");
      isCollapsed = true;
    } else {
      $("dl dd").removeClass("is-hidden");
      $(this).text("Amaga ressenyes");
      isCollapsed = false;
    }
  });
});