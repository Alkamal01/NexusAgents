# NexusAgents: Professional Multi-Agent Framework

<p align="center">
  <b>A production-grade framework for orchestrating complex autonomous agent workflows.</b>
</p>

## Overview

**NexusAgents** (formerly MetaGPT) is a robust framework designed for **Professional AI Agent Engineering**. It enables developers to build, orchestrate, and deploy collaborative teams of LLM-based agents that can solve intricate problems through role specialization, standardized operating procedures (SOPs), and structured communication.

Unlike simple chatbot scripts, NexusAgents treats agents as first-class software components with:
- **Strict Typing & Schema Validation**: Ensure agent outputs match your API contracts.
- **Role-Based Orchestration**: Define complex team structures (e.g., Product Manager, Architect, Engineer).
- **Memory & Context Management**: Sophisticated handling of long-term and short-term agent memory.

## Key Features

- **Multi-Role Collaboration**: Agents work together in a `Team`, passing messages and artifacts to achieve a shared goal.
- **Standardized Actions**: encapsulating prompt logic into reusable `Action` classes.
- **Structured Outputs**: Native support for generating Pydantic models, JSON, and Diagrams (Mermaid).
- **Extensible Architecture**: Easy to customize Roles, Actions, and Memory stores.

## AI Engineering Showcase

This repository serves as a demonstration of advanced AI Engineering patterns.

### 🚀 Featured Example: [Autonomous System Architect Team](examples/showcase/system_architect_agent.py)

We have included a professional-grade example used to simulate a technical review board.
Run the showcase to see agents collaborate on a high-level design:

```bash
# Design an e-commerce system
python examples/showcase/system_architect_agent.py "Scalable E-commerce platform for 1M DAU"
```

**What happens under the hood:**
1. **Chief Architect** analyzes the requirements and produces a *Structured Architecture Design* (JSON + Mermaid).
2. **Security Specialist** reviews the design for vulnerabilities and produces a *Risk Assessment Report*.
3. The system outputs a set of professional artifacts.

## Installation

```bash
pip install -e .
```

## Quick Start

```python
import asyncio
from nexus_agents.roles import Architect, Engineer
from nexus_agents.team import Team

async def main():
    # Assemble your team
    company = Team()
    company.hire([
        Architect(),
        Engineer(),
    ])
    
    # Assign a complex task
    company.invest(investment=3.0)
    company.run_project("Build a snake game in Python")
    
    # execute
    await company.run(n_round=5)

if __name__ == "__main__":
    asyncio.run(main())
```

## Configuration

NexusAgents uses a YAML configuration system.
Run the following to generate your config file:

```bash
nexus --init-config
```

Then edit `~/.metagpt/config2.yaml` (legacy path) to add your API keys.

```yaml
llm:
  api_type: "openai"
  model: "gpt-4-turbo"
  api_key: "sk-..."
```

## License

MIT License.

---

<p align="center">
  Built with ❤️ by <b>kaftandev</b>
</p>
