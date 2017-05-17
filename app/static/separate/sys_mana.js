$(document).ready(function(){
	function getServerStatusInfo(){
    	var url = $SCRIPT_ROOT + '/cluster/info';
    	var serverStatusInfo={};
      	//$.ajaxSetup({async:false});
    	$.getJSON(url, null, function (data) {
      		serverStatusInfomat = data;
      		var serverslist= $('#serversList');//系统管理页面里集群机器信息列表
			var serversStatusinfo = serverStatusInfomat;
			var servers = serversStatusinfo["servers"];
			var count = 0;
		    for (count = 0; count < servers.length; count++){
		      	serverslist.append(serversListFormat(servers[count]["serverId"], count));
		    }

		    for (count = 0; count < servers.length; count++){
				var serverid = '#diskinfo' + servers[count]["serverId"];
				var disklist = $(serverid);
				var diskRow1=$("<div class='diskFa'></div>");
				var diskRow2=$("<div class='diskFa'></div>");
				var diskRow3=$("<div class='diskFa'></div>");
				var diskRow4=$("<div class='diskFa'></div>");
		      	for (var i = 0; i < servers[count]["disks"].length; i++){
			        if(i<3){
					  diskRow1.append(diskContentFormat(servers[count]["disks"][i]["diskId"], i, count));}
					else if(i>=3&&i<6){
    	              diskRow2.append(diskContentFormat(servers[count]["disks"][i]["diskId"], i, count));}
					else if(i>=6&&i<9){
						diskRow3.append(diskContentFormat(servers[count]["disks"][i]["diskId"], i, count));
					}else if(i>=9&&i<12){
						diskRow4.append(diskContentFormat(servers[count]["disks"][i]["diskId"], i, count));
					}
		      	}
				disklist.append(diskRow1);
				disklist.append(diskRow2);
				disklist.append(diskRow3);
				disklist.append(diskRow4);
		    }  //3X4 v1


		    // for (count = 0; count < servers.length; count++){
				// var serverid = '#diskinfo' + servers[count]["serverId"];
				// var disklist = $(serverid);
				// var diskRow1=$("<div></div>");
				// var diskRow2=$("<div></div>");
				// var diskRow3=$("<div></div>");
		    //   	for (var i = 0; i < servers[count]["disks"].length; i++){
			 //        if(i<4){
				// 	  diskRow1.append(diskContentFormat(servers[count]["disks"][i]["diskId"], i, count));}
				// 	else if(i>=4&&i<8){
    	     //          diskRow2.append(diskContentFormat(servers[count]["disks"][i]["diskId"], i, count));}
				// 	else if(i>=8&&i<12){diskRow3.append(diskContentFormat(servers[count]["disks"][i]["diskId"], i, count));}
		    //   	}
				// disklist.append(diskRow1);
				// disklist.append(diskRow2);
				// disklist.append(diskRow3);
		    // }  //3X4 v1


		    //重启机器
            // var restartBtn = $('.serverRestart');
            // restartBtn.each(function () {
				// var $this = $(this);
				// $this.click(function () {
				// 	var thisId = $this.attr("id");
				// 	var machineName = thisId.substr(7);
				// 	$.ajax({
				// 		url: $SCRIPT_ROOT + '/restart/machine',
				// 		data:{
				// 			machineName: machineName
				// 		},
				// 		success:function(data){
				// 			console.log(data);
				// 		}
				// 	})
             //    })
            // });
		    


		    function serversListFormat(serverId, i) {
			    if (servers[i]["serverStatus"] == "Connected"){
			      return '<div class="info-box"><span style = "color:green;" class="info-box-icon">'+
					  '<i class="fa fa-fw fa-tv" title="服务器名称:'+ serverId+'"></i></span>'+
					  '<div class="info-box-content" style="color: black;"> '+
					  '<span class="info-box-text">'+ serverId + '</span> '+
					  '<div class="info-box-number" id="diskinfo'+ serverId + '"></div>'+
					  '<button type="button" class="btn btn-primary btn-sm col-md-offset-10 pull-right serverRestart" id="Restart'+serverId+'"><i class="fa fa-refresh"></i><i style="font-style:normal;" data-lang="restart_mac"></i></button>'+
					  '</div></div>';
			    }else{
			      return '<div class="info-box"><span style = "color:darkslategray" class="info-box-icon">'+
					  '<i class="fa fa-fw fa-tv" title="服务器名称:'+ serverId+'"></i></span>  ' +
					  '<div class="info-box-content" style="color: black"> ' +
					  '<span class="info-box-text">'+ serverId + '</span>' +
					  '<div class="info-box-number" id="diskinfo'+ serverId +'"></div>'+
					  '<button type="button" class="btn btn-primary btn-sm col-md-offset-10 pull-right serverRestart" id="Restart'+serverId+'"><i class="fa fa-refresh" data-lang="restart_mac"></i></button>'+
					  '</div></div>';
			    }
			}
		      
		    function diskContentFormat(diskId , i, count){
			    if (servers[count]["disks"][i]["diskStatus"] == "health") {
			      // return '<a class="btn btn-app" rel="tooltip" title="存储设备名称: 166.111.131.144:/few/fe<br>状态: 在线" data-html="true">  <i class="glyphicon glyphicon-tasks text-success"></i>块名称</a>';
			      return ' <i class="glyphicon glyphicon-tasks text-success" title="磁盘编号:'+ diskId + '"></i>'
			    }else{
			      //  return '<a class="btn btn-app" rel="tooltip" title="存储设备名称: 166.111.131.144:/few/fe<br>状态: 在线" data-html="true">  <i class="glyphicon glyphicon text-danger"></i>块名称</a>';
			      return ' <i class="glyphicon glyphicon-tasks text-danger" title="磁盘编号:'+ diskId + '"></i>'
			    }
			}
      		
    	});
    	//return serverStatusInfomat;
	};
	getServerStatusInfo();
    
    $(".menu-item.system").click(function(){
    	var monitorMNav_hide = $("#monitorMNav").css("height");
    	if(monitorMNav_hide != "0px"){
    		$(".menu-item.monitor .fa.fa-chevron-down").removeClass("fa-chevron-UP");
    		$("#monitorMNav").stop().animate({
    			height:"0"
    		},500)
    	}
    	
    	$(".menu-item.volume .fa.fa-chevron-down").removeClass("fa-chevron-UP");
		$("#volumeMNav").stop().animate({
			height:"0"
		},500)
    })
})
