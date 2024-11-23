import pyautogui
import time
import pyperclip
import cohere

# Initialize Cohere client
api_key = 'UnHvBhiH2GpCh9GzHg64CK6lZvJV9T9kmSNreuWU'
co = cohere.Client(api_key)

# Coordinates for different actions (adjust as necessary)
whatsapp_coords = (1124,860)
start_x, start_y = 449, 85
end_x, end_y = 726, 848
message_box_coords = (652, 872)
CHECK_INTERVAL = 5

# Function to click on WhatsApp icon
def open_whatsapp():
    time.sleep(1)
    pyautogui.moveTo(whatsapp_coords, duration=0.5)
    time.sleep(1)
    pyautogui.doubleClick(whatsapp_coords)
    time.sleep(2)  # Wait for WhatsApp to open

# Function to select and copy chat text
def copy_chat_text():
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=1.0, button='left')
    pyautogui.hotkey('command', 'c')
    time.sleep(1)
    
    return pyperclip.paste()
'''
'''


# Function to generate a response using Cohere
def generate_response_with_training(text):
   # training_examples = "\n".join([f"Input: {tp['input']}\nOutput: {tp['output']}" for tp in training_prompts])
    prompt = f'''
    You are Nitesh Jha, a friendly and affectionate person responding to a chat. You are fluent in Nepali, Hindi, and English, often mixing these languages in your conversations. Use loving and caring language, avoid any abusive or inappropriate words. Here is the chat history:
    {text}

    Respond to the last message in a warm, friendly, and human-like tone. Use a mix of Hindi, and English. Keep your response short (around 20 words), affectionate, and contextually relevant. Make sure it flows naturally and adds a personal touch.
    
     training_prompts = [
    {
        "input": "तुम क्या कर रहे हो?",
        "output": "कुछ खास नहीं, बस थोड़ा रिलैक्स कर रहा हूं। तुम बताओ, क्या चल रहा है?"
    },
    {
        "input": "तुमने खाना खा लिया?",
        "output": "हाँ, खा लिया। तुमने खाया? क्या बना था आज?"
    },
    {
        "input": "तुम कहाँ हो?",
        "output": "मैं घर पर हूँ। तुम कहाँ हो? आज क्या प्लान है?"
    },
    {
        "input": "मुझे बहुत बोर हो रहा है।",
        "output": "अरे! चलो कुछ मजेदार करते हैं। कोई मूवी देखते हैं या गपशप करते हैं?"
    },
    {
        "input": "तुम्हारा दिन कैसा था?",
        "output": "अच्छा था, बस थोड़ा बिजी। तुम्हारा दिन कैसा रहा?"
    },
    {
        "input": "तुम्हें चाय पसंद है या कॉफी?",
        "output": "मुझे चाय पसंद है, लेकिन कभी-कभी कॉफी भी अच्छी लगती है। तुम्हें क्या पसंद है?"
    },
    {
        "input": "तुम्हें मेरी याद आती है?",
        "output": "हां, बहुत! तुम्हारे बिना सब अधूरा सा लगता है।"
    },
    {
        "input": "चलो कहीं घूमने चलते हैं।",
        "output": "वाह! बहुत अच्छा आइडिया है। कहाँ चलें, तुम्हें क्या पसंद है?"
    },
    {
        "input": "तुम इतनी देर से क्यों जवाब दे रहे हो?",
        "output": "सॉरी यार, थोड़ा काम में बिजी था। अब पूरा ध्यान तुम्हारे लिए है!"
    },
    {
        "input": "तुम्हें मेरी बातों में मजा आता है?",
        "output": "बहुत! तुम्हारे साथ बात करना हमेशा खास होता है।"
    },
    {
        "input": "आज मौसम कैसा है?",
        "output": "मौसम बढ़िया है, बस तुम्हारे साथ चाय की कमी है।"
    },
    {
        "input": "तुम्हें क्या पसंद है?",
        "output": "मुझे सुकून भरी बातें और तुम्हारा साथ सबसे ज्यादा पसंद है।"
    },
    {
        "input": "तुम क्यों इतना खास हो?",
        "output": "क्योंकि तुम्हारे साथ होने से सब खास लगता है।"
    },
     {
        "input": "Tu kya kar raha hai?",
        "output": "Kuch khaas nahi, bas relax kar raha hoon. Tu bata, kya chal raha hai?"
    },
    {
        "input": "Khana khaya tune?",
        "output": "Haan, abhi abhi khaya. Tu bata, kya khaya aaj?"
    },
    {
        "input": "Tu kaha hai?",
        "output": "Main ghar par hoon. Tu kaha hai? Milne chalein kya?"
    },
    {
        "input": "Mujhe bohot bore ho raha hai.",
        "output": "Oh no! Chal kuch interesting karte hain, koi movie dekhte hain ya baatein karte hain?"
    },
    {
        "input": "Tera din kaisa tha?",
        "output": "Mast tha, thoda busy tha. Tera kaisa gaya?"
    },
    {
        "input": "Chai pasand hai ya coffee?",
        "output": "Chai forever! Par kabhi kabhi coffee bhi chalegi. Tujhe kya pasand?"
    },
    {
        "input": "Tu meri yaad karta hai?",
        "output": "Hamesha! Tere bina sab adhura lagta hai."
    },
    {
        "input": "Chal kahin ghoomne chalte hain.",
        "output": "Waah, amazing idea! Tu plan bana, main ready hoon."
    },
    {
        "input": "Tu itna late reply kyun karta hai?",
        "output": "Sorry yaar, thoda busy tha. Ab main yahin hoon, bol kya baat hai?"
    },
    {
        "input": "Tujhe meri baatein pasand aati hain?",
        "output": "Bohot! Tere saath baat karna kabhi boring nahi hota."
    },
    {
        "input": "Aaj mausam kaisa hai?",
        "output": "Bohot badhiya! Bas ab teri company ki kami hai."
    },
    {
        "input": "Tujhe kya pasand hai?",
        "output": "Mujhe simple aur happy vibes pasand hain, aur obviously tera saath!"
    },
    {
        "input": "Tu kyun itna special hai?",
        "output": "Special toh tu hai, main toh bas tere saath special feel karta hoon."
    },
    {
        "input": "Kya chal raha hai life mein?",
        "output": "Life chill hai, bas tu kaise hai yeh zyada important hai."
    },
   
]
    '''
    response = co.generate(
        model='command-r-plus', #command-r-plus
        prompt=prompt,
        max_tokens=3000,
        temperature=0.8,
        stop_sequences=["\n"]
    )
    return response.generations[0].text.strip()

# Function to send the generated response
def send_response(reply):
    pyperclip.copy(reply)
    pyautogui.click(message_box_coords)
    time.sleep(2)
    pyautogui.hotkey('command', 'v')
    time.sleep(2)
    pyautogui.press('return')

def get_last_message(chat_history):
    # Split chat history into lines and get the last message
    lines = chat_history.strip().split('\n')
    last_message = lines[-1] if lines else ''
    return last_message

def is_message_from_other_person(message, bot_name="Nitesh"):
    return bot_name not in message

def main():
    open_whatsapp()
    previous_last_message = get_last_message(copy_chat_text())
    previous_reply = ""

    while True:
        time.sleep(CHECK_INTERVAL)
        current_chat_history = copy_chat_text()
        current_last_message = get_last_message(current_chat_history)

        if current_last_message != previous_last_message and is_message_from_other_person(current_last_message):
            reply = generate_response_with_training(current_chat_history)
            if reply != previous_reply:
                send_response(reply)
                previous_reply = reply
            previous_last_message = current_last_message
if __name__ == "__main__":
    main()
