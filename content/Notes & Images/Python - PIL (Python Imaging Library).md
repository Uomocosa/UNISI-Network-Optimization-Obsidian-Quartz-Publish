```python
from PIL import Image

orginal_image = Image.open('__porva__.png')
```

---
# Usefull commands
```python
orginal_image.show()

orginal_image.save('new_name.jpg') #can also change the format

size = (300, 300)
orginal_image.thumbnail(size) #scale to PIXEL size
```
---

# IMPORTANT
### Relative Path
The PIL library supports relative path: if instead of **'file_name'** you use **'directory1/file_name'** it will save the file, or get the file named file_name from directory1

---
# IMPORTANT
### Image Size and Numpy Array Shape
When converting an **image** to a **[[numpy.array]]**  rember that **width and height must be inverted**:
```python
width, height = image(size)
## ... other code
numpy_matrix = np.array(image_pixels)
numpy_matrix = numpy.matrix.reshape(height, width)
```

---

Convert an RPG image to Black and White 
```python
image_BW = image_RGB.convert(mode = 'L')
```

---
Blur the image:
```python
blured_image = orginal_image.filter(ImageFilter.GaussianBlur(value))

```

