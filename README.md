$env:Path += ";C:\ffmpeg\bin"



pip install --upgrade pip
pip install --upgrade transformers datasets[audio] accelerate





problema com o torch:

python -m pip install --upgrade pip setuptools wheel


pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

python -c "import torch; print(torch.cuda.is_available())"

