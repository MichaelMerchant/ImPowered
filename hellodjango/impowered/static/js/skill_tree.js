var labelType, useGradients, nativeTextSupport, animate;

(function() {
  var ua = navigator.userAgent,
      iStuff = ua.match(/iPhone/i) || ua.match(/iPad/i),
      typeOfCanvas = typeof HTMLCanvasElement,
      nativeCanvasSupport = (typeOfCanvas == 'object' || typeOfCanvas == 'function'),
      textSupport = nativeCanvasSupport 
        && (typeof document.createElement('canvas').getContext('2d').fillText == 'function');
  //I'm setting this based on the fact that ExCanvas provides text support for IE
  //and that as of today iPhone/iPad current text support is lame
  labelType = (!nativeCanvasSupport || (textSupport && !iStuff))? 'Native' : 'HTML';
  nativeTextSupport = labelType == 'Native';
  useGradients = nativeCanvasSupport;
  animate = !(iStuff || !nativeCanvasSupport);
})();


var Log = {
  elem: false,
  write: function(text){
    if (!this.elem) 
      this.elem = document.getElementById('log');
    this.elem.innerHTML = text;
    this.elem.style.left = (500 - this.elem.offsetWidth / 2) + 'px';
  }
};

//Create a node rendering function that plots a fill  
//rectangle and a stroke rectangle for borders  
$jit.ST.Plot.NodeTypes.implement({  
  'stroke-rect': {  
    'render': function(node, canvas) {  
      var width = node.getData('width'),  
          height = node.getData('height'),  
          pos = this.getAlignedPos(node.pos.getc(true), width, height),  
          posX = pos.x + width/2,  
          posY = pos.y + height/2,
          lWidth = node.Node.CanvasStyles.lineWidth;
      this.nodeHelper.rectangle.render('fill', {x: posX, y: posY}, width, height, canvas);  
      this.nodeHelper.rectangle.render('stroke', {x: posX, y: posY}, width-lWidth, height-lWidth, canvas);
    }  
  }  
});

function calculateNodeInnerHtml(node){
	html = node.name;
	if($jit.id('all-nodes').checked || (node.selected && $jit.id('selected-nodes').checked) ){
		html += "<meter min=0 max=100 value="+node.data.progress+"></meter>";
	}
	return html;
};

function renderNodeLabels(){
	st.graph.eachNode(function(node){
		var label = $jit.id(node.id);
		if(label){ label.innerHTML = calculateNodeInnerHtml(node); }
	});
};

function init(){
	
    //init Spacetree
    //Create a new ST instance
    st = new $jit.ST({
        //id of viz container element
        injectInto: 'infovis',
        //set duration for the animation
        duration: 800,
        //set animation transition type
        transition: $jit.Trans.Quart.easeInOut,
        //set distance between node and its children
        levelDistance: 50,
        //enable panning
        Navigation: {
          enable:true,
          panning:true
        },
        //set node and edge styles
        //set overridable=true for styling individual
        //nodes or edges
        Node: {
            height: 40,
            width: 75,
            type: 'stroke-rect',
            color: '#aaa',
            overridable: true,
            CanvasStyles: {  
	          fillStyle: '#aaa',  
	          strokeStyle: '#aaa',  
	          lineWidth: 5,
        	},  
        },
        
        Edge: {
            type: 'bezier',
            overridable: true
        },
        
        onBeforeCompute: function(node){
            Log.write("Loading " + node.name + " node");
        },
        
        onAfterCompute: function(){
            Log.write("Done Loading");
        },
        
        //This method is called on DOM label creation.
        //Use this method to add event handlers and styles to
        //your node.
        onCreateLabel: function(label, node){
            label.id = node.id;            
            label.innerHTML = calculateNodeInnerHtml(node);
            label.onclick = function(){
            	  st.onClick(node.id);
            };
            //set label styles
            var style = label.style;
            style.width = 75 + 'px';
            style.height = 37 + 'px';            
            style.cursor = 'pointer';
            style.color = '#333';
            style.fontSize = '0.8em';
            style.textAlign= 'center';
            style.paddingTop = '3px';
        },
        
        //This method is called right before plotting
        //a node. It's useful for changing an individual node
        //style properties before plotting it.
        //The data properties prefixed with a dollar
        //sign will override the global node style properties.
        onBeforePlotNode: function(node){
            //add some color to the nodes in the path between the
            //root node and the selected node.
//            if (node.selected) {
//                node.data.$color = "#ff7";
//            }
//            else {
//                delete node.data.$color;
//                //if the node belongs to the last plotted level
//                if(!node.anySubnode("exist")) {
//                    //count children number
//                    var count = 0;
//                    node.eachSubnode(function(n) { count++; });
//                    //assign a node color based on
//                    //how many children it has
//                    node.data.$color = ['#aaa', '#baa', '#caa', '#daa', '#eaa', '#faa'][count];                    
//                }
//            }
			if(node.selected){
				node.setCanvasStyle('strokeStyle','#ffc');
			}else{
				node.setCanvasStyle('strokeStyle','#aaa');
			}
			var label = $jit.id(node.id);
			if(label){ label.innerHTML = calculateNodeInnerHtml(node); }
        },
        
        //This method is called right before plotting
        //an edge. It's useful for changing an individual edge
        //style properties before plotting it.
        //Edge data proprties prefixed with a dollar sign will
        //override the Edge global style properties.
        onBeforePlotLine: function(adj){
            if (adj.nodeFrom.selected && adj.nodeTo.selected) {
                adj.data.$color = "#eed";
                adj.data.$lineWidth = 3;
            }
            else {
                delete adj.data.$color;
                delete adj.data.$lineWidth;
            }
        }
    });
    
    
    //load json data
    st.loadJSON(st_json);
    //compute node positions and layout
    st.compute();
    //optional: make a translation of the tree
    st.geom.translate(new $jit.Complex(-200, 0), "current");
    //emulate a click on the root node.
    st.onClick(st.root);
    
    var st_title = document.getElementById('st_title');
	st_title.style.left = (500 - st_title.offsetWidth / 2) + 'px';

	var selectNodes = $jit.id('selected-nodes'),
		allNodes = $jit.id('all-nodes');
	//select listeners
	$jit.util.addEvent(allNodes,'click',function(){
		if(this.checked){
			selectNodes.disabled = true;
			selectNodes.checked = true;
		}else{
			selectNodes.disabled = false;
		}
		renderNodeLabels();
	});
	
	$jit.util.addEvent(selectNodes, 'click', function(){
		renderNodeLabels();
	});
	
//	st.switchPosition("top","replot", {});
    //end


}

