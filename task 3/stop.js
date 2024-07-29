let minutes = 0;
let seconds = 0;
let milliseconds = 0;
let intervalId = null;
let isRunning = false;

const minutesElement = document.getElementById('minutes');
const secondsElement = document.getElementById('seconds');
const millisecondsElement = document.getElementById('milliseconds');
const startButton = document.getElementById('start-btn');
const pauseButton = document.getElementById('pause-btn');
const resetButton = document.getElementById('reset-btn');

startButton.addEventListener('click', startTimer);
pauseButton.addEventListener('click', pauseTimer);
resetButton.addEventListener('click', resetTimer);

function startTimer() {
    if (!isRunning) {
        intervalId = setInterval(updateTimer, 10);
        isRunning = true;
        startButton.disabled = true;
        pauseButton.disabled = false;
        resetButton.disabled = false;
    }
}

function pauseTimer() {
    clearInterval(intervalId);
    isRunning = false;
    startButton.disabled = false;
    pauseButton.disabled = true;
}

function resetTimer() {
    minutes = 0;
    seconds = 0;
    milliseconds = 0;
    minutesElement.textContent = '00';
    secondsElement.textContent = '00';
    millisecondsElement.textContent = '000';
    clearInterval(intervalId);
    isRunning = false;
    startButton.disabled = false;
    pauseButton.disabled = true;
    resetButton.disabled = true;
}

function updateTimer() {
    milliseconds += 10;
    if (milliseconds >= 1000) {
        milliseconds = 0;
        seconds++;
        if (seconds >= 60) {
            seconds = 0;
            minutes++;
        }
    }
    minutesElement.textContent = pad(minutes);
    secondsElement.textContent = pad(seconds);
    millisecondsElement.textContent = pad(milliseconds, 3);
}

function pad(number, length = 2) {
    return String(number).padStart(length, '0');
}