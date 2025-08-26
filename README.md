# 🎬 Movie Recommendation System  

This is a **Movie Recommendation System** built using **Python, Machine Learning, and Streamlit**.  
It recommends movies based on similarity scores calculated from a dataset of popular movies.  
The web app is deployed on **Streamlit Community Cloud** for free access.  

---

## 🚀 Features
- ✅ Recommend movies similar to the one selected by the user  
- ✅ Interactive UI using Streamlit  
- ✅ Uses cosine similarity for recommendation logic  
- ✅ Dataset created by merging **two TMDB datasets**  

---

## 🛠️ Tech Stack
- Python 🐍  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Pickle (for saving models)  

---

## 📂 Project Structure
```

movie-recommendation-system/
│
├── app.py                # Main Streamlit app
├── requirements.txt      # Project dependencies
├── movie.pkl             # Pickle file (movie data)
├── similarity.pkl        # Pickle file (similarity matrix)
├── tmdb\_5000\_movies.csv  # Original dataset 1
├── tmdb\_5000\_credits.csv # Original dataset 2
└── README.md             # Project description

````

---

## ⚡ How to Run Locally

1. **Clone the repository**  
   ```bash
   git clone https://github.com/pinkaofc/movie-recommendation-system.git
   cd movie-recommendation-system
````

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

5. Open the local URL provided (e.g. `http://localhost:8501`) in your browser 🎉

---

## 📊 Dataset Details

This project uses **two datasets from TMDB** (The Movie Database):

1. `tmdb_5000_movies.csv` – Contains movie metadata (titles, genres, keywords, etc.)
2. `tmdb_5000_credits.csv` – Contains information about cast and crew

These two datasets were **merged on the `movie_id` column** to create a single dataset that includes:

* Movie titles
* Genres
* Cast & crew details
* Overview (plot summary)
* Keywords

👉 The merged dataset is then preprocessed and transformed into feature vectors for building the recommendation engine.

Dataset Source: [Kaggle – TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 🌐 Deployment on Streamlit Cloud (Free)

1. Push your project to a **GitHub repository**.
2. Go to 👉 [Streamlit Cloud](https://streamlit.io/cloud).
3. Sign in with GitHub and click **“New App”**.
4. Select your repository, branch (`main`), and file path (`app.py`).
5. Click **Deploy** 🚀
6. Your app will be live at:

   ```
   https://movie-recommender-system-pikaofc.streamlit.app
   ```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss your idea.

---

## 📜 License

This project is licensed under the MIT License.
