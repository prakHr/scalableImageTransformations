import albumentations as A
from pprint import pprint
import os
from pprint import pprint
import multiprocessing
from mpire import WorkerPool
import cv2

def get_new_image(image_path,transformations_list):
    status = "ok"
    try:
        transform = A.Compose(transformations_list)
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        transformed = transform(image=image)
        image = transformed["image"]
        cv2.imwrite(image_path, image)
        return {"status":status,"image_path":image_path}
    except:
        return {"status":f"not {status}","image_path":image_path}

def apply_transformation_to_folder_of_images(folder_path,transformations_list,progress_bar):
    image_namea = os.listdir(folder_path)
    results = []
    for image_name in image_namea:
        image_path = os.path.join(folder_path,image_name)
        if not os.path.isfile(image_path):
            continue
        my_dict = {
            "image_path":image_path,
            "transformations_list":transformations_list
        }
        results.append(my_dict)
    num_cores = max(multiprocessing.cpu_count()//2,1)
    with WorkerPool(n_jobs=num_cores,daemon=False) as pool:
        results = pool.map(get_new_image,results,progress_bar=progress_bar)
    return results
