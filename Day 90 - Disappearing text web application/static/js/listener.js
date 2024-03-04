var textArea = document.getElementsByClassName('textarea')[0];

const maxTime = 5000;
const step = 100;

let timerRunning = false;
let elapsedTime = 0;
let boxShadowSize = 0;

const timer = () => {
    elapsedTime += 100;
    boxShadowSize += 0.4

    if (elapsedTime <= maxTime) {
        setTimeout(timer, step);
        console.log(elapsedTime);
        if (elapsedTime > 4000) {
            boxShadowSize += 0.4
            textArea.style.boxShadow = `0 0 ${boxShadowSize}px 6px crimson`
        } else if (elapsedTime > 3000) {
            boxShadowSize += 0.2
            textArea.style.boxShadow = `0 0 ${boxShadowSize}px 4px orange`
        } else if (elapsedTime > 2000) {
            textArea.style.boxShadow = `0 0 ${boxShadowSize}px 2px yellow`
        }
    } else {
        textArea.value = ''
        textArea.style.boxShadow = 'none'
        timerRunning = false
    };
};

textArea.addEventListener('input', () => {
    elapsedTime = 0;
    if (!timerRunning) {
        timer();
        timerRunning = true;
    }
});
