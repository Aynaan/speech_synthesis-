from TTS.api import TTS
# Wav file as input ONLY
def synth_voice(input_audio,output_audio):

    tts = TTS(model_name="tts_models/multilingual/multi-dataset/your_tts", progress_bar=False, gpu=False)
    tts.tts_to_file("Hello today my voice is going to be synthesized and I am going to have an artificial sound", speaker_wav=input_audio, language="en", file_path=output_audio)
    

#Input path according to flexibility
synth_voice("sample_audio\Sample_freeman.wav", "generated_audio/freeman2.wav")