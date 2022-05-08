
<div id="header" align="center">
  <img src="https://media.giphy.com/media/M9gbBd9nbDrOTu1Mqx/giphy.gif" width="100"/>
</div>

<h1>
  hey there
  <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="30px"/>
</h1>


### 🧑‍💻: About Us :
- :telescope: We are Studying as a Data & AI and contributing for building a analyzer images of profile linkedin.


# DeepAnalyzer

# Les membres du groupes :
-Walid KHIRDINE
-Oussama BOUACEM
-Racim CHEBLI 
-Redouane KARA
-Maha Yasmine AOUISSAT
-Dora DEBBICHE

# DeepAnalyzerImages

## Ressources

* Manage the stress of the consultant in case of not signing a client contract

* Be able to have parameters prior to the interview to determine whether or not there is a possibility of getting it to adhere (define a benchmark before the interview)

* Define the best strategy during the meeting with the customer to get them on board and create a tool for this purpose, operational and of the AI ​​vision type (cf. Microservices and DevOps systems)

## Dependencies

* Anaconda or Miniconda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

## Setup

1. Create a new conda env named deepsimageanalyser (if you haven't already) for the project in the Conda application or in the terminal:
```
conda create --name deepsimageanalyser python=3.7 
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

5. Launch the scraper to get profiles images from linkedin :

```
python scrap.py
```

## Project structure

    
-- images : this folder will contains all images
    
----- scraper.ipynb : contains class definitions for each database model

-- webdriver : the webdriver.exe repository
    
------- .env : contains variable PATH_WEBDRIVER, LINKEDIN_USERNAME, LINKEDIN_PASSWORD

-- requirements.txt : this files will list the dependencies of the project
    
----- 

-- 

-- 


