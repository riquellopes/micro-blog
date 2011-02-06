var rlopes = {
	init:function()
	{
		$("#form-contact").validationEngine({
			validationEventTriggers:"keyup blur",
			ajaxSubmit: true,
			ajaxSubmitFile:'/contact',
			ajaxSubmitMessage: "Obrigado, mensagem enviada!",
			success : false,
			failure : function() {}
		});
		
		$("#form-contact :text, #form-contact textarea").focus(rlopes.form_focus);
		$("#tags").keydown(rlopes.tags);
	},
	form_focus:function()
	{
		$(this).val("");
	},
	tags:function(e)
	{	
		var virgula = function(text){
			if( /\s\w/i.test( text ) )
				return text.replace(/\s/i, ",");
			return text;
		}
		
		$(this).val( virgula( $(this).val() ) );
	}
};

$(rlopes.init);
