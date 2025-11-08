import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
from langsmith import traceable

load_dotenv(dotenv_path="../.env",override=True)

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

@traceable(name="upload_note")
def upload_note(note: str) -> bool:
    """
    上传笔记到云端
        Args:
            note (str): 笔记内容
        Returns:
            str: 上传是否成功
    """
    print(f"上传笔记: {note}")
    return True

@traceable(name="main")
def main():
    system_prompt_template = """
    #ROLE
    你是一个笔记上传工程师，
    #Task
    - 不管我输入什么，必须对我输入的数据后面加上"---完成"。
    - 使用【upload_note】工具将笔记上传到云端。"""

    editor_agent = create_agent(
        model=deepseek_chat,
        tools=[upload_note],
        system_prompt=system_prompt_template,
    )

    editor_agent.invoke(
        # input={"human_ptompt":"我是个天才"} ,
        {"messages": [{"role": "user", "content": "# 我是个天才，我会用Python写程序。-- 这就是我的笔记"}]}
        # [{"role": "user", "content": "我是个天才，我会用Python写程序。"}]

    )

if __name__ == '__main__':
    main()