(function($){
	$.fn.twitteLitle = function(opcoes)
	{
		var setting = $.extend({
			user:""
		}, opcoes),
		
		url = "http://twitter.com/status/user_timeline/"+setting.user+".json?count=2&callback=?",
		
		msg = "",
		
		_this = this,
		
		to_date = function(date)
		{
			var times_temp = Date.parse(date),
				date       = new Date(times_temp);
				
			return date.getDate()+"/"+date.getMonth()+"/"+date.getFullYear();
		},
		
		to_url  = function(url)
		{
			
		};
		
		$.getJSON(url, function(json){
			$.each(json, function(index, item){
				$(_this).html("<div class='tweet'><p>"+item.text+"</p><p><strong>"+to_date(item.created_at)+"</strong></p></div>");
			});
		});
	
	};
})(jQuery);