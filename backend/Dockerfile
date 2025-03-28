FROM python:3.13.2-bookworm

RUN apt-get update && apt-get install -y \
    --no-install-recommends curl ca-certificates git

WORKDIR /usr/app

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"
COPY --from=ghcr.io/astral-sh/uv:0.6.10 /uv /uvx /bin/


COPY . .

RUN uv sync --frozen
RUN uv pip install Cython pytest go-task-bin

CMD ["uv", "run", "task", "serve"]