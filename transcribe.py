from openai import OpenAI
client = OpenAI(api_key="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")

audio_file = open("audio_file.wav", "rb")
def transcribe(audio_file, speaker_name):
    transcript = client.audio_transcriptions.create(
        model="whisper-1",
        file=audio_file,
    )

system_prompt = "You are a helpful assistant for the company ZyntriQix. Your task is to correct any spelling discrepancies in the transcribed text. Make sure that the names of the following products are spelled correctly: ZyntriQix, Digique Plus, CynapseFive, VortiQore V8, EchoNix Array, OrbitalLink Seven, DigiFractal Matrix, PULSE, RAPT, B.R.I.C.K., Q.U.A.R.T.Z., F.L.I.N.T. Only add necessary punctuation such as periods, commas, and capitalization, and use only the context provided."

def generate_corrected_transcript(temperature, system_prompt, audio_file):
    response = client.chat.completions.create(
        model="gpt-4",
        temperature=temperature,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": transcribe(audio_file, "")
            }
        ]
    )
    return response['choices'][0]['message']['content']

corrected_text = generate_corrected_transcript(0, system_prompt, audio_file)
