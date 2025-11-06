FROM n8nio/n8n:latest

# Set working directory
WORKDIR /home/node

# Expose n8n port
EXPOSE 5678

# Set environment variables (can be overridden)
ENV N8N_BASIC_AUTH_ACTIVE=false
ENV N8N_HOST=0.0.0.0
ENV N8N_PORT=5678
ENV N8N_PROTOCOL=http

# Create directory for files
RUN mkdir -p /files

# Run n8n
CMD ["n8n", "start"]

