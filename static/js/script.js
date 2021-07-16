// const nav = document.querySelector('.navbar-nav');
// nav.addEventListener('click', function (e) {
// 	const newLocal = 'nav-item nav-link';
// 	if (e.target.className == newLocal) {
// 		// console.log(e.target);
// 		e.preventDefault();
// 		e.target.classList.remove('active');
// 	}
// 	e.target.classList.add('active');
// });



$(function () {

	$('.tombolTambahData').on('click', function () {
		$('#nama').val('');
		$('#npm').val('');
		$('#email').val('');
		$('#jurusan').val('');
		$('#id').val('');

		$('#formModalLabel').html('Tambah Data Mahasiswa');
		$('.modal-footer button[type=submit]').html('Tambah Data');



	});

	$('.tampilModalUbah').on('click', function () {

		$('#formModalLabel').html('Ubah Data Mahasiswa');
		$('.modal-footer button[type=submit]').html('Ubah Data');
		$('.modal-body form').attr('action', 'http://127.0.0.1/phpmvc/public/mahasiswa/edit');


		const id = $(this).data('id');

		$.ajax({
			url: 'http://127.0.0.1/phpmvc/public/mahasiswa/getEdit',
			data: { id: id },
			method: 'post',
			dataType: 'json',
			success: function (data) {
				$('#nama').val(data.nama);
				$('#npm').val(data.npm);
				$('#email').val(data.email);
				$('#jurusan').val(data.jurusan);
				$('#id').val(data.id);
			}
		})
	});
});




