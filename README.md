# ITS_us

ITS_us is a robust package for performing arbitrary single and two qubit quantum operations, structured to intuitively construct quantum circuits.

## Contributors

- Sara Cender
- Theo Iosif
- Ivan Shalashilin

## Notebook examples
Also available in HTML form in the `docs` folder

- [Using `States`](https://github.com/QC2-python-SE/ITS_us/blob/main/docs/source/states_example.ipynb)
- [Using `Gates`](https://github.com/QC2-python-SE/ITS_us/blob/main/docs/source/gates_example.ipynb)
- [Using `Circuits` - Constructing the Bell states](https://github.com/QC2-python-SE/ITS_us/blob/main/docs/source/bell_circuit.ipynb)

# Installation[^1]

## Stable version

The latest stable version of ITS_us can be installed via
pip:

```bash
pip install its_us
```


## Development version
> **Warning**
>
> This version is possibly unstable and may contain bugs.

> **Note**
>
> We advise you create virtual environment before installing:
> ```
> conda create -n its_us_experimental python=3.10.0
> conda activate its_us_experimental
>  ```


# Citing ITS_us[^1]

If you use ITS_us in your research, please cite our [Nature paper](https://github.com/QC2-python-SE/ITS_us/tree/main).

```
@article{CenderIosifShalashilin2024,
  doi = {10.31415/nat.31415},
  url = {https://doi.org/10.31415/joss.271828},
  year = {2024},
  publisher = {The CDT},
  volume = {1},
  number = {1},
  pages = {00},
  author = {T},
  title = {ITS_us: A python framework for quantum circuits},
  journal = {Nature}
}
```

[^1]: Not yet implemented


