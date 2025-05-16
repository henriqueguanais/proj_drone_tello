from streamlit_webrtc import webrtc_streamer
import av

def record_audio():
    def audio_frame_callback(frame: av.AudioFrame) -> av.AudioFrame:
        # Processar frame aqui (opcional)
        return frame

    webrtc_ctx = webrtc_streamer(
        key="audio-recorder",
        mode="recording",
        audio_frame_callback=audio_frame_callback,
        media_stream_constraints={"audio": True}
    )

    return webrtc_ctx.input_audio_queue