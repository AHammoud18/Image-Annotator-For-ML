# Image Annotator for ML

#### Image Annotator creates a JSON file of image annotations necessary for machine learning models.
##### This script is for CoreML which requires as JSON of image attributes along with the training data. [^1]

---

#### 1. You can get started by selecting the `browse folder` button.
#### 2. Hightlight the region desired within the image.
#### 3. Re-highlight regions until you find it satisfactory, when the bounding box is correct, select `confirm`.
#### 4. Each time you confim, the script will append the annoations of the bounding box and the image name to a dictionary and then forwards to the next image.
#### 5. After you've created bounding boxes for each image, select `done` to convert the dictionary into the required JSON format. 
> Exported JSON will be in the same path as the script.
[^1]: https://developer.apple.com/documentation/createml/building-an-object-detector-data-source.
  This link will direct you to apple's documentation page about JSON formatting, feel free to see how it's structured
  
 ###### Enjoy!
