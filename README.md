# Mega Evolution Candy Calculator

![GitHub last commit](https://img.shields.io/github/last-commit/statist32/mega-evolution-candy-calculator)
![GitHub](https://img.shields.io/github/license/statist32/mega-evolution-candy-calculator)

## Overview

This repository contains the source code for a web application that helps Pokemon Go players quickly identify which mega evolution provides the most additional candy during events. The web application is hosted using GitHub Pages, and it is built using the SvelteKit framework.

## Features

- **Candy Calculation:** The application calculates and displays the additional candy gained from each available mega evolution in Pokemon Go.

- **Event Integration:** Pokemon Go events are parsed and incorporated into the calculations using the `event-downloader` module.

- **Pokemon Types:** The application fetches Pokemon types from [PokeAPI](https://pokeapi.co/), enhancing the accuracy of candy calculations.

## Usage

Visit the [Mega Evolution Candy Calculator](https://your-username.github.io/mega-evolution-candy-calculator/) to use the tool. Simply select the relevant options, and the application will provide insights into the candy gain for each mega evolution.

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/statist32/mega-evolution-candy-calculator.git
    ```

2. Install dependencies:

    ```bash
    cd mega-evolution-candy-calculator
    npm install
    ```

3. Start the development server:

    ```bash
    npm run dev
    ```

4. Open your browser and navigate to [http://localhost:5173](http://localhost:5173) to view the application.

## Contributing

Contributions are welcome!


## Acknowledgments

- Pokemon types data is fetched from [PokeAPI](https://pokeapi.co/).
