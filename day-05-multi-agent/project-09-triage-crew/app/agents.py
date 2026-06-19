"""The four triage-crew agents. Safety is encoded in every goal/backstory."""
import os
from dotenv import load_dotenv
from crewai import Agent
from app.tools import symptom_reference

load_dotenv()
MODEL = "gpt-4o-mini"

intake = Agent(
    role="Clinical Intake Specialist",
    goal="Convert a free-text complaint into a clean structured summary: symptom(s), "
         "duration, severity, risk factors. Do not interpret.",
    backstory="You are precise and neutral. You record, you do not diagnose.",
    llm=MODEL, verbose=True, allow_delegation=False)

researcher = Agent(
    role="Medical Reference Researcher",
    goal="Use the Symptom Reference Lookup tool to gather vetted context and red-flags "
         "for the reported symptoms. Flag gaps; never invent facts.",
    backstory="A careful clinical librarian who prefers cautious, general information.",
    tools=[symptom_reference], llm=MODEL, verbose=True, allow_delegation=False)

differential = Agent(
    role="Differential Reasoning Assistant",
    goal="Produce a short list of possible explanations, each with one supporting reason. "
         "Emphasise this is informational, not a diagnosis.",
    backstory="You reason transparently and rank patient safety above completeness.",
    llm=MODEL, verbose=True, allow_delegation=False)

safety_writer = Agent(
    role="Patient Safety & Communication Writer",
    goal="Write a calm, plain-English briefing. Lead with 'seek care now' red-flags and "
         "always advise consulting a qualified clinician.",
    backstory="You turn clinical caution into clear, non-alarming, actionable language.",
    llm=MODEL, verbose=True, allow_delegation=False)
