
//All the variables
var elx = 90
	, elxlen = 495
	, elylen = 300
	, colorCount = 3
	, minTop = 590
	, maxTop = 650
	, maxDeg = 360
	, allLeafId = []
	, leafOnTree = [];

function Circle(x, y, radius){
	this.x = x;
	this.y = y;
	this.radius = radius;
}

function calcRandX(circle){
	//Calculate the x position
	var radians = Math.floor(Math.random() * maxDeg) * Math.PI /180
		, adjRadius = Math.floor(Math.random() * circle.radius)
		, randx = Math.floor(Math.cos(radians) * adjRadius);
		
	return randx;
}

function calcRandY(circle){
	//Calculate the y position
	var radians = Math.floor(Math.random() * maxDeg) * Math.PI /180
		, adjRadius = Math.floor(Math.random() * circle.radius)
		, randy = Math.floor(Math.sin(radians) * adjRadius);
		
	return randy;
}

function makeNuLeaf(leafNum, cirNum, circle){
	//Making the randoms
	var randX = calcRandX(circle) + circle.x
		, randY = calcRandY(circle) + circle.y
		, randColor = Math.floor(Math.random() * (colorCount + 1))
		, randDeg = Math.floor(Math.random() * (maxDeg + 1));

	//Make the new li element
	var nuLeaf = document.createElement("li")
		, nuId = "leaf" + leafNum + "-" + cirNum;
		
	allLeafId.push(nuId);
		
	nuLeaf.setAttribute("id", nuId);
	nuLeaf.innerHTML = "&nbsp;";
	
	//Picking the leaf color
	switch(randColor){
		case 1:
			nuLeaf.className = "dark";
			break;
		case 2:
			nuLeaf.className = "med";
			break;
		default:
			nuLeaf.className = "lig";
			break;
	}
	
	//Picking the leaf angle
	nuLeaf.style.webkitTransform = "rotate(" + randDeg + "deg)";
	nuLeaf.style.setProperty("-moz-transform","rotate(" + randDeg + "deg)","");
	nuLeaf.style.setProperty("transform","rotate(" + randDeg + "deg)","");

	
	//Setting the location
	nuLeaf.style.top = randY + "px";
	nuLeaf.style.left = randX + "px";
		
	//Adding it to the dom
	var allLeaves = document.getElementById("leaves");
	allLeaves.appendChild(nuLeaf);
	
}

function makeLeaves(howMany){
	//Circles
	var circ1 = new Circle(305, 205, 165)
	, circ2 = new Circle(180, 150, 180)
	, circ3 = new Circle(225, 75, 180)
	, circ4 = new Circle(385, 80, 180)
	, circ5 = new Circle(400, 150, 180)
	, circ6 = new Circle(305, 100, 165);
	
	for (var i = 0; i < howMany; i++){
		makeNuLeaf(i, 1, circ1);
		makeNuLeaf(i, 2, circ2);
		makeNuLeaf(i, 3, circ3);
		makeNuLeaf(i, 4, circ4);
		makeNuLeaf(i, 5, circ5);
		makeNuLeaf(i, 6, circ6);
	}
}

function changeRandColor(){
	//Get random leaf by id, and get random color
	var leafId = Math.floor(Math.random() * allLeafId.length)
		, leaf = document.getElementById(allLeafId[leafId])
		, randColor = Math.floor(Math.random() * (colorCount + 1));
	
	//Change the color here (changing class)
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
	
	//Remove the changed color
	allLeafId.splice(leafId, 1);
}

function leafFall(){
	//Getting random leaf
	var leafId = Math.floor(Math.random() * leafOnTree.length)
		, leaf = document.getElementById(leafOnTree[leafId])
		, randTop = Math.floor(Math.random() * (maxTop - minTop + 1)) + minTop;
	
	//Move the leaf
	leaf.className = leaf.className + " fallen";
	leaf.style.top = randTop + "px";
	
	//Remove the leaf
	leafOnTree.splice(leafId, 1);
}

function main(){
	
	var d = new Date()
		, t = d.getMinutes();
	
	//Put the leaves on the tree
	makeLeaves(100);
	
	//Copy leaf id array
	leafOnTree = allLeafId.slice(0);
	
	//Adjust to the time
	if (t < 30){
		for (var i=0; i < t*20; i++){
			changeRandColor();
		}
	}
	else {
		for (var k=0; k < leafOnTree.length; k++){
			changeRandColor();
		}
		for (var j=0; j < t*20/2; j++){
			leafFall();
		}
	}
	
	
	//Loop through the animation
	setInterval(function(){
		if (allLeafId.length > 0) { 
			changeRandColor();	
		}
		else if (leafOnTree.length > 0) { 
			leafFall();
		}
	}, 3000);
}

//MAIN FUNCTIONS
main();

