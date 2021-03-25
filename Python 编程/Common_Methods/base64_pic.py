import base64

img_path = "../file/2.jpg"
with open(img_path, 'rb') as f:
    """编码base64图片"""
    img_data = f.read()
    base64_data = base64.b64encode(img_data)
    # base64_data = str(base64_data,'utf-8')
    file = open('1.txt','wb')
    file.write(base64_data)
    file.close()

with open('1.txt','r') as f:
    """解码base64为图片"""
    img_data = base64.b64decode(f.read())
    file = open('1.jpg','wb')
    file.write(img_data)
    file.close()