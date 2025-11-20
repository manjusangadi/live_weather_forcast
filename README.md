# live_weather_forcast
Utility script that collects 5-day/3-hour forecast data from the OpenWeatherMap API and writes a structured weather report to a text file with aligned columns for temperature, humidity, weather status, and wind information.
# Live Weather Forecast Table Generator

This project fetches the **5-day / 3-hour weather forecast** from the **OpenWeatherMap API** using Python and saves the results in a clean, formatted text table (`data.txt`).

---

## 📌 Features

* Fetches live forecast data for any city using OpenWeatherMap
* Extracts details such as:

  * Date & Time
  * Temperature
  * Humidity
  * Weather (Main)
  * Weather Description
  * Wind Speed
  * Wind Degree
* Saves results into a neat, fixed-width table
* Simple and beginner friendly

---

## 📝 How It Works

The script performs the following steps:

1. Makes an API request to OpenWeatherMap `/forecast`
2. Parses the returned JSON
3. Iterates through each 3‑hour weather entry
4. Writes all information into `data.txt` with aligned columns

---

## ▶️ Running the Script

Make sure Python 3 is installed.

### Install dependencies:

```bash
pip install requests
```

### Run the script:

```bash
python your_script_name.py
```

The output will be saved automatically as:

```
data.txt
```

---

## 🔑 API Key Requirement

This script requires an **OpenWeatherMap API Key**.

Get your free key from:
[https://home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)

Update this line in your script:

```python
api_key = "26631f0f41b95fb9f5ac0df9a8f43c92"
```

## 📂 File Output Example (data.txt)

```
Weather report city: Bangalore
================================================================================
Sl No  Date and time       Temperature Humidity  Weather  Description          wind speed  wind degree
--------------------------------------------------------------------------------
1      2025-11-20 12:00    27.5        63        Clouds   scattered clouds     3.2         190
2      ...
```

---

## 📦 Requirements

* Python 3.x
* `requests` module

---

## 🛠️ Inside the Script

Main functions included:

* `weather_forcast()` → Fetches forecast JSON
* `write_table_file()` → Writes neatly formatted table
* `main()` → Coordinates fetching and saving

---

## 🤝 Contributing

Feel free to fork this repository and make improvements.

---

## 📜 License

This project is free to use for learning and development purposes.
