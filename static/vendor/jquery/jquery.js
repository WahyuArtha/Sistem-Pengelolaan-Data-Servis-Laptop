<!-- script jquery -->
<script type='text/javascript' src='js/jquery-1.11.3.min.js'></script>
<!-- script javascript dan jquery animation untuk menu-->
<script type='text/javascript'>
 $(document).ready(function(){
  $('.toggle').click(function(){
   $('ul.menu').slideToggle(500);  
  });
 
 $(window).resize(function(){
  var menu=$('ul.menu');
  var w=$(window).width();
  if (w > 320 && menu.is(':hidden')) {
   menu.removeAttr('style');
  };
 });
 
 });
</script>