
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

function show_msg(){
    //이미지 사라지는 것을 1초뒤로 딜레이.
    setTimeout(function(){$('#bye').hide();},1000);
    //이미지 크기 조절 애니메이션
    $('#img').animate({
        width: '50%',height:'auto'
    },500,function() {
        $(this).animate({
            width: '90%',height:'auto'
        }, 200, function () {
            $(this).animate({
                    width: '70%',height:'auto'
                },
                300);
        });
    });
}

function box_change(){
    var msg2 = document.getElementById('pop');
        msg2.style.zIndex = '5';
}

function posting_img() {
    show_modal()
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
            // alert(response["msg"])
            setTimeout(function() {
                window.location.href = '/pokedex/' + title;
            }, 2000);
        }
    });

}

function show_modal() {
    $('.modal_container').show();
    $('html').css("overflow", "hidden");
}
