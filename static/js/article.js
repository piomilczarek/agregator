/*global $*/
/*global Cropper*/
var cropData;

$(function() {

/*
form validation based on submit or cancel button click

*/

	$("#submit").click( function(e) {
	    e.preventDefault();
        var art = createArticle();
        console.log(art.artImgCrop);
        console.log(cropData);
        console.log(croppDataToObj(art.artImgCrop));
        sendToFlask(art);
	});

	$("#cancel").click( function(e) { //when cancel reload the page to reset the form
		  /*var article = createArticle();
		  displayArticle(article); */
	    window.location.href = window.location.protocol +'//'+ window.location.host; // + window.location.pathname;
	});
	
	$("#get").click( function(e) {
	    window.location.href = window.location.protocol +'//'+ window.location.host;
	});
    
    cropData = croppDataToObj($('#flaskdata').data('cropp'));
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
    //cropper.cropstart;
    console.log(cropper);
});//documnet ready

function createArticle(){
    var artId = $('#artId').val();
    var artTitle = $('#artTitle').val();
    var artDescr = $('#artDescr').val();
    var artUrl = $('#artUrl').val();
    var artImgUrl = $('#artImgUrl').val();
    var artTags = $('#artTags').val();
    var artStatus = $('#artStatus').val();
    var artUpdate = $('#artUpdate').val();
    var imgCrop = croppDataToString(cropData);
    var statusObj={"artId":artId, "artTitle":artTitle, "artDescr":artDescr, "artUrl":artUrl, "artImgUrl":artImgUrl, "artImgCrop":imgCrop, "artTags":artTags, "artStatus":artStatus, "artUpdate": artUpdate};
    return statusObj;
}

function croppDataToString(croppObj){
    var cropString=croppObj.height+";"+croppObj.width+";"+croppObj.rotate+";"+croppObj.scaleX+";"+croppObj.scaleY+";"+croppObj.x+";"+croppObj.y;
    return cropString;
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

function displayArticle(article){ // Push the object data to the div's on the website
    $('#artId').val(article.artId);
    $('#artTitle').val(article.artTitle);
    $('#artDescr').val(article.artDescr);
    $('#artUrl').val(article.artUrl);
    $('#artImgUrl').val(article.artImgUrl);
    $('#artTags').val(article.artTags);
    $('#artStatus').val(article.artStatus);
    $('#artUpdate').val(article.artUpdate);
}

function sendToFlask(article){ //
    //var statusObj={"artId":artId, "artTitle":artTitle, "artDescr":artDescr, "artUrl":artUrl, "artImgUrl":artImgUrl, "artTags":artTags, "artStatus":artStatus};
    $.ajax({
        url:"/robot/api/"+article.artId,
        type: "PUT",
        contentType:"application/json",
        dataType:"json",
        data: JSON.stringify(article),
        success: function(data) {
                //console.log(data);
                displayArticle(data);
                $("#artUpdate").css({"background-color":"#d6f5d6"});
        }
    
        
    });
}