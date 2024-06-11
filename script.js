
const apiURL = "https://5xuj7ap5ok.execute-api.us-west-1.amazonaws.com/prod/";

function nifty() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log(this.responseText);
    }
  };
  xhttp.open(
    "GET",
    "https://5xuj7ap5ok.execute-api.us-west-1.amazonaws.com/prod/",
    true,
  );
  xhttp.send();
}
