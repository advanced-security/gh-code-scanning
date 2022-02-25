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

Enable all repositories in the organization _foo_ that have CodeQL "interpreted" languages (`javascript`, `python`, `go`, `ruby`) and none of the CodeQL "compiled" languages (`java`, `csharp`, `cpp`):

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

#### List Code-Scanning alerts

List the alerts of a single repository:

```shell
gh code-scanning alerts mario-campos/gh-code-scanning
```

List the alerts of all repositories in the organization _foo_:

```shell
gh repo list foo --json nameWithOwner --jq '.[].nameWithOwner' | xargs gh code-scanning alerts
```

#### List Code-Scanning analyses

List the analyses of a repository:

```shell
gh code-scanning analyses mario-campos/gh-code-scanning
```

Delete all analyses of a repository:

#### Delete Code-Scanning analyses (and alerts)

```shell
gh code-scanning analyses -d mario-campos/gh-code-scanning
```
