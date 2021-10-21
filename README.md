# gh-code-scanning

A GitHub CLI extension to bulk-enable GitHub Code-Scanning!

### Installation

```shell
gh extension install mario-campos/gh-code-scanning
```

### Usage
#### Enable Code Scanning

Enable a single repository:

```shell
gh code-scanning enable mario-campos/gh-code-scanning
```

Enable all repositories in the organization _foo_:

```shell
gh repo list foo --json nameWithOwner --jq '.[].nameWithOwner' | xargs gh code-scanning enable
```

Enable all Python repositories in the organization _foo_:

```shell
gh repo list foo \
  --json nameWithOwner,languages \
  --jq '.[] | select(.languages.[].node.name == "Python") | .nameWithOwner' \
| xargs gh code-scanning enable
```

#### List Code-Scanning Alerts

List the alerts of a single repository:

```shell
gh code-scanning alerts mario-campos/gh-code-scanning
```

List the alerts of all repositories in the organization _foo_:

```shell
gh repo list foo --json nameWithOwner --jq '.[].nameWithOwner' | xargs gh code-scanning alerts
```
