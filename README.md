# IPL Win Probability Predictor

This project predicts the win probability of an IPL match based on various match parameters using historical IPL data from 2008 to 2019. The prediction model is implemented using a Logistic Regression classifier.

## Dataset

The dataset used for this project can be found on Kaggle: [IPL Data Set](https://www.kaggle.com/datasets/ramjidoolla/ipl-data-set).

## Installation

1. Clone the repository or download the project files.
2. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have the dataset files (`matches.csv` and `deliveries.csv`) in a `datasets` folder.

## Project Structure

- `app.py`: Streamlit app for predicting IPL win probabilities.
- `train.py`: Script for training the model.
- `pipe.pkl`: Serialized model pipeline.

## Usage

### Training the Model

To train the model, run:

```bash
python train.py
```

This script will load the data, preprocess it, train a Logistic Regression model, and save the trained model to `pipe.pkl`.

### Running the Streamlit App

To start the Streamlit app, run:

```bash
streamlit run app.py
```

This will launch a web interface where you can input match details and get win probability predictions.

## Features

- Select the batting and bowling teams.
- Select the host city.
- Input the target score, current score, overs completed, and wickets out.
- Get the win probability prediction for the batting team.

## Example

1. Select the batting team: `Mumbai Indians`.
2. Select the bowling team: `Chennai Super Kings`.
3. Select the host city: `Mumbai`.
4. Input the target score: `180`.
5. Input the current score: `100`.
6. Input the overs completed: `12`.
7. Input the wickets out: `3`.

Click on `Predict Probability` to get the win probability for the batting team.

## Model Training Script

The training script performs the following steps:

1. Load the match and delivery data.
2. Calculate total scores for each inning.
3. Merge match data with total scores.
4. Preprocess team names.
5. Filter relevant teams and non-Duckworth-Lewis matches.
6. Merge match and delivery data.
7. Calculate match progression parameters (runs left, balls left, wickets left, etc.).
8. Train a Logistic Regression model.
9. Save the trained model.

## Dependencies

- pandas
- numpy
- scikit-learn
- streamlit
- matplotlib
