# scalableImageTransformations


Python package related to scaling image transformations

```python
import scalableImageTransformations 
from scalableImageTransformations import imageTransformation
from pprint import pprint

if __name__=="__main__":
    folder_path = r"C:\Users\prakhar.a.gandhi\Downloads\New folder"
    transformations_list = [A.HorizontalFlip(p=1)]
    progress_bar = True
    results = imageTransformation.apply_transformation_to_folder_of_images(folder_path,transformations_list,progress_bar)
    pprint(results)
```

