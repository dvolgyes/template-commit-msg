# template-commit-msg

A trivial way to add templated commit message to git.

Add to your .pre-commit-config.yaml:
```
repos:
-   repo: https://github.com/dvolgyes/template-commit-msg
    rev: "v0.1.0"
    hooks:
    -   id: template-commit-msg
        args: ['--pattern=[]  (#)']
   
```

Installing hook:

```
pre-commit install-hooks -t prepare-commit-msg
```
