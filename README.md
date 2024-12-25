# Python Developer Task: Data Storage, Algorithms, Polygon Collision, and File Operations

## Description
This Python project implements the following key features:

- **DataStorage Class:** A class to manage key-value data efficiently, supporting adding, retrieving, deleting, and listing data.
- **Top-K Frequent Words Algorithm:** A function to identify the most frequent words in a given text.
- **Polygon Collision Detection:** A function to check if two polygons intersect or if one contains the other.
- **File Processing:** A class that provides utilities to copy entire directories and process files with specific extensions (e.g., `.txt`, `.log`).
- **Logging:** The project includes logging functionality to track actions performed in the system, logged to `app.log`.

## Setup and Installation

### Clone the Repository:
To get started with the project, first clone the repository:
```bash
git clone https://github.com/shuhratkulboboev/Python-Developer-Task.git
cd path/to/directory
 ```

### Install Dependencies: 
    - Ensure that Python 3.8 or higher is installed .
    - Install the required package `shapely` using `pip install shapely`.

This makes it clear for users how to set up the environment for your project. Replace `<username>` with your GitHub username in the clone URL.
### Run Script: 
Run the main scirpt:
```bash
python main.py
 ```

## Features
### Logging:
All actions and significant events (e.g., adding a new key, copying directories, processing files) are logged in the app.log file, including timestamps.
```bash
tail -f app.log
 ```
### Project Structure:
```bash
/python-data-storage-algorithms
│
├── main.py        # Main script with all implemented features
├── app.log        # Log file for application actions
└── README.md      # Instructions for running the project
 ```
## Usage Examples
```bash
def main():
    
    # 1. Data Storage
    storage = DataStorage()
    storage.add("name", "Shukhrat")
    print(storage.get("name"))  
    storage.delete("name")
    print(storage.get("name"))

    # 2. Algorithm Implementation
    text = "Hello world! Hello everyone. This is the best company. Company, world,company, hello,world,world"
    print(find_top_k_frequent_words(text, 2))

    # 3. Polygon Collision Detection
    polygon1 = [(0, 0), (4, 0), (4, 4), (0, 4)]
    polygon2 = [(2, 2), (6, 2), (6, 6), (2, 6)]
    polygon3 = [(5, 5), (7, 5), (7, 7), (5, 7)]
    print(check_polygon_collision(polygon1,polygon2))
    print(check_polygon_collision(polygon1,polygon3))

    # 4. File Processing
    source_dir = 'D:/AI_based_control/project'
    target_dir = 'D:/AI_based_control/Thesis'
    FileProcessor.copy_directory(source_dir, target_dir)  
    print(FileProcessor.process_files(target_dir, ['.txt', '.log']))
if __name__ == "__main__":
    main()
 ```
