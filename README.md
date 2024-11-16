#### **Project Overview**
This project demonstrates the integration of **FastAPI** with a machine learning model using a serialized **pickle file** for handling predictions. The key objectives include modular design, input validation, error handling, and scalable API architecture.

---

#### **Key Features**
1. **Separation of Concerns**:
   - Training logic is isolated in `train_model.py`.
   - Prediction logic is encapsulated in `predictor.py`.
   - API handling is managed separately in `main.py`.

2. **Scalability**:
   - Modular design supports easy model replacement.
   - Adding new endpoints or features is straightforward.
   - Maintains clean and structured code for long-term maintainability.

3. **Security**:
   - Input validation is handled with **Pydantic**.
   - Error responses are structured for better API usability.

---

#### **System Architecture**
- **Component Diagram**: Provides a high-level view of how the components interact.
- **Data Flow Diagram**: Describes the flow of data between the system components.

---

#### **Directory Structure**
The project is organized into three main modules:

1. **Model Training (`train_model.py`)**:
   - Uses synthetic dataset generation with `make_regression`.
   - Trains a **Linear Regression** model.
   - Serializes the trained model into a pickle file for later use.

2. **Prediction Module (`predictor.py`)**:
   - Deserializes the trained model.
   - Handles input data preprocessing and prediction generation.

3. **FastAPI Application (`main.py`)**:
   - Sets up the **FastAPI** server.
   - Implements Pydantic models for input validation.
   - Handles structured error responses and request routing.

---

#### **Getting Started**
1. **Prerequisites**:
   - Python 3.11
   - FastAPI
   - Uvicorn
   - Required Python libraries: `scikit-learn`, `pickle`

2. **Installation**:
   ```bash
   pip install fastapi uvicorn scikit-learn
   ```

3. **Usage**:
   - Train the model: 
     ```bash
     python train_model.py
     ```
   - Run the API server:
     ```bash
     uvicorn main:app --reload
     ```
---

#### **Key Components**
- **FastAPI**: Lightweight web framework for handling HTTP requests.
- **Pickle**: For model serialization and persistence.
- **Pydantic**: To ensure type-safe input validation.

---

#### **License**
This project is licensed under Apache 2.0.
