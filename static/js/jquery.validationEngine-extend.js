(function($){
	$.extend($.validationEngine, {
		submitForm:function(caller){
			if($.validationEngine.settings.ajaxSubmit){		
			if($.validationEngine.settings.ajaxSubmitExtraData){
				extraData = $.validationEngine.settings.ajaxSubmitExtraData;
			}else{
				extraData = "";
			}
			$.ajax({
			   	type: "POST",
			   	url: $.validationEngine.settings.ajaxSubmitFile,
			   	async: true,
			   	data: $(caller).serialize()+"&"+extraData,
			   	error: function(data,transport){ $.validationEngine.debug("error in the ajax: "+data.status+" "+transport) },
			   	success: function(data){
			   		if(data == "true"){// the form clean  and show message
			   			var form = $(caller);
			   			$.each($(':text, textarea', form),function(){
							$(this).val( $(this).attr('default') );
			   			});

						$.validationEngine.buildPrompt("#send-contact", $.validationEngine.settings.ajaxSubmitMessage, true);
						$(".send-contactformError").addClass("blackPopup")
						.fadeOut(850, function(){ $(this).remove(); });
						
						
			   			if ($.validationEngine.settings.success)
			   			{	// AJAX SUCCESS, STOP THE LOCATION UPDATE
							$.validationEngine.settings.success && $.validationEngine.settings.success(); 
							return false;
						}
							
		   			}else{						// HOUSTON WE GOT A PROBLEM (SOMETING IS NOT VALIDATING)
			   			data = eval( "("+data+")");	
			   			if(!data){
			   				 $.validationEngine.debug("you are not going into the success fonction and jsonValidateReturn return nothing");
			   			}
			   			errorNumber = data.length	
			   			for(index=0; index<errorNumber; index++){	
			   				fieldId = data[index][0];
			   				promptError = data[index][2];
			   				type = data[index][1];
			   				$.validationEngine.buildPrompt(fieldId,promptError,type);
		   				}
	   				}
   				}
			})	
			return true;
		}
		// LOOK FOR BEFORE SUCCESS METHOD		
			if(!$.validationEngine.settings.beforeSuccess()){
				if ($.validationEngine.settings.success){	// AJAX SUCCESS, STOP THE LOCATION UPDATE
					if($.validationEngine.settings.unbindEngine){ $(caller).unbind("submit") }
					$.validationEngine.settings.success && $.validationEngine.settings.success(); 
					return true;
				}
			}else{
				return true;
			} 
		return false;
		}
	});
	
})(jQuery);
