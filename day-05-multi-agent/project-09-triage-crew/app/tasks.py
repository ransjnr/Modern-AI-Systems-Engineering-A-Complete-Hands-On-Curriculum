"""Tasks with context handoffs so each agent builds on the previous one."""
from crewai import Task
from app.agents import intake, researcher, differential, safety_writer

def build_tasks():
    t1 = Task(description="Patient complaint: '{complaint}'.\nExtract and normalise main "
              "symptom(s), duration, severity (1-10 if stated), risk factors.",
              expected_output="Structured normalised complaint.", agent=intake)
    t2 = Task(description="Using the normalised complaint, call the Symptom Reference Lookup "
              "for each symptom. Summarise context and red-flags; note any gaps.",
              expected_output="Reference brief: context + red-flags per symptom.",
              agent=researcher, context=[t1])
    t3 = Task(description="From intake + research, list 3-5 possibilities each with one "
              "reason. Add a 'not a diagnosis' disclaimer.",
              expected_output="Short ranked list with reasons + disclaimer.",
              agent=differential, context=[t1, t2])
    t4 = Task(description="Write the patient-facing briefing: (1) RED-FLAGS seek care now, "
              "(2) common associations, (3) suggested next step, (4) consult a clinician.",
              expected_output="A clear, safe, structured triage briefing.",
              agent=safety_writer, context=[t1, t2, t3])
    return [t1, t2, t3, t4]
