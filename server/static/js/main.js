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
function list_hide(){
          $(".menu li").each(function(){
			$(this).hide();
			});
      }
       function list_show(){
          $(".menu li").each(function(){
			$(this).show();
			});
      }

	  function menu_hide(){
          $(".test_menu li").each(function(){
			$(this).hide();
			});
      }
       function menu_show(){
          $(".test_menu li").each(function(){
			$(this).show();
			});
      }

    $(window).load(function () {
        $("#choose").click(function(){
	      console.log("test","test");
             list_show();
	  });
      $("#mycanvas").click(function(){
	      console.log("test","test");
             list_hide();
             menu_hide();

	  });
      $("#save").click(function(){
	      console.log("test","test");
             menu_show();
	  });
      list_hide();
	  menu_hide();
    });


    //node express搭建服务器 资源已被阻止,因为 MIME 类型(“text/html”)不匹配(X-Content-Type-Options:在IE报404的问题
    //https://blog.csdn.net/weixin_40336827/article/details/88901363