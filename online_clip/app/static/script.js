function onSubmit(){
    var textarea = document.getElementsByTagName("textarea")[0];
    var http = new XMLHttpRequest()
    http.open("POST", "/post");
    http.setRequestHeader('text', encodeURIComponent(textarea.value))
    http.send();
}

function onCatch(){
    var textarea = document.getElementsByTagName("textarea")[0];
    var http = new XMLHttpRequest()
    http.open("GET", "/data");
    http.send();
    http.onload = function () {
        textarea.value = http.responseText
    };
}

function onCopy(){
    var textarea = document.getElementsByTagName("textarea")[0];
    textarea.select();
    document.execCommand("copy");
    textarea.blur();
}

function onPaste(){
    var textarea = document.getElementsByTagName("textarea")[0];
    textarea.focus()
    document.execCommand("paste");
}

window.onload = function(){
    onCatch()
}