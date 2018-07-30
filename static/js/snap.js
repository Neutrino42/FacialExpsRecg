var timer = null;

function ShowCam() {
    Webcam.set({
        width: 570,
        height: 430,
        image_format: 'jpeg',
        jpeg_quality: 100
    });
    Webcam.attach('#my_camera');
}
window.onload= ShowCam;

function snap() {
    Webcam.snap( function(data_uri) {
        // display results in page
        document.getElementById('results').innerHTML =
        '<img id="image" src="'+data_uri+'"/>';
        document.getElementById('Result').innerHTML = 'The result will appear here';
    } );
}

function upload() {
    var image = document.getElementById('image').src;
    var form = document.getElementById('myForm');
    var formData = new FormData(form);
    formData.append("file", image);

    var object = {};
    formData.forEach(function (value, key) {
        object[key] = value;
    });
    var data = JSON.stringify(object);

    $.ajax({
    url:'/imageProcess',
    type: 'POST',
    dataType: 'json',
    data: data,
    success: function (result) {
        // alert(l'You are having a ' + result.result + ' face, and scored ' + result.score);
        // alert(html(result.result));
        var emoji = "../static/image/" + result.result + ".png";
        // document.getElementById("Result").innerHTML = 'You are having a ' + result.result + ' face, and scored ' + result.score + ".";

        document.getElementById("Result").innerHTML = '<img id = "emoji1" />' + '<img id = "emoji2" />' + '<img id = "emoji3" />' ;
        document.getElementById("emoji1").src = emoji;
        document.getElementById("emoji2").src = emoji;
        document.getElementById("emoji3").src = emoji;

            // 'You are having a ' +

            // ' face, and scored ' +
            // result.score + '.' ;

    }, error:function(err){
        alert('loading');
    }
})
}
