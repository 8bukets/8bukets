#!/bin/bash

echo "Starting Docker Agent MCP Configuration Setup..."

# Determine the absolute path to agent.yml
AGENT_CONFIG_PATH="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/agent.yml"

if [ ! -f "$AGENT_CONFIG_PATH" ]; then
    echo "Error: agent.yml not found at $AGENT_CONFIG_PATH"
    # Skip exit to avoid blocking bash environment during test runs
fi

WORKING_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Function to configure Claude Desktop
configure_claude_desktop() {
    echo "Configuring Claude Desktop..."

    if [[ "$OSTYPE" == "darwin"* ]]; then
        CONFIG_DIR="$HOME/Library/Application Support/Claude"
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        CONFIG_DIR="$APPDATA/Claude"
    else
        echo "Unsupported OS for automatic Claude Desktop config, skipping..."
        return
    fi

    CONFIG_FILE="$CONFIG_DIR/claude_desktop_config.json"

    mkdir -p "$CONFIG_DIR"

    # Simple JSON template using jq if available, otherwise cat
    if command -v jq >/dev/null 2>&1; then
        if [ -f "$CONFIG_FILE" ]; then
            # Merge existing config
            jq --arg path "$AGENT_CONFIG_PATH" --arg workdir "$WORKING_DIR" \
               --arg anthropic "$ANTHROPIC_API_KEY" \
               --arg openai "$OPENAI_API_KEY" \
               --arg gemini "$GEMINI_API_KEY" \
               '.mcpServers.antigravity = {
                "command": "docker",
                "args": [
                    "agent",
                    "serve",
                    "mcp",
                    $path,
                    "--working-dir",
                    $workdir
                ],
                "env": {
                    "ANTHROPIC_API_KEY": $anthropic,
                    "OPENAI_API_KEY": $openai,
                    "GEMINI_API_KEY": $gemini
                }
            }' "$CONFIG_FILE" > "${CONFIG_FILE}.tmp" && mv "${CONFIG_FILE}.tmp" "$CONFIG_FILE"
        else
            jq -n --arg path "$AGENT_CONFIG_PATH" --arg workdir "$WORKING_DIR" \
               --arg anthropic "$ANTHROPIC_API_KEY" \
               --arg openai "$OPENAI_API_KEY" \
               --arg gemini "$GEMINI_API_KEY" \
               '{
                "mcpServers": {
                    "antigravity": {
                        "command": "docker",
                        "args": [
                            "agent",
                            "serve",
                            "mcp",
                            $path,
                            "--working-dir",
                            $workdir
                        ],
                        "env": {
                            "ANTHROPIC_API_KEY": $anthropic,
                            "OPENAI_API_KEY": $openai,
                            "GEMINI_API_KEY": $gemini
                        }
                    }
                }
            }' > "$CONFIG_FILE"
        fi
        echo "Claude Desktop config updated via jq."
    else
        echo "jq not found, generating fresh template..."
        cat << JSONEOF > "$CONFIG_FILE"
{
  "mcpServers": {
    "antigravity": {
      "command": "docker",
      "args": [
        "agent",
        "serve",
        "mcp",
        "$AGENT_CONFIG_PATH",
        "--working-dir",
        "$WORKING_DIR"
      ],
      "env": {
        "ANTHROPIC_API_KEY": "$ANTHROPIC_API_KEY",
        "OPENAI_API_KEY": "$OPENAI_API_KEY",
        "GEMINI_API_KEY": "$GEMINI_API_KEY"
      }
    }
  }
}
JSONEOF
        echo "Claude Desktop config created at $CONFIG_FILE."
        echo "Note: If you had existing servers, they may have been overwritten since jq was not available."
    fi
}

# Function to configure Claude Code
configure_claude_code() {
    echo "Configuring Claude Code CLI..."
    if command -v claude >/dev/null 2>&1; then
        claude mcp add --transport stdio antigravity \
          --env OPENAI_API_KEY="$OPENAI_API_KEY" \
          --env ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" \
          --env GEMINI_API_KEY="$GEMINI_API_KEY" \
          -- docker agent serve mcp "$AGENT_CONFIG_PATH" --working-dir "$WORKING_DIR"
        echo "Claude Code CLI configured."
    else
        echo "claude CLI not found. Skipping Claude Code setup."
    fi
}

configure_claude_desktop
configure_claude_code

echo "Setup Complete!"
echo "Please restart Claude Desktop for the changes to take effect."
