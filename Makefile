.PHONY: install test demo clean

install:
	pip install -e .

test:
	pytest tests

demo:
	python examples/showcase/system_architect_agent.py "Design a decentralized voting system using Blockchain"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
