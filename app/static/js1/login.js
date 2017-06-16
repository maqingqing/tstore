$(function(){


	$('#user').blur(function () {
		var username = $(this).val();
		$.ajax({
			url:$SCRIPT_ROOT+'/confirm/name',
			type: "post",
			data:{
				username: username
			},
			success:function(data){
				console.log(data);
				if(data=="False"){
					$('#flash_message').html("此用户名已被占用，请立即修改");
					$('#flash_message').css("display","block");
				}else{
					$('#flash_message').css("display","none");
				}
			}
		})
    })
    $('#passwd').blur(function () {
		var email = $(this).val();
		//对电子邮件的验证
      	var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
      	if(!myreg.test(email)){
			$('#erroeEmail').css("display","block");
			$('#passwd').focus();
     	}else{
      		$('#erroeEmail').css("display","none");
		}
		$.ajax({
			url:$SCRIPT_ROOT+'/confirm/eamil',
			type: "post",
			data:{
				email: email
			},
			success:function(data){
				if(data=="False"){
					$('#flash_message').html("此邮箱已被占用，请立即修改");
					$('#flash_message1').css("display","block");
				}else{
					$('#flash_message1').css("display","none");
				}
			}
		})
    });

    // $('#regUser').submit(function () {
		// var status = $('#flash_message').css("display");
		// var status1 = $('#flash_message1').css("display");
		// console.log(status,status1);
		// if(status == "block"||status1 == "block"){
		// 	return false;
		// }
    // });

	$('#reg').click(function () {
		var name = $('#user').val();
		var email = $('#passwd').val();
		var key = $('#passwd2').val();
		if(name==""){
			$('#flash_message').html("用户名不能为空");
			$('#flash_message').css("display","block");
			$('#user').focus();
		}else if(email==""){
			$('#flash_message1').html("邮箱不能为空");
			$('#flash_message1').css("display","block");
			$('#passwd').focus();
		}else if(key==""){
			$('#pasNone').css("display","block");
			$('#passwd2').focus();
		}else{
			$('#pasNone').css("display","none");
		}



		var status = $('#flash_message').css("display");
		var status1 = $('#flash_message1').css("display");
		var status2 = $('#pasNone').css("display");
		console.log(status,status1);
		if(status == "block"||status1 == "block"||status2 == "block"){
			return false
		}else{
			$.ajax({
                url: $SCRIPT_ROOT + '/signup',
                type: 'post',
                data: {
                    user: name,
					email:email,
                    password: key
                },
                success: function (data) {
                    console.log(data);
                    if (data == "true") {
                        alert("注册成功");
                        window.location.href = "/login";
                    }
                }
            })
		}
    });


	$("#loginBtn").click(function () {
		var username=$('#u').val();
		var password=$('#p').val();
		console.log(username);
		console.log(password);
		if(username==""){
			$('#none1').css("display","block");
			// $('#u').focus();
		}
		else if(password==""){
			$('#none2').css("display","block");
			// $('#p').focus();
		}else {

            $.ajax({
                url: $SCRIPT_ROOT + '/login',
                type: 'post',
                data: {
                    username: username,
                    password: password
                },
                success: function (data) {
                    console.log(data);
                    if (data == "true") {
                        window.location.href = "/index";
                    } else {
                        $('#wrong').css("display", "block");
                    }
                }
            })
        }
    })

	$(window).keydown(function(e){
		if (!e) e = window.event;
		if ((e.keyCode || e.which) == 13) {
			$("#loginBtn").click();
		}
    });

	$("#u,#p").focus(function () {
		$('#wrong').css("display","none");
		$('#none1').css("display","none");
		$('#none2').css("display","none");
    })

});