function foo(){
	var rand = Math.random,
        floor = Math.floor,
        colors = ['#33a', '#55b', '#77c', '#99d', '#aae', '#bf0', '#cf5', 
                  '#dfa', '#faccff', '#ffccff', '#CCC', '#C37'],
        colorLength = colors.length;
	st.graph.eachNode(function(n) {  
    //set random width and height node styles  
    n.setData('width', floor(rand() * 40 + 20), 'end');  
    n.setData('height', floor(rand() * 40 + 20), 'end');  
    //set random canvas specific styles  
    n.setCanvasStyle('fillStyle', colors[floor(colorLength * rand())], 'end');  
    n.setCanvasStyle('strokeStyle', colors[floor(colorLength * rand())], 'end');  
    n.setCanvasStyle('lineWidth', 10 * rand() + 1, 'end');  
    //set label styles  
    n.setLabelData('size', 20 * rand() + 1, 'end');  
    n.setLabelData('color', colors[floor(colorLength * rand())], 'end');  
    //set adjacency styles  
    n.eachAdjacency(function(adj) {  
      adj.setData('lineWidth', 10 * rand() + 1, 'end');  
      adj.setData('color', colors[floor(colorLength * rand())], 'end');  
    });  
  });  
  st.compute('end');  
  st.geom.translate({x:-130, y:0}, 'end');  
  st.fx.animate({  
    modes: ['linear',   
            'node-property:width:height',  
            'edge-property:lineWidth:color',  
            'label-property:size:color',  
            'node-style:fillStyle:strokeStyle:lineWidth'],  
    duration: 1500,  
    onComplete: function() {  
      init.busy = false;  
    }  
  }); 
}

function printNodes(){
	console.log(st.graph);
}

function foo2(){
	var rand = Math.random,
        floor = Math.floor,
        colors = ['#33a', '#55b', '#77c', '#99d', '#aae', '#bf0', '#cf5', 
                  '#dfa', '#faccff', '#ffccff', '#CCC', '#C37'],
        colorLength = colors.length;
	st.graph.eachNode(function(n){
	  n.setCanvasStyle('fillStyle', colors[floor(colorLength * rand())], 'end');  
	  n.setCanvasStyle('strokeStyle', colors[floor(colorLength * rand())], 'end');  
	  n.setCanvasStyle('lineWidth', 10 * rand() + 1, 'end');  
	});
    st.compute('end');  
    st.fx.animate({  
      modes: ['node-style:fillStyle:strokeStyle:lineWidth'],  
      duration: 1500,  
    }); 
	
}

function refreshNode3(){
//	st.graph.nodes.node3.setLabelData('innerHTML',"Hello",'end');
	st.graph.nodes.node3.setLabelData('fontSize','2','end');
	st.compute();
//	st.fx.animate({modes:['linear', 'label-property:innerHTML'],duration:1000});
	st.fx.animate({modes:['linear', 'label-property:color'],duration:1000});
}

function initLegend(){
	
}