import os
from openai import OpenAI

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)


def ask_chatgpt(question):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
            model="gpt-4o",
            temperature=1,
            max_tokens=4096,
            top_p=1,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def chat_loop():
    while True:
        user_input = input("q : ")  # 사용자의 질문을 입력받음

        if not user_input.strip():  # 입력이 비어있는 경우
            continue

        if user_input.lower() in ["q"]:  # 종료 명령어
            print("프로그램을 종료합니다.")
            break

        response = ask_chatgpt(user_input)  # 질문을 챗봇에 전달하고 답변을 받음
        print(f"\na : {response}\n")  # 챗봇의 답변을 출력


if __name__ == "__main__":
    chat_loop()  # 챗봇 루프 실행
