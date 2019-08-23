window.onload = window.onresize = function(){
    pageResponse({
       selectors : '.main,.process',     //模块选择器，使用querySelectorAll的方法
       mode : 'contain',          // auto || contain || cover ，默认模式为auto 
       width : '750',             //输入页面的宽度，只支持输入数值，默认宽度为320px
       height : '1355',           //输入页面的高度，只支持输入数值，默认高度为504px
       origin : 'left center 0'
   })
}

   document.addEventListener("DOMContentLoaded", function() {
    pageResponse({
       selectors: '.main,.process',     //模块的类名，使用class来控制页面上的模块(1个或多个)
       mode : 'contain',       // auto || contain || cover 
       width : '750',          //输入页面的宽度，只支持输入数值，默认宽度为320px
       height : '1355',        //输入页面的高度，只支持输入数值，默认高度为504px
       origin : 'left top 0'
       })
   });
