// Instantiate and configure YUI Loader:
(function(){ 
    var loader = new YAHOO.util.YUILoader({ 
        base: "http://ajax.googleapis.com/ajax/libs/yui/2.8.2r1/build/", 
        require: ["animation", "autocomplete", "button","connection","container","dom","editor","element","event","menu"], 
        loadOptional: false, 
        combine: false, 
        filter: "MIN", 
        allowRollup: true, 
        onSuccess:function(){ 
            var my_editor = new YAHOO.widget.Editor('text', {
															width:'750px',
															height:'300px',
															animate:true,
															dompath:true,
															focusAtStart:true
															});

				my_editor.on('toolbarLoaded', function(){
					var button = {
						type:'push',
						label:'Prettify',
						value:'code'
					};

				my_editor.toolbar.addButtonToGroup(button, 'insertitem');

				this.toolbar.on('codeClick', function(o){
					this._focusWindow();
					this.execCommand('inserthtml', '<code class="prettyprint">add code</code>');
				}, my_editor, true);

			}, my_editor, true);
			
            my_editor.render();
			
            YAHOO.util.Event.on('form-salvar', 'click',function(){
				my_editor.saveHTML();
            });
        } 
    }); 
 
// Load the files using the insert() method. 
loader.insert();
	 
})();
