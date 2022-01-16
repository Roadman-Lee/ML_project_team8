$(document).ready(function (){//페이지 불러와지면
    $('#dex_container').hide(); //결과창은 숨기고
})
//
function clickmsg(){
    $('#msg_container').hide();
    $('#oh_box').hide();
    //도감이미지 서서히 출력되도록함
    $('#dex_container').fadeIn('slow');
}

