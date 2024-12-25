# import needed libraries
import re
import logging
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
# Example usage of functions

def main():
    
    # 3. Polygon Collision Detection
    polygon1 = [(0, 0), (4, 0), (4, 4), (0, 4)]
    polygon2 = [(2, 2), (6, 2), (6, 6), (2, 6)]
    polygon3 = [(5, 5), (7, 5), (7, 7), (5, 7)]
    print(check_polygon_collision(polygon1,polygon2))
    print(check_polygon_collision(polygon1,polygon3))


if __name__ == "__main__":
    main()