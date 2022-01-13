
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