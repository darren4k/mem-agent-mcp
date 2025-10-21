# vLLM model name - should match the model name served by your vLLM server
# This can be overridden by setting VLLM_MODEL_NAME in .env
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file from the repository root
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

MEMORY_AGENT_NAME = os.getenv("VLLM_MODEL_NAME", "mem-agent")

# MLX model names
MLX_4BIT_MEMORY_AGENT_NAME = "mem-agent-mlx-4bit"
MLX_8BIT_MEMORY_AGENT_NAME = "mem-agent-mlx-8bit"
MLX_MEMORY_AGENT_NAME = "driaforall/mem-agent-mlx-bf16"
# Default MLX model (kept for backwards compatibility)
MLX_MEMORY_AGENT_NAME = MLX_4BIT_MEMORY_AGENT_NAME