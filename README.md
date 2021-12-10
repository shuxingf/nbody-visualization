How to run
1. Go to load.py. Between line 14 to line 29, change the paths to where you store the corresponding data.
2. Go to plot.py. Betweem line 14 to line 21, change the paths to where you want to store the images.
3. Run by using command line arguments, for example:

    "python main.py LMC 200 210" will generate 11 images centered on LMC using snapshots from number 200 to number 210.

    "python main.py MW 200 210" will generate images centered on MW using snapshots from number 200 to number 210.

   If you only want to generage an image for a specific snapshot, just add the single snapshot number after LMC or MW, for example
   
     "python main.py LMC 100"

The range of shnapshot numner is [10,235]

Due to the large amount of memory it consumes, it is not recommended to generate too many images at one go. 

Links to sample images and movies can be found in the folder "links"

The function to plot density profile is still in development.
