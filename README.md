# Centrilearn-Web-Application
Centrilearn web application frontend and backend

# Project ReadME

This ReadME file contains information to guide the developer who will continue working on this project.

## Django App

The Django app that was being built is called `Base`. You can find the following components in their respective files:

- Models: `models.py`
- Views: `views.py`
- URLs: `urls.py`

## Development Environment Setup

Create a `.devcontainer` with a prebuilt Ubuntu environment and install Python 3.12. Note that Python 3.13 is incompatible with `crewai`.

To set up the development environment, follow these steps:

1. Create a `.devcontainer` configuration file.
2. Install Ubuntu and Python 3.12 in the `.devcontainer`.
3. Install the dependencies from the `pyproject.toml` file.
4. Run the Django project normally.

## Models and Code Generation

The `chatModel` is located within a directory inside the `Base` folder, which contains the Django app. The `code.py` module contains the code generation model that is used to build the code generator.

Both the `chatModel` and `code.py` should work if the development environment is configured properly. However, the `chatModel` generator was not tested because OpenAI blocked my account during the building process.

The RAG is used as a tool for the crew. please find the RAG data directory path `Centrilearn\base\chatModel\tools\crew\tools\data_dir`. after more RAG data has been filled, save them preferrably as a `.csv` file and place within that directory.

## Design Philosophy

The design philosophy for this project is contained within a PowerPoint file. To get a better understanding of the design philosophy, please request the PowerPoint file.

A snippet of the design philosophy is to store all user and AI responses within the chat model and code model databases before passing the entire history associated with the session to the models. This was done because the models are stateless and to facilitate easy migration to the cloud in the form of an API when the model becomes cumbersome.

## Scraping Tool

To use the scraping tool, visit [Bright Data](https://brightdata.com/) and subscribe to access their remote server for scraping. Do not connect the driver locally because there are two drivers for the two tools. The remote connection currently used will not work anymore.

## Contact Information

If you have any follow-up questions, please reach out to me via email at [My-Mail](mailto:okbusinessfarms@gmail.com).

