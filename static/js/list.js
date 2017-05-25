$(function() {
    
    var image = document.getElementById('image');
    var cropper = new Cropper(image, {
    aspectRatio: 350 / 180, checkCrossOrigin: false, data: cropData,
        crop: function() {
        var c=document.getElementById("canvas");
        c.width=350;
        c.height=180;
        var ctx=c.getContext("2d");
        var img=cropper.getCroppedCanvas({
                width: 350,
                height: 180});
        ctx.drawImage(img,0,0);
        cropData = cropper.getData(true);
        //console.log(cropper);
    }
    
    });
    
    
}

function croppDataToObj(croppString){
    var result = croppString.split(";");
    var croppObj = {
        "height": parseInt(result[0]),
        "width": parseInt(result[1]),
        "rotate": parseInt(result[2]),
        "scaleX": parseInt(result[3]),
        "scaleY": parseInt(result[4]),
        "x": parseInt(result[5]),
        "y": parseInt(result[6])
    };
    return croppObj;
}

function myFunc(vars) {
    console.log(vars);
    return vars
}