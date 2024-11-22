<div align="left" style="position: relative;">
<img src="https://img.icons8.com/?size=512&id=55494&format=png" align="right" width="30%" style="margin: -20px 0 0 20px;">
<h1>BGE-M3-SERVER</h1>
<p align="left">
	<em>Embed, Rerank, and Scale with Precision!</em>
</p>
<p align="left">
	<img src="https://img.shields.io/github/license/harshsavasil/bge-m3-server?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/harshsavasil/bge-m3-server?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/harshsavasil/bge-m3-server?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/harshsavasil/bge-m3-server?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="left"><!-- default option, no dependency badges. -->
</p>
<p align="left">
	<!-- default option, no dependency badges. -->
</p>
</div>
<br clear="right">

## 🔗 Quick Links

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📁 Project Structure](#-project-structure)
  - [📂 Project Index](#-project-index)
- [🚀 Getting Started](#-getting-started)
  - [☑️ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#-installation)
  - [🤖 Usage](#🤖-usage)
  - [🧪 Testing](#🧪-testing)
- [📌 Project Roadmap](#-project-roadmap)
- [🔰 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The bge-m3-server project leverages FastAPI to deliver advanced text embedding and re-ranking solutions, enhancing search and retrieval operations across various applications. It supports multiple embedding types, ensuring flexibility and precision in data handling. Ideal for developers and enterprises looking to optimize text-based data insights, this tool streamlines integration and boosts performance with its robust, scalable architecture.

---

## 👾 Features

|      | Feature         | Summary       |
| :--- | :---:           | :---          |
| ⚙️  | **Architecture**  | <ul><li>Utilizes `FastAPI` for efficient request handling and routing.</li><li>Structured around modern Python practices with `Pydantic` for data validation.</li><li>Modular design with clear separation of concerns between server logic and embedding models.</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Adheres to Pythonic standards with clear, concise code.</li><li>Uses `poetry` for dependency management, ensuring reproducible builds.</li><li>Includes type hints and extensive use of classes for clarity and maintenance.</li></ul> |
| 📄 | **Documentation** | <ul><li>Includes detailed `Dockerfile` and `pyproject.toml` for setup and configuration.</li><li>Well-documented API endpoints in `server.py`.</li><li>Usage and installation instructions provided for both `poetry` and `docker`.</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Designed to be containerized with `Docker` for easy deployment and scaling.</li><li>Integrates with various Python libraries such as `FastAPI` and `Pydantic` for web services and data handling.</li><li>Supports different embedding types through modular class design.</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Codebase includes separate modules for different embedding types and response schemas.</li><li>Clear separation between API layer and model processing logic.</li><li>Facilitates easy expansion or modification of embedding types and processing algorithms.</li></ul> |
| 🧪 | **Testing**       | <ul><li>Includes commands for running tests using `poetry`.</li><li>Structured to support unit and integration testing.</li><li>Testability is a core consideration in the design, particularly through the use of `Pydantic` models for data validation.</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Optimized for performance with asynchronous capabilities of `FastAPI`.</li><li>Efficient handling of I/O operations, crucial for embedding processing.</li><li>Scalable architecture to handle varying loads with potential for horizontal scaling.</li></ul> |
| 🛡️ | **Security**      | <ul><li>Uses `FastAPI` security features for robust API protection.</li><li>Containerization with `Docker` adds an additional layer of isolation and security.</li><li>Dependency management through `poetry` helps mitigate risks from outdated or vulnerable packages.</li></ul> |

---

## 📁 Project Structure

```sh
└── bge-m3-server/
    ├── Dockerfile
    ├── LICENSE
    ├── README.md
    ├── enums
    │   ├── __init__.py
    │   └── embedding_type.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── schemas
    │   ├── __init__.py
    │   ├── embedding_request.py
    │   ├── embedding_response.py
    │   ├── reranker_request.py
    │   └── reranker_response.py
    └── server.py
```


### 📂 Project Index
<details open>
	<summary><b><code>BGE-M3-SERVER/</code></b></summary>
	<details> <!-- __root__ Submodule -->
		<summary><b>__root__</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
				<td>- Defines the configuration for the "bge-m3-server" project using Poetry, specifying metadata such as project name, version, and authors<br>- It sets up dependencies essential for the project, including Python, FastAPI, and others, ensuring a consistent development environment<br>- Additionally, it configures the build system required for package installation and distribution.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/server.py'>server.py</a></b></td>
				<td>- Server.py establishes a web service using FastAPI to handle requests for text embeddings and re-ranking based on predefined models<br>- It configures environmental settings for model operations, defines endpoints for receiving text data, and processes it using the FlagEmbeddingModelRunner class to return the computed embeddings and re-ranking scores.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td>- Constructs a Docker image for a FastAPI application, starting with a base Python environment and installing dependencies via Poetry<br>- It sets up a working directory, installs necessary utilities, and prepares the environment for deployment by copying and installing project requirements and source code, ultimately configured to run with a simple command.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- enums Submodule -->
		<summary><b>enums</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/enums/embedding_type.py'>embedding_type.py</a></b></td>
				<td>- Defines a set of embedding types available within the system, categorizing them as dense, sparse, colbert, and hybrid<br>- Each type represents a different method of data representation and processing, supporting the system's flexibility in handling various data complexities and optimizing search or retrieval functionalities across the codebase architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
	<details> <!-- schemas Submodule -->
		<summary><b>schemas</b></summary>
		<blockquote>
			<table>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/schemas/embedding_response.py'>embedding_response.py</a></b></td>
				<td>- Defines the `EmbeddingResponse` model within the codebase, which standardizes the format for returning different types of embeddings, including dense, sparse, and ColBERT embeddings<br>- This model ensures consistent data structure across services that process and retrieve various embedding vectors, facilitating easier integration and maintenance.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/schemas/reranker_request.py'>reranker_request.py</a></b></td>
				<td>- Defines a `RerankerRequest` model using Pydantic, specifying a structure for incoming data with a target string and a list of sentences<br>- This model ensures data validation and serialization for requests in a reranking system, facilitating efficient processing and manipulation of text data within the application's architecture.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/schemas/embedding_request.py'>embedding_request.py</a></b></td>
				<td>- Defines a data model for embedding requests within the application, specifying the structure for input sentences and the type of embeddings required<br>- It utilizes Pydantic for data validation, ensuring that each request adheres to predefined constraints such as sentence length and count<br>- This model supports the application's processing of text data for generating embeddings.</td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/schemas/reranker_response.py'>reranker_response.py</a></b></td>
				<td>- Defines a Python class, RerankerResponse, using the Pydantic library to model the output structure for a reranking system<br>- It encapsulates a list of scores, which are likely used to represent the relevance or ranking of items processed by the system, facilitating structured data exchange and validation within the application's architecture.</td>
			</tr>
			</table>
		</blockquote>
	</details>
</details>

---
## 🚀 Getting Started

### ☑️ Prerequisites

Before getting started with bge-m3-server, ensure your runtime environment meets the following requirements:

- **Programming Language:** Python
- **Package Manager:** Poetry
- **Container Runtime:** Docker


### ⚙️ Installation

Install bge-m3-server using one of the following methods:

**Build from source:**

1. Clone the bge-m3-server repository:
```sh
❯ git clone https://github.com/harshsavasil/bge-m3-server
```

2. Navigate to the project directory:
```sh
❯ cd bge-m3-server
```

3. Install the project dependencies:


**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry install
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t harshsavasil/bge-m3-server .
```




### 🤖 Usage
Run bge-m3-server using the following command:
**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run python {entrypoint}
```


**Using `docker`** &nbsp; [<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


### 🧪 Testing
Run the test suite using the following command:
**Using `poetry`** &nbsp; [<img align="center" src="https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json" />](https://python-poetry.org/)

```sh
❯ poetry run pytest
```


---
## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## 🔰 Contributing

- **💬 [Join the Discussions](https://github.com/harshsavasil/bge-m3-server/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/harshsavasil/bge-m3-server/issues)**: Submit bugs found or log feature requests for the `bge-m3-server` project.
- **💡 [Submit Pull Requests](https://github.com/harshsavasil/bge-m3-server/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/harshsavasil/bge-m3-server
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/harshsavasil/bge-m3-server/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=harshsavasil/bge-m3-server">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [SELECT-A-LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## 🙌 Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---
