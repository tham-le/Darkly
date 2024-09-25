const formData = new FormData();
formData.append('file', document.querySelector('input[type=file]').files[0]);

fetch('http://192.168.56.3/index.php?page=upload', {
  method: 'POST',
  body: formData,
})
.then(response => response.text())
.then(data => console.log(data))
.catch(error => console.error('Error:', error));
