from setuptools import setup, find_packages

setup(
    name="tf_intelgpu_benchmark",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "tensorflow-directml"
    ],
    entry_points={
        "console_scripts": [
            "tf_intelgpu_benchmark = tf_intelgpu_benchmark.benchmark:main",
        ],
    },
    author="Equinet Paul",
    author_email="paulequiney@gmail.com",
    description="Un outil simple pour comparer les performances de TensorFlow avec DirectML sur CPU et GPU",
    license="MIT",
    url="https://github.com/EquinetPaul/tf_intelgpu_benchmark",
)
