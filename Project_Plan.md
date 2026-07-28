Code review inforcer 
Description - Review pr for Linting, Security and Code Quality, According to Company Standards


- [X] Configure Github to pick up the review.yaml file for cicd Execution

2. [ ] Understand responsee git generates for PULL request

3. Learn to Trigger Test Cases and Collect 
    Data
    responsee timee
    Error log
    Flow log maybe, run on sample Langchain Project and Use LangSmith

4. Code reviewer.py to 
    Fetch Pull Req VIA Github API
        Dynamically Access Github Access token and Repository Name
    catch Code Changes
    Run Test Cases

5. Implement LLM to review actuall codebase using PROMPT in LLM_PROMPTEr.py

6. Implement Dynamic Org Rules file 
    rules:
        max_file_lines: 500

        forbid:
            - console.log
            - debugger

        require_tests: true

        require_docs: true

        max_complexity: 15


project Structure

          GitHub PR
              │
              ▼
      GitHub Webhook
              │
              ▼
        Review Service
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
    Linter   Security   AI
      │       │        │
      └───────┼────────┘
              ▼
      Aggregate Results
              ▼
      GitHub Checks API
              ▼
       Pass / Fail PR


Tech Stack
GitHub Actions – Trigger on pull requests.
Python – Orchestrate the review process.
GitHub REST or GraphQL API – Fetch PR details and publish comments.
LLM API (or a local model) – Perform semantic code review.
Ruff/ESLint/Pylint/SonarQube – Static analysis.
GitHub Checks API – Report results and block merges if required.