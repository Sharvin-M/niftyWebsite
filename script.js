function nifty() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      const res = this.responseText.split(",");
      const projectElement = document.getElementById("projects");
      const nameElement = document.getElementById("name");

      projectElement.innerHTML = "";
      nameElement.innerHTML = "";

      const project = document.createElement("p2");
      const name = document.createElement("p1");
      project.innerText = res[0].replace(/"$/, "").replace(/^\["/, "");
      name.innerText = res[1].replace(/^"/, "").replace(/"]$/, "");

      projectElement.appendChild(project);
      nameElement.appendChild(name);

      projectElement.style.display = "block";
      nameElement.style.display = "block";
    }
  };
  xhttp.open(
    "GET",
    "https://5xuj7ap5ok.execute-api.us-west-1.amazonaws.com/prod/",
    true
  );
  xhttp.send();
}
