
<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>

<h1>
  hey there
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>
</h1>


### 🧑‍💻: About Us :
- :telescope: We are Studying Data & AI and contributing for building a image analyzer of LinkedIn profile pictures.

- At the origin of the idea and our Business Coach : Jean-Charles TASSAN
- Our Technical Coach : Théo GIGANT


# DeepAnalyzer

# Group members :
-Walid KHIRDINE

-Oussama BOUACEM

-Racim CHEBLI 

-Redouane KARA

-Maha Yasmine AOUISSAT

-Dorra DEBBICHE

# DeepAnalyzerImages

## Ressources

* Manage the stress of the consultant in case of not signing a client contract

* Be able to have parameters prior to the interview to determine whether or not there is a possibility of getting it to adhere (define a benchmark before the interview)

* Define the best strategy during the meeting with the customer to get them on board and create a tool for this purpose, operational and of the AI ​​vision type (cf. Microservices and DevOps systems)

## Dependencies for the Scraper

* Anaconda or Miniconda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

## Setup

1. Create a new conda env named deepsimageanalyser (if you haven't already) for the project in the Conda application or in the terminal:
```
conda create --name deepsimageanalyser python=3.9.7 
```

2. Activate the conda env (you can check your availables env with: conda env list):
```
conda activate deepsimageanalyser
```

3. Install the project python dependencies :
```
pip install -r requirements.txt
```

4. Install Webdriver in your computer to be able to launch it, this is the link:
```
https://chromedriver.chromium.org/downloads
```

After download it to your repository of project add the path of webdriver.exe into scraper.py and linkedin profile to the .env file

5. Launch the scraper to get profiles images from linkedin My Network :

```
python scrapernetwork.py
```

There is also scraperprofile.py which enter to each profile and scrape a picture to have better quality of images but there is restriction to enter for a many number of profiles, 30 profiles per day

```
python scraperprofile.py
```

<div align="center">
  <img src="https://lalalab.zendesk.com/hc/article_attachments/4411304152338/LoathsomeWaryDugong-max-1mb.gif" width="300"/>
</div>


## Project structure

    
-- Scraper/images/ : this folder contains all profiles images
    
-- Scraper/scrapernetwork.py : contains functions to do the scraping of images from the page My network

-- Scraper/scraperprofile.py : contains functions to do the scraping of images from the page of each profile

-- Scraper/webdriver : the webdriver.exe repository
    
-- Scraper/.env.dist : contains variable WEBDRIVER_PATH, LOCAL_IMAGES, LINKEDIN_USERNAME, LINKEDIN_PASSWORD 

   don't forget to remove .dist to the .env and adding for each field the values of the path and linkedin profile

-- Scraper/requirements.txt : this files will list the dependencies of the scraper

-- Scraper/storelink.txt : this files contains the link of each profile visited

-- Scraper/imagename.txt : this files contains the link of each picture profile scraped
  
----- 

-- Clip model/Roboflow_CLIP_Zero_Shot_Classification.ipynb : this file contain the model clip to train on the images

-- 


