
let sel_file;

// input에 파일이 올라올 때 (input에 change를 트리거할 때) 함수 실행
$(document).ready(function() {
    $("#input_img").on("change", handleImgFileSelect);
});

function handleImgFileSelect(e) {
    let files = e.target.files;
    // =arguments =object (not array)
    let filesArr = Array.prototype.slice.call(files);
    // 이 코드가 존재하는 함수의 매개변수로 넘어온 값들을 array로 변환

    filesArr.forEach(function (f) {
        sel_file = f;
        // 파일을 읽기 위한 FileReader 객체 생성
        let reader = new FileReader();
        // 이미지가 로드 되면,
        reader.onload = function (e) {
            // 이미지 Tag의 SRC 속성에 읽어들인 file 내용을 지정
            $("#img").attr("src", e.target.result);
        }
        // reader가 file 내용을 읽어 dataURL 형식의 문자열로 저장
        reader.readAsDataURL(f);
    });
}

function show_msg(){
    //풀 이미지 사라지는 것을 1초뒤로 딜레이.
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
                },300);
        });
    });
}

function box_change(){ //메세지1 클릭시 여기서 메세지2의 zindex를 변경
    var msg2 = document.getElementById('pop');
        msg2.style.zIndex = '5';
//  document.getElementById('pop').style.zIndex = '5';
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
