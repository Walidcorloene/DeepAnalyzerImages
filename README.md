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

* Project objectives : 
Gérer le stress du consultant en cas de non signature de contrat client

Pouvoir disposer de paramètres en amont de l’entretien permettant de  déterminer s’il y a ou non une possibilité de le faire adhérer (définir un repère avant l’entretien)

Définir la meilleure stratégie lors de l’entretien avec le client pour le faire adhérer et créer un outil à cette fin, opérationnel et de type vision I.A. (cf. Microservices et systèmes DevOps)

## Dependencies

* Anaconda or Miniconda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html

## Setup

1. Create a new conda env named md4-api (if you haven't already) for the project in the Conda application or in the terminal:
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

4. Install Webdriver in your computer to be able to launch it:
```
https://chromedriver.chromium.org/downloads
```

After download it to your repository of project add the path of webdriver.exe and linkedin profile to the .env file

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


