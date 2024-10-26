# PyTorch_HuggingFace_NLP
This tutorial will fine-tune a language model using the HuggingFace Transformers library in a federated learning environment.

The tutorial has been tested using Python 3.10 on Linux and Windows operating systems.

## Step 0: Installation
Create a virtual environment and install OpenFL using:

https://openfl.readthedocs.io/en/latest/get_started/installation.html

## Step 1: Environment Setup
We need three terminals for the director, envoy, and experiment.

After activating the virtual environment in all three terminals, run the following:

```sh
git clone https://github.com/securefederatedai/openfl.git
cd openfl/openfl-tutorials/interactive_api/PyTorch_HuggingFace_NLP
export SETUPTOOLS_USE_DISTUTILS=stdlib
```

## Step 2: Run the Director
In the director's terminal, run the following:

```sh
cd director
./start_director.sh
```

## Step 3: Run the Envoy
In the envoy's terminal, run the following:

```sh
cd envoy
./start_envoy.sh
```

## Step 4: Run the Experiment
In the experiment's terminal, run the following:

```sh
cd workspace
jupyter execute PyTorch_HuggingFace_NLP.ipynb
```
