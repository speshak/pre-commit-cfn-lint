cfn-lint
========

### Using cfn-lint with pre-commit

Add this to your `.pre-commit-config.yaml`

    -   repo: https://github.com/speshak/pre-commit-cfn-lint
        rev: ''  # Use the sha / tag you want to point at
        hooks:
        -   id: cfnlint
