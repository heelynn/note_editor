import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek

load_dotenv()

deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")

# --------------------- 初始化LLm ----------

deepseek_chat = ChatDeepSeek(
    api_key=deepseek_api_key,
    model="deepseek-chat",  # 或 "deepseek-reasoner"（推理模式）
    temperature=1.0,
    max_tokens=2048,
    timeout=30,
    max_retries=3,
)

def upload_note(note: str) -> bool:
    """
    上传笔记
        Args:
            note (str): 笔记内容
        Returns:
            str: 上传是否成功
    """

    return True

system_prompt_template = """请上传笔记:"""

editor_agent = create_agent(
    model=deepseek_chat,
    tools=[upload_note],
    system_prompt=system_prompt_template,
)

editor_agent.invoke(
    input={"human_ptompt":"请上传笔记:"} ,

)