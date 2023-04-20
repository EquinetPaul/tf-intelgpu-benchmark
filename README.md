# tf-intelgpu-benchmark
Benchmark on Tensorflow using Intel GPU with Directml.

# Usage
```bash
tf_intelgpu_benchmark
```

> Temps d'exécution sur le CPU : 8.0040 secondes


> Temps d'exécution sur le GPU avec DirectML : 0.7991 secondes


> Le GPU a été 10.02 fois plus rapide que le CPU.

# Installation

### Environnement 

```bash
conda create --name intelgpu_tf_benchmark python=3.7 
conda activate intelgpu_tf_benchmark
```

### Clone the repository

In a folder, 

```bash
git clone https://github.com/EquinetPaul/tf-intelgpu-benchmark
```

### Install the package

```bash
cd tf-intelgpu-benchmark
pip install . 
```


# Sources
- https://learn.microsoft.com/en-us/windows/ai/directml/gpu-tensorflow-windows
- https://pypi.org/project/tensorflow-directml/
