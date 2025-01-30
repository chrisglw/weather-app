# API &#8614; DATA &#8614; DASHBOARD

We use APIs to digest streaming data, and this challenge will require you to figure out an API and then build the data from that API into your Dashboard. Our current challenge is the [Open-Meteo API](https://open-meteo.com/). We learned about [Streamlit](https://streamlit.io/) and [Docker](https://www.docker.com/) for application development. We will build an app that uses the API to display weather data for decision-making.

__NOTE!__

They provide python code examples with the API.  You will need to tweak yours to use Polars and to not use the Caching.  See these two chunks for examples to prompt your coding (note the second one is not a complete code snippet).

```python
openmeteo = openmeteo_requests.Client()
```


```python
start = datetime.fromtimestamp(hourly.Time(), timezone.utc)
end = datetime.fromtimestamp(hourly.TimeEnd(), timezone.utc)
freq = timedelta(seconds = hourly.Interval())

df = pl.select(
  date = pl.datetime_range(start, end, freq, closed = "left"),
  temperature_2m = hourly_temperature_2m)
```

## Coding Challenge

### Driving needs

_Each of the items below must be addressed by your app._

1. Allow the user to pull 15 days of [historical forecast data](https://open-meteo.com/en/docs/historical-forecast-api#start_date=2024-07-02) and [historical data](https://open-meteo.com/en/docs/historical-weather-api) for the three BYU locations (Idaho, Hawaii, Provo) at an hourly resolution.
  - Make sure that the date and time is understandable by the user.
  - Use display units for the United States of America.
2. Display summary tables comparing the forecasts and actual weather for all three cities that lets them compare;
  - The three cities to each other.
  - The forecast to the actual weather at each city.
3. Provide multiple visualizations to facilitate these comparisons.
  - Daily highs over the month for each location.   
  - A visualization that uses boxplots to show each city's varied hourly temperature readings.
  - A novel visualization of your creation (no bar charts or pie charts)  
4. Build KPIs into your dashboard.
  - Provide KPIs that show the highest value for the selected variable in that period and the respective city.
  - Provide KPIs that show the lowest value for the selected variable in that period and the respective city.
5. Include the following user elements in your dashboard.
  - Allow the user to pick the 15 days they want to compare within the limits of the API.
  - Allow the user user pick the weather variables of interest from at least ten different options of the API.
  - Ask the user for their time zone choice (Hawaii or Mountain). Display all data in that time zone.
  - Add two additional user inputs of your choice (for example; change the graph, additional API inputs, different summaries for your table)  

### Data Science Dashboard

We will use Streamlit as our prototype dashboard tool, but we need to embed that streamlit app into a Docker container.

Within this repository you can simply run `docker compose up` to leverage the `docker-compose.yaml` with your local folder synced with the container folder where the streamlit app is runnning. 

Additionally, you can use `docker build -t streamlit .` to use the `Dockerfile` to build the image and then use `docker run -p 8501:8501 -v "$(pwd):/app:rw" streamlit` to start the container with the appropriate port and volume settings.

### Repo Structure

Your repo should be built so that I can clone the repo and run the Docker command (`docker compose up`) as described in your `readme.md` that allows me to see your app in my web browser without requiring me to install Streamlit on my computer.

1. Fork this repo to your private space
2. Add me to your private repo in your space (`hathawayj`)
3. Build your app and Docker container
4. Update your `readme.md` with details about your app and how to start it.
5. Include a screen shot of your working app in your repository.
6. Build your app in Hugging Face using the [ds460 template](https://huggingface.co/spaces/ds460/_template_streamlit_docker).
  - place the app within our ds460 org.
  - Change the title of the App to your name and change the color.
7. Submit the link to your repo and Hugging Face App to me in Canvas within your vocabulary/lingo challenge.

## Vocabulary/Lingo Challenge

_Within a `.md` file in your repository and as a submitted `.pdf` or `.html` on Canvas, address the following items;_

1. A link to your repo that you have shared with me and a screenshot of your app.
2. Explain the added value of using DataBricks in your Data Science process (using text, diagrams, or tables).
3. Compare and contrast PySpark to either Pandas or the Tidyverse (using text, diagrams, or tables).
4. Explain Docker to somebody intelligent but not a tech person (using text, diagrams, or tables).

Your answers should be clear, detailed, and no longer than is needed. Imagine you are responding to a client or as an interview candidate._

- _Clear:_ Clean sentences in nicely laid out format.
- _Detailed:_ You touch on all the critical points of the concept. Speak at a reasonable level.
- _Brevity:_ Don't ramble. Get to the point, and don't repeat yourself.

## Submission

Submit your work on Canvas.  It can be a link to your repository or a PDF/HTML file with your vocabulary challenge, a link to your repo, and a link to the Hugging Face app.

## References

- [Streamlit Dashboard](https://streamlit.io/)
- [Docker](https://www.docker.com/)
- [Dockerfile cheat sheet](https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index)
- [Streamlit deploy in Docker](https://docs.streamlit.io/knowledge-base/tutorials/deploy/docker)
- [Streamlit and Docker](https://maelfabien.github.io/project/Streamlit/#)
- [open-meteo/python-requests: Open-Meteo Python Library using `requests`](https://github.com/open-meteo/python-requests?tab=readme-ov-file#polars)
- [openmeteo-requests · PyPI](https://pypi.org/project/openmeteo-requests/)
