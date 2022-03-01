# gh-code-scanning

A GitHub CLI extension for GitHub Code-Scanning!

### Dependencies

- [`gh`](https://cli.github.com/)
- `git`
- Python (version 3.5 or higher)

### Installation

```shell
# Disable gh's "interactive" mode, since gh-code-scanning is designed to be used in scripts.
gh config set prompt disabled

# Configure gh to use SSH instead of HTTPS for git operations. This is required.
gh config set git_protocol ssh

# Install the extension.
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

```shell
gh code-scanning analyses mario-campos/gh-code-scanning
```

#### Delete Code-Scanning analyses (and alerts)

```shell
gh code-scanning analyses -d mario-campos/gh-code-scanning
```
