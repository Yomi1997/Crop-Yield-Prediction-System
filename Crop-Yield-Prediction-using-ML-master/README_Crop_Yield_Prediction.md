
# 🌾 Crop Yield Prediction using Machine Learning

This project predicts the optimal crop yield based on soil nutrients, temperature, humidity, pH, and rainfall using a trained Random Forest model. The system combines a **PHP frontend** with a **Python backend** and **machine learning model** integration.

---

## 📁 Project Structure

- `index.php` – Main web interface
- `predict.php` – Connects PHP with the Python model
- `style.css` – Styling for the frontend
- `Final_Data.csv` – Training dataset
- `train_model.py` – Trains the Random Forest model
- `RF_predict.py` – Used by PHP to predict via the trained model
- `model.pkl` – Saved trained machine learning model
- `app.py` – Optional Flask app version (not essential if using PHP)
- `imgs/` – Images used in the web interface

---

## ✅ Requirements

### 🧠 Python Dependencies
Install the following with pip (Python 3.6+ recommended):

```bash
pip install pandas numpy scikit-learn joblib
```

### 🌐 PHP Setup
Use **XAMPP** or **WAMP** with PHP 7+ and Apache. Place project files inside the `htdocs` folder.

---

## ⚙️ Setup Instructions

### Step 1: Install Python and Required Libraries
Make sure Python is installed (preferably 3.6 or later):

```bash
python --version
```

Then install dependencies:

```bash
pip install pandas numpy scikit-learn joblib
```

### Step 2: Train the Model (Optional)
If you want to retrain the model:

```bash
python train_model.py
```

This will generate `model.pkl`.

### Step 3: Configure XAMPP

1. Copy the project folder (e.g., `Crop-Yield-Prediction-using-ML-master`) into `C:\xampp\htdocs\`.
2. Start **Apache** from XAMPP Control Panel.
3. Make sure Python is added to your system environment path.

### Step 4: Set Python Path in `predict.php`

Edit this line in `predict.php` if your Python path is different:

```php
$command = escapeshellcmd("python RF_predict.py $n $p $k $temp $humidity $ph $rainfall");
```

If using `python3`, change it to:

```php
$command = escapeshellcmd("python3 RF_predict.py $n $p $k $temp $humidity $ph $rainfall");
```

### Step 5: Run the Web App

Visit in your browser:

```
http://localhost/Crop-Yield-Prediction-using-ML-master/index.php
```

Input the values and click **Predict** to get crop recommendations.

---

## 💻 Software Versions

| Software        | Recommended Version |
|-----------------|---------------------|
| Python          | 3.6+                |
| scikit-learn    | 0.24+               |
| PHP             | 7.x or 8.x          |
| XAMPP/WAMP      | Latest              |
| Web Browser     | Chrome / Firefox    |

---

## 🛠️ Troubleshooting

- ❌ **Python not found?** Add Python to your system's PATH environment variable.
- ❌ **Blank prediction?** Check if `model.pkl` exists and Python path in `predict.php` is correct.
- ❌ **Permission denied?** Ensure Apache has rights to execute Python scripts.
