# Group Playlist Recommender
![Size](https://github-size-badge.herokuapp.com/sparsh-ai/reco-tut-gpr.svg)

In many social situations, like parties and road trips, groups of people with different music tastes will listen to music together. It's hard to please everyone, and it's even harder if you don't know what each person likes. There are multiple ways to synthesize the preferences of a group. Should you average their preferences? Should you try to make sure that no one hates the choices at the cost of excluding someone's favorites? This tutorial explores these questions by first generating a music profile for each person, and then applying different strategies to combine their preferences into a single playlist.

## Project structure
```
.
├── artifacts                         
│   ├── le_item.pkl                            # item label encoder
│   ├── le_user.pkl                            # user label encoder
│   └── models                                 # holds temp model files
├── code
│   ├── __init__.py
│   └── load_data.py                           # download raw dataset into bronze data layer
├── data
│   ├── bronze                                 # holds raw dataset file
│   └── silver
│       ├── test.parquet.gz                    # preprocessed test data
│       └── train.parquet.gz                   # preprocessed train data
├── docs                                
├── extras
├── LICENSE
├── notebooks
│   ├── reco-tut-gpr-01-data-ingestion.ipynb   # data ingestion notebook
│   └── reco-tut-gpr-t1-02-notebook.ipynb      # track-1 (T1) end-to-end notebook
├── outputs
│   ├── eval_results.csv                       # T1 evaluation results
│   ├── model_result_ensemble.csv              # T1 ensemble model results
│   ├── rankings_avg.csv                       # T1 average rankings
│   └── results.csv                            # T1 final outputs
├── README.md
├── requirements.txt
└── setup.py
```