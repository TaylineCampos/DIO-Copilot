def quiz(user_responses=None):
    # Lista de perguntas do quiz, cada uma com suas opções e resposta correta
    questions = [
        {
            "question": "Qual é a capital da Austrália?",
            "options": ["a) Sydney", "b) Melbourne", "c) Canberra", "d) Brisbane"],
            "answer": "c"
        },
        {
            "question": "Qual é a capital do Canadá?",
            "options": ["a) Toronto", "b) Vancouver", "c) Ottawa", "d) Montreal"],
            "answer": "c"
        },
        {
            "question": "Qual é a capital do Japão?",
            "options": ["a) Osaka", "b) Kyoto", "c) Tóquio", "d) Hiroshima"],
            "answer": "c"
        },
        {
            "question": "Qual é a capital da Rússia?",
            "options": ["a) São Petersburgo", "b) Moscou", "c) Novosibirsk", "d) Ecaterimburgo"],
            "answer": "b"
        },
        {
            "question": "Qual é a capital do Egito?",
            "options": ["a) Alexandria", "b) Luxor", "c) Cairo", "d) Gizé"],
            "answer": "c"
        }
    ]

    # Inicializa a pontuação do usuário
    if user_responses is None:
        user_responses = []
    response_index = 0
    score = 0

    # Itera sobre cada pergunta no quiz
    for q in questions:
        # Exibe a pergunta
        print(q["question"])
        # Exibe as opções de resposta
        for option in q["options"]:
            print(option)
        # Solicita a resposta do usuário
        if response_index < len(user_responses):
            answer = user_responses[response_index].lower()
            response_index += 1
        else:
            answer = input("Digite a letra da resposta correta: ").lower()
        # Verifica se a resposta está correta
        if answer == q["answer"]:
            score += 1
            print("Correto!\n")
        else:
            print("Errado. A resposta correta é:", q["answer"], "\n")

    # Exibe a pontuação final do usuário
    percentage = (score / len(questions)) * 100
    print(f"Você acertou {percentage:.2f}% das perguntas.")
    

# Executa o quiz se o script for executado diretamente
if __name__ == "__main__":
    quiz()