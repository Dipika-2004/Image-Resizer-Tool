import os
from PIL import Image
input_folder = "D:\\project_images\\original_images"
output_folder = "D:\\project_images\\result_images"
new_size = (800, 800)  
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.webp')):
        file_path = os.path.join(input_folder, filename)
        try:
            with Image.open(file_path) as img:
                img = img.convert('RGB')
                img_resized = img.resize(new_size, Image.LANCZOS) 
                output_path = os.path.join(output_folder, filename)
                img_resized.save(output_path)
                print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")
print("All images have been resized and saved.")
