from setuptools import setup

setup(
    name="chat-cli",
    version="1.0",
    py_modules=["chat"],
    install_requires=[
        "openai",  # 필요한 라이브러리
    ],
    entry_points={
        "console_scripts": [
            "chatgpt=chat:chat_loop",  # 'chat' 명령어로 chat_loop 함수를 실행
        ],
    },
)
