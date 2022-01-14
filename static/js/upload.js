
let sel_file;

$(document).ready(function() {
    $("#input_img").on("change", handleImgFileSelect);
});

function handleImgFileSelect(e) {
    let files = e.target.files;
    let filesArr = Array.prototype.slice.call(files);

    filesArr.forEach(function (f) {
        sel_file = f;
        let reader = new FileReader();
        reader.onload = function (e) {
            $("#img").attr("src", e.target.result);
        }
        reader.readAsDataURL(f);
    });
}
function box_change(){
    var wrap = document.getElementById('pop');
           wrap.style.zIndex = '3';
}
function posting_img() {
    let d = new Date()
    let time = d.getTime()
    let title = String(time)
    let file = $('#input_img')[0].files[0]
    let form_data = new FormData()
    form_data.append("file_give", file)
    form_data.append("title_give", title)

    $.ajax({
        type: "POST",
        url: "/api/upload/",
        data: form_data,
        cache: false,
        contentType: false,
        processData: false,
        success: function (response) {
            alert(response["msg"])
            window.location.href = '/pokedex/' + title
        }
    });
}