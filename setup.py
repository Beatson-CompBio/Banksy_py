from setuptools import setup, find_packages

setup(
    name='banksy_py',
    version='0.0.1',
    description='Pip installable version of Banksy_py; all credit goes to the Banksy authors.',
    author='Nigel Chou;Yifei Yue',
    author_email='Nigel_Chou@gis.a-star.edu.sg',
    maintainer='albert.plaplanas@sanofi.com',
    maintainer_email='albert.plaplanas@sanofi.com',
    packages=["banksy_py", "banksy_py.banksy_utils", "banksy_py.banksy"],
    install_requires=[
        'anndata>=0.10.8',
        'anyio>=4.0.0',
        'certifi',
        'h5py>=3.10.0',
        'igraph>=0.10.6',
        'importlib-metadata>=4.6',
        'joblib>=1.3.2',
        'jsonschema>=4.19.1',
        'jsonschema-specifications>=2023.7.1',
        'matplotlib<3.9.0',
        'matplotlib-inline>=0.1.6',
        'numpy>=1.24.4',
        'pandas>=2.1.1',
        'pickleshare>=0.7.5',
        'scanpy>=1.9.5',
        'scikit-learn>=1.3.1',
        'scipy>=1.11.3',
        'seaborn>=0.13.0',
        'tornado>=5.1',
        'umap-learn>=0.5.4',
        'urllib3<4.0',
        'websocket-client<3.0',
        'leidenalg>=0.10.2',
        'IPython',
        'rpy2'
    ],
    python_requires='>=3.6',
)
