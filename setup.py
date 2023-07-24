from setuptools import setup, find_packages


setup(
    name="konanai",
    version="0.0.1",
    description=(
        "Konanai is a comprehensive Python package for speech analysis and "
        "modeling. It facilitates acoustic, phonetic, and linguistic "
        "processing, alignment, visualization, and estimation. The package is "
        "enhanced with various external utilities, including UMAP models, "
        "audio feature extraction tools, and forced alignment methods."
    ),
    author="Joseph Konan",
    author_email="konan@konanai.com",
    url="https://github.com/KonanAI-LLC/konanai",
    packages=find_packages(where="src"),
    package_dir={
        "": "src",
        "Charsiu": "src/konanai/externals/lib/charsiu/src",
    },
    install_requires=[
        "tensorflow",
        "torch",
        "torchaudio",
        "numpy",
        "matplotlib",
        "scikit-learn",
        "umap-learn",
        "pandas",
        "opensmile",
        "transformers",
        "soundfile",
        "librosa",
        "argparse",
        "tqdm",
        "datasets",
        "g2p_en",
        "jiwer",
        "praatio",
        "scipy",
        "g2pM",
        "typing-extensions",
    ],
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
