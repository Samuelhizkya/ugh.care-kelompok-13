let buku = {
  judul: "Belajar JS",
  penulis: {
    'penulis utama': {
      nama: "Avav",
      age: 30,
      job: "author",
    },
    'penulis pendamping': {
      nama: "Juan",
      age: 28,
      job: "co-author",
    },
  },
  tahun: 2023,
  penerbit: "Gramedia",
  rating: 4.5,
}

console.log("Halo nama saya " + buku.penulis['penulis utama'].nama + ", saya berumur " + buku.penulis['penulis utama'].age + " tahun. " + "Saya bersama " + buku.penulis['penulis pendamping'].nama + " menulis buku " + buku.judul + " yang diterbitkan oleh " + buku.penerbit + " pada tahun " + buku.tahun + ". " + "Buku ini mendapatkan rating " + buku.rating + " dari pembaca.");

console.log("tes")
console.log("amel")