# Multi-stage Dockerfile — same pattern the session used.
# Fill in the TODOs. Two stages: build the jar with Maven, then run it on a
# slim JRE so the final image doesn't ship the whole Maven toolchain.

# ---- stage 1: build ----
# TODO: FROM the right maven+temurin base image, AS build
# TODO: WORKDIR /app
# TODO: COPY pom.xml . then RUN mvn -q dependency:go-offline (caches deps)
# TODO: COPY src ./src then RUN mvn -q clean package -DskipTests

# ---- stage 2: run ----
# TODO: FROM a slim eclipse-temurin JRE image (not the full JDK/Maven one)
# TODO: WORKDIR /app
# TODO: COPY --from=build the built jar into this stage as app.jar
# TODO: ENTRYPOINT that runs `java -jar app.jar`
