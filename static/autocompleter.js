/**
 * Created by owner on 8.6.2019.
 */


document.onkeypress = function (e) {
    e = e || window.event;
    console.log(e.target);
    if(e.key == "#" || activateSearch){
        var activateSearch = true;
        /*autocompleter_search()*/
    }
    else{
        var activateSearch = false;
    }
}


function autocompleter_search(text){
     $.ajax({
                    type:  "POST",
                    dataType: "json",
                    async: true,
                    url: '/autocomplete/',
                    data: {
                        csrfmiddlewaretoken: '{{ csrf_token }}',
                        autocompleterText: text
                    },

                    success: function (json) {
                    }
                }
            )
}

