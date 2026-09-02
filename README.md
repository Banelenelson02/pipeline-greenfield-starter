# 🩺 Pipeline Greenfield — CI/CD Project (FORGE)

You did the [session-cicd-pipeline](https://github.com/ai-builder-circle/session-cicd-pipeline)
tutorial. This is where you prove it stuck.

## The problem

Most beginner pipelines only tell you **red or green**. When they fail, you get a wall of
raw logs and have to go hunting for the actual cause. That's fine for a tutorial — not fine
for a real team, where someone else has to figure out why *your* push broke the build.

**Your job:** build a CI/CD pipeline for the small app in `app/` that doesn't just run tests
and build a Docker image — it also explains *why* it failed, in plain English, whenever it
breaks.

## What's here

```
app/                     a tiny order-total calculator (Java + Maven) — has a real bug in it
.github/workflows/ci.yml your pipeline — currently just TODOs, you build it
.github/workflows/grade.yml   DO NOT EDIT — auto-checks your submission, runs on every push
CHECKLIST.md              plain-English version of what grade.yml checks
BRIEF.md                  the full problem writeup
```

## How this works

1. Fork this repo.
2. Read `BRIEF.md`, then work through `app/` — there's a failing test. Find it, understand
   it, fix it (this is Step 4 of the session: reading a failing run for real, not staged).
3. Fill in `.github/workflows/ci.yml` — the jobs are stubbed with `# TODO` comments mapped
   to the session steps. Chain them with `needs` the way the tutorial showed you.
4. Add the failure-diagnosis job — this is the new part, not covered verbatim in the
   session. It should run only `if: failure()` and post a plain-English summary of what
   broke and where, using `GITHUB_STEP_SUMMARY`.
5. Push. `grade.yml` runs automatically and gives you a pass/fail breakdown as a job
   summary — no one needs to manually review your code for the basics to be verified.

## Done means

See `CHECKLIST.md`. Short version: pipeline triggers on push, tests genuinely gate the
build, Docker image builds, and a real human could read your failure summary and know
what to fix without opening the raw logs.
