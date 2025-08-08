# LoLAnalyzer

A command-line tool to fetch, analyze, and display statistics from League of Legends matches using the Riot Games API.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation & Configuration](#installation--configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Summoner Lookup**: Fetch basic summoner information (level, icon) by summoner name.
- **Match History**: Retrieve a list of recent matches for a given player.
- **Performance Analysis**: Calculate and display key in-game statistics for recent games, such as:
  - Kills/Deaths/Assists (KDA)
  - Creep Score (CS) per minute
  - Vision Score
  - Win Rate

## Prerequisites

Before you begin, ensure you have the following installed:

- [Java Development Kit (JDK)](https://www.oracle.com/java/technologies/javase-downloads.html) (Version 11 or newer recommended)
- [Apache Maven](https://maven.apache.org/download.cgi)
- A **Riot Games API Key**. You can get one from the [Riot Developer Portal](https://developer.riotgames.com/).

## Installation & Configuration

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/LoLAnalyzer.git
    cd LoLAnalyzer
    ```

2.  **Configure your API Key:**
    Create a configuration file at `src/main/resources/config.properties` with the following content:
    ```properties
    riot.api.key=YOUR_API_KEY_HERE
    ```
    Replace `YOUR_API_KEY_HERE` with your actual Riot Games API key.
    *(Note: The `config.properties` file is included in `.gitignore` to prevent you from accidentally committing your secret key.)*

3.  **Build the project:**
    Use Maven to compile the source code and package it into an executable JAR.
    ```bash
    mvn package
    ```
    The final JAR file (`LoLAnalyzer-1.0-SNAPSHOT.jar`) will be located in the `target/` directory.

## Usage

Run the application from the command line, passing the summoner name and region as arguments.

```bash
java -jar target/LoLAnalyzer-1.0-SNAPSHOT.jar "Your Summoner Name" NA1
```

Supported regions include: `BR1`, `EUN1`, `EUW1`, `JP1`, `KR`, `LA1`, `LA2`, `NA1`, `OC1`, `TR1`, `RU`.

## Contributing

Contributions are welcome! Please feel free to fork the repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
