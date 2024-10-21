function selection(option) {
    // 이미 선택된 경우 선택 해제
    if (option.classList.contains('selected')) {
        option.classList.remove('selected');
    } else {
        // 다른 모든 선택된 옵션의 'selected' 클래스 제거
        const options = document.querySelectorAll('.option');
        options.forEach(opt => {
            opt.classList.remove('selected');
        });

        // 선택된 옵션에 'selected' 클래스 추가
        option.classList.add('selected');
    }
}

function showTestScreen() {
    document.getElementById('home-screen').classList.remove('active');
    document.getElementById('test-screen').classList.add('active');
}

function nextQuestion() {
    const currentScreen = document.querySelector('.screen.active');
    currentScreen.classList.remove('active');

    const nextScreen = currentScreen.nextElementSibling;
    if (nextScreen && nextScreen.classList.contains('screen')) {
        nextScreen.classList.add('active');
    } else {
        alert("모든 질문이 끝났습니다!");
    }
}

function previousQuestion() {
    const currentScreen = document.querySelector('.screen.active');
    currentScreen.classList.remove('active');

    const previousScreen = currentScreen.previousElementSibling;
    if (previousScreen && previousScreen.classList.contains('screen')) {
        previousScreen.classList.add('active');
    } else {
        alert("첫 번째 질문입니다!");
    }
}

// Initialize first screen as active
document.getElementById('home-screen').classList.add('active');
 