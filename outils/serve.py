"""Serveur local du site, comme Vercel : adresses sans .html, pas de cache.
Usage : python3 outils/serve.py [port]   puis ouvrez http://localhost:5188"""
import http.server, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'site')
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 5188

class H(http.server.SimpleHTTPRequestHandler):
    def __init__(s, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def translate_path(s, path):
        p = super().translate_path(path)
        if not os.path.exists(p) and os.path.exists(p + '.html'): return p + '.html'
        return p
    def end_headers(s):
        s.send_header('Cache-Control', 'no-cache'); super().end_headers()
    def log_message(s, *a): pass

print(f'site servi sur http://localhost:{PORT}')
http.server.ThreadingHTTPServer(('', PORT), H).serve_forever()
