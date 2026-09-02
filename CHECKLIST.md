# Checklist — what "done" means

Self-tick these before you consider it finished. `grade.yml` checks all of them
automatically and posts the results as a job summary on every push.

- [ ] The bug in `OrderTotal.java` is actually fixed — `mvn test` passes locally, all 5 tests
- [ ] `ci.yml` triggers on push and pull_request to `main`
- [ ] `run-tests` job exists and runs `mvn test`
- [ ] `build-jar` job exists, has `needs: run-tests`, and uploads the jar as an artifact
- [ ] `build-docker-image` job exists, has `needs: build-jar`, and builds from `app/Dockerfile`
- [ ] `diagnose-failure` job exists, runs only `if: failure()`, and writes to
      `$GITHUB_STEP_SUMMARY`
- [ ] The Docker image actually builds successfully (multi-stage, matches the session pattern)
- [ ] You did **not** edit `grade.yml`

If every box is genuinely true, the grading workflow's summary should show all green.
- [ ] `SUBMISSION.md` is filled in with real answers, not the placeholder comments
