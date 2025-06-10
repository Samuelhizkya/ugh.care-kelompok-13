document.addEventListener('DOMContentLoaded', function() {
    // Elemen DOM
    const video = document.getElementById('video');
    const canvas = document.getElementById('canvas');
    const photoResult = document.getElementById('photoResult');
    const captureBtn = document.getElementById('captureBtn');
    const retakeBtn = document.getElementById('retakeBtn');
    const saveBtn = document.getElementById('saveBtn');
    const countdownOverlay = document.getElementById('countdownOverlay');
    const countdownNumber = document.getElementById('countdownNumber');
    
    // Variabel
    let cameraStream = null;
    let photoDataUrl = null;
    let countdownInterval = null;

    // 1. Fungsi memulai kamera
    async function startCamera() {
        try {
            // Hentikan kamera jika sedang berjalan
            if (cameraStream) {
                cameraStream.getTracks().forEach(track => track.stop());
            }
            
            // Minta akses kamera
            cameraStream = await navigator.mediaDevices.getUserMedia({
                video: {
                    facingMode: 'user',
                    width: { ideal: 640 },
                    height: { ideal: 480 }
                },
                audio: false
            });
            
            // Tampilkan video
            video.srcObject = cameraStream;
            video.style.display = 'block';
            photoResult.style.display = 'none';
            
        } catch (error) {
            console.error("Error mengakses kamera:", error);
            alert("Oops! Kamera tidak dapat diakses. Pastikan Anda memberikan izin.");
            
            // Tampilkan pesan error
            const cameraFrame = document.querySelector('.camera-frame');
            cameraFrame.innerHTML = '<div style="color:white;text-align:center;padding-top:180px;font-size:1.5rem;">Kamera tidak dapat diakses 😢</div>';
            cameraFrame.style.backgroundColor = '#FF6B8B';
        }
    }

    // 2. Fungsi hitungan mundur
    function startCountdown() {
        let count = 3;
        
        // Tampilkan overlay hitungan
        countdownOverlay.style.display = 'flex';
        countdownNumber.textContent = count;
        countdownNumber.className = 'countdown-number countdown-3';
        captureBtn.disabled = true;
        
        countdownInterval = setInterval(() => {
            count--;
            
            if (count > 0) {
                countdownNumber.textContent = count;
                countdownNumber.className = `countdown-number countdown-${count}`;
            } else {
                // Selesai hitungan
                clearInterval(countdownInterval);
                countdownOverlay.style.display = 'none';
                captureBtn.disabled = false;
                
                // Ambil foto
                takePhoto();
            }
        }, 1000);
    }

    // 3. Fungsi ambil foto
    function takePhoto() {
        if (video.readyState === 4) {
            // Atur ukuran canvas
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;
            
            // Ambil gambar
            const context = canvas.getContext('2d');
            context.drawImage(video, 0, 0, canvas.width, canvas.height);
            
            // Simpan hasil
            photoDataUrl = canvas.toDataURL('image/png');
            photoResult.style.backgroundImage = `url(${photoDataUrl})`;
            
            // Tampilkan hasil
            video.style.display = 'none';
            photoResult.style.display = 'block';
            
            // Update tombol
            captureBtn.style.display = 'none';
            retakeBtn.style.display = 'inline-block';
            saveBtn.style.display = 'inline-block';
        }
    }

    // 4. Event listener tombol
    captureBtn.addEventListener('click', startCountdown);
    
    retakeBtn.addEventListener('click', function() {
        video.style.display = 'block';
        photoResult.style.display = 'none';
        captureBtn.style.display = 'inline-block';
        retakeBtn.style.display = 'none';
        saveBtn.style.display = 'none';
    });
    
    saveBtn.addEventListener('click', function() {
        if (photoDataUrl) {
            const link = document.createElement('a');
            link.href = photoDataUrl;
            link.download = `photobooth-${new Date().getTime()}.png`;
            link.click();
            alert('Foto berhasil disimpan! 😊');
        }
    });

    // 5. Mulai kamera saat halaman dimuat
    startCamera();

    // 6. Hentikan kamera saat keluar
    window.addEventListener('beforeunload', function() {
        if (cameraStream) {
            cameraStream.getTracks().forEach(track => track.stop());
        }
        if (countdownInterval) {
            clearInterval(countdownInterval);
        }
    });
});