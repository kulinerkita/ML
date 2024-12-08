# 🍲 KulinerKita - Machine Learning
## 🍴 KulinerKita (Team C242-PS155) - ML Repository

KulinerKita Machine Learning Repository for Bangkit Capstone Project. Building Model of Culinary Location Recommendation System Based on Distance, Best Reviews, and Best Rating.
## KulinerKita's Developer of Machine Learning Bangkit Academy Capstone Team C242-PS155
|            Member           | Student ID |        Path        |                    Role                    |                                                       Contacts                                                      |
| :-------------------------: | :--------: | :----------------: | :----------------------------------------: | :-----------------------------------------------------------------------------------------------------------------: |
| Adib Haidar Zaky  | M312B4KY0092 |  Machine Learning  |Machine Learning Engineer |[DreadTyyy](https://github.com/DreadTyyy)|
| Hamidah Nabila Zahra | M312B4KX1694  |  Machine Learning  | Machine Learning Engineer | [seobbil](https://github.com/seobbil) |
| Luthfi Mahendra Widiarto | M312B4KY2307  |  Machine Learning  | Machine Learning Engineer | [luthfimw](https://github.com/luthfimw) |

## Tech Stack
![TensorFlow](https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-%23D00000.svg?style=for-the-badge&logo=Keras&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-purple?logo=pandas&logoColor=white&style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij48cGF0aCBkPSJNOC4wNSAxLjQ0Yy4yMy0uMTMgLjUyLS4wOC43Ni4xNWw0LjI0IDMuODRjLjI0LjIxLjI0LjU3IDAgLjc4TDguODEgOS44M2MuMjQuMi4yNS41OC4wMy43OWwtNC4yMyAzLjgzYy0uMjMuMjA1LS41OC4xNS0uODEtLjA1TC4zMiA4LjgyYy0uMjMtLjItLjIzLS41MS4wMi0uNzJsNy43MS02LjY2eiIgZmlsbD0iI0ZGRiIgZmlsbC1ydWxlPSJub256ZXJvIi8+PC9zdmc+&logoColor=white)

## About 
We have model, local culinary in Surakarta datasets, and recomendation algorithm in this repository

#### Model Training Performance
![trainingmae](https://github.com/kulinerkita/ML/blob/main/grafik%20mae.png)

#### Performance Summary
Models | MAE | Val MAE
------------ | ------------- | -------------
Recommendation System Based on Distance, Best Reviews, and Best Rating | 0.0102 | 0.0087

## Scrapping Dataset from Google Maps Using [Octoparse](https://www.octoparse.com/)

We have collected 607 lines of local food data in the city of Surakarta with the fields Page URL, shop name, rating, reviews, category, address, phone number, opening hours, price range, latitude, longitude. The data collection consists of 607 rows and 11 columns, intended to facilitate the development of a culinary recommendation system in the city of Solo based on the closest distance, user ratings, reviews and weather. The data set is stored in [df.all.vew.xlsx](https://github.com/kulinerkita/ML/blob/main/df_all_new.xlsx)

### Metadata
- **Page_URL:** The URL of the page that leads to the detailed information of the culinary location, where the link will direct to the Google Map of the culinary location.
- **Shop_name:** The name of the restaurant or culinary location.
- **Rating:** The assessment score given by the customer is in the range of 1-5.
- **Reviews:**  Number of reviews left by customers.
- **Kategori:** Traditional food categories in Surakarta. For example, pecel, satay, and others.
- **Address:** The full address of the restaurant. 
- **Phone_Number:** Phone number to contact for reservations or further information.
- **Opening_Hours:** The restaurant's operating hours, using format of days and hours.
- **Range_Harga:** Price range of food and beverages offered.
-**Latitude:** The latitude coordinates of the restaurant location in decimal format. 
- **Longitude:** The longitude coordinates of the dining location in decimal format. 
- **Eco_Friendly:** An indicator of whether a restaurant has an eco-friendly policy is usually seen from the use of packaging and the way dishes are served. Contains True or False values. 

## Culinary Recommendations Based on User Preferences
The primary purpose of the KulinerKita recommendation module is to enhance the user experience by offering curated dining suggestions that align with user preferences, including cuisine type, current weather, and top-rated establishments.

### ALgorithm Recommendation
The [recommendation algorithm](https://github.com/kulinerkita/ML/blob/main/Model_ML_Fix.ipynb) uses content-based filtering techniques to provide appropriate dining recommendations. The content-based filtering adjustment is based on the characteristics of each restaurant and the distance from the user to each restaurant. Restaurants are filtered according to the current weather and the category desired by the user.

## Run the ipynb in Google Colab
You don't need to install anything just follow the steps below:
1. Download or clone this repository
2. Open Google Colab
3. Import the .ipynb file
4. Run the code

## Run in Local
1. Download the .ipynb file or clone this repostitory
2. Run this locally using ex: jupyter notebook
3. Install all the dependencies
  ```
  ! pip install -r requirements.txt
  ```
4. Run all the code


