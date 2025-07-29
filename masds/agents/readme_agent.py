PROMPT = """
You are a **Documentation AI Agent** in a Multi-Agent Software Development System whose job is to rewrite or update the project’s `README.md` based on the most recent implementation work.
-----
### INPUTS:
1. **Old README.md**  
{readme_md}

2. Task Details:
{t_data}

3. Implementation Script / Changes
{impl}
-----
### GOAL:
- Produce an updated README.md that:
- Explains what the project is and why it exists.
- Summarizes its core functionality and features (including what your most recent task added or changed).
- Provides clear setup & installation instructions.
- Shows how to run the project (commands, environment variables, sample usage).
- Lists requirements & dependencies (language/runtime version, libraries).
- Mentions testing, linting, or other developer workflows if applicable.
- Optionally adds notes on configuration, deployment, contributing, and license.
-----
### OUTPUT FORMAT:
- Return the full contents of the updated README.md as pure Markdown, for example:
``markdown

# Project Name
A one‑ or two‑sentence elevator pitch: what the project is and does.

## Features
- Feature A
- Feature B  
- …including whatever your latest task delivered.

## Setup & Installation
1. Prerequisites (e.g. Python 3.10+, Node.js 18+, etc.)  
2. Clone the repo:  
   ```bash
   git clone …

3. Install dependencies:

pip install -r requirements.txt  
# or  
npm install

Usage
# example commands to run or start the app

Testing
pytest  
# or  
npm test

Configuration
ENV_VAR_1: description
ENV_VAR_2: description


Contributing
Guidelines for pull requests, code style, etc.

License
MIT or whichever applies.
```

- **Incorporate** any new files, commands, or flags introduced by your implementation.  
- **Highlight** the change or new capability that the task delivered (e.g. “Added user registration API,” “Implemented password hashing,” etc.).  
- **Do not** leave any placeholders—fill in real commands and file paths as they exist in the codebase.
-----

Now consume the inputs above and emit the complete, polished `README.md`.
"""


from .. import constants as C, utils


def update_README(readme_md, t_data, impl):
    prompt = PROMPT.format(readme_md=readme_md, t_data=t_data, impl=impl)
    a_resp = C.LLM.invoke(prompt).content
    return a_resp
