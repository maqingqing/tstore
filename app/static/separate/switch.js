// window.onload=function(){
	
	$(".v_menu_list li:odd").addClass("alt");	
	$("#menuClick").click(function(){
		$("#vMenuList").slideToggle();	
		return false;
	});
	$(".v_menu_list > li > i").hover(function(){
		$(this).animate({
			paddingLeft: 20				
		},100);									  
	},function(){
		$(this).animate({
			paddingLeft: 5				
		},50);	
	});

    $(document).click(function(event){
        var ele = $(this)[0].activeElement.className;
        if(ele == 'lang_list'){
            var checked = $(this)[0].activeElement.innerHTML;
            $(".rel").html(checked);
        };
        $("#vMenuList").slideUp();  
    })

	var record_lang=null;
	$.extend({
		loadProperties : function(new_lang){
			record_lang=new_lang;
			var tmp_lang = new_lang;
			jQuery.i18n.properties({//加载资浏览器语言对应的资源文件
				name: 'strings', //资源文件名称
				path:'static/language/', //资源文件路径
				language: tmp_lang,
				cache: false,
				mode:'map', //用Map的方式使用资源文件中的值
				callback: function() {//加载成功后设置显示内容
					$('#menuClick').attr('data-language',tmp_lang);
					for(var i in $.i18n.map){
						$('[data-lang="'+i+'"]').text($.i18n.map[i]);
						$('input[data-lang="'+i+'"]').attr("placeholder",$.i18n.map[i]);
					}
				}
			});
		}
	});

	// setTimeout(function(){
		var dafal_lang='zh';
		$.loadProperties(dafal_lang);
		var lang_html=$('.lang_list[data-number="'+dafal_lang+'"]').html();
		$('.rel').html(lang_html);
		$(".lang_list").click(function(){
			var $this=$(this), icon=$this.data('number');
			var checked=$(this).html();
			$('.rel').html(checked);
			$.loadProperties(icon);
			record_lang=icon;
		})
		var monitorNavs = $("#monitorMNav").find("li");
		monitorNavs.on('click', function (e) {
			$.loadProperties(record_lang);
			e.preventDefault;
		});
	// },1500);
// };
