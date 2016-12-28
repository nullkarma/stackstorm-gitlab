# Gitlab Integration Pack

## Actions

### Projects

* `project.list` - Returns a list of gitlab projects

### Pipelines

* `project.pipelines.list` - List all pipelines in a project
* `project.pipelines.run` - Create a new Pipeline

### Artifacts

* `artifact.dl.and.unzip` - Download the latest artifact and unzip it

## Dependencies

### packs

* [tools](https://github.com/nullkarma/stackstorm-tools) - used by `artifact.dl.and.unzip` workflow.

Since `artifact.dl.and.unzip` is a workflow build from a 3rd party pack,
it won't be able to read `url` and `token` from your `gitlab.yaml` config.
It may be stored and encrypted in st2's key-value store.
