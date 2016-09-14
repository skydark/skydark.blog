//$(document).ready(function(){
$('.js-toggle-next').click(function(){
	$(this).next().slideToggle('normal');
}) ;
$('.js-toggle-next').filter('.dropdown').append($('<b class="caret"></b>'));
$('.js-toggle-next').not('.show').next().hide();
$('.main-content a').each(function(){
	var href = $(this).attr('href');
	if (href) {
		if(href.indexOf('#') == 0 || href.indexOf('/') == 0){
		}else{
			$(this).attr('target','_blank');
			$(this).addClass('external');
		}
	}
});
$('a[rel=tooltip]').tooltip();
$(".slider").click(function(){
	$(this).next().toggle('normal').css('left', $(this).position().left).css('top', $(this).position().bottom);
}).next().hide();
$('#toc-here').replaceWith((function(){
	var toc = $('<div class="toc"></div>');
	var toc_pointer = toc;
	var toc_level = 0;
	$('h1,h2,h3,h4', '.entry-content').each(function(i, heading) {
		var id = heading.id;
		if (!id) {
		   	id = 'toc-' + i;
			heading.id = id;
		}
		var new_toc_level = parseInt(heading.nodeName.slice(1), 10);
		var j = toc_level;
		for (; j < new_toc_level; j++) {
			toc_pointer = $('<li>').appendTo($('<ul class="nav nav-toc nav-toc-'+j+'">').appendTo(toc_pointer));
		}
		for (j = toc_level; j > new_toc_level; j--) {
			toc_pointer = toc_pointer.parent().parent();
		}
		if (toc_level >= new_toc_level) toc_pointer = $('<li>').appendTo(toc_pointer.parent());
		toc_pointer.append($('<a href="#'+id+'">'+heading.innerHTML+'</a>'));
		toc_level = new_toc_level;
	});
	return toc;
})());
//});
