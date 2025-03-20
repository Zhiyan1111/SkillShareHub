/*一、banner轮播*/
/*1、手动点击换图*/
/* (1) 获取元素*/
var leftBtn=document.getElementById("leftBtn");
var rightBtn=document.getElementById("rightBtn");
var oLis=document.getElementById('banner').getElementsByTagName("li");
/* (2) 存储序号变量*/
var idx=0;
/* (3) 改变图片函数*/
function changePic(){
    //清洗class
    for(var i=0;i<oLis.length;i++){
        oLis[i].className="";
    }
    oLis[idx].className="cur";
}
/* (4) 点击右箭头改变图片*/
rightBtn.onclick=function(){
    idx++;
    if(idx>oLis.length-1){
        idx=0;
    }
    changePic();
}

/* (5) 点击右箭头改变图片*/
leftBtn.onclick=function(){
    idx--;
    if(idx<0){
        idx=oLis.length-1;
    }
    changePic();
}

/* 2、自动播放换图*/
/* (1) 播放时间记录*/
var timeRec;

/* (2) 播放函数*/
function timePlay(){
    timeRec=setInterval(
        function(){
            rightBtn.onclick();
        },3000
    );
}
timePlay();

/*暂停播放函数*/
var banner=document.getElementById("banner");
function stopTime(){
    clearInterval(timeRec);
}
banner.onmouseover=stopTime;
banner.onmouseout=timePlay;
