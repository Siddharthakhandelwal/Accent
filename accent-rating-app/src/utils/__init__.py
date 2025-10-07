from email.utils import unquote
from urllib.parse import parse_qs, urlparse
import ffmpeg

def convert_mp4_to_mp3(mp4_path, mp3_path=None):
    if mp3_path is None:
        mp3_path = mp4_path.rsplit('.', 1)[0] + '.mp3'
    
    try:
        ffmpeg.input(mp4_path).output(mp3_path, format='mp3', acodec='libmp3lame').run(overwrite_output=True)
        print(f"✅ Converted to: {mp3_path}")
        return mp3_path
    except ffmpeg.Error as e:
        print("❌ FFmpeg error:", e)
        return None

def get_file_id(url):
    try:
        parsed_url = urlparse(url)
        path = parsed_url.path
        query = parsed_url.query

        # Pattern 1: /file/d/{fileid}/
        file_id_marker = "/file/d/"
        if file_id_marker in path:
            start = path.index(file_id_marker) + len(file_id_marker)
            end = path.find('/', start)
            if end == -1:
                end = len(path)
            return path[start:end]

        # Pattern 2: id={fileid} in query params
        if query:
            query_params = parse_query_params(query)
            if "id" in query_params:
                return query_params["id"]
    except Exception:
        pass  # Handle/log exception if needed

    return None

def parse_query_params(query):
    parsed = parse_qs(query)
    # parse_qs returns values as lists, e.g., {'id': ['FILE_ID']}
    return {k: unquote(v[0]) for k, v in parsed.items() if v}