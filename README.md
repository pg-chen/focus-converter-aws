# FOCUS Converter (This version is only applicable to AWS.)

The FOCUS Converter is a command-line utility to convert billing data files from popular public cloud providers,
such as **Amazon Web Services**, **Microsoft Azure**, **Google Cloud** and **Oracle Cloud**, into the common
schema known as FOCUS. You can read the specification at [FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec].

The converter is optimized for:

* Ability to act on the large files and wire formats provided by cloud providers.
* Comprehensibility of the conversion process which encodes _an_ understanding of the specification as-written.
* Best-effort conversion where the appropriate data for FOCUS does not exist in the provider's data file.
* Modularity so that new types of billing data can be supported.

## Currently Supported Cloud Providers

* [Amazon Web Services]
* [Google Cloud]
* [Microsoft Azure]
* [Oracle Cloud]

Want to add your own? See [CONTRIBUTING.md]

## Conversion Rules

The conversion rules are defined in YAML files in the `conversion_configs` directory. Each file contains a list of
conversion rules, which are applied in order.

Rules are also exported per provider in the following directories based on format:

* **Markdown**: [Rules Export Markdown]
* **CSV**: [Rules Export CSV]

## Development setup

1. Clone this repository.
1. [Install Poetry]
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    export PATH="/home/pg103426/.local/bin:$PATH"
    ```
1. [Install AWS CLI]
    ```sh
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
    unzip awscliv2.zip
    sudo ./aws/install
    ```
1. Add credential to aws config file
    `aws configure --profile cathay-finops-internal`
1. Run the following shell snippet:
    ```sh
    cd focus-converter-aws/
    poetry install --only main --no-root
    poetry shell
    ```



## Example Usage

1. Local
```bash
python -m focus_converter.main convert --provider aws --data-path /Users/pg/Desktop/Work/Project/TW-CathayFinOps/SampleData/CUR2024-07.snappy.parquet --data-format parquet --parquet-data-format dataset --export-path /Users/pg/Desktop/Work/Project/TW-CathayFinOps/SampleData/
```

2. Cloud Shell
```bash
python -m focus_converter.main convert \
    --provider aws \
    --data-path s3://jay-cur-demo/momo-cur/demo/data/BILLING_PERIOD=2024-08/demo-00001.snappy.parquet \
    --data-format parquet \
    --parquet-data-format s3 \
    --export-format s3 \
    --export-path s3://benson-test-cathay-finops/focus-converter/
``` 


[Install Poetry]: https://python-poetry.org/docs/#installation

[Install libmagic]: https://formulae.brew.sh/formula/libmagic

[FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec]: https://github.com/FinOps-Open-Cost-and-Usage-Spec/FOCUS_Spec

[Amazon Web Services]: https://github.com/finopsfoundation/focus_converters/tree/master/focus_converter_base/focus_converter/conversion_configs/aws

[Google Cloud]: https://github.com/finopsfoundation/focus_converters/tree/master/focus_converter_base/focus_converter/conversion_configs/gcp

[Microsoft Azure]: https://github.com/finopsfoundation/focus_converters/tree/master/focus_converter_base/focus_converter/conversion_configs/azure

[Oracle Cloud]: https://github.com/finopsfoundation/focus_converters/tree/master/focus_converter_base/focus_converter/conversion_configs/oci

[Rules Export Markdown]: https://github.com/finopsfoundation/focus_converters/tree/master/conversion_rules_export/markdown

[Rules Export CSV]: https://github.com/finopsfoundation/focus_converters/tree/master/conversion_rules_export/csv

[pie charts]: https://github.com/finopsfoundation/focus_converters/tree/master/progress/README.md

[Install AWS CLI]: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html