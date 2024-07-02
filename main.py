#importing necessary libraries
import boto3

#setting up AWS session
session = boto3.Session(region_name='ca-central-1') 
polly_client = session.client('polly')

def text_to_speech(text, voice_id='Kevin', output_format='mp3'):
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat=output_format,
        VoiceId=voice_id
    )
    audio_stream = response['AudioStream'].read()
    return audio_stream
