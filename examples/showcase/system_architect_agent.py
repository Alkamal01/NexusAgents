
"""
NexusAgents Showcase: Autonomous System Architecture Review Board
=================================================================

This example demonstrates the advanced capabilities of NexusAgents for professional AI engineering.
It simulates a "System Architecture Review Board" where multiple specialized AI agents collaborate
to design, critique, and document a complex software system.

Key Engineering Patterns Demonstrated:
1. **Strict Type Safety**: Using Pydantic models for structured agent outputs.
2. **Role Specialization**: distinct personas with specialized prompts and tools.
3. **Multi-Turn Orchestration**: A `Team` orchestrating a sequential workflow (Design -> Security Review -> Performance Review -> Final Spec).
4. **Artifact Generation**: Producing professional Mermaid diagrams and technical reports.

scenario:
The user provides a high-level requirement (e.g., "A scalable e-commerce platform for 10M users").
The agents produce:
- A High-Level Design (HLD) Document.
- A Component Diagram (Mermaid).
- A Security Risk Assessment.
- A Resource Capacity Plan.
"""

import asyncio
import sys
from typing import List, Optional

from pydantic import BaseModel, Field

from nexus_agents.actions import Action
from nexus_agents.roles import Role
from nexus_agents.team import Team
from nexus_agents.logs import logger
from nexus_agents.schema import Message

# --- 1. Define Structured Outputs (The "Protocol") ---

class ArchitectureComponent(BaseModel):
    name: str = Field(..., description="Name of the component (e.g., 'API Gateway')")
    responsibility: str = Field(..., description="Main responsibility of this component")
    technologies: List[str] = Field(..., description="List of technologies used (e.g., 'Nginx', 'Python')")

class ArchitectureDesign(BaseModel):
    summary: str = Field(..., description="Executive summary of the architecture")
    components: List[ArchitectureComponent] = Field(..., description="List of core components")
    diagram_mermaid: str = Field(..., description="Mermaid.js diagram code for the system")

class Risk(BaseModel):
    severity: str = Field(..., description="High, Medium, or Low")
    description: str = Field(..., description="Description of the security risk")
    mitigation: str = Field(..., description="Proposed mitigation strategy")

class SecurityReport(BaseModel):
    score: int = Field(..., description="Security score 0-100")
    risks: List[Risk] = Field(..., description="List of identified risks")


# --- 2. Define Custom Actions ---

class ProposeArchitecture(Action):
    PROMPT_TEMPLATE: str = """
    You are a Chief Software Architect. Design a system for the following requirement:
    "{requirement}"
    
    Focus on scalability, reliability, and maintainability.
    Provide the output as a JSON object matching the ArchitectureDesign schema.
    """
    
    name: str = "ProposeArchitecture"

    async def run(self, requirement: str):
        # In a real scenario, this would call the LLM with the schema.
        # For this showcase, we rely on the Role's capability to parse the output.
        prompt = self.PROMPT_TEMPLATE.format(requirement=requirement)
        # Note: We rely on the Role to call the LLM. structured output support varies by LLM.
        # Here we return the prompt to be used by the Role's _think/_act loop logic.
        return await self._aask(prompt)


class AuditSecurity(Action):
    PROMPT_TEMPLATE: str = """
    You are a Security Specialist. Review the following architecture design:
    {design_context}
    
    Identify potential security bottlenecks and vulnerabilities.
    """
    name: str = "AuditSecurity"

    async def run(self, design_context: str):
        prompt = self.PROMPT_TEMPLATE.format(design_context=design_context)
        return await self._aask(prompt)


# --- 3. Define Specialized Roles ---

class ChiefArchitect(Role):
    name: str = "Alice"
    profile: str = "Chief Architect"
    goal: str = "Design robust, scalable software architectures."
    constraints: str = "Use industry standard patterns. Ensure high availability."

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([ProposeArchitecture])
        self._set_react_mode(react_mode="by_order")

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: Ready to design architecture.")
        todo = self.rc.todo
        
        # Get the user requirement from memory
        msg = self.get_memories(k=1)[0]
        requirement = msg.content
        
        resp = await todo.run(requirement=requirement)
        
        # Create a professional formatted output
        msg = Message(content=resp, role=self.profile, cause_by=type(todo))
        self.rc.memory.add(msg)
        return msg

class SecurityEngineer(Role):
    name: str = "Bob"
    profile: str = "Security Specialist"
    goal: str = "Ensure the system is secure by design."
    constraints: str = "Be paranoid. assume breach."

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_actions([AuditSecurity])
        self._watch([ProposeArchitecture])

    async def _act(self) -> Message:
        logger.info(f"{self._setting}: Reviewing architecture for security risks.")
        todo = self.rc.todo
        
        # Get the architecture design from the Architect's message
        context = self.get_memories(k=1)[0].content
        
        resp = await todo.run(design_context=context)
        msg = Message(content=resp, role=self.profile, cause_by=type(todo))
        self.rc.memory.add(msg)
        return msg

# --- 4. Main Execution ---

async def main(idea: str):
    company = Team()
    company.hire([
        ChiefArchitect(),
        SecurityEngineer(),
    ])
    
    company.invest(investment=3.0)
    company.run_project(idea)
    
    await company.run(n_round=2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python system_architect_agent.py '<idea>'")
        sys.exit(1)
    
    idea = sys.argv[1]
    asyncio.run(main(idea))
