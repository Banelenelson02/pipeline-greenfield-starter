# Brief: Pipeline Greenfield

## Scenario

`app/` is a tiny order-total calculator for a small shop — it applies a discount and tax
to an order. It's small on purpose, same spirit as the session's calculator app, so your
attention goes on the pipeline, not the business logic.

There's a real bug in `OrderTotal.java`. One of the tests in `OrderTotalTest.java` currently
fails against it. That's intentional — before you touch the pipeline, run the tests locally
(`mvn test`) and actually read why it's failing. This is the same skill as
[Step 4](https://github.com/ai-builder-circle/session-cicd-pipeline/blob/main/steps/04-break-it-on-purpose.md)
of the session, except this time nobody staged the break for you — you have to find it like
you would in a real codebase.

## What you're building

A GitHub Actions pipeline (`.github/workflows/ci.yml`) with these jobs, chained with `needs`
exactly like the session taught:

1. **run-tests** — checks out the code, sets up Java 21, runs `mvn test`
2. **build-jar** — needs `run-tests`; packages the jar and uploads it as an artifact
3. **build-docker-image** — needs `build-jar`; builds the Docker image from `app/Dockerfile`
4. **diagnose-failure** — the new part. Runs `if: failure()`, i.e. only when something
   upstream broke. It should look at what failed and write a short, human-readable summary
   to the GitHub Actions job summary (`$GITHUB_STEP_SUMMARY`) — e.g. "Tests failed: 1 of 5
   assertions failed in OrderTotalTest — check the discount rounding logic" rather than just
   "job failed, see logs above."

You don't need anything fancy for #4 — even a shell step that greps the previous job's
conclusion and echoes a plain-English guess of the cause into the summary is enough to prove
you understand *why* pipelines should communicate failure, not just detect it.

## Why this matters

Anyone can copy a working `ci.yml` from a tutorial. Fixing a real bug you had to find
yourself, and adding a step the tutorial never gave you, is what actually proves the session
landed — and it's a small, legible thing to point to on your own GitHub afterward.
