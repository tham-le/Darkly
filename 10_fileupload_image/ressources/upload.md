# File upload vulnerability report

### Location: 
***http://192.168.56.3/index.php?page=upload***

## Description:

```
<form enctype="multipart/form-data" action="#" method="POST">

	<input type="hidden" name="MAX_FILE_SIZE" value="100000">
	Choose an image to upload:
	<br>
	<input name="uploaded" type="file"><br>
	<br>
	<input type="submit" name="Upload" value="Upload">

	</form>
```

## Recommendations: