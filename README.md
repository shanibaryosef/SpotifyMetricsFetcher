# SpotifyMetricsFetcher
Music Listening Habits in Israel: Impact of War on Streaming Behavior

This project analyzes music listening behavior in Israel using Spotify's weekly Top Songs data, focusing on changes before and after the "Haravot Barzel" war (2023). The analysis leverages Spotify API, automation tools, audio feature extraction, and statistical methods to uncover trends in mood-related musical attributes.
Project Overview

    Objective:
    Investigate how external events (specifically, the "Haravot Barzel" war) influence music consumption patterns and mood-related song features in Israel.

    Data Sources:
        Spotify Charts (via Selenium)
        Spotify API
        YouTube (via Pytubefix)

    Features Analyzed:
        Danceability
        Valence
        Arousal
        Dynamic Complexity
        Key Scale (Major/Minor)

Tools & Technologies Used

    Spotify API:
    For metadata and chart extraction.

    Selenium:
    Automated scraping of weekly Spotify charts to avoid manual downloads.

    Pytubefix & yt-dlp:
    Downloaded song audio files from YouTube.

    Essentia:
    Extracted detailed musical features (key scale, mood probabilities, energy, danceability, etc.).

    Pandas & NumPy:
    For data wrangling, cleaning, and transformation.

    Matplotlib & Seaborn:
    Data visualization.

    Scipy.stats:
    Statistical testing (T-tests, ANOVA, etc.).

    pyHomogeneity:
    For Homogeneity and Change Point Detection (Standard Normal Homogeneity Test - SNHT).

Project Highlights

    Automated weekly Spotify chart downloads using Selenium.
    Built a database of 156 weekly Top Songs lists.
    Extracted and enriched song features (danceability, valence, arousal, key scale, etc.).
    Time-series visualization of key musical attributes across weeks and months.
    Applied statistical tests:
        T-test / Mann-Whitney U to compare attributes before/after the war.
        SNHT (Standard Normal Homogeneity Test) to detect distribution shifts in time series.
    Clustering analysis (Dynamic Time Warping) to compare Israeli trends to global ones.
