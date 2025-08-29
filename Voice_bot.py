import asyncio
import edge_tts
import os

async def sing_text(text, voice="vi-VN-HoaiMyNeural"):
    communicate = edge_tts.Communicate(text, voice)
    print("🔄 Đang tạo file âm thanh...")
    await communicate.save("output.mp3")
    print("▶️ Phát âm thanh...")
    # Phát file mp3 theo OS
    if os.name == "nt":  # Windows
        os.system("start output.mp3")
    elif os.name == "posix":  # macOS hoặc Linux
        os.system("afplay output.mp3" if sys.platform == "darwin" else "mpg123 output.mp3")
    else:
        print("Không hỗ trợ phát nhạc trên hệ điều hành này.")
    print("✅ Hoàn thành!")

if __name__ == "__main__":
    print("🎤 Nhập đoạn văn bản bạn muốn 'hát' (Text-to-Speech). Nhập xong, nhấn Enter 1 dòng trống để kết thúc:")
    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)
    text = "\n".join(lines)

    asyncio.run(sing_text(text))
