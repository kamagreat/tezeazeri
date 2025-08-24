#!/usr/bin/env python3
"""
Публичный сервер для тренажера азербайджанского языка
"""

import http.server
import socketserver
import socket
import threading
import time
import os

def get_local_ip():
    """Получить локальный IP адрес"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def start_server(port=8000):
    """Запустить веб-сервер"""
    handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(("", port), handler) as httpd:
        print("="*60)
        print("🎯 ТРЕНАЖЕР АЗЕРБАЙДЖАНСКОГО ЯЗЫКА")
        print("="*60)
        print(f"🚀 Сервер запущен на порту {port}")
        print(f"📱 Локальный доступ: http://localhost:{port}")
        print(f"🌐 Сетевой доступ: http://{get_local_ip()}:{port}")
        print()
        print("📖 Ссылки на файлы:")
        print(f"   • Тренажер: http://localhost:{port}/deepseek_html_20250823_8bb39b.html")
        print(f"   • Инструкции: http://localhost:{port}/index.html")
        print(f"   • Простая страница: http://localhost:{port}/simple_share.html")
        print()
        print("🎯 НОВЫЕ ВОЗМОЖНОСТИ:")
        print("✅ Примеры использования слов в предложениях")
        print("✅ Красивое оформление с иконками")
        print("✅ Автоматическое отображение после ответов")
        print("="*60)
        print("\nНажмите Ctrl+C для остановки сервера")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Сервер остановлен")

if __name__ == "__main__":
    start_server()