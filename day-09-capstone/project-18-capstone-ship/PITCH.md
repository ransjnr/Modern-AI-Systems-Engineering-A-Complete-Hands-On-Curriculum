# Capstone Pitch (5 minutes)

A demo is a story, not a feature list. Take the audience on one request's journey.

| Minute | Section | Do |
|--------|---------|----|
| 0:00–0:45 | The problem | One sentence on the user and their pain. Make them feel it. |
| 0:45–2:30 | Live demo | Type a real request; walk the trace (guard → route → retrieve → answer → guard). Show one moment of intelligence. |
| 2:30–3:15 | Safe & grounded | Trigger a guardrail (block an injection/PII). Show a grounded answer + its source. Show a scorecard number. |
| 3:15–4:00 | Architecture (30s) | One slide: the reference architecture, your choices highlighted, your omissions greyed. |
| 4:00–5:00 | Reliability & next | Show the live URL/health. State an honest limitation and what you'd build next. |

## Checklist
- [ ] Core runs end-to-end (one request flows the whole pipeline)
- [ ] A grounded KB answer with its source
- [ ] A guardrail blocks live (injection or PII)
- [ ] Scorecard numbers (correctness + faithfulness), incl. an out-of-scope refusal
- [ ] Deployed / live URL responds on /health
- [ ] A 60-second backup recording in case live fails

## My system (fill in)
- **User & job:** …
- **Components IN / OUT:** …
- **KB & tools:** …
- **Scorecard result:** …
- **Honest limitation & next step:** …
