# Parallel Domain Educational Suite

The Parallel Domain platform contains a rich and diverse set of tools for generating and using synthetic data for machine learning model training in the autonomous vehicle and drone spaces. Data Lab allows us to configure and capture scenarios which provide us valuable training data for a given use case, while the PD-SDK gives us the tools to easily load and interact with this output along with well-known public datasets in a unified development space of Python objects, making it easy to load into training pipelines and encode into our chosen ontology and file schema. It also contains tools to evaluate our datasets at a statistical level, helping to guide the process of tuning our data generation parameters in a way which produces the most potent training data for our use case.

The recommended workflow when using this repository is to first follow the Data Lab educational notebooks, which will empower the user to produce Parallel Domain data for themselves and give introductory exposure to PD-SDK in the process. Then, once the user is comfortable generatng datasets, they can follow up by digging deeper into the features offered by the PD-SDK to get the most out of their data quckly by becoming familiar with the structure of the Python objects and the methods they offer, including comparing their data at a quantitative level to their real-world data by calculating statistics which are relevant to their use case (i.e. classwise pixel distributions for semantic segmentation model training).

## [Data Lab Educational Notebooks](./data_lab/notebooks/README.md)

Follow this numbered set of notebooks to take a guided tour through the functionality of Data Lab, starting simple and building in use case complexity along the way. By the end of this series, the user should be comfortable using Data Lab to produce data tailored to their use case by having full control over the environment as well as the placement and behavior of the ego and other agents within it. To begin, we utilize generators that guide the behavior of the native Parallel Domain simulation stack, then expand on this by mixing in agents which obey custom simulation behaviors constructed by the user. These concepts then unlock more advanced usage of Data Lab, including the powerful generative AI capabilities of Reactor, allowing us to place custom objects into our scenes using textual prompting, which can give us valuable training examples of difficult-to-record agent types (i.e. pedestrians with strollers or using mobility devices).

## [PD-SDK Masterclass Notebooks](./pd_sdk/notebooks/README.md)

The PD-SDK provides an intuitive interface for loading and interacting with machine learning datasets, but to achieve full mastery over the rich and diverse features it offers us, a guided tour can once again help us to reduce onboarding time for the user and streamline their workflows. This section will aim to do just that, by shifting the focus from dataset generation over to interacting with premade datasets using the PD-SDK for various use cases. We will look at using decoders to load datasets into our Python objects, the features offered by these objects, and how we can use these features to easily and effectively use our data. We will then look at the visualization capabilities offered by the PD-SDK of simulation files as well as rendered data and associated statistics. Finally, we review the use of encoders, which allow us to manipulate the ontology and annotation rules of our data so that there is no label space domain gap between our synthetic and real data, as well as enabling us to write the data back out to disk in a file schema of our choice, which can be desirable for easy loading into established training pipelines.

---

## Usage Instructions
<br>

### For first install and when getting updates:
1. Install Git LFS (Large File Storage) by following the instructions here: [Git LFS Installation Docs](https://github.com/git-lfs/git-lfs?utm_source=gitlfs_site&utm_medium=installation_link&utm_campaign=gitlfs#installing)
2. Pull this repo locally and navigate to it in a terminal
3. Create a fresh Python virtual environment (venv) for working with this repo by running `python -m venv ./venv`
4. Activate your venv in your terminal by running one of the following:
    - Windows Powershell: `./venv/scripts/activate.ps1`
    - Linux: `./venv/bin/activate`
5. Install requirements to your venv by running `pip install -r requirements.txt` in your terminal

<br>

### For each use:
- With your venv activated in a terminal:
    1. Ensure `PYTHONPATH` environment variable is empty string:
        - Windows Powershell: `$env:PYTHONPATH=""`
        - Linux: `export PYTHONPATH=""`
    2. Navigate to the `notebooks` folder you want to work with, for example `cd ./data_lab/notebooks`, and run `jupyter notebook`
        - Note that this launches a Jupyter classic server and browser window. Optionally, you can use `JupyterLab` or `VSCode` for more advanced notebook features