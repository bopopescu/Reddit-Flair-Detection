# Reddit Flair Detector

A Reddit Flair Detector web application to detect flairs of India subreddit posts using Machine Learning algorithms. The application can be found live at [Reddit Flair Detector](https://flair-detector-anshumanpati.herokuapp.com).

### Directory Structure

The directory is a ***Flask*** web application set-up for hosting on *Heroku* servers. The description of files and folders can be found below:
 1. [Data-Acquisition Notebook](https://github.com/AnshumanPati/Reddit-Flair-Detection/tree/master/Jupyter%20Notebooks/reddit_data_collection.ipynb) contains all the code that was used to fetch data using PRAW API from reddit and adding it to the mongodb database using pymongo. It was the fetched back from the data base and pre-processed to add it into a CSV file to do the data analysis and build the machine learning model. It was also preprocessed and stored as a json file.
 2. [Exploratory Data Analysis Notebook](https://github.com/AnshumanPati/Reddit-Flair-Detection/tree/master/Jupyter%20Notebooks/exploratory_data_analysis.ipynb) contains the code used to do various visual and inferential data analysis and make conclusions based on the visualizations.
  3. [Flair-Detector Models Notebook](https://github.com/AnshumanPati/Reddit-Flair-Detection/blob/master/Jupyter%20Notebooks/flair_detection_models.ipynb) contains the code used to train various machine learning models and check the accuracy on different features and to choose the best model for evaluation.
  4. [requirements.txt](https://github.com/AnshumanPati/Reddit-Flair-Detection/blob/master/requirements.txt) - Containing all Python dependencies of the project.
  5. [nltk.txt](https://github.com/AnshumanPati/Reddit-Flair-Detection/blob/master/nltk.txt) - Containing all NLTK library needed dependencies.
  6. [Procfile](https://github.com/AnshumanPati/Reddit-Flair-Detection/blob/master/app/Procfile) - Needed to setup Heroku.
  7. [templates](https://github.com/AnshumanPati/Reddit-Flair-Detection/tree/master/app/templates) - Folder containing HTML files.
  8. [static](https://github.com/AnshumanPati/Reddit-Flair-Detection/tree/master/app/static) - Folder containing CSS and JS files.
  9. [app](https://github.com/AnshumanPati/Reddit-Flair-Detection/tree/master/app) - Folder containing the main application which loads the Machine Learning models and renders the results on the web application.
  10. [Data](https://github.com/AnshumanPati/Reddit-Flair-Detection/tree/master/Data) - Folder containing CSV, JSON and MongoDB instances of the collected data.
  11. [model](https://github.com/AnshumanPati/Reddit-Flair-Detection/tree/master/app/model) - Folder containing the saved model.
  12. [Jupyter Notebooks](https://github.com/AnshumanPati/Reddit-Flair-Detector/tree/master/Jupyter%20Notebooks) - Folder containing Jupyter Notebooks to collect Reddit India data and train Machine Learning models.
  
### Codebase

The entire code has been developed using Python programming language, utilizing it's powerful text processing and machine learning modules. The application has been developed using Flask web framework and hosted on Heroku web server.

### Project Execution

  1. Open the `Terminal`.
  2. Clone the repository by entering `git clone https://github.com/AnshumanPati/Reddit-Flair-Detection.git`.
  3. Ensure that `Python3` and `pip` is installed on the system.
  4. Create a `virtualenv` by executing the following command: `virtualenv -p python3 env`.
  5. Activate the `env` virtual environment by executing the follwing command: `source env/bin/activate`.
  6. Enter the cloned repository directory and execute `pip install -r requirements.txt`.
  7. Enter `python` shell and `import nltk`. Execute `nltk.download('stopwords')` and exit the shell.
  8. Now, execute the following command: `python manage.py runserver` and it will point to the `localhost` with the port.
  9. Hit the `IP Address` on a web browser and use the application.
  
### Dependencies

The following dependencies can be found in [requirements.txt](https://github.com/radonys/Reddit-Flair-Detector/blob/master/requirements.txt):

  1. [praw](https://praw.readthedocs.io/en/latest/)
  2. [scikit-learn](https://scikit-learn.org/)
  3. [nltk](https://www.nltk.org/)
  4. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
  5. [bs4](https://pypi.org/project/bs4/)
  6. [pandas](https://pandas.pydata.org/)
  7. [numpy](http://www.numpy.org/)
  8. [matplotlib](https://matplotlib.org/)
  
### Approach

Going through various literatures available for text processing and suitable machine learning algorithms for text classification, I based my approach using [[2]](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568) which described various machine learning models like Naive-Bayes, Linear SVM and Logistic Regression for text classification with code snippets. Along with this, I tried other models like Random Forest and Multi-Layer Perceptron for the task. I have obtained test accuracies on various scenarios which can be found in the next section.

The approach taken for the task is as follows:

  1. Collect 100 India subreddit data for each of the 12 flairs using `praw` module [[1]](http://www.storybench.org/how-to-scrape-reddit-with-python/).
  2. The data includes *title, comments, body, url, author, score, id, time-created* and *number of comments*.
  3. For **comments**, only top level comments are considered in dataset and no sub-comments are present.
  4. The ***title, comments*** and ***body*** are cleaned by removing bad symbols and stopwords using `nltk`.
  5. Five types of features are considered for the the given task:
    
    a) Title
    b) Comments
    c) Urls
    d) Body
    e) Combining Title, Comments and Urls as one feature.
  6. The dataset is split into **70% train** and **30% test** data using `train-test-split` of `scikit-learn`.
  7. The dataset is then converted into a `Vector` and `TF-IDF` form.
  8. Then, the following ML algorithms (using `scikit-learn` libraries) are applied on the dataset:
    
    a) Naive-Bayes
    b) Linear Support Vector Machine
    c) Logistic Regression
    d) Random Forest
    e) MLP
   9. Training and Testing on the dataset showed the **Random Forest** showed the best testing accuracy of **77.97%** when trained on the combination of **Title + Comments + Url** feature.
   10. The best model is saved and is used for prediction of the flair from the URL of the post.
    
### Results

#### Title as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.6011904762      |
| Linear SVM                 | 0.6220238095      |
| Logistic Regression        | **0.6339285714**  |
| Random Forest              | 0.6160714286      |
| MLP                        | 0.4970238095      |

#### Body as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.2083333333      |
| Linear SVM                 | 0.2470238095      |
| Logistic Regression        | 0.2619047619      |
| Random Forest              | **0.2767857143**  |
| MLP                        | 0.2113095238      |

#### URL as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.3005952381      |
| Linear SVM                 | **0.3898809524**  |
| Logistic Regression        | 0.3690476190      |
| Random Forest              | 0.3005952381      |
| MLP                        | 0.3214285714      |

#### Comments as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.5357142857      |
| Linear SVM                 | 0.6190476190      |
| Logistic Regression        | **0.6220238095**  |
| Random Forest              | 0.6011904762      |
| MLP                        | 0.4761904762      |

#### Title + Comments + URL as Feature

| Machine Learning Algorithm | Test Accuracy     |
| -------------              |:-----------------:|
| Naive Bayes                | 0.6190476190      |
| Linear SVM                 | 0.7529761905      |
| Logistic Regression        | 0.7470238095      |
| Random Forest              | **0.7797619048**  |
| MLP                        | 0.4940476190      |


### Intuition behind Combined Feature

The features independently showed a test accuracy near to **60%** with the `body` feature giving the worst accuracies during the experiments. Hence, it was excluded in the combined feature set.

### References

1. [How to scrape data from Reddit](http://www.storybench.org/how-to-scrape-reddit-with-python/)
2. [Multi-Class Text Classification Model Comparison and Selection](https://towardsdatascience.com/multi-class-text-classification-model-comparison-and-selection-5eb066197568)
