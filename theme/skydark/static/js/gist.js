var github_gist = (function(){
  function render(target, gists, callback){
    var i = 0;
    var fragment = '';
    var t = $(target)[0];
    var gist = '';

    for(i = 0; i < gists.length; i++) {
      gist = gists[i];
      fragment += '<li data-id="'+gist.id+'"><a href="'+gist.html_url+'" target="_blank">'+gist.name+'</a><p class="gist-desc">'+gist.description+'</p></li>';
    }
    t.innerHTML = fragment;
    if (callback) {
      callback();
    }
  }
  return {
    showGists: function(options){
      $.ajax({
          url: "https://api.github.com/users/"+options.user+"/gists?callback=?"
        , dataType: 'jsonp'
        , error: function (err) { $(options.target + ' li.loading').addClass('error').text("Error loading gists"); }
        , success: function(data) {
          data = data.data;
          if (!data) { return; }
          var gists = [];
          for (var i = 0; i < data.length; i++) {
            var files = data[i].files;
            for (var n in files) {
                data[i].name = files[n].filename;
                break;
            }
            gists.push(data[i]);
          }
          render(options.target, gists, options.callback);
        }
      });
    }
  };
})();

