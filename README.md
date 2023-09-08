# CV-IMAGE-SEARCH-PREDICTION

## Problem Statement:

Reverse image search is a search engine technology that takes an image file as input query and returns results related to the image.

## Solution:

The solution is distributed across three main components:

1. **Data Collection**: Responsible for collecting and storing image data.
2. **Model Training**: Focuses on training the image search model.
3. **Prediction**: Handles the prediction and retrieval of related images based on the input.

### 1. Data Collection

- **Repository**: [CV-IMAGE-SEARCH-DATA-COLLECTION](https://github.com/pranavrelds/CV-IMAGE-SEARCH-DATA-COLLECTION)

#### Features:

- Fetch available labels from the database.
- Add new labels to the database.
- Single and bulk image upload to S3 storage with associated labels.

### 2. Model Training

- **Repository**: [CV-IMAGE-SEARCH-MODEL-TRAINING](https://github.com/pranavrelds/CV-IMAGE-SEARCH-MODEL-TRAINING)

#### Features:

- The repository is dedicated to training the model. Specific functionalities can be derived from the codebase.

### 3. Prediction

- **Repository**: [CV-IMAGE-SEARCH-PREDICTION](https://github.com/pranavrelds/CV-IMAGE-SEARCH-PREDICTION)

#### Features:

- Welcome route to introduce the Image Search functionality.
- Upload an image and get predictions.
- Reload predictions.
- Dynamically reload the model in production with minimal downtime.
- Gallery route to display predicted images.

## Tech Stack:

- **FastAPI**: Used for creating the API endpoints in both the Data Collection and Prediction components.
- **MongoDB**: Utilized in the Data Collection component for storing image labels.
- **AWS S3**: Employed in the Data Collection component for storing the image data.
- **Python Libraries**: Various Python libraries like `pandas`, `scikit-learn`, `boto3`, `annoy`, and others are used, especially in the Model Training component.

---
