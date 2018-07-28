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
        // alert('You are having a ' + result.result + ' face, and scored ' + result.score);
        
    }, error:function(err){
        alert('loading');
    }
})
}
