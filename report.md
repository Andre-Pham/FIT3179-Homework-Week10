# FIT3179 Week 10 Homework

IMPORTANT: I have added text annotations - they are only viewable after a filter is applied, as they would clutter the visualisation otherwise.

| Student Details |                                                              |
| --------------- | ------------------------------------------------------------ |
| Name            | Andre Pham                                                   |
| Email           | [apha0019@student.monash.edu.au](mailto:apha0019@student.monash.edu.au) |
| Student Number  | 31448232                                                     |
| Studio          | Studio 03                                                    |
| Tutor           | Dr Jesmin Nahar                                              |

### URL: [VISUALISATION URL](https://andre-pham.github.io/FIT3179-Homework-Week10/)

### Screen Capture

 <img src="C:\Users\andre\Desktop\Repositories\FIT3179\FIT3179-Homework-Week10\figure1.PNG" alt="figure1" style="zoom:67%;" />

*Figure 1: Task 1 (No filter applied) (Note - annotations are applied after a filter is).*

<img src="C:\Users\andre\Desktop\Repositories\FIT3179\FIT3179-Homework-Week10\figure2.PNG" alt="figure2" style="zoom:67%;" /> 

*Figure 2: Task 1 (Filtered to "Highway vehicles") (Annotation visible bottom right) (Tooltip being shown).*

### Domain

This visualisation presents the state of air quality in the United States. It provides context on the number of tones of pollutants that are being produced annually in the U.S. (and how that has changed over the past six decades) as well as the current state of the United State's air quality, geographically.

### Dataset

The stacked area chart's dataset is available [here](https://www.bts.gov/content/estimated-national-emissions-volatile-organic-compounds). It contains the estimated annual U.S. emissions of volatile compounds from 1970 to 2021. It is hosted by the [Bureau of Transportation Statistics](https://www.bts.gov/) and was originally sourced from the U.S. Environmental Protection Agency's Air Emissions Inventories, available [here](https://www.epa.gov/air-emissions-inventories/air-pollutant-emissions-trends-data).

The dataset is of the table dataset type, where the items are annual U.S. VOC emissions. The source, year and measurement attributes are categorical, ordinal and quantitative respectively.

The choropleth map's dataset is available on Kaggle [here](https://www.kaggle.com/datasets/calebreigada/us-air-quality-1980present). It contains approximately 5.72 million AQI measurements across the United States from 1980 to 2022. It was uploaded to Kaggle by user [Caleb Reigada](https://www.kaggle.com/calebreigada), where the [original locational data](https://simplemaps.com/data/us-cities) was sourced from [simplemaps](https://simplemaps.com/data) and the [original aqi data](https://aqs.epa.gov/aqsweb/airdata/download_files.html) from the [United States Environmental Protection Agency](https://www.epa.gov/).

### Data Transformation

The stacked area chart's dataset required the rows to be pivoted, the filtering of 2020 and 2021 data (due to incomplete measurements), and the conversion from U.S. short tones to metric tones. 

The choropleth map's dataset required the filtering of items to 2021 only, the removal of columns not required, and the grouping of CBSA measurements to then identify the mean.

Python was used in conjunction with the pandas module to process and export both datasets.

### Idiom Justification

A stacked area chart was used to visualise the change of VOC emissions annually produced by the U.S. The use of a stacked area chart means that the total VOC emissions can be visualised, as well as broken down by their sources. For example, if a line chart was to be used to show the sources, the net VOC emissions wouldn't be identifiable - only by stacking the sources via a stacked area chart is this information conveyed. The option to filter by source also negates the largest drawback of the stacked area chart (readability of each category) by allowing each source to be read in isolation.

The justification for the choropleth idiom was covered in homework week 9 and hence will not be re-stated.