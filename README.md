# CO2 Emissions Prediction Model

This project uses multiple linear regression to predict CO2 emissions based on various features from a vehicle fuel consumption dataset.

## Project Overview

The goal of this project is to build a model that can accurately predict CO2 emissions from vehicles. We use a multiple linear regression approach, leveraging several features from our dataset to make these predictions.

## Dataset

The project uses the FuelConsumption.csv dataset, which includes the following features:
- MODELYEAR
- MAKE
- MODEL
- VEHICLECLASS
- ENGINESIZE
- CYLINDERS
- TRANSMISSION
- FUELTYPE
- FUELCONSUMPTION_CITY
- FUELCONSUMPTION_HWY
- FUELCONSUMPTION_COMB
- FUELCONSUMPTION_COMB_MPG
- CO2EMISSIONS

## Features

- Data loading and exploration using pandas
- Data visualization with matplotlib and seaborn
- Statistical analysis including correlation studies
- Multiple linear regression model using scikit-learn
- Model evaluation and scoring

## Technologies Used

- Python 3.11.9
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy

## Getting Started

1. Clone this repository
2. Install required packages: `pip install -r requirements.txt`
3. Run the Jupyter notebook or Python scripts to explore the data and train the model

## Files in the Repository

- `data_exploration.py`: Code for loading and exploring the dataset
- `model_training.py`: Code for training and evaluating the regression model
- `app.py`: Flask application for model deployment (if applicable)
- `requirements.txt`: List of required Python packages
- `data/FuelConsumption.csv`: Dataset used for the project

## Future Improvements

- Feature engineering to improve model performance
- Experimenting with other regression algorithms
- Creating a web interface for predictions

## Contributing

Feel free to fork this project and submit pull requests with improvements or suggestions.

## License

[MIT License](https://opensource.org/licenses/MIT)
