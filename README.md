# Used Car Price Prediction API

This repository contains a **Python-based API** designed to predict the prices of used cars. This project was developed as a **course activity** for the **Fundamentals of AI and Data Analysis** course.

The application uses machine learning techniques to analyze vehicle data and provide price estimations. A live version of the interface associated with this project can be found at [drive-wise-guess.lovable.app](https://drive-wise-guess.lovable.app/).

## 📂 Repository Structure

*   `app.py`: The main entry point for the Python API.
*   `dataset_carros_usados_2.csv`: The dataset containing used car information.
*   `requirements.txt`: List of dependencies required to run the project.
*   `.gitignore`: Configuration to exclude unnecessary files from the repository.

## 🚀 Features

*   **Price Prediction:** Predicts the market value of used cars based on input features.
*   **Machine Learning Integration:** Utilizes data analysis and AI models to generate results.
*   **REST API:** Built with Python to serve predictions programmatically.
*   **Formatted Output:** The API returns results under the key `Preço`.

## 🛠️ Technologies Used

This project leverages a modern stack for data science, web services, and frontend hosting:

*   **Python:** The core programming language used for all backend logic.
*   **Pandas & NumPy:** Essential libraries for data manipulation and cleaning the car dataset (`dataset_carros_usados_2.csv`).
*   **Scikit-learn:** The core library for implementing the Machine Learning model.
*   **Flask / FastAPI:** Frameworks used in `app.py` to create the REST API endpoints.
*   **Render:** The cloud platform used for **hosting the API**, ensuring it is accessible online.
*   **Lovable:** The platform used to build and host the **frontend interface** ([drive-wise-guess.lovable.app](https://drive-wise-guess.lovable.app/)).

### 📦 Key Libraries and Tools

This project leverages the Python ecosystem for data science and web services. The main libraries used include:

*   **Pandas & NumPy:** Used for data manipulation, cleaning the car dataset, and performing numerical operations.
*   **Scikit-learn:** The core library for implementing the Machine Learning model responsible for predicting car prices based on historical data.
*   **Flask / FastAPI (API Framework):** Used in `app.py` to create the REST API that handles prediction requests and returns results in JSON format.
*   **Gunicorn / Uvicorn:** Typically used as the production web server to run the API (check your `requirements.txt` for specific versions).

> **Note:** All specific versions of the libraries used in this project are listed in the `requirements.txt` file to ensure environment reproducibility.

## 🔧 Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/maezono00/atividade-final-fundamentos-ia-analise-dados.git
    cd atividade-final-fundamentos-ia-analise-dados
    ```

2.  **Install dependencies:**
    Ensure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the API:**
    ```bash
    python app.py
    ```

### 🌐 Using the API Directly

You can interact with the API directly without running it locally. The service is hosted on **Render**.

*   **Base URL:** `https://atividade-final-fundamentos-ia-analise.onrender.com`
*   **Endpoint:** `/prever`
*   **Method:** `POST`

#### Request Format
To get a price prediction, send a **POST** request to `https://atividade-final-fundamentos-ia-analise.onrender.com/prever` with a **JSON** body following this structure:

```json
{
  "ano": 2020,
  "quilometragem": 45000,
  "motor": 1.6,
  "num_revisoes": 3
}
```

#### Fields Description:
*   **ano**: The manufacture year of the car.
*   **quilometragem**: The current mileage of the vehicle.
*   **motor**: The engine capacity (e.g., 1.0, 1.6, 2.0).
*   **num_revisoes**: The total number of professional services/revisions performed.

> [!NOTE]
> **Observation:** Since the API is hosted on Render's free tier, it may take a few seconds to "wake up" and respond to the first request after a period of inactivity. This is a standard behavior for the hosting service.

## 📝 Project Context

This project is a key **activity** within the **Fundamentals of AI and Data Analysis** course, demonstrating the practical application of data processing, model implementation, and API deployment,.

## 👤 Author

*   **Arthur (maezono00)** - [GitHub Profile](https://github.com/maezono00) 