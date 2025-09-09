# 🎤 Text-to-Speech (TTS) Python App

Ứng dụng Python chuyển văn bản tiếng Việt thành giọng nói sử dụng dịch vụ **Edge TTS** (Microsoft Azure). Tệp âm thanh đầu ra sẽ được phát tự động ngay sau khi tạo.

## 🚀 Tính năng

- Hỗ trợ giọng nói tự nhiên tiếng Việt (mặc định: `vi-VN-HoaiMyNeural`)
- Tạo và phát file âm thanh `.mp3`
- Tự động nhận diện hệ điều hành và phát âm thanh phù hợp:
    ✅ Windows
    ✅ Linux

## 🧰 Yêu cầu hệ thống

- Python 3.7+
- `edge-tts` thư viện
- Trình phát âm thanh phù hợp với hệ điều hành:
  - **Windows**: `start`
  - **Linux**: `mpg123` (bạn cần cài đặt thủ công nếu chưa có)

## 🛠️ Cài đặt

### 1. Clone dự án (hoặc tải file `.py`)

```bash
git clone https://github.com/haivoDA22TTD/Text_To_Speech.git
cd Text_To_Speech
```
#### 2. Cài đặt thư viện phụ thuộc
```bash
pip install edge-tts
```
### 3. (Tuỳ chọn) Cài đặt trình phát âm thanh cho Linux

Ubuntu/Debian:
```bash
sudo apt install mpg123
```

Arch Linux:
```bash
sudo pacman -S mpg123
```
## ▶️ Cách sử dụng

Chạy ứng dụng:
### Windows
```bash
python Voice_bot.py
```

### Linux
```bash
python3 Voice_bot.py
```
