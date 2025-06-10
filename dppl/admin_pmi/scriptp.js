
       // Sidebar Toggle
document.querySelector('.sidebar-toggle')?.addEventListener('click', function() {
    document.querySelector('.sidebar').classList.toggle('collapsed');
    document.querySelector('.main-content').classList.toggle('expanded');
});

// Highlight active menu item based on current page
document.addEventListener('DOMContentLoaded', function() {
    const currentPage = window.location.pathname.split('/').pop();
    const menuItems = document.querySelectorAll('.sidebar-menu li a');
    
    menuItems.forEach(item => {
        const href = item.getAttribute('href');
        if (href === currentPage) {
            item.classList.add('active');
        } else {
            item.classList.remove('active');
        }
    });
    
    // Form submission for adding blood stock
    document.getElementById('addStockForm')?.addEventListener('submit', function(e) {
        e.preventDefault();
        // Add your form submission logic here
        console.log('Form submitted');
    });
});

// Initialize Charts
function initializeCharts() {
    // Donor Statistics Chart (Bar Chart)
    const donorStatsCtx = document.getElementById('donorStatsChart')?.getContext('2d');
    if (donorStatsCtx) {
        new Chart(donorStatsCtx, {
            type: 'bar',
            data: {
                labels: ['Total Pendonor', 'Bulan Ini', 'Hari Ini'],
                datasets: [{
                    label: 'Jumlah Pendonor',
                    data: [1245, 156, 15],
                    backgroundColor: [
                        'rgb(255, 0, 21)',
                        'rgb(255, 0, 21)',
                        'rgb(255, 0, 21)'
                    ],
                    borderColor: [
                        'rgba(230, 57, 70, 1)',
                        'rgba(230, 57, 70, 1)',
                        'rgba(230, 57, 70, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }

    // Blood Stock Chart (Pie Chart)
    const bloodStockCtx = document.getElementById('bloodStockChart')?.getContext('2d');
    if (bloodStockCtx) {
        new Chart(bloodStockCtx, {
            type: 'pie',
            data: {
                labels: ['A', 'B', 'AB', 'O'],
                datasets: [{
                    data: [120, 85, 45, 150],
                    backgroundColor: [
                        'rgba(255, 0, 0, 0.7)',
                        'rgba(0, 153, 255, 0.7)',
                        'rgba(248, 178, 0, 0.7)',
                        'rgba(0, 55, 255, 0.7)'
                    ],
                    borderColor: [
                        'rgba(255, 0, 0, 0.7)',
                        'rgba(0, 153, 255, 0.7)',
                        'rgba(248, 178, 0, 0.7)',
                        'rgba(0, 55, 255, 0.7)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true
            }
        });
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeCharts();
    
    // Add event listener for view buttons
    document.getElementById('viewDonorReport')?.addEventListener('click', function() {
        document.getElementById('donorReportModal').style.display = 'block';
    });
    
    document.getElementById('manageBloodStock')?.addEventListener('click', function() {
        document.getElementById('bloodStockModal').style.display = 'block';
    });
    
    document.getElementById('viewEmergencyCases')?.addEventListener('click', function() {
        document.getElementById('emergencyCasesModal').style.display = 'block';
    });
    
    // Close modals
    document.querySelectorAll('.close-modal').forEach(btn => {
        btn.addEventListener('click', function() {
            this.closest('.modal').style.display = 'none';
        });
    });
    
    // Close modal when clicking outside
    window.addEventListener('click', function(e) {
        if (e.target.classList.contains('modal')) {
            e.target.style.display = 'none';
        }
    });
});

function confirmDonor(id, nama) {
    if(confirm(`Apakah ${nama} sudah memenuhi syarat donor (berat badan >45kg, tekanan darah normal)?`)) {
        // Lanjutkan proses donor
    }
}

// Notifikasi sukses
notyf.success('Permintaan darah darurat telah dikirim ke 10 pendonor terdekat!');
// Notifikasi gagal
notyf.error('Stok darah golongan AB+ habis! Hubungi UTD terdekat.');

if(golonganDarah === "" || alamat === "") {
    notyf.error('Golongan darah dan alamat wajib diisi!');
    return false;
}


<select onchange="filterPendonor(this.value)">
    <option>Pilih Golongan Darah</option>
    <option value="A">A</option>
    <option value="B">B</option>
    <option value="AB">AB</option>
    <option value="O">O</option>
</select>


function confirmDeletePendonor(id) {
    if(confirm("Data pendonor akan dihapus permanen. Lanjutkan?")) {
        window.location.href = `delete.php?id=${id}`;
    }
}


function showStatusDonor(nama, terakhirDonor) {
    alert(`${nama} terakhir donor pada ${terakhirDonor}. Interval donor minimal 3 bulan.`);
}


if ($auth->login($username, $password, $role)) {
    header("Location: $role.php"); // Redirect berdasarkan role (admin/pendonor/staf)
} else {
    notyf.error('Login gagal: Kredensial tidak valid');
}


try {
    $db->insert('donors', $data);
    notyf.success('Pendonor berhasil didaftarkan!');
} catch (Exception $e) {
    notyf.error('Gagal: ' . $e->getMessage());
}



$stmt = $db->prepare("INSERT INTO donors (nama, golongan_darah) VALUES (?, ?)");
$stmt->execute([$nama, $golonganDarah]);
