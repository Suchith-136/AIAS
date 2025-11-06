import random

class BankCustomerSupportChatbot:
    def __init__(self, language='en', accessibility_mode=False):
        self.language = language
        self.accessibility_mode = accessibility_mode

        # Internationalized responses for English and Spanish
        self.responses = {
            'en': {
                "greeting": [
                    "Hello! Welcome to BankAssist. How may I help you today?",
                    "Hi! This is your bank's virtual assistant. How can I help you?",
                    "Greetings from your bank's support team! What can I do for you today?"
                ],
                "goodbye": [
                    "Thank you for banking with us. Have a great day!",
                    "Goodbye! If you have more questions, feel free to ask anytime.",
                    "It was a pleasure assisting you. Take care!"
                ],
                "account_balance": [
                    "To check your account balance, please provide your account number.",
                    "I'd be happy to help you with your balance. What is your account ID?",
                    "For account balance details, can you confirm your account information?"
                ],
                "transaction_issue": [
                    "I'm sorry to hear about a transaction issue. Could you describe the problem or provide the transaction ID?",
                    "I'll help you with your transaction problem. Could you give me the transaction details or amount?",
                    "Let me assist you with your transaction issue. Please share either the transaction reference or the issue you're experiencing."
                ],
                "card_block": [
                    "Do you need to block your card due to loss or theft? Please confirm the last four digits of the card.",
                    "I can help block your card. Can you provide the card type (debit/credit) and its last four digits?",
                    "To proceed with blocking your card, may I have the card details?"
                ],
                "loan_inquiry": [
                    "For loan information or application, can you specify the type of loan you're interested in?",
                    "I'd be glad to assist with loan queries. What type of loan do you need help with?",
                    "Let me know about your loan inquiry or if you'd like to apply for a new loan."
                ],
                "default": [
                    "I'm sorry, I didn't understand. Could you please rephrase your issue related to your bank account?",
                    "Can you provide more specifics about your banking problem?",
                    "For complex issues, I can connect you to a human representative."
                ]
            },
            'es': {
                "greeting": [
                    "¡Hola! Bienvenido a BankAssist. ¿Cómo puedo ayudarte hoy?",
                    "¡Hola! Soy el asistente virtual de tu banco. ¿En qué puedo ayudarte?",
                    "Saludos del equipo de soporte de tu banco. ¿En qué puedo ayudarte hoy?"
                ],
                "goodbye": [
                    "Gracias por confiar en nosotros. ¡Que tenga un buen día!",
                    "¡Adiós! Si tienes más preguntas, puedes consultarnos en cualquier momento.",
                    "Fue un placer ayudarte. ¡Cuídate!"
                ],
                "account_balance": [
                    "Para verificar tu saldo, por favor proporciona tu número de cuenta.",
                    "Con gusto te ayudo a consultar el saldo. ¿Cuál es tu número de cuenta?",
                    "Para detalles del saldo, ¿puedes confirmar tu información de cuenta?"
                ],
                "transaction_issue": [
                    "Lamento escuchar que tienes un problema con una transacción. ¿Puedes describir el problema o darme el número de transacción?",
                    "Te ayudaré con el problema de la transacción. ¿Puedes darme los detalles o el monto?",
                    "Permíteme asistirte con la transacción. Por favor, comparte el referencia o el tema del problema."
                ],
                "card_block": [
                    "¿Necesitas bloquear tu tarjeta por pérdida o robo? Por favor confirma los últimos cuatro dígitos de la tarjeta.",
                    "Te ayudo a bloquear tu tarjeta. ¿Puedes darme el tipo de tarjeta (débito/crédito) y sus últimos cuatro dígitos?",
                    "Para bloquear la tarjeta necesito sus datos, por favor."
                ],
                "loan_inquiry": [
                    "Para información o solicitud de préstamos, ¿puedes especificar el tipo de préstamo que te interesa?",
                    "Con gusto te ayudo con consultas sobre préstamos. ¿Qué tipo de préstamo deseas?",
                    "Dime tu consulta de préstamo, o si quieres aplicar para uno nuevo, por favor acláralo."
                ],
                "default": [
                    "Lo siento, no entendí bien. ¿Puedes aclarar tu problema bancario?",
                    "¿Puedes brindarme más detalles sobre tu inconveniente en el banco?",
                    "Para casos complejos, puedo conectarte con un representante humano."
                ]
            }
        }

        # Banking-related keywords per language to map user intent
        self.keywords = {
            'en': {
                "balance": "account_balance",
                "account balance": "account_balance",
                "how much money": "account_balance",
                "transaction": "transaction_issue",
                "payment": "transaction_issue",
                "unauthorized": "transaction_issue",
                "failed": "transaction_issue",
                "card": "card_block",
                "lost card": "card_block",
                "block card": "card_block",
                "stolen": "card_block",
                "loan": "loan_inquiry",
                "apply loan": "loan_inquiry",
                "hello": "greeting",
                "hi": "greeting",
                "bye": "goodbye",
                "goodbye": "goodbye"
            },
            'es': {
                "saldo": "account_balance",
                "cuenta": "account_balance",
                "dinero": "account_balance",
                "transacción": "transaction_issue",
                "pago": "transaction_issue",
                "no autorizado": "transaction_issue",
                "fallido": "transaction_issue",
                "tarjeta": "card_block",
                "perdí mi tarjeta": "card_block",
                "bloquear tarjeta": "card_block",
                "robada": "card_block",
                "préstamo": "loan_inquiry",
                "solicitar préstamo": "loan_inquiry",
                "hola": "greeting",
                "buenos días": "greeting",
                "adiós": "goodbye",
                "bye": "goodbye"
            }
        }

        self.exit_commands = {
            'en': ["bye", "goodbye", "exit", "quit"],
            'es': ["adiós", "salir", "bye"]
        }

    def accessible_output(self, text):
        if self.accessibility_mode:
            print(f"Bot (Screen Reader): {text}")
        else:
            print(f"Bot: {text}")

    def get_response(self, message):
        lang = self.language
        message_lower = message.lower()
        found_intent = None
        # Match by whole-phrase keywords first
        for keyword in self.keywords[lang]:
            if keyword in message_lower:
                found_intent = self.keywords[lang][keyword]
                break
        if not found_intent:
            # Try to match by individual words (for more flexible matching)
            msg_words = message_lower.split()
            for word in msg_words:
                if word in self.keywords[lang]:
                    found_intent = self.keywords[lang][word]
                    break

        if found_intent and found_intent in self.responses[lang]:
            return random.choice(self.responses[lang][found_intent])
        return random.choice(self.responses[lang]["default"])

    def chat(self):
        # Accessibility intro
        if self.accessibility_mode:
            intro = {
                'en': "You are chatting with BankAssist, your accessible bank support chatbot. Please type your banking issue and press Enter. Screen reader-friendly output will be used.",
                'es': "Está conversando con BankAssist, su asistente bancario accesible. Escriba su problema bancario y presione Enter. Se usará una salida apta para lectores de pantalla."
            }
            self.accessible_output(intro[self.language])
        self.accessible_output(random.choice(self.responses[self.language]["greeting"]))
        while True:
            try:
                user_input = input("You: ").strip()
            except EOFError:
                self.accessible_output(random.choice(self.responses[self.language]["goodbye"]))
                break
            if user_input.lower() in self.exit_commands[self.language]:
                self.accessible_output(random.choice(self.responses[self.language]["goodbye"]))
                break
            response = self.get_response(user_input)
            self.accessible_output(response)

def select_language():
    print("Select language / Seleccione el idioma: (en/es)")
    lang = input("Language/Idioma [en]: ").strip().lower()
    if lang not in ('en', 'es'):
        lang = 'en'
    return lang

def select_accessibility():
    resp = input("Enable accessibility mode for screen readers? (y/n): ").strip().lower()
    return resp == 'y'

if __name__ == "__main__":
    language = select_language()
    accessibility = select_accessibility()
    bot = BankCustomerSupportChatbot(language=language, accessibility_mode=accessibility)
    bot.chat()


