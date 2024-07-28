const video = document.getElementById('video');
const canvas = document.getElementById('canvas');
const qrContent = document.getElementById('qr-content');
const openLinkBtn = document.getElementById('open-link');
const canvasContext = canvas.getContext('2d');

let scanning = false;

navigator.mediaDevices.getUserMedia({ video: { facingMode: 'environment' } })
    .then(stream => {
        video.srcObject = stream;
        video.setAttribute('playsinline', true);
        video.play();
        scanning = true;
        requestAnimationFrame(scanQRCode);
    })
    .catch(error => {
        alert('Error accessing camera: ' + error);
    });

function scanQRCode() {
    if (scanning && video.readyState === video.HAVE_ENOUGH_DATA) {
        canvas.height = video.videoHeight;
        canvas.width = video.videoWidth;
        canvasContext.drawImage(video, 0, 0, canvas.width, canvas.height);
        const imageData = canvasContext.getImageData(0, 0, canvas.width, canvas.height);
        const code = jsQR(imageData.data, imageData.width, imageData.height, {
            inversionAttempts: 'dontInvert',
        });

        if (code) {
            qrContent.textContent = `Scanned QR Code Content: ${code.data}`;
            openLinkBtn.style.display = 'block';
            openLinkBtn.onclick = () => {
                if (code.data.startsWith('http://') || code.data.startsWith('https://')) {
                    window.open(code.data, '_blank');
                } else {
                    alert('Scanned content is not a link.');
                }
            };
            scanning = false; // stop scanning once a code is found
        }
    }
    if (scanning) {
        requestAnimationFrame(scanQRCode);
    }
}