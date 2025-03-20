var remenber_pwd = document.getElementById("remenber_pwd");
var user = document.getElementById("user");
var pwd = document.getElementById("pwd");
var message = document.getElementById("login_message")

//Remember password
// Assign the function to the onload object.
window.onload = function ()
{
    //Getting a username from a cookie
    var username = getCookie("This is username") ;
    //If the username is null, assign a null value to the form element.
    if ( username == "" )
    {
        user.value="" ;
        pwd.value="" ;
        remenber_pwd.checked = false ;
    }
    //Get the corresponding password, and assign the username and password to the form.
    else
    {
        var password = getCookie(username) ;
        user.value = username ;
        pwd.value = password ;
        remenber_pwd.checked = true ;
    }
}
function getCookie(name)
{
    var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
    if(arr=document.cookie.match(reg))
        return unescape(arr[2]);
    else
        return null;
}
function delCookie(name)
{
    var exp = new Date();
    exp.setTime(exp.getTime() - 1);
    var cval=getCookie(name);
    if(cval!=null)
        document.cookie= name + "="+cval+";expires="+exp.toGMTString();
}
function setCookie(name,value)
{
    var Days = 30;
    var exp = new Date();
    exp.setTime(exp.getTime() + Days*24*60*60*1000);
    document.cookie = name + "="+ escape (value) + ";expires=" + exp.toGMTString();
}
//Login
function login() {
    var username = user.value;
    var password = pwd.value;
    var isRmbPwd = remenber_pwd.checked;
    if(!username || !password){ //拦截空内容
        msg("block","red","用户名或密码为空");
    }else{
        //Request operation
        if(username == "admin" && password == "admin" ){
            msg("block","green","登陆成功，1s后自动跳转...");
            //若复选框勾选,则添加Cookie,记录密码
            if ( isRmbPwd == true )
            {
                setCookie ( "This is username", username, 7 ) ;
                setCookie ( username, password, 7 ) ;
            }
            //Otherwise clear cookies
            else
            {
                delCookie ( "This is username" ) ;
                delCookie ( username ) ;
            };
            setTimeout(function(){ //2s跳转到首页
                window.reload();
            },1000)
        }else{
            msg("block","red","登陆失败，请确认用户名或密码")
        }
    }


}
//Alerts message
function msg(show,color,txt) {
    message.style.display = show;
    message.style.background = color;
    message.innerText = txt;
}
