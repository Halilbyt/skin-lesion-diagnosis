# Setup
Here is a quick guide to setting up the local environment for NN.

### 1. Virtual Environment

It is best to work in an isolated environment. Run these commands in the project root:

```Bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

Install the required data science libraries and PyTorch:

```Bash
pip install ipykernel numpy pandas matplotlib seaborn scikit-learn
```

For AMD GPU users, install the ROCm version of PyTorch (tested):
```Bash
pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm6.3
```

For NVIDIA GPU users, install the CUDA version of PyTorch (not tested):
```Bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### 3. Jupyter Kernel Setup

Link this virtual environment to Jupyter so you can use it in your notebooks:

```Bash
python -m ipykernel install --user --name=venv --display-name="NN Training (venv)"
```

### 4. Running in VS Code
Open the project in VS Code and go to notebooks/03_nn_training.ipynb.

Click the Select Kernel button in the top right corner.

Choose Jupyter Kernel, then select NN Training (venv) from the list.