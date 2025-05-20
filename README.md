
Passo a passo para rodar:

py -3.10 -m venv venv310

.\venv310\Scripts\activate   


 pip install -r requirements.txt

pip install fastapi[standard]

pip install --upgrade transformers datasets[audio] accelerate



problema com o torch:

python -m pip install --upgrade pip setuptools wheel


pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

python -c "import torch; print(torch.cuda.is_available())"



$env:Path += ";C:\ffmpeg\bin"


fastapi dev main.py --port 8085




