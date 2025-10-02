# GenAI LabNote

**An Agentic AI Research Assistant for Reproducible Experimentation in Jupyter Notebooks.**

[![PyPI version](https://badge.fury.io/py/genai_labnote.svg)](https://badge.fury.io/py/genai_labnote)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/github/actions/workflow/status/aniruddha-dhawale/genai-lab-notebook/publish-to-pypi.yml)](https://github.com/aniruddha-dhawale/genai-lab-notebook/actions)

## Overview

Computational research and development within Jupyter notebooks often suffer from poor documentation, leading to a lack of reproducibility and lost knowledge. `GenAI LabNote` is a Python package designed to solve this problem by integrating a powerful AI assistant directly into the notebook environment. It automates the process of logging experiments, creating summaries, and building a searchable, long-term memory of your work. By leveraging a state-of-the-art agentic framework, it goes beyond simple record-keeping, allowing you to converse with your research history, synthesize insights, and perform complex, multi-step queries.

## Key Features

* **Automated Experiment Logging:** Capture experiment code, outputs, and metadata with a simple `%%log_experiment` magic command, without disrupting your workflow.
* **AI-Powered Summarization:** A fast, local AI model generates concise, human-readable summaries for each logged experiment.
* **Semantic Search Capability:** The system builds a local vector database (FAISS) of your work, enabling you to search for past experiments using natural language queries based on conceptual meaning, not just keywords.
* **Advanced AI Agent Framework:** The core of the system is an intelligent agent powered by the Google Gemini API and orchestrated with LangChain. This agent can reason about complex questions and use a dynamic set of tools to find answers.
* **Extensible Tooling:** The agent has access to a `search_lab_notebook` tool to query your past work and a `Python REPL` tool to perform live calculations, data analysis, or code execution.
* **Local-First Storage:** All experiment logs, summaries, and search indices are stored securely on your local machine, ensuring your work remains private.

## Getting Started

Follow these steps to integrate `GenAI LabNote` into your projects.

### 1. Prerequisites

To use the full capabilities of the AI agent, you will need a Google Gemini API key.

* Visit **Google AI Studio** to generate your free API key.

### 2. Installation

Install the package from the Python Package Index (PyPI):

```bash
pip install genai_labnote
```

### 3. Configuration
The system requires your Gemini API key to be accessible as an environment variable. The recommended way to manage this for local development is with a `.env` file.

### 4. Usage Example
Refer to examples folder for sample usage and required practices: `usage_example_main.ipynb`

