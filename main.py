# import needed libraries
import os
import re
import logging
import shutil
from collections import Counter
from typing import Tuple,List
from shapely.geometry import Polygon
#-----------------------------------------------------------------------------------------------------------------

# Configuring the logging

logging.basicConfig(
    filename = "app.log",
    level = logging.INFO,
    format = "%(asctime)s ACTION : %(message)s",
    datefmt = "%Y-%m-%d %H:%M:%S"
)
#-----------------------------------------------------------------------------------------------------------------
# Datastorage Class

class DataStorage:
    
    def __init__(self):
        """Initialize with an empty dictionary."""
        self._data = {}
        logging.info(f"DataStorage Class started")
        
    def add(self, key: str, value: str):
        """Add or update a key-value pair."""
        self._data[key] = value
        logging.info(f"Added/update key:{key} with value:{value}")
        
    def get(self, key: str) -> str:
        """Retrieve the value for a given key."""
        if key in self._data:
            value = self._data[key]
            logging.info(f"Successfuly extracted key:{key} with corresponding value:{value}")
            return value 
        else:
            logging.info("tried to extract non-existing key:{key}")
            return "Key has not been found "
        
    def delete(self,key:str) -> None :
        """Delete a key-value pair if it exists."""
        if key in self._data:
            del self._data[key]
            logging.info(f"Deleted key:{key}")
        else:
            logging.info(f"tried to delete non-existing key:{key}")
            
    def list(self) -> dict: 
        logging.info(f"Listing all items in the dictionary")
        return self._data
#-----------------------------------------------------------------------------------------------------------------  
# Return the top k most frequent words in a text

def find_top_k_frequent_words(text: str, k: int) -> List[Tuple[str, int]]:
    words = re.findall(r"\b\w+\b", text.lower())
    words_counting = Counter(words)
    top_k_words = words_counting.most_common(k)
    return top_k_words

#-----------------------------------------------------------------------------------------------------------------
# Checking polygons collision or not

def check_polygon_collision(polygon1: List[Tuple[float, float]], polygon2: List[Tuple[float, float]]) -> bool:
    poly_1 = Polygon(polygon1)
    poly_2 = Polygon(polygon2)
    if poly_1.intersects(poly_2) or poly_1.contains(poly_2) or poly_2.contains(poly_1):
        return True
    else: 
        return False
#-----------------------------------------------------------------------------------------------------------------
# File Processing

class FileProcessor:
    @staticmethod
    def copy_directory(source_dir: str, target_dir: str) -> None:
        """Copy all contents from the source directory to the target directory."""
        try:
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                logging.info(f"Created target directory: {target_dir}")
            
            shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)
            logging.info(f"Copied directory from {source_dir} to {target_dir}")
        
        except Exception as e:
            logging.error(f"Error copying directory: {e}")

    @staticmethod
    def process_files(directory: str, extensions: List[str]) -> List[Tuple[str, int]]:
        """Process files in the directory with specific extensions and count lines."""
        results = []
        try:
            for root, _, files in os.walk(directory):
                for file in files:
                    if any(file.endswith(ext) for ext in extensions):
                        path = os.path.join(root, file)
                        with open(path, 'r') as f:
                            line_count = sum(1 for _ in f)
                        results.append((file, line_count))
                        logging.info(f"Processed file: {file}, Lines: {line_count}")
        except Exception as e:
            logging.error(f"Error processing files: {e}")
        
        return results
#-----------------------------------------------------------------------------------------------------------------
# Example usage of functions

def main():
    
    # 4. File Processing
    source_dir = 'D:/AI_based_control/project'
    target_dir = 'D:/AI_based_control/Thesis'
    FileProcessor.copy_directory(source_dir, target_dir)  
    print(FileProcessor.process_files(target_dir, ['.txt', '.log']))


if __name__ == "__main__":
    main()
#-----------------------------------------------------------------------------------------------------------------