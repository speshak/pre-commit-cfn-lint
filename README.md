# Archived

*The [cfn-lint](https://github.com/awslabs/cfn-python-lint) project has proper pre-commit support.  Use that directly rather than this wrapper.*

cfn-lint
========

### Using cfn-lint with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: https://github.com/speshak/pre-commit-cfn-lint
        rev: ''  # Use the sha / tag you want to point at
        hooks:
        -   id: cfnlint
