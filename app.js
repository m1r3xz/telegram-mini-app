// Initialize Telegram WebApp
const tg = window.Telegram.WebApp;

// Enable closing confirmation
tg.enableClosingConfirmation();

// Initialize the WebApp
tg.ready();

// Set up counter
let count = 0;
const countDisplay = document.getElementById('count');
const mainButton = tg.MainButton;

// Update display and main button
function updateDisplay() {
    countDisplay.textContent = count;
    mainButton.setText(`Count: ${count}`);
    if (!mainButton.isVisible) {
        mainButton.show();
    }
}

// Increase counter
function increase() {
    count++;
    updateDisplay();
    tg.HapticFeedback.impactOccurred('light');
}

// Decrease counter
function decrease() {
    count--;
    updateDisplay();
    tg.HapticFeedback.impactOccurred('light');
}

// Initialize
updateDisplay();

// Show user info
const userInfo = document.getElementById('username');
if (tg.initDataUnsafe?.user) {
    const user = tg.initDataUnsafe.user;
    userInfo.textContent = `Welcome, ${user.first_name}!`;
} else {
    userInfo.textContent = 'Welcome, Guest!';
}

// Handle popup button
const showPopupBtn = document.getElementById('showPopup');
showPopupBtn.addEventListener('click', () => {
    tg.showPopup({
        title: 'Hello!',
        message: 'This is a Telegram Mini App popup message.',
        buttons: [
            {type: 'ok'},
            {type: 'cancel'}
        ]
    });
});

// Set theme class
document.documentElement.className = tg.colorScheme;
