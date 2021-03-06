// 자바스크립트로 작성. 카운트다운
const remainTime = document.querySelector("#remain-time");
const remainText = document.querySelector("#remain-text")

function diffDay() {
    const birthTime = new Date("2022-08-28");
    const todayTime = new Date();
    const diff = birthTime - todayTime;

    const diffDay = Math.floor(diff / (1000 * 60 * 60 * 24));
    const diffHour = Math.floor((diff / (1000 * 60 * 60)) % 24);
    const diffMin = Math.floor((diff / (1000 * 60)) % 60);
    const diffSec = Math.floor(diff / 1000 % 60);

    if (diff <= 0) {
        remainText.style.display = "none"
        remainTime.innerHTML = "생일 축하해, 라이네라"
    } else {
        remainText.innerHTML = "라이네라 생일까지 앞으로"
        remainTime.innerHTML = `${diffDay}일 ${diffHour}시간 ${diffMin}분 ${diffSec}초`;
    }
}

diffDay();
setInterval(diffDay, 1000);

//클라이언트

$(document).ready(function() {
    save_message()
    show_message()
})

function save_message() {
    let name = $('#name').val()
    let message = $('#message').val()

    $.ajax({
        type: 'POST',
        url: '/post',
        data: {
            name_give: name,
            message_give : message
        },
        success: function(response) {
            console.log(response['msg'])
        }
    })
}

function show_message() {
    $('#order-box').empty()

    $.ajax({
        type: 'GET',
        url: '/post',
        data: {},
        success: function(response) {
            let rows = response['comments']
            for (let i = 0; i < rows.length; i++) {
                let name = rows[i]['name']
                let message = rows[i]['message']

                let temp_html = `<p id="user-message">${message}</p>
                                 <p id="user-name">${name}</p>`
                $('#order-box').append(temp_html)
            }
        }
    })
}