# from PIL import Image
#
#
# def get_jpg_size(jpg_file):
#     try:
#         with Image.open(jpg_file) as img:
#             return img.size
#     except FileNotFoundError:
#         print(f"Error: File '{jpg_file}' not found.")
#         return None
#     except Exception as e:
#         print(f"Error processing file '{jpg_file}': {str(e)}")
#         return None
