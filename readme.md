#  💜 Readme 💛
For my final year project I worked with the FashionMNIST data set and looked at working with fashion data. 
As part of this I found myself cleaning and prepping alot of data and experimenting with efficient ways to clean data. 

I came up with a method that worked for me using some snippets of code and utilities. 

**Note**: These are things that worked for me personally, there may be better ways to do things but I wanted to create something that might have helped someone like me at the start of my journey and I thought this process might be of use to someone out there.  

# Prerequisites  (Data Gathering) 
 - Gathering Data
 
First I gathered a dataset. To gather a large custom data set fast I used https://shoplook.io. 
When on shoplook I accessed lists of people's "likes." I chose to gather images from here because often these 
images were pre-formatted to appear on a white background and cutout around the image already. 

![enter image description here](https://i.ibb.co/F4Wd0k8/md1.png)

I used [this chrome bulk image downloader](https://chrome.google.com/webstore/detail/image-downloader/cnpniohnfphhjihaiiggeabnkjhpaldj) to select and download the images I wanted to add setting the 
directory to the images folder in my project. 

When I selected all the images I wanted for my dataset then I wanted to convert and rename all these images to the same type. I didn't write a script for this I was familiar with the ['Bulk Rename Utility'](https://www.bulkrenameutility.co.uk/) program already. As mentioned above this is not perhaps the best way to do things - just something that worked for me. To cut down on time it might be beneficial to write a script or executable file to rename all the images and convert to the same file type or even a webcrawler that downloads and gathers images for the dataset. 

Here I have shown the options I changed in the bulk rename utility. I set the name field to be removed, to prefix numbering - in this instance was from 1914. The extension has been set to .jpeg to match all of the other images to work well in the code and handle the images all in the same way. 
![enter image description here](https://i.ibb.co/Tr7704w/md1.png)


## Contouring Images 

The first thing I did was to contour the images and use canny edge detection to get an extracted version of the image. I used some pre-existing code for this which can be found [here](https://github.com/murtazahassan/OpenCV-Python-Tutorials-and-Projects/blob/master/Intermediate/RealTime_Shape_Detection_Contours.py). 

Image thresholds can be adjusted to get a more workable output. There are 2 classes provided for handling multiple images where you can pass in a range of images and can cycle through and adjust the threshold values and one that just takes in one image which can be used if you want to go back and adjust and resave an image (for example). 

Here we can see this being applied to a method and the pane with threshold that can be adjusted for the image. This is applied to data/1.jpeg that I have included as some sample data. 

Press any key to close the window or to go to the next image, alternatively I set a wait time so that images could be cycled through automatically and be set up to run when away from keyboard. 

![enter image description here](https://i.ibb.co/2MrqBdK/md2.png)

## Resize and view on MatLibPlot

The images were then resized and viewed on matlibplot. I read in the fashionmnist data set so I could cycle through those images and view and compare my results to those provided already. I found that contouring the images in this way, resizing and then viewing them tended to yield more clear and intrepretable images that could be used. 


## Results Comparison 

This is a result in fashion MNIST currently of a pair of trousers. As you can see we also want the background to be black and the output to look similar to this. 

![enter image description here](https://i.ibb.co/dfMQtWt/md3.png)

When inputting just the image without contours of the trousers from image 1 we get the result as shown below. The background is still white and even though this example looks relatively clear a large difference can be seen for items that are white on a white background or for images that resize and lose qualities such as logos and patterns. 

![enter image description here](https://i.ibb.co/Gxt8BpH/md4.png)

Here you can see the white background is replaced with a black background and the image matches the format of the fashion mnist outputs more clearly. Although we are losing some quality around the buttons of this image, quality is maintained at a higher level for images of shoes and bags also. 

![md5](https://i.ibb.co/mb2mDGD/md5.png)


