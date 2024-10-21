// CSRF 토큰을 가져오는 함수 (Django에서 필요)
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

// 사용자가 입력한 데이터를 백엔드로 전송하는 함수
function sendOptionsToBackend() {
    // 입력 값 가져오기
    const gender = document.getElementById("gender").value;
    const season = document.getElementById("season").value;
    const time = document.getElementById("time").value;
    const style = document.getElementById("style").value;
    const skinType = document.getElementById("skinType").value;
    const preferredScent = document.getElementById("preferredScent").value;
    const unpreferredScent = document.getElementById("unpreferredScent").value;

    // 사용자 선택 정보를 담은 객체
    const selectedOptions = {
        gender: gender,
        season: season,
        time: time,
        style: style,
        skinType: skinType,
        preferredScent: preferredScent,
        unpreferredScent: unpreferredScent
    };

    // Django 백엔드로 POST 요청 보내기
    fetch("/api/get-gpt-response/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken // Django CSRF 보호
        },
        body: JSON.stringify(selectedOptions)
    })
    .then(response => response.json())
    .then(data => {
        console.log("GPT 응답:", data.gpt_response);
        document.getElementById("gpt-response").innerText = data.gpt_response;
    })
    .catch(error => console.error("Error:", error));
}


