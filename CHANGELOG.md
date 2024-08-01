# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## SemVer public API

The [public API](https://semver.org/spec/v2.0.0.html#spec-item-1)  for this project is defined by the set of functions provided by the `src` folder.

---

## [1.1.0](https://github.com/crowdsecurity/cs-thehive-cortex-analyzer/releases/tag/v1.1.0) - 2024-08-01

### Changed

- Update long report to add additional information

### Added

- Add new taxonomies: reputation, behaviors, mitre techniques and cves

- Add configuration to enable/disable each taxonomy individually: 
    - reputation (enabled by default)
    - as_name (disabled by default)
    - ip_range_score (disabled by default)
    - last_seen (disabled by default)
    - attack_details (disabled by default)
    - behaviors (enabled by default)
    - mitre_techniques (disabled by default)
    - cves (enabled by default)
    - not found (enabled by default)

---

## [1.0.0](https://github.com/crowdsecurity/cs-thehive-cortex-analyzer/releases/tag/v1.0.0) - 2024-07-18

- Initial release: synchronization with TheHive/Cortex Analyzers `1.0` release
