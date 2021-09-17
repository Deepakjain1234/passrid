var registerform = document.getElementById("registerid");
var b1 = document.getElementById("colorbtn1");
var b2 = document.getElementById("colorbtn2");

var loginform = document.getElementById("loginid");
loginform.style.display = "none";
var form1 = document.getElementById("loginbtn");
b2.style.display = " none";
form1.onclick = function () {
  registerform.style.display = "none";
  loginform.style.display = "";
  form1.style.color = "white";
  form1.style.background = "#0266D9";
  form.style.color = "#0266D9";
  form.style.background = "none";
  //    loginform.style.height=" 400px"
  b2.style.display = " block";
  b1.style.display = " none";
};

var form = document.getElementById("registerbtn");
form.onclick = function () {
  loginform.style.display = "none";
  registerform.style.display = "";
  form1.style.color = "#0266D9";
  form1.style.background = "none";
  form.style.color = "white";
  form.style.background = "#0266D9";
  b1.style.display = " block";
  b2.style.display = " none";
};
