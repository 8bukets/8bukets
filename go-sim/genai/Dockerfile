# Base build directly instead of multi-stage to avoid Docker cache mount issues on this specific host runner
FROM golang:1.24-alpine

WORKDIR /app

# Install CA certificates to ensure secure HTTPS calls to the Gemini API
RUN apk --no-cache add ca-certificates

# Copy dependency files and download
COPY go.mod go.sum ./
RUN go mod download

# Copy the source code and build
COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o genai_example main.go

# Expose no ports since it's a CLI app, but define the default command
CMD ["./genai_example"]
