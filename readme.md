# Livability Analysis Project

## Project Overview
This project provides an interactive platform to analyze and predict livability scores for different countries using key indices such as Health, Education, Environment, Economic, and Quality of Life.

## Features
- Predict and visualize livability rankings based on pre-existing data.
- User-friendly interface built with Streamlit.
- Engaging UI animations for a dynamic experience.
- Pretrained livability score model for predictions.
- Integrated Power BI analysis for data insights.

## File Structure
```plaintext
├── static 
│   ├── background.jpg              # Image for background visual
│   ├── floating_background.css      # Styles for animated background elements
│   ├── page_animations.css          # Styles for button animations and dynamic elements
│   └── streamlit_theme.css          # Theme definitions for Streamlit UI
├── .devcontainer
│   └── devcontainer.json            # Container setup file
├── app.py                           # Main application entry point
├── livability_score_model.pkl       # Serialized ML model for livability score prediction
├── predict_page.py                  # Script for prediction page with data visualization
├── requirements.txt                 # Python dependencies
├── world 2023.csv                   # Dataset containing country indices and livability scores
├── livability_analysis.pbix         # Power BI report for detailed livability analysis
└── .gitattributes                    # Configuration for consistent Git behavior
```

## Key Functionalities
### 1. Predicting Livability Rankings
The application ranks countries based on the indices present in `world 2023.csv`. For each country, it provides individual and overall rankings.

### 2. Interactive UI
- Select a country to view its livability rankings.
- Use visually engaging cards to highlight different indices.

### 3. Power BI Integration
- The `livability_analysis.pbix` Power BI report provides in-depth analysis and visualization of livability data.
- Gain insights into trends and patterns across various indices.

## Styling Highlights
- **Animations:** The UI elements such as buttons have animation effects using keyframes defined in `page_animations.css`【7†source】.
- **Floating Backgrounds:** Background elements animate smoothly as defined in `floating_background.css`【8†source】.
- **Card Design:** Interactive prediction cards enhance user experience by scaling on hover【9†source】.

## Dependencies
Listed in `requirements.txt`, the key dependencies include:
- Streamlit
- Pandas
- Numpy
- Pickle

## Dataset
The `world 2023.csv` dataset contains indices for countries including Health, Education, Environment, Economy, and Quality of Life.

## Model
The `livability_score_model.pkl` file contains a pre-trained model used for predicting livability scores based on the provided indices.

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For any queries or support, please reach out to the project maintainers.
