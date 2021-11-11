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

Enable all repositories that have CodeQL "interpreted" languages (`javascript`, `python`, `go`, `ruby`) and none of the CodeQL "compiled" languages (`java`, `csharp`, `cpp`):

```shell
gh repo list foo \
  --json nameWithOwner,languages \
  --jq '
  .[] | (.languages) = [.languages[].node.name] |
  select(.languages | all(. != "Java" and . != "C#" and . != "C" and . != "C++")) |
  select(.languages | any(. == "JavaScript" or . == "TypeScript" or . == "Python" or . == "Go" or . == "Ruby")) |
  .nameWithOwner' \
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
