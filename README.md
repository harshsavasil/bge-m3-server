# BGE-M3 FASTAPI Server


Embedding type can be `hybrid`, `dense`, `sparse` and `colber`.

```
curl -X POST -k -v http://127.0.0.1:3000/embedding -H "Content-Type: application/json" -d '{"sentences":["xx"], "type":"dense"}'
```
```
curl -X POST -k -v http://127.0.0.1:3000/reranker -H "Content-Type: application/json" -d '{"target": "What is BGE M3?","sentences":["BGE M3 is an embedding model supporting dense retrieval, lexical matching and multi-vector interaction.", "xxx"], "type":"dense"}'
```



<p align="center">
	<img src="data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4KICAgIDxzdmcgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2aWV3Qm94PSIwIDAgODAwIDIwMCI+CiAgICAgICAgPGRlZnM+CiAgICAgICAgICAgIDxsaW5lYXJHcmFkaWVudCBpZD0iYmctZ3JhZGllbnQiIHgxPSIwJSIgeTE9IjAlIiB4Mj0iMTAwJSIgeTI9IjEwMCUiPgogICAgICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIwJSIgc3R5bGU9InN0b3AtY29sb3I6IzQxNThEMDtzdG9wLW9wYWNpdHk6MSIgLz4KICAgICAgICAgICAgICAgIDxzdG9wIG9mZnNldD0iNTAlIiBzdHlsZT0ic3RvcC1jb2xvcjojQzg1MEMwO3N0b3Atb3BhY2l0eToxIiAvPgogICAgICAgICAgICAgICAgPHN0b3Agb2Zmc2V0PSIxMDAlIiBzdHlsZT0ic3RvcC1jb2xvcjojRkZDQzcwO3N0b3Atb3BhY2l0eToxIiAvPgogICAgICAgICAgICA8L2xpbmVhckdyYWRpZW50PgogICAgICAgICAgICA8ZmlsdGVyIGlkPSJzaGFkb3ciPgogICAgICAgICAgICAgICAgPGZlRHJvcFNoYWRvdyBkeD0iMCIgZHk9IjQiIHN0ZERldmlhdGlvbj0iNCIgZmxvb2Qtb3BhY2l0eT0iMC4yNSIgLz4KICAgICAgICAgICAgPC9maWx0ZXI+CiAgICAgICAgPC9kZWZzPgogICAgICAgIDxyZWN0IHdpZHRoPSI4MDAiIGhlaWdodD0iMjAwIiBmaWxsPSJ1cmwoI2JnLWdyYWRpZW50KSIgcng9IjE1IiByeT0iMTUiLz4KICAgICAgICA8dGV4dCB4PSI0MDAiIHk9IjEwMCIgZm9udC1mYW1pbHk9IkFyaWFsLCBzYW5zLXNlcmlmIiBmb250LXNpemU9IjQ4IgogICAgICAgIGZvbnQtd2VpZ2h0PSJib2xkIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBkb21pbmFudC1iYXNlbGluZT0ibWlkZGxlIgogICAgICAgIGZpbGw9IiNGRkZGRkYiIGZpbHRlcj0idXJsKCNzaGFkb3cpIj5CR0UtTTMtU0VSVkVSPC90ZXh0PgogICAgPC9zdmc+" alt="bge-m3-server-banner" width="800">
</p>
<p align="center">
	<em>This server can be used for deploy bge-m3 embedding models as REST APIs.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/harshsavasil/bge-m3-server?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/harshsavasil/bge-m3-server?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/harshsavasil/bge-m3-server?style=default&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/harshsavasil/bge-m3-server?style=default&color=0080ff" alt="repo-language-count">
</p>
<p align="center"><!-- default option, no dependency badges. -->
</p>
<p align="center">
	<!-- default option, no dependency badges. -->
</p>
<br>

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

<code>❯ REPLACE-ME</code>

---

## 👾 Features

<code>❯ REPLACE-ME</code>

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
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/server.py'>server.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/pyproject.toml'>pyproject.toml</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/Dockerfile'>Dockerfile</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
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
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/schemas/reranker_request.py'>reranker_request.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/schemas/embedding_request.py'>embedding_request.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
			</tr>
			<tr>
				<td><b><a href='https://github.com/harshsavasil/bge-m3-server/blob/master/schemas/reranker_response.py'>reranker_response.py</a></b></td>
				<td><code>❯ REPLACE-ME</code></td>
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
				<td><code>❯ REPLACE-ME</code></td>
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
