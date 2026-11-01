from PIL import Image, ImageOps
import numpy as np
import tensorflow as tf

def get_class(model_path, labels_path, image_path):
    """
    Функция для анализа изображения
    """
    np.set_printoptions(suppress=True)
    model = tf.keras.models.load_model(model_path, compile=False)
    with open(labels_path, 'r', encoding='utf-8') as f:
        class_names = f.readlines()
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert('RGB')
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.0)
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    return class_name[2:]

if __name__ == "__main__":
    name = get_class(model_path="keras_model.h5",
                     labels_path="",
                     image_path="")
    print(name)