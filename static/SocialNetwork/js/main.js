$(document).ready(function(){
  $(window).scroll(function(){
      if($(window).scrollTop() > 50){
          $(".menu").css({"background-color":"white"});
          $('.menu a').addClass('text-dark');
      }
      else{
          $(".menu").css({"background-color":"transparent"});
          $('.menu a').removeClass('text-dark');
      }

  })
})
