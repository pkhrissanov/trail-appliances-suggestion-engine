# Appliance Recommendation Engine

A machine learning project exploring different approaches to appliance recommendation systems.

The goal is to build a recommendation engine capable of suggesting similar appliances based on their specifications, features, and pricing, while providing a foundation for future personalized and context-aware recommendations.

---

## Project Overview

Modern e-commerce websites often recommend products that are similar to one currently being viewed. This project recreates that workflow using machine learning.

The current implementation focuses on kitchen ranges and follows a complete machine learning pipeline:

1. Generate a realistic appliance dataset
2. Preprocess and encode product attributes
3. Convert products into numerical feature vectors
4. Apply multiple recommendation algorithms
5. Compare recommendation quality

Future versions will introduce context-aware recommendations that learn which product attributes matter most based on multiple user selections.

---

## Machine Learning Pipeline

```
Synthetic Product Generation
            │
            ▼
      Data Cleaning
            │
            ▼
 Feature Engineering
            │
            ▼
Data Vectorization
(Standard Scaling +
One-Hot Encoding +
MultiLabel Binarization)
            │
            ▼
 Recommendation Models
            │
    ┌───────┼────────┐
    ▼       ▼        ▼
Cosine   Nearest   K-Means
Similarity Neighbours Clustering
```

---

## Current Recommendation Models

### Cosine Similarity

Treats every appliance as a feature vector and compares products using cosine similarity.

Useful as a simple baseline recommendation algorithm.

---

### Nearest Neighbours

Uses Scikit-Learn's `NearestNeighbors` implementation with cosine distance to efficiently retrieve the closest matching products.

This approach scales better than manually comparing every product.

---

### K-Means Clustering

Groups appliances into clusters of similar products.

Although clustering is not currently used directly for recommendations, it helps understand the structure of the dataset and provides opportunities for future improvements.

---

## Data Generation

Rather than scraping existing retailers, this project generates realistic appliance data using the Faker library together with custom generation logic.

Each generated appliance contains information such as:

* Brand
* Brand tier
* Appliance category
* Fuel type
* Finish
* Dimensions
* Burner count
* Price
* Rating
* Feature list

Approximately 25,000 realistic appliance records are generated for experimentation.

---

## Data Preprocessing

Before applying machine learning algorithms, the dataset is transformed into a numerical representation.

Current preprocessing includes:

* Standard scaling of numerical features
* One-hot encoding of categorical variables
* Ordinal encoding of brand tiers
* Multi-label binarization of product feature lists
* Construction of a final feature matrix used by all recommendation models

---

## Project Structure

```
.
├── appliance-recommendation-engine.ipynb   # Recommendation algorithms
├── data-creation.ipynb                     # Synthetic dataset generation
├── data-preprocessing.ipynb                # Feature engineering pipeline
├── test-data-vectorization.py              # Vectorization testing
├── data/
│   ├── ranges.csv
│   ├── final_data.csv
│   ├── features_encoded.csv
│   ├── encoded_categorical_values.csv
│   ├── numeric_data_scaled.csv
│   └── ...
└── README.md
```

---

## Technologies

* Python
* Pandas
* NumPy
* Scikit-Learn
* Faker
* Matplotlib

---

## Future Improvements

* Context-aware recommendations using multiple product selections
* Dynamic feature weighting
* SQLite product catalogue
* Recommendation explanations ("Why this product?")
* Principal Component Analysis (PCA) experiments
* Interactive web interface
* Hybrid recommendation algorithms

---

## Current Status

This project is an active learning project focused on understanding the machine learning techniques behind recommendation systems.

Current progress:

* ✅ Synthetic appliance dataset generation
* ✅ Feature engineering pipeline
* ✅ Data vectorization
* ✅ Cosine similarity recommendations
* ✅ Nearest Neighbour recommendations
* ✅ K-Means clustering experiments
* ⏳ Context-aware recommendation engine
* ⏳ Personalized feature weighting
* ⏳ Interactive application
