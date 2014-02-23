/*
* Kai Austin Spring 2014
* tree_script.js = functions and main script to put leaves
* on tree and change css for animation
*/

var allTree = [];

function makeLeaf(x){
	var nuLeaf = document.createElement("li")
		, nuId = "leaf" + x;

	nuLeaf.setAttribute("id", nuId);
	nuLeaf.innerHTML = "&nbsp;";

	allTree.push(nuId);

	//Sets color
	var  randColor = Math.floor(Math.random() * 3);
	console.log(randColor);
	switch(x){
		case 0:
			nuLeaf.className = "dark";
			break;
		case 1:
			nuLeaf.className = "med";
			break;
		default:
			nuLeaf.className = "lig";
			break;
	}
	

	//Random position
	var randX = Math.floor(Math.random() * 1000)
		, randY = Math.floor(Math.random() * 800);
	nuLeaf.style.top = randY + "px";
	nuLeaf.style.left = randX + "px";

	//Random angle
	var randAng = Math.floor(Math.random() * 360);
	nuLeaf.style.webkitTransform = "rotate(" + randAng + "deg)";
	nuLeaf.style.setProperty("-moz-transform","rotate(" + randAng + "deg)","");
	nuLeaf.style.setProperty("transform","rotate(" + randAng + "deg)","");

	//Put leaves on the tree
	var allLeaves = document.getElementById("leaves");
	allLeaves.appendChild(nuLeaf);
}

function allDaLeaves(maxLeaves){
	for (var k=0; k<maxLeaves; k++){
		makeLeaf(k);
	}
	console.log(allTree);
}

function changeColor(z){
	//Change the color of all the leaves on the tree
	var randColor = Math.floor(Math.random() * 3)
		, leaf = document.getElementById(z);

	//all the color here (changing class)
	switch(randColor){
		case 1:
			leaf.className = "red";
			break;
		case 2:
			leaf.className = "orange";
			break;
		default:
			leaf.className = "yellow";
			break;
	}
}

function leafFall(z){
	var leaf = document.getElementById(z);
	leaf.className = leaf.className + " fallen";
	leaf.style.top = 1000 + "px";
}

allDaLeaves(10);

var e = 0
	, q = 0;

setInterval(function(){
	if (e < allTree.length){
		changeColor(allTree[e]);
		 e++;
	} else if (q < allTree.length){
		leafFall(allTree[q]);
		q++;
	}
}, 1000);


