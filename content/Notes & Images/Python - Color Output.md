```python
def colorify_output(text, text2 = None,COLOR = None, on_COLOR = None):
    output_text = colored('%s'%text,'%s'%COLOR,'%s'%on_COLOR,attrs =[] )
    return output_text
```