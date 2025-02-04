# Contributing
Bugcrowd welcomes community feedback and direct contributions to the Bugcrowd VRT. We accept comments for public discussion via GitHub Issues, but can also accommodate comments made via email to [vrt@bugcrowd.com](mailto:vrt@bugcrowd.com).

## Process
Please open your feedback as an **Issue**. The Bugcrowd team strives to review and comment on new Issues within five business days. Large or systemic changes should first be discussed in an Issue rather than be submitted as a pull request directly. If you have a suggested minor change that includes:

- Additional subcategories or variants
- Rewording of existing entries
- Corrections of typographical or other minor errors

you may open a pull request directly for these examples. Prior to opening a pull request please ensure your suggested changes pass schema validation. The repository includes a [`validate_vrt.py`](../validate_vrt.py) script that can be used to perform JSON validation using [`vrt.schema.json`](../vrt.schema.json) (see examples below).

### Example Git Hook Validation
1. Install `jsonschema` and `GitPython` via pip with `pip install jsonschema GitPython`
 - If you don't have pip, you can install it like so: `easy_install pip`
2. Add a pre-commit hook that will automatically run the validation script every time you run `git commit`
 - Windows: `mklink /H .git\hooks\pre-commit validate_vrt.py`
 - Linux/macOS: `ln -s ../../validate_vrt.py .git/hooks/pre-commit`

### Example Manual JSON validation
 1. Install `jsonschema` and `GitPython` via pip with `pip install jsonschema GitPython`
  - If you don't have pip, you can install it like so: `easy_install pip`
 2. Run `validate_vrt.py`

 ### This validation is also run in github actions
 You can find the Validate VRT action [here](https://github.com/bugcrowd/vulnerability-rating-taxonomy/actions?query=workflow%3A%22Validate+VRT%22)

### CHANGELOG Entry
When opening a Pull Request append an entry to the [`CHANGELOG`](../CHANGELOG.md) under the `[Unreleased]` header, following the format from [Keep a CHANGELOG](http://keepachangelog.com/en/0.3.0/) and our previous releases.

To detail, an entry can go in one of three headers, `Added`, `Removed`, or `Changed`. For `Added` or `Removed` categories add a bullet (`-`) then state the `ID` of the entry that was either added or removed.  With `Changed`, we handle attribute or parent changes.

If a data attribute (name or priority) changes, use the format of:
```
- {ID} {attribute} changed from {old value} to {new value}
```

Yet if the parent changes, the format below should be used:
```
- {old ID} moved via {type} change to {new ID}
```

### Deprecated Node Mapping
When a breaking change occurs, a new entry should be added to [`deprecated-node-mapping.json`](../deprecated-node-mapping.json).

#### Format
```json
{
  "deprecated_id": {
    "1.3": "new_id",
    "2.0": "newest_id"
  }
}
```

### Mapping to Other Systems
When adding, removing or modifying VRT entries, the [mapping files](../mappings) will also need to be updated. Check
the [README](../README.md#mapping-to-other-systems) for details about the file formats.
