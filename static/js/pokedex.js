$(document).ready(function (){//페이지 불러와지면
    $('#dex_container').hide(); //결과창은 숨기고
})
function clickmsg(){
    $('#msg_container').hide();
    $('#dex_container').show();
}
function show_mon(){
    $.ajax({
        type: 'GET',
        url: '/pokedex/',
        data: {},
        success: function (response){
         alert('두구두구 당신은 어떤 포켓몬과 닮았을까요?')
        }
    })
}
