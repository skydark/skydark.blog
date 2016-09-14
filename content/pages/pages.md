title: 页面
slug: pages

<div markdown="1" id="tabcontent-wrapper">

## MC

* [女仆守护](http://www.mcbbs.net/thread-496515-1-1.html)
* [女仆铁匠](http://www.mcbbs.net/thread-496802-1-1.html)
* [Yet Another Useless Mod](https://github.com/skydark/yaum)

-----------------------

## Galgame

### 移植(自主规避) {: .hide}

* [Fate](/pages/fate)
* [3days](/pages/3days)
* [实妹相伴的大泉君](/pages/realsister)
* [秽翼](/pages/eustia)

### 其他

* [赤印 CG 100% 补丁](/pages/ci)

-----------------------

## 其他

* [百万亚瑟王国服ONS剧情移植与html5卡牌浏览器](https://github.com/skydark/matools)

-----------------------

</div>

<script type="text/javascript">
var navtab = $('<ul class="nav nav-tabs" id="tabs"></ul>');
var navcontainer = $('<div class="tab-content"></div>');
$('#tabcontent-wrapper>h2').each(function(index){
  var tabid = 'tab-'+index;
  $(this).clone().wrapInner('<a>').children().unwrap()
      .attr('href', '#'+tabid)
    .wrap('<li>').parent()
    .appendTo(navtab).html();
  $(this).nextUntil('h2').last().filter('hr').remove();
  $(this).nextUntil('h2').andSelf()
    .wrapAll('<div>')
    .parent()
    .attr('id', tabid)
    .appendTo(navcontainer).html();
});
navcontainer.find('div>h3').addClass('js-toggle-next dropdown').filter(':not(.hide)').addClass('show').end().removeClass('hide');
$('#tabcontent-wrapper').empty().append(navtab).append(navcontainer);
$(".tab-content a").attr('target', '_blank').tooltip();
if (!($.browser.msie && ($.browser.version == "6.0"))) {
	$("#tabs>li>a").attr("data-toggle", "tab");
	$(".tab-content>div").addClass("tab-pane");
	$(".tab-content>div.tab-pane>h2").remove();
	$(".tab-content>div.tab-pane>ul").addClass("nav nav-list");
	$("#tabs a:first").tab('show');
	var href = '/'+decodeURIComponent(window.location.href).split('/').slice(-1);
	$(document).ready(function(){
		$("#tabs a[href='"+href+"']").click();
	});
}
</script>
