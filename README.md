# make image dataset

### Parent Scrip Files

- edit_files.py

  Tools to edit files as batch run.

- edit_images.py

  Tools to edit image files as batch run.

- edit_texts.py

  Tools to edit texts in files as batch run.

- make_image_dataset.py
   End-to-end dataset composition tool.

### Baseline (Recommended) Work Flow

#### 1. Data Preparation

1. Collect images and puts the files in a directory
2. Generate caption files with kohya_ss, etc, then the directory includes both of images and captions
3. make directories for image and caption to manage both separately.
4. Make Directories as a classs based on poses and camera angles
   for example, "below", "directright", "drectfront", "front", "left"
5. Put image and caption files to the directories (drag and drop works)


#### 2. Remove Background in images

This work improves the accuracy of image generation.

#### 3.Check Directories
- edit_files.py
  - report duplicated files across directories
  - remove duplicate files across directories in both of image and caption
  - rename a part of file name (ex. prefix) for all files
  - add prefix to all files
  - find file


#### 4. Edit Caption Files

- edit_texts.py
    - adding text in all text files
    - remove spaces in text for all files
    - remove duplicated commas for all files
    - remove particular words described in list file for all files
    - statistics report, how many tags and words are in the caption files

#### 5. Setup make_image_dataset.py

**Recommend:** Backup image and caption directories before run script.
The script genarates temporal directries for every steps, recommend to removes the directories before retrying the making.


**You need;**
- set directory paths in make_image_dataset.py including the temporal directories

The script also does rescaling images.

The script makes lr-flip then;
- make flipped files both of images and caption, separately in specified directories.
- the directory name having "right" and "left"are replaced with "left" and "right", respectively
- "right" or left in caption text also replaced, respectively
- when the right or left is not specified in caption, the replacement will use directory name directory "directright" adds "from directly right, from right, from side" for example for original directory and do lr-flip
