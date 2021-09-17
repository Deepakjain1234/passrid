function clearErrors() {
  errors = document.getElementsByClassName("formerror");
  for (let item of errors) {
    item.innerHTML = "";
  }
}
function seterror(id, error) {
  //sets error inside tag of id
  element = document.getElementById(id);
  element.getElementsByClassName("formerror")[0].innerHTML = error;
}

function validateFormuser() {
  var returnval = true;
  clearErrors();

  //perform validation and if validation fails, set the value of returnval to false
  var name = document.forms["myForm"]["first_name"].value;
  var lname = document.forms["myForm"]["last_name"].value;

  if (name.indexOf(" ") >= 0) {
    seterror("name", "*First Name should not contain any spaces");
    returnval = false;
  }

  if (lname.indexOf(" ") >= 0) {
    seterror("lname", "*Last Name should not contain any spaces");
    returnval = false;
  }

  var email = document.forms["myForm"]["email"].value;
  const re =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  if (re.test(String(email).toLowerCase()) == false) {
    seterror("email", "*Please enter a valid email.");
    returnval = false;
  }

  var phone = document.forms["myForm"]["phone_number"].value;
  if (phone.length != 10) {
    seterror("phone", "*Phone number should be of 10 digits.");
    returnval = false;
  }

  var password = document.forms["myForm"]["password1"].value;
  if (password.length < 6) {
    seterror("pass", "*Password should be  6 Integers long!");
    returnval = false;
  }

  var cpassword = document.forms["myForm"]["password2"].value;
  if (cpassword != password) {
    seterror("cpass", "*PIN confirmation does not match.");
    returnval = false;
  }

  return returnval;
}

function loginformvalid() {
  var returnval = true;
  clearErrors();
  console.log("login form work");

  //perform validation and if validation fails, set the value of returnval to false

  var email = document.forms["logForm"]["username"].value;
  const re =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  if (re.test(String(email).toLowerCase()) == false) {
    seterror("email-login", "*Please enter a valid email.");
    returnval = false;
  }

  var password = document.forms["logForm"]["password"].value;
  if (password.length < 6) {
    seterror("logpass", "*Please enter a valid PIN.");
    returnval = false;
  }

  return returnval;
}

function validateForm() {
  var returnval = true;
  clearErrors();

  //perform validation and if validation fails, set the value of returnval to false
  var name = document.forms["myForm1"]["first_name"].value;
  var lname = document.forms["myForm1"]["last_name"].value;

  if (name.indexOf(" ") >= 0) {
    seterror("name", "*First Name should not contain any spaces");
    returnval = false;
  }

  if (lname.indexOf(" ") >= 0) {
    seterror("lname", "*Last Name should not contain any spaces");
    returnval = false;
  }

  var email = document.forms["myForm1"]["email"].value;
  const re =
    /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

  if (re.test(String(email).toLowerCase()) == false) {
    seterror("email", "*Please enter a valid email.");
    returnval = false;
  }

  var phone = document.forms["myForm1"]["phone_number"].value;
  if (phone.length != 10) {
    seterror("phone", "*Phone number should be of 10 digits.");
    returnval = false;
  }

  var password = document.forms["myForm1"]["password1"].value;
  if (password.length < 6) {
    seterror("pass", "*Password should be  6 Integers long!");
    returnval = false;
  }

  var cpassword = document.forms["myForm1"]["password2"].value;
  if (cpassword != password) {
    seterror("cpass", "*PIN confirmation does not match.");
    returnval = false;
  }

  // this is the domin validator
  var urlname = document.forms["myForm1"]["domain"].value;
  console.log(urlname);

  const pattern =
    /^[a-zA-Z0-9][a-zA-Z0-9-]{1,61}[a-zA-Z0-9](?:\.[a-zA-Z]{2,})+$/;
  let val = pattern.test(urlname);
  console.log(val);

  if (val == 0) {
    seterror("dominname", "*Invalid URL");
    returnval = false;
  }

  return returnval;
}
